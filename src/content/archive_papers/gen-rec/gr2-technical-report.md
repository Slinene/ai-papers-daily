---
title: GR2 Technical Report
authors: Yufei Li, Zaiwei Zhang, Mingfu Liang, Kavosh Asadi, Jay Xu, et al. (71 人)
date: 2026-06
venue: arXiv
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: GR2 通过语义 ID mid‑training、强师推理轨迹蒸馏、可验证奖励 RL 三阶段训练，弥合 LLM 在工业重排中的推理、词汇与成本鸿沟；并引入
  OPD、上下文压缩和推理内化，实现排序质量大幅提升与高效部署。
paperUrl: https://arxiv.org/abs/2606.31984
codeUrl: null
tags:
- Generative Recommendation
- Re‑Ranking
- Semantic ID
- Chain‑of‑Thought
- Reinforcement Learning
unverified: true
---

## 核心思路
GR2 解决工业推荐系统重排阶段 LLM 应用的三大差距：推理能力未充分释放、物品 ID 词汇表不匹配、工业规模成本过高。通过 (i) 语义 ID mid‑training 使 LLM 识别物品，(ii) 强师生成推理轨迹蒸馏到学生，赋予推理先验，(iii) 设计可验证奖励（AUC/NDCG 及防作弊条件格式奖励）用 DAPO 进行 RL 后训练，直接优化重排目标；(iv) 提出上下文压缩器、On‑Policy Distillation (OPD) 和推理内化，保证排序质量同时大幅降低部署成本。

## 整体实现思路
端到端 pipeline：
```
物品文本特征 → 语义ID Tokenizer (RQ‑VAE) → 语义ID序列
↓
预训练LLM (Qwen3‑8B) + 混合语料 (语义ID+世界知识) → Mid‑Training → 对齐领域LLM
↓
强师LLM (Qwen3‑32B) + 重排专用Prompt → Targeted/Rejection Sampling → 高质量推理轨迹数据集
↓
学生LLM SFT (或 OPD) 训练 → 获得推理先验 → RL后训练 (DAPO, AUC/NDCG + 条件格式奖励) → 精排策略
↓ [部署优化]
上下文压缩 (GRPO+Judge) → 缩短输入 → 推理内化 (第二次RL无CoT) → 无推理输出 → 系统优化 (剪枝+KV缓存) → 在线服务
```

## 子模块实现（可复现细节）

### 1. 语义ID Tokenizer 与 Mid‑Training

- **Tokenizer**: 基于 RQ‑VAE，将物品文本特征 $x$ 映射为 $K$ 个离散语义 ID: $\text{Tokenizer}(x) = (z_1, \dots, z_K) \in \{1,\dots,C_1\}\times\cdots\times\{1,\dots,C_K\}$，$C_i$ 为第 $i$ 个码本大小。这些语义 ID 作为特殊 token 加入 LLM 词汇表，确保 $\ge 99\%$ 唯一性，避免 ID 冲突。
- **Mid‑Training**: 将语义 ID 与自然语言 token 交错拼接为单一序列，采用 next‑token prediction 目标优化语义 ID 嵌入表。任务设计同先前技术报告 (Liang et al., 2026)，多任务学习，包括序列推荐、物品描述生成等，使 LLM 将对齐推荐知识与世界知识。

### 2. 推理增强

#### 2.1 聊天格式模板
- **输入/输出**：
  - System: 扮演分析师，定义重排任务。
  - User: 包含用户历史交互序列（每条为 `[SID, 标题, 类别]`）和候选列表（相同格式，预排序）。
  - Assistant: 输出包含 CoT 推理轨迹 $\tau$ 和 JSON 排序结果 $o$。推理中必须用 SID 引用物品。
- 训练时仅对 assistant 部分计算损失。

#### 2.2 推理轨迹生成
- **Targeted Sampling**: 给定历史 $[s_{v_1},\dots,s_{v_k}]$、候选 $[s_{y_1},\dots,s_{y_c}]$ 和目标物品 $s_{v_{n+1}}$，构造 prompt $P_{\text{targeted}}(x,y,z)$，由强师生成解释为何用户会选择 $z$。得到轨迹 $\tau$，保证与真实目标一致。
- **Rejection Sampling**: prompt $P_{\text{rejection}}(x,y)$ 不提供目标，强师反复采样预测 $\hat{s}_{y_c}$ 直到与真实 $s_{v_{n+1}}$ 匹配，保留该轨迹。可生成更真实、非事后归因的推理。
- **Prompt 设计 5 原则**：(1) 明确系统角色和重排任务；(2) 同时呈现历史与候选；(3) 引导领域知识（如序列模式：洗发水→护发素）；(4) 强制输出用 SID 引用；(5) 制定多步推理格式示例。

#### 2.3 SFT 训练
- **损失函数**：
  $$ \mathcal{L}_{\text{SFT}} = -\lambda_r \sum_{i=1}^{M} \log P(r_i|\mathcal{P}, r_{<i}) - \lambda_o \sum_{j=1}^{T} \log P(o_j|\mathcal{P}, \tau, o_{<j}) $$
  其中 $M$ 为推理 token 数，$T$ 为排序输出 token 数，$\lambda_r < \lambda_o$（典型值 $\lambda_r=0.1, \lambda_o=1$）以强调排序精度。
