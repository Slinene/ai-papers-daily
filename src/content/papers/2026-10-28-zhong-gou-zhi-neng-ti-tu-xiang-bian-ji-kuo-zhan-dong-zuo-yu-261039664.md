---
title: 'EditAgent: Rethinking Agentic Image Editing'
title_zh: 重构智能体图像编辑：扩展动作与观察空间
authors:
- Haiyang Xu
- Tianyu Wang
- Jialu Li
- Jiteng Mu
- Yuanjun Xiong
- Jianming Zhang
- Zhuowen Tu
- Mingze Xu
affiliations:
- UC San Diego
- Adobe Research
arxiv_id: '2610.39664'
url: https://arxiv.org/abs/2610.39664
pdf_url: https://arxiv.org/pdf/2610.39664
published: '2026-10-28'
collected: '2026-11-01'
category: Agent
direction: Agent 动作/观测空间扩展与并行评判
tags:
- Agent
- VLM Judge
- Verification Record
- Listwise
- Data Engine
- Image Editing
one_liner: 并行调用多类编辑器、为候选附验证记录并用 VLM 列表式评判，提升成功率并降低 judge 调用
practical_value: '- 在生成式推荐、文案/主图生成 Agent 中，避免单一模型反复 retry：并行生成不同模板/模型/策略的候选，再用 Listwise
  比较一次筛选；原文显示并行比顺序精修在 78.5% 的已决定比较中更受专家偏好，且 judge 调用至少减半。

  - 为每个候选附结构化 verification record（变化图、局部前后对比、mask、数值统计、代码核验事实等），off-the-shelf VLM
  就能超过 finetuned reward model；迁移到电商场景时，可为候选附上价格/利益点一致性、属性匹配、CTR 预估等证据。

  - 评判器扩展 observation space 比 finetune reward model 更划算：用规则/代码/检索结果生成证据，提升 VLM judge
  的可靠性，尤其是没有稳定 GT 的生成任务。

  - 可作为 data engine：用 Agent 并行生成多候选 + VLM judge 构建偏好对，蒸馏训练更强的生成式推荐或文案模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 agentic image editor 在步骤失败时，大多用同样窄的工具集重试，评判器直接看输出打分。作者认为这类 Agent 受限于两个空间：动作空间和观察空间。专家标注基准上，通用编辑器在超过 40% 的案例中得不到可用结果，且没有单个 judge 对所有编辑类型都可靠。

**方法关键点**：EditAgent 同时扩展两个空间。动作空间上，每步路由到通用编辑器和专用方法，候选并行生成；观察空间上，为每个候选附验证记录，包括 change map、局部前后对比、目标 mask、亮度/颜色统计、几何倾斜/缩放/位置、代码核验事实等。评判时，候选在单次 listwise 调用中比较，使用 off-the-shelf VLM 加验证记录，不需要 finetune reward model。

**关键结果**：带验证记录的 off-the-shelf VLM judge 超过 finetuned reward model；专家在 78.5% 的已决定比较中偏好并行候选生成而非顺序精修，且 judge 调用不超过后者一半。EditAgent 提升两个开源编辑器在三个基准上的表现，并可作为数据引擎训练更强编辑器。
