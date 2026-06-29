---
title: 'From Bootstrapping to Sequence Modeling: A Unified Generative Framework for
  Personalized Landing-Page Modeling'
authors: Fan Li, Chang Meng, Jiaqi Fu, Shuchang Liu, Tianke Zhang, et al. (9 人)
date: 2026-06
venue: arXiv
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: 将个性化着陆页选择（PLPM）建模为序列决策问题，用 Decision Transformer 捕捉跨会话长程依赖，避免马尔可夫假设和 TD 自举误差。通过
  L-RTG 模块提供日级全局消费目标，HRM 模块分解会话奖励以消除信用模糊，实现日级轨迹的统一生成。
paperUrl: https://arxiv.org/abs/2606.27865
codeUrl: null
tags:
- Decision Transformer
- Offline Reinforcement Learning
- Page Navigation
- Long-Horizon Credit Assignment
- Constrained Optimization
unverified: true
---

## 核心思路
传统 CQL 方法在着陆页推荐中存在马尔可夫假设失效和 TD 学习自举误差累积问题。本文提出 GLAN，将 PLPM 形式化为序列建模任务，采用 Decision Transformer 直接建模日内会话轨迹，避免自举误差与 Markov 限制。同时设计两个关键模块：L-RTG 预测用户日总消费时间作为全局回报指引，HRM 将会话奖励分解为页面级消费与跳出风险，提供精确局部监督，二者协同提升长期指标。

## 整体实现思路
在线服务流程：
- 每日首次登录：
  1. L-RTG 模块预测当天预期总 app 使用时间，作为初始 RTG `R_1`。
  2. 初始化轨迹列表 `τ` 为空。
- 每次 app 进入（新会话）：
  3. 根据当前状态 `s_t`、剩余 RTG `R_t` 和历史轨迹 `τ_{<t}`，GLAN（因果 Transformer）自回归输出动作 `a_t`（选择落地页：Following/Explore/Featured）。
  4. 执行动作，用户会话结束，收集行为日志。
  5. HRM 模块根据会话日志计算精细化奖励 `r_t = (1 - ŷ_sw) * Σ_j Ť_j`。
  6. 更新剩余 RTG：`R_{t+1} = R_t - r_t`。
- 重复步骤 3-6 直至当日不再有会话。

离线训练三阶段：
1. 训练 L-RTG：利用历史 30 天序列（daily session freq & usage time）预测下一天使用时间与频次，带约束优化。
2. 训练 HRM：从日志中提取页面消费时长与跳出标签，监督多任务学习。
3. 训练 GLAN（DT）：用 HRM 为每条离线轨迹计算逐会话奖励，构建完整 (R_t, s_t, a_t) 序列，以教师强制方式训练动作预测。

## 子模块实现（可复现细节）

### 1. L-RTG 模块：日级 RTG 预测
**输入**：
- 用户特征 `x_i`（年龄、地域、活跃度等），统计特征 `t_i`（7/30 天消费统计），历史行为序列 `se_i = {v_{i,1},..., v_{i,L}}`，`L=30` 天，每个 `v_{i,t}` 包含当日会话频次 `y_session` 和总使用时间 `y_wt`。
- 标签：下一天的 `y_wt_i` 和 `y_session_i`。

**输出**：预测值 `ŷ_wt_i`（用作初始 RTG `R_1`）和 `ŷ_se_i`（仅辅助训练）。

**架构**：
1. 嵌入层：用户特征 `x_i` 和统计特征 `t_i` 分别经 embedding 得到 `e_x_i`, `e_t_i`，拼接为上下文嵌入 `e_context_i = Concat(e_x_i, e_t_i)`。
2. 历史序列嵌入：`H_i = transform(se_i) ∈ R^{L×d}`，`d` 为嵌入维度。
3. 周期感知注意力：
   - 查询：`q_i = e_context_i W_Q ∈ R^{d_k}`
   - 键：`K_i = H_i W_K ∈ R^{L×d_k}`
   - 周期偏置：`b_period[t] = B_week[Δ_t mod 7] + B_dist[bucket(Δ_t)]`，`B_week ∈ R^7`, `B_dist ∈ R^B`（B 为时间分桶数，非均匀）。
   - 注意力分数：`w_i = (q_i K_i^T)/√d_k + b_period`
   - 聚合值：`V_i = H_i W_V ∈ R^{L×d_v}`，输出序列表示 `e_p_i = softmax(w_i)·V_i`。
4. 用户表示：`u_i = Concat(e_context_i, e_p_i)`。
5. 序列动态建模：对 `H_i` 加绝对位置编码 `P`，送 Transformer Encoder 得 `H_i^d`，再经 AttentionPooling 得趋势向量 `e_d_i`。
6. 自适应门控（MoE 风格）：
   - 从 `u_i` 生成 `M` 个专家 `{d_i_m}_{m=1}^M`（如 MLP）。
   - 两个任务（wt, se）各有门控：`g_i^k = Softmax(W_g^k (e_d_i || u_i) + b_g^k)`，`W_g^k ∈ R^{M×d}`, `b_g^k ∈ R^M`。
   - 输出组合：`z_i^k = Σ_m g_i^k(m)·d_i_m`。
