---
title: 'RecRSI: Mechanism-Guided Discovery of Recommendation Algorithms'
title_zh: RecRSI：机制引导的推荐算法自动发现
authors:
- Tingran Gan
- Zhouziyue Lu
- Dian Jin
- Tao Li
- Yang Gao
- Ming Liu
- Weiwen Liu
- Jianghao Lin
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- Meituan
arxiv_id: '2611.02487'
url: https://arxiv.org/abs/2611.02487
pdf_url: https://arxiv.org/pdf/2611.02487
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 自动推荐算法发现 · 机制假设
tags:
- Automated Algorithm Discovery
- Recommendation Systems
- LLM Agents
- Mechanism Hypothesis
- Experiment Feedback
- Search Efficiency
one_liner: 用机制假设组织推荐算法搜索，在16个设置上平均NDCG@5相对初始模型提升8.48%
practical_value: '- 在推荐模型自动迭代或人工算法迭代中，把每次实验从“改一个候选程序”升级为“机制假设”：记录 reference design、changed/unchanged
  mechanisms、rationale、expected observation 和实际结果。失败实验可以不丢弃成功设计，而是把失败转化为下一个假设，例如 MoRec
  搜索中 pairwise margin 回归后恢复 BCE+pairwise 并测试 cosine-temperature scoring，最终 NDCG@5
  从 0.3438 提升到 0.4097。

  - 为排序/召回模型建立可组合的 MechSpace：把模型拆成 scoring、objective、representation、architecture、sampling
  等原语，并约束 composition rules 和 effect path。这样 LLM 生成的改动更易落地和校验，避免无效候选；自动生成 space 在该文实验中比人工设计
  space 的最终 NDCG@5 高 19.65%。

  - 在 LLM agent 搜索中采用固定角色覆盖和 stable tie-breaking 的 proposal 选择策略，避免早期过度偏向某一类 proposal；同时保留继续搜索而非
  restart 的预算，该文 continuation 在 24 次评估中比两个 12 次 restarts 在多个 block 上更高，且后段仍能发现新的 scoring+objective
  组合。

  - 对排序模型，显式共享 training 和 ranking 的 scores 是有效干预点，例如 cosine-temperature scoring 与
  label smoothing 组合，或 margin-based pairwise objective 与 focal weighting 的替换；业务中可优先搜索
  scoring-objective 兼容组合。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐算法设计需要协调表征、打分函数、学习目标、优化过程等相互依赖的机制。现有自动算法发现多以候选程序为单位，难以定位该改哪些机制、如何复用失败实验的上下文，导致搜索效率低。RecRSI 用机制假设作为组织单位，把每次实验同时变成算法干预和可积累的研究问题。

**方法关键点**：
- **MechSpace**：从初始源码和任务接口生成可实现的 primitives 和组合规则，覆盖 representation、scoring、objective、update、architecture、sampling 等轴。每个 primitive 明确 effect path，说明改动参与训练还是预测。生成后由 LLM reviewer 检查覆盖、冗余、可组合性，再通过确定性 assembler 校验 schema 和 mutation targets。
- **Research Line**：四种角色组成 hypothesis pool——Mechanism Composer 提出组合，Lineage Refiner 发展已有方向，Falsification Designer 构造解释对比，Frontier Architect 探索未覆盖方向。固定 selector 按角色覆盖和优先级分配实验机会。
- **Mechanism Feedback**：将实验结果关联到假设、reference design、changed/unchanged mechanisms、性能差和成本，更新共享研究状态。后续假设可以基于成功设计的 reference，并用失败实验指导新干预。

**关键实验**：在 SASRec、MoRec、BERT4Rec、NGCF 四个初始推荐器和 Amazon CDs、Electronics、Office、MovieLens-1M 四个数据集共 16 个设置上评估。对比 RecHarness、DeepEvolve、OpenEvolve、ShinkaEvolve、Self-EvolveRec。RecRSI 相对初始算法平均提升 NDCG@5 8.48%、HR@5 6.88%；相对各设置最强竞品平均提升 NDCG@5 2.60%、HR@5 2.20%。消融显示显式 MechSpace + Mechanism Feedback 的交互效应为 +0.6064 pp；自动生成的 MechSpace 比人工设计 space 高 19.65% NDCG@5；continuation 搜索比 restart 更能发现后段组合收益。

**最值得记住的一句话**：把每次实验写成“改什么机制、为什么改、期望观察到什么”，让失败和成功都能成为下一次设计决策的证据。
