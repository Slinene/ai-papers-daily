---
title: Closed-Form Spectral Regularization for Multi-Task Model Merging
title_zh: 多任务模型合并的闭式谱正则化方法
authors:
- Yongxian Wei
- Runxi Cheng
- Xingxuan Zhang
- Li Shen
- Chun Yuan
- Peng Cui
- Dacheng Tao
affiliations:
- Tsinghua University
- Sun Yat-sen University
- Nanyang Technological University
arxiv_id: '2606.07289'
url: https://arxiv.org/abs/2606.07289
pdf_url: https://arxiv.org/pdf/2606.07289
published: '2026-06-05'
collected: '2026-06-08'
category: Other
direction: 模型合并 · 谱正则化
tags:
- Model Merging
- Spectral Regularization
- Closed-form Solver
- Multi-task Learning
- Data-free
one_liner: 将模型合并视为带噪线性逆问题，用闭式谱滤波替代迭代优化，加速28-72倍且精度不减
practical_value: '- **多任务模型合并的加速与显存优化**：电商推荐系统中常需合并多个专用模型（如CTR、CVR、多目标专家），SWUDI/SWUDI-A
  的闭式解可替代 WUDI 的数百步 Adam 迭代，将合并时间从数十分钟降至分钟级，显存占用减少 50%，适合线上快速迭代与多模型部署。

  - **噪声抑制的谱截断策略**：合并不同任务向量时，小特征值方向会放大代理噪声，硬截断（hard truncation）可以将其直接归零，防止合并时性能退化。这一思路可直接用于推荐场景中合并多个
  LoRA 适配器或任务向量，提升多任务融合稳定性。

  - **自适应层维秩选择**：SWUDI-A 无需手动设置全局秩阈值，利用参与比率平方根规则或 Gavish-Donoho 阈值自动决定每层保留的特征值个数，适配不同架构（视觉/语言/多模态）。在推荐模型中，不同层对任务冲突的敏感度不同，自适应规则能减少调参成本，提高合并鲁棒性。

  - **数据无关与测试时适配结合**：闭式谱合并结果可与 AdaMerging 等测试时适应方法正交，作为 data-free 初始化进一步提升精度。在 agent
  多智体系统中，可先融合专家模型再根据少量在线反馈微调，兼顾效率和效果。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

**动机**  
当前最优的多任务模型合并方法（WUDI、OptMerge）需要数百步迭代优化，耗时巨大且显存占用高，但其闭式伪逆解（DC†）却显著劣于早停的迭代解，原因一直未明。本文重新审视该问题，揭示迭代求解器本质上扮演了隐式谱正则化的角色——它通过早停抑制了法方程小特征值方向上的代理噪声放大。基于此，将模型合并形式化为一个带噪线性逆问题，提出闭式谱滤波估计器，以取代迭代优化。

**方法要点**  
- **线性逆问题建模**：将逐层 WUDI 目标转化为法方程 τC=D，其中 C 为任务向量内积的叠加，D 为右端项。直接求逆（τcf=DC†）会因小特征值 λk 放大噪声 ξk 而退化。
- **统一谱滤波估计器**：定义有方向性滤波 hk，估计器为 τ̂_h = τ_init + (D−τ_init C) C_h†，其中 C_h†=Q diag(hk/λk) Q^T。不同 hk 对应不同正则化：全1即伪逆，指数衰减匹配梯度流早停，硬截断消除尾部噪声。
- **SWUDI**：组合软指数滤波（s_t(λ)=1−e^{−tλ}）与硬截断（mk=1[k≤K]），形成 hk=mk·s_t(λk)，既保留了迭代早停的正则效果，又硬性去除噪声方向。
- **SWUDI-A**：自适应变种，用层级别谱规则自动确定 Kℓ：参与比率平方根规则（K=(∑σk)²/∑σk²）适用于重尾谱，Gavish-Donoho 阈值适用于尖峰加噪声谱，完全免除全局秩超参数。

**实验结果**  
在 4 个通用基准（CLIP-ViT TA8/TALL20、Flan-T5 GLUE、Llama-3.2-3B MergeBench）和自建多模态合并基准（InternVL2.5-1B、Qwen2-VL-7B 的视觉问答、几何、图表、OCR、指代消解能力合并，以及图像/音频/视频模态合并）上评估。SWUDI/SWUDI-A 在绝大多数设置下匹配或超越迭代基线 WUDI/OptMerge，同时将合并时间缩短 28–72 倍（如 CLIP-B/32 从 86.3s 降至 2.8s，Llama-3.2-3B 从 5126s 降至 70.7s），峰值 GPU 显存最高降低 50%。SWUDI-A 在无需额外调参的情况下，平均精度达到 CLIP-ViT TA8 85.53%，Flan-T5 GLUE 82.98%，多模态综合 QA 70.58%，与调参版 SWUDI 相当。进一步与测试时适应 AdaMerging 结合，精度可再提升 0.2–2.5 个百分点。

**核心结论**  
有效合并无需依赖长优化轨迹：一旦逆问题被形式化，核心设计选择就是施加的谱滤波器。闭式谱正则化取代迭代，在精度不减的前提下实现大幅加速和内存节省。
