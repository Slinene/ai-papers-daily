---
title: 'Multi-View MoE: Letting Every Router Shape Expert Computation'
title_zh: 多视角 MoE：让每个路由头共同塑造专家计算
authors:
- Zelin Zhao
- Tianchi Ma
- Junyuan Shang
- Shuohuan Wang
- Dianhai Yu
affiliations:
- Baidu ERNIE Team
arxiv_id: '2610.40577'
url: https://arxiv.org/abs/2610.40577
pdf_url: https://arxiv.org/pdf/2610.40577
published: '2026-10-29'
collected: '2026-10-31'
category: Training
direction: 稀疏 MoE 多路由与视角混合
tags:
- MoE
- Multi-Router
- LatentMoE
- Expert Routing
- Sparse Mixture-of-Experts
- Training
one_liner: 通过多路由聚合与路由偏好驱动的专家输入混合，在固定专家预算下提升稀疏 MoE 选路与表达能力
practical_value: '- 如果线上大模型采用 MoE 推理，可在不增加专家 FLOPs 与 all-to-all 通信量的前提下，仅增加约 0.19%
  参数，通过多路由头求和与多视角输入混合获得稳定下游收益；对固定延迟预算的搜索/推荐大模型升级较友好。

  - 借鉴 score-conditioned input mixing：对每个选中专家，用其跨路由头的归一化 sigmoid 分数混合多个 latent view，在同一
  token 下让不同专家看到不同输入；实现时在 dispatch 前完成混合，保持通信量不变。

  - 路由诊断可复用：用 dense evaluation 计算所有专家输出 L2 norm 归一化后与 router score 的 Spearman 相关性，定位中深层选路与真实专家效用弱对齐的层；发现弱对齐后针对性地引入多路由或重新训练。

  - 从已有 LatentMoE 或类似 checkpoint 升级时，保留 backbone 投影为 View 1，其余视图用 ramp perturbation
  从零逐步放开，能在不明显破坏初期训练的情况下平滑加入多视角能力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
稀疏 MoE 模型每个 token 只激活少量专家，路由分数直接决定专家选择与输出组合。但密集评估所有专家后发现，单路由分数排序与真实专家效用排序的一致性较弱，尤其在中层和深层；未选中专家没有来自该 token 的直接任务梯度，选路错误可能自我强化。为了获得更丰富的选择信号并调节专家计算，已有方法要么需要额外预计算（如 activation-based routing），要么增加专家前向计算。论文目标是在保持 active expert 数、专家 FLOPs 和 all-to-all 通信量不变的前提下，改善选路并让路由偏好参与专家计算。

**方法关键点**  
- Multi-Router：使用 R 个独立初始化的 sigmoid 路由头，先对各路由头分数做 sigmoid 再求和，然后 top-k 选择；相比 logit 求和，post-sigmoid 求和保留了多个非线性评分函数，既允许某路由头的强偏好，也允许多路由头联合支持影响选择。
- Multi-View：将 R 个路由头与 K 个 latent views 一一对应；对每个选中专家 i，把它们各自的原始 sigmoid 分数跨路由头归一化，得到混合比例 a_{m,i}，再混合各 view 的投影结果作为该专家的输入。这样每个专家只执行一次前向，且输入同时依赖 token 和 expert。
- 输出门控与输入混合分离：输出 gate 用跨专家归一化的 summed score；输入混合用每个专家跨路由头归一化的比例，二者不共享 bias 和输出缩放。
- 初始化：View 1 复用 backbone 投影，其余视图从 ramp perturbation 逐步增强；参数总增量约 0.19%。

**关键实验与结果**  
在 24 层 10B-A1B LatentMoE backbone、top-8 routing、708B tokens 训练预算下：九个下游任务 unweighted mean 从 baseline 33.07 提升到 Multi-Router 33.69，Multi-View 进一步到 34.25，即全方法相对 baseline +1.18 pp，相对 Multi-Router +0.56 pp。路由诊断显示 Multi-Router 将 router score 与 normalized expert-output norm 的全局 Spearman 相关从 0.1245 提升到 0.1346，相对 +8.1%，在单路由对齐最差的第 20 层相对提升约 57.7%。干预实验在 final MoE layer 固定 expert 选择与输出 gate，仅 permute 跨专家的 view 混合比例，NLL 上升 0.01340 nats/token，证明模型确实使用了 expert-token 相关的输入差异。

最值得记住的一句话：路由偏好不仅能决定选哪个专家，还可以构造每个专家看到什么输入；在固定 MoE 预算下，这条“偏好信号复用”路线同时改善选路和专家计算。
