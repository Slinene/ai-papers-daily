---
title: "How speculative decoding makes LLMs go brrr"
authors: "Leonie Monigatti"
affiliation: 个人技术博客（leoniemonigatti.com）
date: 2026-08
venue: Blog（技术综述）
topic: llm-general
topic_name: LLM通用
topic_icon: 🧠
idea: 系统梳理投机解码（speculative decoding）这一「无损」推理加速范式：用轻量 drafter 一次提议 γ 个候选 token，target 模型单次 forward 并行验证，靠拒绝采样保证输出分布与 target 严格一致——加速不以质量为代价。核心概念区分在于它不是量化/剪枝那类近似压缩，而是把 memory-bound 的自回归解码换成 compute-bound 的批量验证。全文以 L = (T_draft + T_verify)/τ 这一延迟公式为主线，把近三年 drafter 设计串成一条演进链：独立草稿模型 → Medusa 多头 → MTP → EAGLE 系列特征级自回归 → DFlash 块扩散并行 → DSpark 半自回归 + 置信度调度验证，并指出最新的范式转折：到了一定服务规模，投机解码不再只是「起草问题」，更是「验证调度问题」。
paperUrl: https://leoniemonigatti.com/blog/speculative-decoding.html
codeUrl: null
tags:
  - Speculative Decoding
  - Inference Acceleration
  - Draft-Verify
  - EAGLE
  - Block Diffusion
unverified: false
---

