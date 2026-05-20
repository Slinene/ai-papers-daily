---
title: 'TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents'
title_zh: TOBench：面向真实工作流的全模态工具使用基准与闭环验证
authors:
- Zhiqiang Liu
- Wenhui Dong
- Yilang Tan
- Yuwen Qu
- Haochen Yin
- Chenyang Si
affiliations:
- Nanjing University
- Huazhong University of Science and Technology
- Southwest Jiaotong University
- The Chinese University of Hong Kong
arxiv_id: '2605.16909'
url: https://arxiv.org/abs/2605.16909
pdf_url: https://arxiv.org/pdf/2605.16909
published: '2026-05-15'
collected: '2026-05-20'
category: Eval
direction: 全模态工具使用评估 · 闭环验证
tags:
- Tool-Using Agents
- Multimodal Benchmark
- MCP
- Closed-Loop Verification
- Evaluation
one_liner: 提出全模态工具使用基准TOBench，通过闭环验证评估 agent 在真实专业任务中的表现
practical_value: '- 在电商智能客服或内容生成 Agent 中引入闭环验证：生成回复或创意后自动渲染/解析并检查是否满足业务规则（格式、品牌一致性、价格合规），失败则触发修正循环，可大幅提升终态交付质量。

  - 采用 MCP 统一工具接口集成商品搜索、订单查询、价格计算等，降低多工具编排成本；同时设计任务特定的 grounded verifier，通过代码检查 +
  VLM 判断 + 工具结果重查，实现自动化质量校验。

  - 对于生成式推荐产出的图文素材，可借鉴多模态工件审查方案：对生成的文案配图进行视觉布局审核、合规性检测，利用规则与 VLM 协同打分，形成可量化的离线评估流水线。

  - 从错误分析中吸取教训：工具调用中参数幻觉和缺失自检是主要失败点，实际系统应强化参数校验、提供更结构化的工具反馈，并强制 Agent 在终态前执行至少一次视觉/内容核查（如渲染
  PPT 后截图对比），而非仅检查元数据。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有工具使用基准大多将多模态感知、工具调用和计算机操作分开评估，与真实专业工作流脱节。实际任务常要求 agent 处理图文音视频等多模态输入，调用多个工具生成或编辑文档、图片、PPT等，然后检查输出是否符合要求，并在不符合时修正。这种“感知-执行-检查-修正”的闭环在现有基准中缺乏系统性评测，导致模型在真实场景中表现远低于预期。  

**方法关键点**  
- **任务设计**：基于真实用户需求构造 100 个可执行任务，覆盖客服和智能创作两大类别、20 个子类；配套 27 个 MCP 服务器共 324 个工具，形成完整的工具生态。  
- **闭环验证**：每个任务绑定一个特定的 grounded verifier，结合代码检查、VLM 判断和工具/结果验证，要求 agent 执行工具后必须检查渲染或转换得到的工件，并在不合格时自我修正。  
- **评估流程**：先为每个任务生成细致的评估点（格式、多模态、工具约束三类），再合成专用评估脚本并人工审核；执行时实时运行评估脚本，而非静态答案匹配。  
- **半自动构建管线**：从场景发现、任务实例化到评估器合成，均由 LLM 辅助生成，再经人工审核校准，保证规模与质量。  

**关键实验**  
评测 15 个主流模型（含闭源和开源），以任务完成率作为主指标。最高得分模型 Qwen3.5-Plus 仅 41.0%，Claude Opus 4.6 仅 32.0%，而人类基准为 94.0%。错误分析显示：工具调用错误和参数错误是最大瓶颈；多模态推理错误在基本执行成功后成为主导；视觉验证缺失是智能创作类任务卡死的特有原因。  

**核心启示**  
“闭环多模态验证是评估下一代全模态工具使用 agent 不可或缺的基元”——不只看最终答案，还看中间输出的自我检查和修正能力，这应是未来 agent 设计的核心一环。