7. 任务塔：`ŷ_wt_i = softplus(h_wt(z_i^wt))`，`ŷ_se_i = softplus(h_se(z_i^se))`（保证非负）。

**训练损失**（约束优化）：
主损失：Huber 损失（δ 阈值）
```
L_wt = huber(y_wt_i, ŷ_wt_i) = {
  0.5*(y - ŷ)^2          if |y-ŷ| ≤ δ
  δ*(|y-ŷ| - 0.5δ)      else
}
```
约束：
- `L_se = MSE(y_se_i, ŷ_se_i)`
- 结构一致性损失：`L_rel = [ŷ_wt_i - a·ln(1+ŷ_se_i) - b]^2`，其中 a,b 从数据统计拟合（见图 2(a)）。

Lagrangian 对偶问题：
```
min_Θ max_{λ_se,λ_rel≥0} L_wt_bar + λ_se*(L_se_bar - ε_se) + λ_rel*(L_rel_bar - ε_rel)
```
对偶变量更新（EMA 平滑）：
```
̃L_k ← ρ·̃L_k + (1-ρ)·L_k_bar    (k∈{se, rel})
λ_k ← clip([λ_k + η_λ*(̃L_k - ε_k)]_+, 0, λ_max)
```
超参：`δ`（Huber 阈值），`ε_se`, `ε_rel`，`η_λ`，`ρ`，`λ_max`。

**推理**：仅使用 `ŷ_wt_i` 作为当天初始 RTG `R_1`。

### 2. HRM 模块：会话级分层奖励
**输入**：
- 用户特征 `x_i`，上下文特征 `c_i`（实时日内消费统计、关注博主直播数、当日已进入次数等），会话特征 `v_i`，落地页嵌入 `k_i`。
- 标签：`Y_i = {T_i^1, T_i^2, T_i^3, y_sw_i}`，其中 `T^j` 为第 j 类页面（可能对应 Featured/Explore/Following）的消费时长，`y_sw∈{0,1}` 表示是否快速离开落地页（若落地页停留时长 < τ，则 `y_sw=1`，τ 为阈值）。

**输出**：预测值 `Ť_i^j (j=1,2,3)` 和 `ŷ_sw_i`，组合为奖励 `r_i = (1-ŷ_sw_i)·Σ_j Ť_i^j`。

**架构**：
1. 嵌入：所有特征通过对应 embedding 表得到 `e_x_i, e_c_i, e_v_i, e_k_i`，维度均为 d。
2. 页面特征选择（目标注意力）：
   将 `e_x_i, e_c_i, e_v_i` 拼接成 F 个 field 级嵌入 `e_o_i ∈ R^{F×d}`，使用落地页 `k_i` 对应参数计算注意力：
   ```
   w_i = Softmax(W_k e_k_i + b_k)  # W_k ∈ R^{F×d}, b_k ∈ R^F
   e_u_i = Σ_{j=1}^F w_i(j)·e_o_i,j
   ```
   然后 `f_i = Concat(e_u_i, e_k_i)`。
3. MMoE 共享底层与 4 个任务塔：
   4 个门控网络输出 `z_1, z_2, z_3, z_sw = MMoE(f_i)`。
   三个时长为 softplus 激活，跳出为 sigmoid：
   ```
   Ť_i^j = softplus(h_j(z_j)), j=1,2,3
   ŷ_sw_i = σ(h_sw(z_sw))
   ```

**训练损失**：
- 回归损失（Huber）：`L_reg = Σ_{j=1}^3 huber(Ť_i^j, T_i^j)`
- 跳出风险 Focal Loss（带权重 γ）：
  ```
  L_sw = -1/|B| Σ_i [ y_sw_i (1-ŷ_sw_i)^γ log(ŷ_sw_i) + (1-y_sw_i) (ŷ_sw_i)^γ log(1-ŷ_sw_i) ]
  ```
- 总损失：`L_total = L_reg + λ·L_sw`

超参：F（特征域数量），d，τ（跳出门槛），γ（focal 参数），λ（平衡系数）。

### 3. GLAN 主模型：Decision Transformer
**轨迹表示**：
每日一条轨迹 `τ = (R_1, s_1, a_1, ..., R_N, s_N, a_N)`，其中：
- `R_t`：剩余回报（float），初始由 L-RTG 提供，后续更新减法。
- `s_t`：状态向量（用户实时特征 + 日内已消费统计等）。
- `a_t`：离散动作 (0/1/2 对应三个页面)。