- **训练细节**：只对 assistant 消息计算损失，推理和排序段权重分开。使用 teacher forcing，仅在教师轨迹上做行为克隆。但存在训练‑推理分布偏移。

#### 2.4 OPD (On‑Policy Distillation)
- 替代 SFT，学生在自己的采样轨迹上学习，教师仅提供分布 anchor。
- **目标**：
  $$ \mathcal{L}_{\text{OPD}}(\theta) = -\mathbb{E}\Big[\min\big(\rho_t \hat{A}_t, \text{clip}(\rho_t, 1-\epsilon_{\text{lo}}, 1+\epsilon_{\text{hi}}) \hat{A}_t\big)\Big] + \beta \, \text{KL}\big[\pi_\theta(\cdot|s_t) \| \pi_{T}(\cdot|s_t)\big] $$
  其中 $\rho_t = \pi_\theta(o_t|s_t)/\pi_{\theta_{\text{old}}}(o_t|s_t)$，优势 $\hat{A}_t$ 为组内标准化奖励，$\beta$ 蒸馏强度，$\epsilon_{\text{lo}},\epsilon_{\text{hi}}$ 为 PPO clip 参数。
- **奖励**：采用第 4 节的 rank reward，由学生采样完整轨迹获得。
- **维度**：学生模型如 1.7B，教师 32B；组大小 $G$，每轮采样多条轨迹。

### 3. RL 后训练

#### 3.1 奖励设计
- **多正例环境**：每个展示列表有多个 positives（点击、转化等）。
- **AUC 奖励**：
  $$ R_{\text{AUC}}(\pi, \mathbf{y}) = \frac{1}{|M||N|} \sum_{i \in M} \sum_{j \in N} \mathbb{1}[\text{rank}_\pi(i) < \text{rank}_\pi(j)] $$
  $M$ 为正例索引集，$N$ 为负例索引集。适合二值标签，值域 $[0,1]$。
- **NDCG 奖励**（当有分级标签 $g_i \in \{0,1,2\}$）：
  $$ R_{\text{NDCG}}(\pi, \mathbf{g}) = \frac{1}{Z} \sum_{i=1}^{K} \frac{2^{g_{\pi^{-1}(i)}} - 1}{\log_2(i+1)} $$
  $Z$ 为理想 DCG。
- **综合 rank reward**: $R_{\text{rank}} = R_{\text{AUC}}$ 或 $R_{\text{NDCG}}$，过滤无正/负例样本。

#### 3.2 条件格式奖励与防作弊
- **格式奖励** $R_{\text{fmt}} = \Omega(o)$，检查输出可解析且为合法排列。
- **防作弊机制**：若输出为恒等排列 $[1,\dots,K]$ 且该排列 AUC < 1，则只给格式奖励，$R_{\text{rank}}$ 置零。否则正常叠加。
- **最终奖励**：
  $$ R = \begin{cases}
  R_{\text{rank}} + \alpha R_{\text{fmt}}, & \text{if } \pi \neq [1,\dots,K] \text{ or } R_{\text{AUC}}([1,\dots,K],\mathbf{y}) = 1 \\
  \alpha R_{\text{fmt}}, & \text{if } \pi = [1,\dots,K] \text{ and } R_{\text{AUC}}([1,\dots,K],\mathbf{y}) < 1
  \end{cases} $$
  $\alpha$ 为格式奖励权重（如 0.1）。

#### 3.3 DAPO 算法
- 对每个 prompt，采样 $G$ 个输出（如 $G=16$），计算群体内标准化优势 $\hat{A}_{i,t} = (R_i - \text{mean}(\{R_i\}))/\text{std}(\{R_i\})$。
- **优化目标**：
  $$ J_{\text{DAPO}}(\theta) = \mathbb{E}_{(\mathbf{q},\mathbf{a}) \sim \mathcal{D}, \{\mathbf{o}_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}}\left[ \frac{1}{\sum_i |\mathbf{o}_i|} \sum_{i=1}^{G} \sum_{t=1}^{|\mathbf{o}_i|} \min\!\Big( r_{i,t}(\theta) \hat{A}_{i,t},\, \text{clip}(r_{i,t}(\theta), 1-\epsilon_{\text{low}}, 1+\epsilon_{\text{high}})\hat{A}_{i,t} \Big) \right] $$
  其中 $r_{i,t}(\theta) = \frac{\pi_\theta(o_{i,t}|\mathbf{q},\mathbf{o}_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t}|\mathbf{q},\mathbf{o}_{i,<t})}$。
- **DAPO 特性**：解耦上下 clip 范围 ($\epsilon_{\text{low}}, \epsilon_{\text{high}}$)；过滤 accuracy=0 或 1 的 prompt，防止零梯度。
- **训练设置**：在 OPD 或 SFT checkpoint 上继续训练，多轮 RL 直至收敛。

