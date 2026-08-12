---
title: 'Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative
  Evolution'
title_zh: 孟德尔·哥德尔机：基于比较进化的递归自改进编码代理
authors:
- Changzhi Liu
- Yilun Liu
- Sikuan Yan
- Volker Tresp
- Yunpu Ma
affiliations:
- University of Electronic Science and Technology of China
- Ludwig Maximilian University of Munich
- Munich Center for Machine Learning
arxiv_id: '2608.07645'
url: https://arxiv.org/abs/2608.07645
pdf_url: https://arxiv.org/pdf/2608.07645
published: '2026-08-06'
collected: '2026-08-12'
category: Agent
direction: 自改进编码Agent · 比较进化
tags:
- self-improving agents
- comparative evolution
- reaction-norm mutation
- cross-lineage hybridization
- coding agents
- archive-based search
one_liner: 引入反应范型突变和跨谱系杂交，利用存档中多任务、多谱系比较证据提升自改进编码代理的性能与泛化性
practical_value: '- **反应范型突变的迁移**：在电商搜索推荐Agent中，同一Agent往往同时服务于搜索、推荐、广告等多个场景。可以借鉴MGM的思路，比较该Agent在不同场景下的成功/失败轨迹，识别跨场景的通用缺陷（如检索总召回不足、融合逻辑缺陷），从而进行针对性修复，而非孤立地针对单个场景调优。

  - **跨谱系杂交的应用**：在A/B实验或多策略线上共存时，可以将表现更好的Agent视为参照，将其在相同任务（如同一query、同一用户）上的成功轨迹作为对比信号，指导表现较差的Agent自我改写，实现策略能力的定向迁移，避免从头探索。

  - **失败任务池的加权采样**：维护一个全局的“高信息量失败任务池”，在评估Agent时优先采样这些任务，可以更高效地暴露弱点、促成跨Agent对比。这可以应用于构建在线评估流量的分层采样策略，用更少的流量诊断出Agent的真正短板。

  - **存档式自改进框架**：将Agent谱系树与评估轨迹统一存储，用Thompson采样在评估与扩展之间动态分配预算，既保证探索又利用高潜力节点。这种框架可以直接用于自动化优化推荐系统的推理链、工具调用等工作流，通过代码层面的自修改实现持续进化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有自改进编码代理在每一步自我修改时只利用单条失败轨迹，忽略了存档中积累的大量比较证据——同一代理在多任务上的表现模式（反应范型）和不同代理在同一任务上的行为差异。受孟德尔遗传学受控比较的启发，本文提出 Mendel Gödel Machine (MGM)，用两类新自修改算子更充分地复用历史轨迹，提升自改进效率与泛化性。  

**方法**  
- 在存档树搜索框架（HGM）基础上，将扩展算子拆分为三种：  
  - **克隆突变**：标准单轨迹失败修改；  
  - **反应范型突变**：同一代理在多任务上的轨迹对比，诊断跨任务的通用缺陷；  
  - **跨谱系杂交**：不同代理在同一任务上的轨迹对比，实现能力迁移。  
- 维护全局 **失败任务池**，采样新任务时提高失败任务的权重，增加任务重叠，为比较算子创造条件。  
- 扩展时根据可用性采样算子，权重可配；评估与扩展的调度沿用 Thompson 采样。  
- 在加性适应度景观模型中，理论证明比较算子能压缩候选缺陷集，提高有效修复概率，加速收敛。通过蒙特卡洛模拟验证了不同修复概率比和初始难度下的鲁棒性。  

**关键结果**  
- **性能**：在 SWE-bench Verified 和 Polyglot 上，相同 200 次评估预算下，MGM 分别达到 78.3%（初始 68.3%，HGM 73.3%）和 93.2%（初始 50.8%，HGM 77.9%），提升显著。  
- **跨基准泛化**：Polyglot 进化的支架零样本迁移至 SWE-bench Pro 和 Multilingual，分别提升 +10.0 和 +13.3 个百分点，HGM 出现负迁移。  
- **跨模型迁移**：Qwen3.6 上进化的支架替换为 DeepSeek-V4-Pro 后，完整 Polyglot 准确率达 96.9%，支架级改进可被更强的骨干模型放大。  
- **消融**：去掉任一比较算子均导致性能明显下降，且两者 token 开销与克隆突变相近，增益来自诊断质量而非算力堆砌。  

**核心一句话**：通过刻意比较同一个体在不同环境下的表现以及不同个体在同一环境下的表现，自改进代理能更准确地定位缺陷并实现可跨基准、跨模型迁移的支架级进化。