**模型输入**：
对每个 token 三元组，投影到 d_model 维度：
- `e_R_t = Linear_R(R_t)`
- `e_s_t = Linear_s(s_t)`
- `e_a_t = Embedding(a_t)`
然后加位置编码或学得位置嵌入，输入 causal Transformer（仅向前注意力）。

**训练**：
- 使用完整离线轨迹，以教师强制方式预测下一个 token 的动作。损失为交叉熵：
  ```
  L_act = -Σ_{t} log π_θ(a_t | R_t, s_t, τ_{<t})
  ```
- RTG 在训练时按 HRM 提供的精细化奖励计算：`R_t = Σ_{k=t}^N r_k`。
- 训练时可对 RTG 做归一化（如除以最大奖励等）以稳定训练。

**推理**：
- 第 t 步输入当前序列 `(R_1,s_1,a_1,...,R_t,s_t)`，Transformer 输出 `a_t` 的 logits，采样或 argmax 得到动作。新动作 a_t 执行后，更新 `R_{t+1}=R_t - r_t`，续接到序列。
- 使用 KV‑cache 加速，每次新增一步只计算新增 token 的注意力。

**超参/维度**：
- 状态 s_t 维度：取决于特征工程，典型百维级。
- 嵌入维度 d（L-RTG 和 HRM）：论文未明确，可设如 128。
- Transformer 层数、头数、隐藏维度：在工业部署中可能较小（如 2 层，4 头，d_model=128）。
- 序列最大长度 N：日会话数通常 < 100。

## 实验设置与结果
**数据集**：快手短视频平台真实用户日志。
- 日级数据：两月日志，每个样本包含 30 天历史序列（日会话频次和 APP 使用时间）及次日标签。
- 会话级数据：实时流数据，每个会话完整页面序列及页面消费时长、跳出标签（阈值 τ 依业务设定）。

**指标**：
- 核心指标：DAU（日活）、LT（生命周期，30 日回头率指标计算）、APP 使用时长、观看时长、视频观看数。
- PLPM 特化：页面跳出率（Page Drop-off Ratio）、各页面有效进入频次。
- 平台约束：延迟（Latency）。

**基线**：在线基线 KAN (CQL)，采用保守 Q 学习，逐小时更新。

**在线 A/B 测试**：
- 持续 56 天（前 14 天 AA，后 42 天 AB），5% 流量。
- 结果（最后 7 天均值）：

| 指标 | GLAN vs Baseline |
|------|------------------|
| DAU | **+0.158%** |
| LT | **+0.108%** |
| APP 使用时长 | **+0.369%** |
| 观看时长 | **+0.394%** |
| 视频观看数 | **+0.469%** |
| 页面跳出率 | **-15.832%** |
| 整体有效页面进入频次 | **+1.079%** |
| 延迟 | +0.087% (可忽略) |

**消融实验**（在线 AB）：

| 场景 | APP 使用时长 | 观看时长 | 视频观看数 |
|------|------------|----------|-----------|
| GLAN | +0.369% | +0.394% | +0.469% |
| w/o L-RTG (用历史平均 RTG) | +0.137% | +0.175% | +0.158% |
| w/o HRM (用总会话时长) | +0.277% | +0.278% | +0.404% |

结论：L-RTG 缺失导致最大性能下降，表明全局目标指引至关重要；HRM 缺失也明显衰减，证明精细奖励对信用分配的必要性。

**页面分配分布**：
- GLAN 降低了 Featured Page 的垄断分配比例，提升了 Explore/Following 页面的分配，同时各页面有效进入频次均提升，说明策略挖掘了更多元意图而非简单随机分发。

## 思考与可参考价值
**局限**：
- 离线训练 DT 时依赖 HRM 标注的奖励序列，若 HRM 建模有偏，误差会传导至策略。未讨论 HRM 误差对最终策略的影响量化。
- RTG 条件策略的 OOD 问题：用户实际消费可能严重偏离预测 RTG，导致推理时模型输入分布漂移，文中 L-RTG 采用约束优化缓解但未做 OOD 鲁棒性分析。
- 论文未提供 DT 训练细节（如是否使用 RTG 缩放、梯度裁剪等），工业复现时需要额外调优。
- 长周期（多日）策略未涉及，日内建模未考虑跨日影响（RTG 仅当日）。

**可借鉴点**：
- **序列化决策新范式**：用 Transformer 直接建模完整轨迹，替代传统 RL 自举，对电商推荐、搜索重排等存在延迟反馈和强时序依赖的场景有推广价值。
- **分层回报分解**：将粗粒度用户行为（如总时长）拆解为场地消费与跳出风险，解决信用分配模糊问题，可用于信息流混排、广告投放组合优化。
- **带约束的 RTG 预测**：通过 Lagrangian 对偶强制预测结构一致性，可推广到需同时估计多目标（如时长、互动）并保持单调关系的场景。
- **工业部署思路**：离线训练三个模型，在线仅需 DT 推理和轻量 L-RTG/HRM 调用，延迟低（+0.087%），适合高流量系统。
