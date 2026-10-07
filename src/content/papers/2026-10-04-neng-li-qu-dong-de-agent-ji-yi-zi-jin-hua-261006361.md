---
title: Capability-Driven Self-Evolution of Agent Memory
title_zh: 能力驱动的 Agent 记忆自进化
authors:
- Yaoqi Chen
- Yuru Feng
- Qianxi Zhang
- Baotong Lu
- Jianan Lu
- Zhirui Wang
- Shusen Xu
- Zewen Jin
- Zengzhong Li
- Cheng Li
affiliations:
- University of Science and Technology of China
- Microsoft
- University of California, San Diego
arxiv_id: '2610.06361'
url: https://arxiv.org/abs/2610.06361
pdf_url: https://arxiv.org/pdf/2610.06361
published: '2026-10-04'
collected: '2026-10-07'
category: Agent
direction: Agent 记忆自进化 · 能力驱动
tags:
- memory self-evolution
- LLM agents
- capability-driven
- executable memory programs
- long-term memory
one_liner: 将整体性能搜索分解到能力维度，通过能力专家与痕迹引导集成，在百万token基准上比最强基线高7.83–10.54个百分点
practical_value: '- 把记忆系统拆成 Extraction / Indexing / Planning / Retrieval / Answer
  五个可独立修改的接口，让 LLM 只局部改出问题的组件，避免整体重写；可直接迁移到电商 Agent 的记忆或检索模块自动调优。

  - 不要只用整体指标指导进化，按能力维度（事实检索、时间追踪、偏好提取、多会话合成、对抗性）各自维护 specialist，保留被整体分数掩盖的局部增益；这在多目标冲突严重的推荐/广告系统中尤其有用，能防止某个目标的小改进被其他目标回退淹没。

  - 依赖感知能力选择：量化一个能力的缺陷对另一能力任务的错误压力（公式 1-6），优先改瓶颈能力；可用于多目标排序/召回策略的自动搜索调度。

  - 用 paired differential cases 比较 base 与 specialist 在同一批 case 上的行为差异，再让 coding model
  合并互补收益；适合集成多个推荐策略或记忆模块，比直接选择未探索方向更可靠。

  - 工程降本技巧：紧凑诊断上下文可减少 44% token，revision-aware execution reuse 跳过未改动组件；适合工业级 Agent
  pipeline 的低成本自动调优。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

记忆自进化用任务反馈迭代改进 LLM Agent 的 executable memory program。现有方法普遍采用 holistic evolution：用混合反馈推断修改方向、用整体分数判断进步。这会导致两个问题：优化方向模糊、能力级增益被隐藏。例如，拓宽检索可能提升多会话推理但加重过度个性化；图 1(a) 显示 80.5% 的整体无增益改进其实至少提升了一项能力。整体分数一压缩，许多有用机制在平台期被丢弃，探索被限制在局部。

## 方法关键点

PRISMEM 将进化空间从单一整体性能提升到多个能力维度，分三阶段：

- **冷启动**：用能力维度诊断指标表快速建立平衡基座程序。
- **能力细化**：对五个能力（事实检索 F、时间追踪 T、偏好提取 P、多会话合成 M、对抗 A）分别维护 specialist。**依赖感知能力选择**用公式量化直接缺陷与跨能力错误压力，优先选择能带动其他能力的瓶颈；**历史引导诊断**挑选当前失败但过去程序能处理的“回归见证”案例，并折扣重复出现的案例与能力组合，扩大诊断覆盖。
- **痕迹引导集成**：从全局最优程序出发，用 paired differential cases 比较 base 与各 specialist 的行为差异，让 planning model 制定逐步合并计划，再交给 coding model 执行，最多 3 轮。

工程上，用紧凑诊断上下文减少 44% token，利用 revision-aware execution reuse 跳过未改动组件。

## 关键实验

在 BEAM-1M 和 LongMemEval-M 两个百万 token 记忆基准上，用 Qwen3.8-27B 做任务/反思/编码模型，与 Mem0、A-MEM、HippoRAG2、SimpleMem、LightMem、M*、EvolveMem 对比。PRISMEM 比最强基线分别提升 **10.54 pp**（BEAM）和 **7.83 pp**（LongMemEval）。消融显示：去掉能力驱动进化掉 10.15 pp；去掉痕迹引导集成掉 3.16 pp；随机案例选择掉 5.26 pp。进化 token 开销与 M* 相当或更低。

## 最值得记住的一句话

把整体性能搜索提升到能力维度，保留被整体分数掩盖的局部增益，再通过行为对比合并，是记忆自进化突破平台期的关键。
