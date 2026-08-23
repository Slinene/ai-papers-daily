---
title: 'SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution'
title_zh: SkillForge：面向项目特定问题解决的自蒸馏 Agent
authors:
- Silin Chen
- Han Li
- Xiaodong Gu
- Yuling Shi
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.18933'
url: https://arxiv.org/abs/2608.18933
pdf_url: https://arxiv.org/pdf/2608.18933
published: '2026-08-18'
collected: '2026-08-23'
category: Agent
direction: Agent 自蒸馏获取项目特定知识
tags:
- Agent
- Self-Distillation
- Project-Specific Knowledge
- Entity-Grounded Retrieval
- SWE-bench
- Issue Resolution
one_liner: 通过从仓库自身测试与代码合成 issue 并蒸馏为实体级技能，解决 SWE agent 的项目冷启动问题
practical_value: '- **可复用的架构：离线自蒸馏 + 在线检索注入**。电商/广告/推荐 Agent 同样存在“项目冷启动”：新业务域缺乏领域知识。可用仓库测试/日志/历史行为作为监督，先离线合成任务并跑通
  Agent 轨迹，再蒸馏成可检索知识，在线时只做轻量注入，避免每次线上任务都重探。

  - **双级技能库 + 实体对齐的 JIT 注入**。不要把所有知识一次性塞进 prompt。把诊断类知识（模块定位、排障 playbook、关联 API）做全局初始化检索；把干预类知识（修改时的坑、修复模式）绑定到具体实体，Agent
  访问对应实体时再注入。这比纯语义相似度检索更精准，能降低上下文噪声。

  - **合成任务要“功能级”而不是“单函数级”**。只改一个函数往往暴露不了跨模块集成问题。应沿执行 trace 一次覆盖多个协同代码段，合成出来的任务才更接近真实业务故障。

  - **知识是模型相关的，跨模型迁移会掉点**。如果是电商 Agent，不同底座模型编码偏好不同，蒸馏出的领域知识应尽量与线上推理模型绑定，不要拿 A 模型蒸馏的知识直接给
  B 模型用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM-based SWE agent 在具体项目上常常从零开始探索，缺少项目特定知识，导致冷启动问题：反复踩同样的坑、重复发现 API 约束。已有自进化方法要么依赖历史 issue resolution 轨迹，要么在测试期高成本在线探索。SkillForge 提出主动从仓库自身获取项目特定知识，不等真实 issue 暴露知识缺口。

**方法关键点**  
- **项目特定 issue 合成**：从测试覆盖的核心功能出发，跑测试生成执行 trace，定位协同实现同一功能的多段代码；LLM 在遮蔽原实现的情况下重写这些片段，自然引入真实开发中类似的实现错误，产成 SWE-bench 格式的 synthetic instance。
- **双级技能蒸馏**：解析 agent 在合成 issue 上的轨迹，将访问的文件对齐到 AST 实体；蒸馏全局诊断技能 `Mext`（purpose / playbook / related_apis）和局部干预技能 `Mint`（成功/失败轨迹对比得到 intervention_skills）。
- **技能使用**：新 issue 到来时，先用 BM25 检索 top-k 个 `Mext` 记录作为初始项目先验；当 Agent 访问匹配实体时，再 JIT 注入对应的 `Mint` 干预提示，避免一次性灌入大量噪声。

**关键结果**  
在 SWE-bench Verified 上，SkillForge 用 DeepSeek-V3.2 和 GPT-5-mini 分别达到 72.2% / 60.6% Pass@1，比 Mini-SWE-Agent 高 +5.8 / +5.6 个百分点；在 SWE-bench Pro 上达到 34.1% / 51.7%，提升 +5.8 / +4.1 个百分点，均优于 MemGovern、SAGE、SWE-Debate、Live-SWE-agent 等 history-driven / online baseline。消融显示去掉全局诊断技能掉 3.8/3.0 个百分点，去掉局部干预技能掉 4.4/3.4 个百分点；跨 LLM 迁移蒸馏知识会明显掉点。

**最值得记住的一句话**：项目特定知识应当 proactive 地从仓库自身合成任务并蒸馏，且以实体为锚点做双级检索注入，而不是被动等历史轨迹或在线重探。
