---
title: 'Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant
  Task Construction'
title_zh: 多领域编程Agent基准：抗污染任务构建与开放评估
authors:
- Tencent WorkBuddy Bench Team
- Siqi Cai
- Shaopeng Chen
- Xiang Fei
- Yong Mao
- Zihan Xu
- Zhiheng Lyu
- Zhijian Shao
- Yuchen Shi
- Shuwen Zhang
affiliations:
- Tencent (Youtu Lab, Keen Security Lab, Workbuddy, Yunding Security Lab)
arxiv_id: '2607.20911'
url: https://arxiv.org/abs/2607.20911
pdf_url: https://arxiv.org/pdf/2607.20911
published: '2026-07-22'
collected: '2026-07-25'
category: Eval
direction: 多域编码Agent评估与抗污染基准
tags:
- Agent Benchmark
- Contamination Resistance
- Multi-Domain
- Coding Agent
- Open Evaluation
- Sandboxed Scoring
one_liner: 提出跨Code/Web/Office/Security四域的抗污染编程Agent评估套件，任务由真实场景改写且完全开放可审计
practical_value: '- **任务构造抗污染**：从真实commit/PR反向工程并改写为口语化角色请求，隐藏根因和参考diff，使提示无法通过搜索获取，可借鉴用于构造内部Agent评测集，避免记忆偏差。

  - **多域评估设计**：覆盖仓库级代码、前端、办公文件、安全四大类，可按业务需求拆分类似维度评估自研Agent，尤其适合需处理多类型任务的推荐系统辅助Agent。

  - **统一沙盒执行与开放审计**：Harbor风格任务目录打包，双评估器可复现，全部测试和参考方案公开。在电商/广告Agent评测中，可参考其沙盒隔离和评估前隐藏测试的方式保证公平性。

  - **反欺骗与可靠评分**：Security的5层反欺骗机制（禁止字面量扫描、重命名输入等）和Office的证据驱动法官，可用于需要防止Agent走捷径的业务线上评测。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有编码Agent基准（如SWE-bench）基于公开issue，模型可通过记忆污染获得虚高分数，且任务范围窄；闭源基准无法审计。需要一个分布匹配真实工作、能抵抗网络搜索污染、完全开放且可复现的评测套件。

**方法关键点**：
- **任务构造**：从真实commit、PR或业务场景反向工程，重写为角色扮演的简短口语化请求，故意不提供根因和精确方案，避免搜索引擎复原提示。
- **四个子集**：Code（80个仓库级软件工程任务）、Web（70个前端任务）、Office（50个办公文件工作流任务）、Security（60个红蓝队安全任务），总计260任务。
- **统一格式与隔离**：Harbor风格目录，包含workspace Docker镜像和隐藏的评估资产，评估前隔离，确保代理不接触测试。
- **领域定制评分**：Code用隐藏单元测试；Web用规则+LLM/VLM/Agent法官多层检查表；Office用确定性规则检查与证据驱动LLM法官按任务权重混合；Security完全程序化评分且含5层反欺骗机制。
- **双评估器与开放**：同时使用CodeBuddy Code和Claude Code，think模式；任务、测试、参考解全部公开，支持第三方复现和审计。

**关键结果**：在初版260任务上，Claude Opus 4.8总得分最高（75.0%），GLM-5.2（72.9%）、GPT-5.5（72.0%）紧随其后。Code子集最高分74.4%，Web最高68.1%，Office最高82.4%，Security最高76.3%，不同模型在不同子集差异显著，凸显多域评估必要。评测揭示即使强模型在真实仓库级探索和前端交互任务中仍有较大改进空间。
