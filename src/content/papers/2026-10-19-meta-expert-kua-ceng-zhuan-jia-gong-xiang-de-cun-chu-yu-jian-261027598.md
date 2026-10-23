---
title: 'Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient
  MoE'
title_zh: Meta Expert：跨层专家共享的存储与检索高效 MoE
authors:
- Ermo Hua
- Xiangyu Hong
- Baiting Wu
- Che Jiang
- Haozheng Hou
- Yicheng Gu
- Hanjing Wang
- Qirui Zeng
- Ming Zhang
- Ning Ding
affiliations:
- Tsinghua University
- Shanghai AI Laboratory
arxiv_id: '2610.27598'
url: https://arxiv.org/abs/2610.27598
pdf_url: https://arxiv.org/pdf/2610.27598
published: '2026-10-19'
collected: '2026-10-23'
category: LLM
direction: MoE 架构优化 · 跨层参数共享
tags:
- MoE
- Cross-Layer Sharing
- Parameter Efficiency
- Expert Redundancy
- Residual Pathways
- LLM Training
one_liner: 用跨层共享的 Meta Expert 替代层私有专家，在 Iso-FLOPs 下仅需 70-80% 专家数即可匹配 Vanilla MoE
practical_value: '- **推荐/广告大模型 MoE 层可直接复用**：如果业务中训练 MoE 结构的 LLM（如生成式推荐、用户行为序列建模），可将中间的若干层专家改为跨层共享的
  Meta Expert 池，保持每层激活专家数不变，FLOPs 不变，但能节省 20-30% 专家存储参数，降低显存占用和加载成本。

  - **多场景/多域专家共享借鉴拓扑设计**：论文发现“前两层 + 最后两层保持 Local Expert，中间层共享 Meta Expert”以及“Meta
  池分成 2 个 interleaved 子池”效果最好。这可以迁移到多域推荐模型：边界层保留场景特有专家，中间层共享通用专家池，既保留差异化又减少冗余。

  - **专家冗余度量可用于模型诊断**：用线性 CKA 的 Gini 系数衡量专家功能重叠，可以搬到推荐模型的分析中，识别哪些塔/专家在做重复工作，指导剪枝或共享决策。

  - **双向 residual pathway 视角启发架构设计**：共享参数层相当于在单次前向中让浅层和深层相互读取同一存储，等价于增加隐式跨层连接。在用户表征学习或序列建模中，可以考虑类似的“共享模块”让不同深度互相访问，而不必显式增加跳跃连接。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
随着 LLM 规模增长，MoE 成为平衡参数规模与计算效率的主流方案。但主流分层架构中，不同层的专家虽然拓扑独立，存储的知识却高度相似，存在显著层间冗余。已有 Looped Transformer 通过循环复用参数减少冗余，但引入了额外串行深度和延迟。论文探索另一种参数循环方式：保持每层计算量和递归次数不变，将专家跨层共享，称为 Meta Expert。

**方法关键点**
- 将每层私有的 Local Expert 替换为跨所有层共享的 Meta Expert 池和共享 router，每层仍激活相同数量的专家，保证 FLOPs 不变。
- 系统研究了 Meta/Local 专家数量比例（0%-100%）、每层激活比例（25%-75%）、拓扑结构（是否所有层都含 Meta，是否将 Meta 专家分层组织为若干子池）。
- 最优配置为：Meta 专家总数占比 75%，每层激活 4 Meta + 4 Local；前两层和最后两层仅用 Local Expert；Meta 池分为 2 个 interleaved 子池。
- 理论分析表明，共享专家池使得所有层的写入（梯度更新）和读取（前向计算）都针对同一存储，等价于在激活层面提供双向 residual 通路：深层可直接检索浅层写入的内容，浅层也能通过共享参数获取深层信息，超越了传统仅前向的残差连接。

**关键结果数字**
- 在 Iso-FLOPs 条件下，Meta Expert 模型仅用 70-80% 的专家数量（或 75-90% 总参数）即可达到 Vanilla MoE 的交叉熵损失，且节省比例随模型深度和规模增大而提高。
- 6B-A1.6B、200B tokens 训练后，Meta Expert 变体在 MMLU、C-Eval、CMMLU、TriviaQA、BBH、OpenBookQA 上总体优于 Vanilla baseline。例如 MR75+Loop2 在 MMLU 上 0.4175 vs 0.4087，MR75+F2L2 在 C-Eval 上 0.4487 vs 0.4354，MR75+F2L2+Loop2 在 TriviaQA 上 0.2042 vs 0.1924。
- 专家冗余指标（CKA 谱 Gini 系数）显示 Meta Expert 显著降低冗余，且下降趋势随训练计算量增加而更明显。

**最值得记住的一句话**：跨层共享专家实质上是把层间冗余转化为有效容量——在单次前向中提供双向 residual 通路，而不仅是省参数。
