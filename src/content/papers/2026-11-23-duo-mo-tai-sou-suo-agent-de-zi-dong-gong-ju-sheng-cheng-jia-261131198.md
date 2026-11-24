---
title: 'ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents'
title_zh: 多模态搜索 Agent 的自动工具生成框架 ToolSmith
authors:
- Rui Sun
- Junhua Huang
- Luca Zancato
- Md Mofijul Islam
- Kai-Wei Chang
affiliations:
- University of California, Los Angeles
- AWS GenAI
arxiv_id: '2611.31198'
url: https://arxiv.org/abs/2611.31198
pdf_url: https://arxiv.org/pdf/2611.31198
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: Agent 自动工具生成 · 多模态搜索
tags:
- Tool Generation
- Multimodal Search Agents
- VLM
- Self-Improvement
- Tool Library
- Agent
one_liner: 从失败轨迹挖掘能力缺口，自动生成并验证新工具，扩充多模态搜索 Agent 的工具库
practical_value: '- 可复用失败轨迹挖掘 + 聚类提炼能力缺口：线上搜索/推荐 Agent 可定期收集 bad case，用 LLM 自判失败原因并聚类，把高频缺口转化为工具需求，避免人工盘点
  skill。

  - 工具生成统一产出“Python 代码 + typed schema + 描述”，并加 AST 静态检查、smoke test、LLM code review
  两阶段验证：业务中可推广到任何 Python 工具/插件生成，先挡住动态执行和危险 I/O。

  - 推理时按 query embedding 检索 top-K 生成工具而非全量注入 schema，避免工具膨胀压缩上下文、干扰选型，适合工具多、请求长尾的电商
  Agent。

  - 生成器模型比消费模型对最终收益更关键，轨迹挖掘用与部署 Agent 同能力模型自挖掘更优：工程上可把预算投给最强生成模型，对轻量线上模型提升最明显。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：多模态搜索 Agent 依赖固定手工工具库，覆盖有限、维护成本高，遇到新 query 类型、证据格式或失败模式时无法扩展。ToolSmith 让 Agent 从自身失败中自动生成新工具并验证入库。

**方法关键点**：
- **四阶段流水线**：① Trajectory Mining——在训练池 rollout，先用 LLM judge 找最终答案错误，再用 LLM self-critique 标出 `NEW_TOOL_NEEDED` 失败，embedding + 层次聚类得到能力缺口代表；② Reuse-or-Grow——用 TF-IDF 余弦相似度判断缺口是否已被现有工具覆盖，不覆盖才生成；③ Tool Generation——生成器 LLM 按约束（禁止动态执行、硬编码答案）产出 Python 源码、typed schema 和描述；④ Two-Gate Verification——Gate1 sandbox AST 检查 + smoke test，Gate2 LLM 四维静态代码 review，通过后再与现有工具去重。
- **推理时检索**：每 query 用 sentence embedding 对生成工具做 top-K 检索，与 8 个基础工具一起暴露给 Agent，避免全量 schema 膨胀。

**关键实验**：在 3 个 in-domain benchmarks（FVQA、InfoSeek、EncyclopedicVQA）和 10 个 out-of-domain benchmarks 上，用 GPT-5 生成工具。8B 模型 in-domain +2.20pp、OOD +1.33pp；32B OOD +2.98pp；GPT-5 OOD +2.40pp。生成器越强，收益越明显；轨迹挖掘用与消费模型同能力者更好。生成工具在 in-domain 占 27% tool calls、41% 样本被调用。

**最值得记住的一句话**：不是教 Agent 更好用固定工具，而是让 Agent 从自己的失败里长出新工具并验证后再入库。