### 4. 服务 ROI 优化

#### 4.1 上下文压缩
- **压缩器训练**：使用 GRPO，奖励由 LLM‑as‑a‑judge 提供。Judge 评分维度：可解性 $s\in\{0,1\}$，信息保留 $p\in[1,10]$，排序质量 $q\in[1,10]$。
- **奖励构造**：
  $$ r_{\text{judge}} = \begin{cases} 0.2 \bar{p} + 0.8 \bar{q}, & s=1 \\ 0.8 \bar{p} + 0.2 \bar{q}, & s=0 \end{cases} \quad (\bar{p}=p/10, \bar{q}=q/10) $$
  $$ r = \big( \alpha_{\text{comp}} \, r_{\text{comp}} + (1-\alpha_{\text{comp}}) \, r_{\text{judge}} \big) \cdot \lambda_{\text{ellipsis}} $$
  其中 $r_{\text{comp}} = \max(0, 1 - |\text{compressed}|/|\text{original}|)$，$\alpha_{\text{comp}}$ 权衡压缩率与质量，$\lambda_{\text{ellipsis}} \in [0,1]$ 惩罚截断。$s=1$ 时侧重排序质量。
- **效果**：输入长度缩短 >80%，R@3/N@3 不降。

#### 4.2 推理内化 (Implicit CoT)
- 在 RL post‑training 完成的 checkpoint 上，进行第二轮 RL，但策略直接输出排序结果（无 CoT），使用相同奖励。骨干已编码推理先验，此阶段仅调整输出路径。
- **结果**：在推理困难子集上，无 CoT 策略 R@1/N@1 略高于有 CoT，更深位置持平。部署模型无需生成推理，显著降低解码成本。

#### 4.3 系统优化
- **模型剪枝**：深度剪枝（层剪枝）后 knowledge distillation 恢复质量。
- **KV 缓存**：重新排列 prompt 顺序为 system → candidates → user history，候选集 KV 预计算一次并跨请求复用。

## 实验设置与结果

### 数据集
- 内部电商日志，单日训练集约 70k 用户会话，测试集连续 9 天 (02‑01 至 02‑09)。
- 冷启动设置：测试集用户 ID 100% 未见于训练，候选物品 >99% 未见，历史物品 93% 未见。
- 过滤：去重，交互少于 3 次的用户剔除。
- 基线：在线训练的点式 CTR 模型，每 60‑90 分钟更新。

### 主要指标
- **Recall@K** 和 **NDCG@K**（K=1,3,5）

### 主要结果
| 方法 | R@1 提升 | R@3 提升 | N@3 提升 |
|------|----------|----------|----------|
| GR2 vs. Legacy | +18.7% | +7.1%  | +9.6%  |

- 提升对测试规模（0.14x→100x）稳定，对模型陈旧（两周后）无衰减。
- 模型缩放：1.7B → 8B → 32B，收益单调递增未饱和。

### 消融与蒸馏效果
- **OPD 蒸馏**：1.7B 学生从 32B 教师恢复 82% 增益，相当于 2.6x 于 8B 无蒸馏，serving ROI 提升 ~15x。
- **上下文压缩**：80% token 削减，R@3/N@3 不降反微升。
- **推理内化**：第二次 RL 后无 CoT 策略在硬子集上 R@1/N@1 超越 CoT 策略 (0.3012 vs 0.2968)。
- **训练配方对比**：RL‑OPD 在排序和推理质量上均优于 RL‑only，前者避免推理退化。

### 案例研究
展示 GR2 基于物品属性（皮革、枪套）和点击模式推断用户意图，将“复古皮革警服”提至首位，基线排在第四。

## 思考与可参考价值

**局限与批判**：
- 实验仅基于内部数据，缺乏公开基准比较，影响可复现性。
- 依赖强师模型（32B）提供轨迹，实际使用中教师训练成本高。
- 上下文压缩器和推理内化需要额外训练步骤，增加工程复杂度。
- 多正例奖励设计假设标签准确，但在延迟转化、噪声标签场景可能不稳定。
- 防作弊机制针对身份排列，但可能遗漏其他奖励破解模式（如随机排列仍获得不低 AUC）。

**对电商/搜索推荐/Agent 的借鉴**：
- **语义 ID + Mid‑Training**：处理数十亿无语义 ID 物品的可行方案，冷启动场景优势明显（世界知识泛化）。
- **推理增强范式**：通过教师蒸馏赋予模型显式推理能力，RL 进一步优化排序目标，可迁移到搜索重排或对话式推荐。
- **OPD 蒸馏**：替代 SFT，解决工业规模训练坍塌和分布偏移，适用于任何教师‑学生知识迁移。
- **重排专用奖励设计**：AUC/NDCG 处理多目标，条件格式奖励防作弊关键，可直接复用在类似列表排序任务。
- **推理内化**：推理先验内化为隐式能力，实现无推理高吞吐，适合延迟敏感在线服务。
- **系统优化组合**：上下文压缩、KV 缓存、模型剪枝，实现端到端低成本部署。