> 本文是对 Leonie Monigatti 博客 [How speculative decoding makes LLMs go brrr](https://leoniemonigatti.com/blog/speculative-decoding.html)（2026-08-23）的深度整理与扩写。原文配图为作者原创插图，此处不转载，结构图均为重绘的等价示意。

## 核心思路

**问题**：Transformer LLM 自回归生成，每个 token 都要走一次完整 forward。延迟正比于输出长度。更关键的是，低 batch 下解码是 **memory-bandwidth bound** 而非 compute bound——每步都要把全部权重从 HBM 搬到 SRAM，而 GPU 的算力单元大部分时间闲着。对实时对话、多轮 agentic workflow 这类延迟敏感场景，这是生产上的硬瓶颈。

**关键 idea**：token 的预测难度并不均匀。补全常见短语、闭合括号这类 token，小模型猜得和大模型一样准；只有事实性/罕见词才真需要大模型的判断力。投机解码利用这个不均衡：

1. 让一个轻量 **drafter** 一次提议 γ 个候选 token（典型 3–12）；
2. **target 模型单次 forward 并行验证**这 γ+1 个位置——因为权重只需加载一次，验证 γ 个 token 的开销 ≈ 验证 1 个；
3. 用**拒绝采样**决定接受哪些，被拒的位置从残差分布重采样纠正。

**必须点明的范式区分**：投机解码**不是**量化、剪枝、蒸馏那一类「牺牲一点质量换速度」的近似方法。它的输出分布与 target 模型**严格相同**（下面第 3 节给出证明）。drafter 再烂，也只是让加速比退化到 1×，**不会让模型变笨**。这是它能无脑上生产的根本原因。

由 Chen et al.（2023, DeepMind）与 Leviathan et al.（2023, Google）几乎同期独立提出。

## 整体实现思路

一个投机周期（speculative cycle）的端到端流程：

```text
                    ┌──────────────────────────────────────────┐
  prefix x_{<t} ───► │  Drafter q(·)                            │
                    │  自回归 γ 步 / 或并行一次出块              │
                    │  产出候选 x̃_1..x̃_γ 及其概率 q(x̃_i)       │
                    └───────────────┬──────────────────────────┘
                                    │  γ 个候选 token
                                    ▼
                    ┌──────────────────────────────────────────┐
  一次 forward ───► │  Target p(·)                             │
  (γ+1 个位置)      │  causal mask 下同时算出                   │
                    │  p(·|x_{<t}), p(·|x_{<t},x̃_1), ...       │
                    │  ... , p(·|x_{<t},x̃_1..x̃_γ)             │
                    └───────────────┬──────────────────────────┘
                                    ▼
                    ┌──────────────────────────────────────────┐
                    │  Rejection sampling（逐位置 i=1..γ）      │
                    │  以 α_i = min(1, p(x̃_i)/q(x̃_i)) 接受    │
                    │                                          │
                    │  全接受 → 追加 1 个 bonus token          │
                    │  第 i 个被拒 → 丢弃 i..γ，从残差分布      │
                    │               p' = norm(max(0,p−q)) 重采样│
                    └───────────────┬──────────────────────────┘
                                    ▼
                        本轮吐出 τ 个 token（1 ≤ τ ≤ γ+1）
                                    │
                                    └──► 回到 Drafter，进入下一周期
```

关键不变量：**每一轮至少吐出 1 个 token**（即使第一个草稿就被拒，target 也会从残差分布采样出一个正确 token）。所以投机解码在最坏情况下退化为普通自回归解码 + drafter 的额外开销，永远不会死循环。

伪代码：

```python
def speculative_step(prefix, draft_model, target_model, gamma):
    # 1) 起草：drafter 自回归产出 gamma 个候选
    cand, q_probs = [], []
    ctx = prefix
    for _ in range(gamma):
        q = draft_model(ctx)              # [V]
        x = sample(q)
        cand.append(x); q_probs.append(q)
        ctx = ctx + [x]

    # 2) 验证：target 单次 forward 拿到 gamma+1 个位置的分布
    p_probs = target_model(prefix + cand)  # [gamma+1, V]，causal mask

    # 3) 拒绝采样
    out = []
    for i, x in enumerate(cand):
        r = uniform(0, 1)
        if r < min(1.0, p_probs[i][x] / q_probs[i][x]):
            out.append(x)                              # 接受
        else:
            resid = normalize(clamp_min(p_probs[i] - q_probs[i], 0))
            out.append(sample(resid))                  # 拒绝 → 残差重采样，丢弃后缀
            return prefix + out
    out.append(sample(p_probs[gamma]))                 # 全接受 → bonus token
    return prefix + out
```

## 子模块实现（可复现细节）

### 模块 1 — Drafter：起草机制

- **输入**：当前 prefix `x_{<t}`（以及可选的 target 内部特征）
- **输出**：γ 个候选 token `x̃_1..x̃_γ` + 各自的提议概率 `q(x̃_i)`
- **γ 的取值**：实践中 3–12。太小则每轮摊销不够；太大则后段接受率指数衰减（见下面 τ 的公式），且对自回归 drafter 而言每多一个 token 就多一次串行前向。

设计上的核心张力：**drafter 必须同时又快又准**。慢而准的 drafter 吃掉 `T_draft` 预算；快而不准的 drafter 让草稿大量被拒、白烧算力。近三年几乎全部工作都在这条 trade-off 曲线上做文章。

### 模块 2 — 并行验证

- **输入**：`prefix + [x̃_1..x̃_γ]`，长度 `t+γ`
- **输出**：`p(·|x_{<t})`、`p(·|x_{<t},x̃_1)`、…、`p(·|x_{<t},x̃_1..x̃_γ)` 共 **γ+1 个分布**，形状 `[γ+1, V]`

这一步为什么近乎免费，是整个方法的物理基础：

- 低 batch 自回归解码是 **memory-bound**：单步的算术强度极低，时间几乎全花在把权重从 HBM 读进来上，算力单元闲置。
- 把 γ 个 token 一起喂进去，权重**只加载一次**，attention 在 causal mask 下天然一次算出所有前缀位置的分布。原本要付 γ 次的 memory-bound 代价，现在只付 1 次。
- 换句话说：投机解码是**把闲置的算力换成 token**。

工程上要注意 KV cache 的回滚——被拒绝的位置及其之后的 KV 必须丢弃，只保留接受前缀那部分。

### 模块 3 — 拒绝采样与无损性

逐位置比较 target 概率 `p(x̃_i)` 与 drafter 概率 `q(x̃_i)`，以

$$\alpha_i = \min\left(1, \frac{p(x_i)}{q(x_i)}\right)$$

的概率接受第 i 个草稿 token。直觉：

- drafter **低估**了一个 target 喜欢的 token（`p > q`）→ 必然接受；
- drafter **高估**了某个 token（`q > p`）→ 有概率被拒。

两种收尾：

| 情况 | 行为 |
|---|---|
| γ 个全部接受 | target 在验证 pass 中顺带产出第 γ+1 个 token（**bonus token**），本轮吐 γ+1 个 |
| 第 i 个被拒 | 丢弃 `x̃_i..x̃_γ`（**即使后面的本来是对的**），从残差分布重采样纠正第 i 位 |

残差分布：

$$p'(x) = \text{norm}\big(\max(0,\; p(x) - q(x))\big)$$

**为什么严格无损**（原文给的证明思路，值得记住）：把 target 的概率质量拆成两块——

1. 与 drafter 分布 `q` **重叠**的部分 `min(p, q)`：这部分由「被接受的草稿 token」覆盖，因为两个模型在这些 token 上是一致的；
2. **剩余质量** `max(0, p−q)`：target 想要得比 drafter 多的那部分，由「拒绝后的残差重采样」覆盖。

两块拼起来正好重构出完整的 `p`。而 `q > p` 那部分多余的草稿质量（图上打叉的区域）被丢弃。所以 **采样分布 = p，一字不差**。

### 模块 4 — 收益模型（决定一切工程选择）

两个核心量：

- **接受率 α**：草稿 token 被接受的平均概率（把逐位置的 `α_i` 在位置与上下文上平均）。
- **接受长度 τ**：一个投机周期期望吐出的 token 数，**含**验证 pass 顺带产出的那个 target token。

在「各位置接受相互独立」的简化假设下，Leviathan et al. 给出：

$$\tau = \sum_{i=0}^{\gamma} \alpha^{i} = \frac{1 - \alpha^{\gamma+1}}{1 - \alpha}$$

`i = 0` 那一项对应 target **必定**产出的那个 token（拒绝后的纠正，或全接受后的 bonus）。所以 **τ ∈ [1, γ+1]**——最坏也有 1，不会倒退。

平均单 token 延迟（Sadhukhan et al., MagicDec 的近似）：

$$L = \frac{T_{\text{draft}} + T_{\text{verify}}}{\tau}$$

**这个公式是全文主线**。它说明只有三条提速杠杆：

1. 起草更准（τ ↑）；
2. 起草更快（`T_draft` ↓）；
3. 验证更快（`T_verify` ↓）。

由此可见，投机解码**主要是一个 drafter 设计问题**——直到 DSpark 指出验证调度也是问题为止。

一个容易被忽略的推论：因为 `τ = (1−α^{γ+1})/(1−α)` 对 γ 是**次线性**的（α<1 时 α^i 指数衰减），而自回归 drafter 的 `T_draft` 对 γ 是**线性**的，所以存在一个最优 γ*，超过它继续加长草稿反而变慢。这正是后面并行 drafter 想破解的点。

## drafter 设计的演进链

### A. 独立草稿模型（Chen et al. / Leviathan et al., 2023）

- **做法**：同族小模型当 drafter（同 tokenizer、相近 instruction-tuning）。后续工作用 target 蒸馏 drafter 以拉高接受率。
- **收益**：**2–3×**，开箱即用、无需训练。
- **代价**：要额外托管一个模型（显存 + 运维）。而且 drafter 自身是自回归的，γ 每加 1 就多一次串行前向，收益递减 → 存在最优草稿长度，超过就掉速。

```text
prefix ──► [小模型] ─t1─► [小模型] ─t2─► ... ─tγ─►  γ 次串行前向
```

### B. Medusa（Cai et al., ICML 2024）

- **做法**：不再养第二个模型，而是在 target 上**加挂多个轻量预测头**。第 i 个头预测未来第 i+1 个位置的 token（第 1 个位置由 target 自带的 LM head 覆盖）。多个头的候选组织成**树**，用 **tree attention** 一次并行验证多条分支。
- **收益**：Medusa-1 约 **2.2×**；Medusa-2 约 **2.3–3.6×**，接受长度 3.0–3.5 token/step。
- **代价**：额外的头需要训练。更本质的问题是**各头彼此独立预测**——第 3 个头不知道第 2 个头出了什么，导致越靠后的位置草稿质量越差（后缀衰减），接受率被拖下来。

```text
              ┌─ head_1 ─► t+1 候选 ─┐
target 隐状态 ─┼─ head_2 ─► t+2 候选 ─┼─► 组成候选树 ─► tree attention 并行验证
              └─ head_3 ─► t+3 候选 ─┘        （各 head 相互独立 → 后缀衰减）
```

### C. MTP：Multi-token prediction（Gloeckle et al., ICML 2024）

原文特意把它列出来做**概念澄清**：MTP 用的是和 Medusa 一样的多头结构，但**出发点完全不同**——它是在**预训练阶段**就加多个输出头，用「同时预测多个未来 token」这个更丰富的监督信号把**基座模型本身训得更强**。最高 3× 的推理加速只是副产品。

| | Medusa | MTP |
|---|---|---|
| 目的 | 给成品模型加起草能力 | 预训练时提升基座质量 |
| 对基座质量 | 不变 | **提升** |
| 适用性 | 任意现成 checkpoint 可加挂 | 必须从预训练就规划 |

### D. EAGLE / EAGLE-2 / EAGLE-3（Li et al., 2024–2025）

**核心洞察**：Medusa 把 drafter 折进 target 里，省掉了第二个模型，但**各个 token 级的头在逐个重新推导 target 已经算过的上下文**。EAGLE 把「内建 drafter」推进一步——不直接预测未来 token，而是**在特征层（hidden state）外推**，复用 target 冻结的内部表示。

- **EAGLE（2024）**：挂一个小的**自回归 drafter 在特征级**工作。输入 = target 顶层特征（LM head 之前那一层）+ 上一个采样 token 的 embedding，融合后预测**下一个位置的特征**；再把预测出的特征过 target **冻结的 LM head** 得到草稿 token。报告 **2.7–3.5×**（LLaMA2-Chat 70B）。
- **EAGLE-2（2024）**：引入**动态草稿树**——树结构随 drafter 的置信度自适应：可预测的段落长出更长的分支，复杂处则分支短而宽。**3.05–4.26×**。
- **EAGLE-3（2025）**：把训练目标从「预测特征」改回**直接预测 token**，靠 **training-time test**（训练时就用 drafter 自己反馈的输出来训，消除 train/inference 输入错配）来支撑；同时**融合 target 多层特征**而非只取顶层。加速拉到 **6.5×**。

```text
target 冻结                     EAGLE drafter（小、自回归、特征级）
  多层 hidden ──融合──►  f_t ──┐
                              ├─► 预测 f_{t+1} ─► 冻结 LM head ─► x̃_{t+1}
  上一 token embedding ───────┘        │
                                       └─► 再喂回自己，串行推进（仍是 AR）
```

**残留问题**：EAGLE 的 drafter **仍是自回归的**——起草成本随草稿长度线性增长，且误差在块内逐步累积。

### E. DFlash（Chen et al., 2026）：块扩散并行起草

- **动机**：上面几乎所有 drafter 都是自回归的，于是自回归解码的串行瓶颈在 drafter 身上原样重演。按 DFlash 自己的 benchmark，自回归 drafter 大致被卡在 **2–3×**。
- **思路**：用**块扩散（block diffusion）**模型当 drafter——一次并行去噪出一整块 token。纯并行扩散模型有固定长度、缺乏高效 KV cache 的老问题，而块扩散（Arriola et al., ICLR 2025）通过「按块并行去噪」同时拿到并行性与可缓存性。整体 = **并行块扩散起草 + 自回归 target 验证**，速度与质量各取一半。

三个具体步骤：

1. **抽取上下文特征**：target 对 prompt 走一次标准 prefill 产出首个 token（anchor token）；这一 pass 中抽出**固定若干层**的 hidden states，拼接后过一个 projection 层融合成紧凑的 target context feature。
2. **KV 注入做 target 特征条件化**：把融合后的 context feature **注入 drafter 的 KV cache**，供 drafter 每一层 attention 使用。这一步的效果是——**接受长度随 drafter 层数增加而持续提升，而不是很快饱和**。
3. **块并行扩散起草**：drafter 单次 forward 并行去噪出整块未来 token。每个草稿块以一个 anchor token 开头（drafter 据此条件化预测块内其余位置）。训练时从 ground-truth 回复中采样 anchor，mask 掉其后 `block_size − 1` 个位置，让 drafter 并行预测这些被 mask 的 token。

- **收益**：最好基准上 **>6×**，平均 **4–5×**。接受长度随 draft 层数有效 scaling。
- **本质优势**：并行 drafter 单次 forward 产出所有草稿位置，**起草延迟几乎与块大小无关**——这直接打破了自回归 drafter「γ 越长越慢」的诅咒，原则上允许更长的草稿块。
- **残留问题**：并行预测各位置**缺乏 token 间依赖**，实践中出现快速的**接受率衰减**（后缀越靠后越不准）。

### F. DSpark（Cheng et al., 2026）：半自回归 + 置信度调度验证

DSpark 的贡献在于指出一个**框架层面的转折**：到了一定服务规模，投机解码**不只是起草问题，也是验证问题**。

它针对并行 drafter 的两个短板：

1. **生成质量**：块内各位置独立预测 → 缺乏 token 间依赖 → 后缀衰减；
2. **验证浪费**：并行起草可以很快产出很长的块，但**只有被接受才有价值**。高并发下，去验证一个大概率被拒的长块，会白白挤占 target 模型的 batch 容量——那本可以拿去服务其他请求。

对应两个设计：

- **半自回归生成**：并行 backbone + 一个**轻量串行头**。backbone 一次产出整块的 hidden states 和 base logits；串行头在块内**从左到右采样**，并叠加一个**依赖前缀的转移偏置（prefix-dependent transition bias）**。这样既保住了块并行的大部分速度，又让每个采样出的 token 能依赖块内前面的 token，缓解后缀衰减。
- **置信度调度验证**：不再用固定草稿长度，而是**逐请求决定验证多少**。一个 **confidence head** 估计每个草稿 token 通过验证的概率；一个**硬件感知的 prefix scheduler** 把这些估计与引擎当前负载、吞吐结合起来，为每个请求选一个验证长度。

- **收益**：接受长度提升、验证浪费下降，**等吞吐下单用户生成速度 +60–85%**（注意：这是相对 MTP-1 生产基线的 per-user 加速，**不是**相对非投机解码的 wall-clock 加速）。
- **代价**：复杂度显著上升——多了串行头、置信度头、负载感知调度器，以及它们的标定与服务集成。调度的可靠性完全取决于置信度估计，分布漂移时会退化。

## 实验设置与结果

原文汇总的横向对比（**注意**：各方法的接受长度是在不同模型/数据集上报告的，只具指示性，不可直接横比）：

| 方法 | 起草模式 | 接受长度 τ | 报告加速 |
|---|---|---|---|
| 独立草稿模型 | 自回归 | ~3.6 tokens | 2–3× |
| Medusa | 并行（多头） | ~3.0–3.5（Medusa-2） | 2.2–3.6× |
| EAGLE-3 | 自回归（特征级） | ~5–7.5 tokens | 6.5× |
| DFlash | 块并行扩散 | ~4–8 tokens | >6× |
| DSpark | 半自回归 | ~3.1–6.2 tokens | 1.6–1.85×\* |

\* DSpark 未报告相对普通自回归解码的 wall-clock 加速；该数字是相对 **MTP-1 生产基线**的 per-user 生成加速。

**趋势读法**：接受长度 τ 从 ~3.5（第一代）推到 ~5–8（EAGLE-3 / DFlash），加速比从 2–3× 推到 6×+。而演进的主线一直是同一个公式 `L = (T_draft + T_verify)/τ` 的三项——先卷 τ（Medusa → EAGLE），再卷 `T_draft`（DFlash 用并行起草把它压到与块长无关），最后 DSpark 开始卷 `T_verify` 的**调度**。

### 什么时候真的划算（工程判据）

这一节是全文最实用的部分：

- **低 batch**：自回归解码是 memory-bandwidth bound，算力闲置。投机解码把闲置算力换成 token，用一次 forward 的代价验证 γ+1 个位置——**这是收益最大的区间**。
- **高 batch + 短上下文**：target 的矩阵乘法变成 **compute-bound**。此时验证额外的草稿 token 不再接近免费，而是**和其他请求抢已经饱和的算力**。加速比缩小；如果草稿大概率被拒，甚至会**拉低整体吞吐**。
- 所以 batch size 大小与上下文长度共同决定这笔账划不划算——这也正是 DSpark 做负载感知调度的动机。

落地上，主流推理栈已开箱支持（vLLM / SGLang / llama.cpp / MLX），都能挂 draft model，部分还支持 EAGLE / Medusa 式 drafter：

```bash
python -m sglang.launch_server \
  --model-path <target-model> \
  --speculative-algorithm DFLASH \
  --speculative-draft-model-path <draft-model>
```

## 思考与可参考价值

**局限与需要自己验证的点**

- 表中的加速倍数来自各自论文的自报基准，模型/数据集/硬件都不同，**不能横比**，更不能直接当作自家线上的预期收益。真实收益必须在自己的 batch 分布、上下文长度分布、硬件上重测。
- 「无损」是指**分布无损**，不是**逐 token 结果相同**。同一个 seed 下投机解码与普通解码的具体输出会不同（采样路径不同），做回归对齐/diff 测试的团队要提前知道这点，否则会误判为 bug。
- DSpark 这类方案把复杂度推到了调度层，标定成本和分布漂移风险都是真实的运维负担，中小规模服务未必划算。
- 原文是综述性质，DFlash / DSpark 的细节只到「机制描述」层面，真要复现仍需回读原论文。

**对电商 / 搜推 / Agent 方向的可迁移点**

1. **最直接的收益场景是 agentic workflow**。多轮 agent 的每一跳都是低 batch、延迟敏感的解码，正好落在投机解码收益最大的区间。自研 agent 服务（工具调用、query 改写、推词）如果还在裸自回归解码，这是性价比最高的一档优化——挂个同族小模型就有 2–3×，且**不需要任何质量回归验证**（分布无损）。
2. **结构化/低熵输出的收益被低估**。搜推链路里大量是 JSON、标签、类目路径、SQL、商品属性这类**高度可预测**的输出——接受率 α 天然很高，τ 逼近 γ+1，收益远好于开放式创作。谁的输出越模板化，谁越该上。
3. **「起草-验证」这个范式本身可以迁出解码**。用轻量模型批量提议、用重模型一次性批量校验、并保证「校验规则等价于重模型自己的判断」——这套结构可以直接套到**机审/推词质检**上：小模型批量出候选词，大模型一次 forward 批量判定，被拒的走大模型重出。这与本人 SEO 推词评估链路的结构高度同构。
4. **EAGLE 的「复用 target 内部特征」思想值得借鉴到多任务塔**。与其让下游小头从 token 重新推导上下文，不如直接吃主模型的中间层 hidden state——DFlash 的「多层特征融合 + KV 注入」是这套思路目前最成熟的形态，对做「一个主模型 + 多个轻量下游头」的推荐架构有直接参考价值。
5. **DSpark 的框架转折值得记住**：任何「用小模型省大模型」的方案，到了高并发都会从「预测精度问题」变成「资源调度问题」。设计之初就把负载感知留成接口，比事后改造便宜得多。
