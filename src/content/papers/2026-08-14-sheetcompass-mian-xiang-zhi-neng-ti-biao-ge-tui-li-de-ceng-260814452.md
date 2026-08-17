---
title: 'SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning'
title_zh: SheetCompass：面向智能体表格推理的层次关系图框架
authors:
- Panjing He
- Mingyue Cheng
- Yucong Luo
- Li Li
- Xiaohan Zhang
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
arxiv_id: '2608.14452'
url: https://arxiv.org/abs/2608.14452
pdf_url: https://arxiv.org/pdf/2608.14452
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多Agent协同 · 层次图表格推理
tags:
- Hierarchical Graph
- Multi-Agent
- Spreadsheet Reasoning
- LLM
- Agentic Workflow
- Memory
one_liner: 将电子表格从扁平文本转为层次关系图，结合双级记忆与三Agent闭环，在SCB/SB/SheetRM上全面超越既有Agent方案
practical_value: '- 多表/多域结构化数据可建模为表节点+列节点的层次图：显式保留包含、邻接等结构边，再用语义相似度+LLM逻辑打分构建跨表语义边；商品表、订单表、广告报表等联合推理可直接复用，避免扁平序列丢失空间与跨表依赖。

  - 三Agent分工（Explorer 定位与子图提取 → Programmer 受图约束生成代码 → Reflector 用 checklist 校验执行状态）适合需要工具调用的长链路数据流水线，闭环校验显著减少语义错误。

  - 双级记忆：静态专家知识（业务规则、公式模板、工具修复经验）与动态推理经验（当前轨迹、错误日志，成功经验回流长期库）结合，能避免重复犯错，适合长表格/报表生成任务。

  - 用语义相似度筛选种子节点，再通过 BFS 提取共享子图进行上下文压缩，类似 RAG 中的上下文裁剪，可有效控制 prompt 长度，适合大规模表格/文档 Agent
  场景。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
电子表格是半结构化数据的常见载体，但 LLM 自动推理长期受困于信息扁平化：现有方法把多维表格线性序列化为 Markdown/JSON，丢失了 sheet 内行列空间拓扑和 sheet 间隐含依赖。人类专家靠视觉扫描快速恢复二维结构，而文本序列无法提供这种全局布局，导致跨表推理性能大幅下降。

**方法关键点**  
- **层次图构建**：将表格建模为两级顶点——表节点和列节点；列节点由表头名+代表性数据样本表示。边分为结构边（表到列的包含边、同表相邻列的邻接边）和语义边（列特征向量余弦相似度+LLM逻辑关系打分，混合得分超过阈值 α=0.85 才连边）。
- **双级记忆**：专家知识记忆存储领域规则、公式模板、工具使用修复经验；推理经验记忆记录当前任务轨迹、沙箱错误、校验未匹配，成功轨迹提炼后回流长期库，避免重复错误。
- **多Agent工作流**：Explorer 将指令拆成原子步骤，用语义相似度筛选种子节点，再通过 BFS 提取共享子图压缩上下文；Programmer 严格基于图内已验证节点生成 Python 代码并在沙箱执行；Reflector 把指令约束转成 checklist，比对执行后状态元数据，发现偏差触发迭代修正，最多 τ=2 轮。

**关键实验**  
在 SCB（221 样本）、SB（912 指令，每指令配 3 个测试用例）、SheetRM（180 任务取 50% 子集）上对比 Binder、VBA、OS-Copilot、SheetCopilot、SheetAgent。GPT-5 下，SheetCompass 在 SCB pass@1 达到 71.3%，SB hard restriction 22.0%，SheetRM pass@1 52.3%，均显著超过最强基线。消融显示：移除层次图导致 SCB pass@1 下降 14.9%、SheetRM 下降 10.9%、SB hard 下降 7.5%，为最大贡献组件。多表任务中语义边占比从单表的 18.7% 升至 29.9%，证明跨表语义链接对复杂任务更关键。

**最值得记住的一句话**：把表格建模为层次图而非扁平序列，是 LLM 可靠处理多表/跨表任务的基础；Explorer/Programmer/Reflector 分工+双级记忆能显著提升长链路表格推理稳定性。
