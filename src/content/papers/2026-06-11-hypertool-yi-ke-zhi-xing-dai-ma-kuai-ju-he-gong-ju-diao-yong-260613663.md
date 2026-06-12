---
title: 'HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents'
title_zh: HyperTool：以可执行代码块聚合工具调用，减少 Agent 上下文膨胀与推理碎片
authors:
- Yaxin Du
- Yifan Zhou
- Yujie Ge
- Jiajun Wang
- Xianghe Pang
- Shuo Tang
- Tuney Zheng
- Bryan Dai
- Jian Yang
- Siheng Chen
affiliations:
- Shanghai Jiao Tong University
- IQuest Research
- Beijing University of Aeronautics and Astronautics
arxiv_id: '2606.13663'
url: https://arxiv.org/abs/2606.13663
pdf_url: https://arxiv.org/pdf/2606.13663
published: '2026-06-11'
collected: '2026-06-12'
category: Agent
direction: 工具增强 Agent 的执行抽象与上下文管理
tags:
- Tool-Augmented Agents
- MCP
- Context Management
- Execution Abstraction
- Supervised Fine-Tuning
one_liner: 提出 HyperTool 可执行接口，将多步确定性工具调用封装为单个代码块，使模型可见执行粒度更粗，大幅降低上下文消耗并提升复杂工具使用准确率。
practical_value: '- **在 Agent 工程中封装工具子程序**：当工作流中包含一系列无歧义、不需高层推理的 API 调用（如搜索→过滤→聚合→排序）时，可像
  HyperTool 一样用代码块将其合并为单一对外动作，避免每步都往主线径写观察结果，大幅节省 token 开销。

  - **训练数据合成的策略**：借鉴其“组合任务构建＋轨迹展开＋多轮验证”流水线，可以自动生成高质量的工具使用 SFT 数据。关键点是强制约束来自真实工具返回值，并用执行过滤和证据一致性检查淘汰无效轨迹，确保模型学到正确的块边界与内部逻辑。

  - **统一动作空间优于混合接口**：消融实验表明，对中小模型让所有交互统一走 HyperTool 接口（而非原子调用与代码块混合）可避免动作空间异质性带来的认知负载，直接提高准确率。在电商
  Agent 设计中，如果模型需要同时处理简单 API 和复杂子流程，统一为代码执行入口可能是更好的选择。

  - **注意执行安全与超时设置**：实际部署时，代码块可能触发恶意行为或无限循环，务必引入沙箱隔离与严格的超时限制（尤其对复杂聚合块可给予更长的单次执行超时）。同时对关键中间返回值做必要日志，平衡可解释性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：当前基于 MCP 的工具增强 LLM Agent 普遍采用原子化逐步调用：每执行一个工具、拿到一个观察结果、写回主线径，导致即使只是局部确定性工作流（如“根据地址查坐标→根据坐标搜咖啡馆→计算时间差”）也被展开成多轮模型可见交互。这造成两大问题：一是观察值的累积导致上下文膨胀，二是模型被迫在高层推理和底层数据搬运之间反复切换，推理碎片化。现有压缩、剪枝、子 agent 等方法都只是在“事后”处理轨迹，未改变执行粒度。

**方法关键点**：
- **HyperTool 接口**：将工具调用抽象为一个可执行的 MCP 工具，输入是一段 Python 代码块。代码块内可以用原有 schema 调用任何工具，存储中间结果为局部变量，执行过滤、转换、汇总等操作，最终只返回一个块级观察值给主轨迹。原子调用被包含为特例（单调用块）。设计原则：只有需要高层推理、可能改变计划的结果才暴露到外部。
- **数据合成流水线**：① 基于真实实体种子，让教师模型在 MCP 环境中收集跨工具属性，生成只靠单个工具无法回答的组合性任务；② 按照“推理优先、块化执行、内部逻辑自包含”三大规则展开轨迹，并在展开时对旧工具响应做摘要压缩（保留数值/URL等关键信息），对失败的代码块进行本地修复；③ 用执行正确性过滤和 LLM 多数投票证据一致性验证，保留高质量轨迹。
- **监督微调**：在保留的 10,422 条轨迹上训练 Qwen3-8B/32B，损失仅作用于模型生成的推理和代码块部分。

**关键实验**：在 MCP-Universe 四个域（财务分析、仓储管理、位置导航、Web 搜索）上评估，HyperTool 将 Qwen3-32B 平均准确率从 15.69% 提高到 35.29%，Qwen3-8B 从 9.93% 提高到 33.33%，超越 GPT-OSS、Kimi-k2.5 等 Agent 模型。同骨干的 ReAct-SFT 仅达 20.92% (8B)，且 HyperTool 几乎消除了工具选择错误，执行失败大幅下降。Token 分析显示，HyperTool 在财务分析域用 78% 更少 Token 实现近倍准确率提升。块类型分布中，超过 55% 的块包含多步工具编排，链式调用和聚合块平均代码复杂度最高达 44-75 行。

**核心启示**：工具增强 Agent 不应只学“该调哪个工具”，更要学“以什么样的粒度暴露执行过程”——将局部确定性流程内化为可执行块，是平衡能力与上下文效率的有效方向。
