---
title: 'Calibrated Enough to Know, Not Calibrated to Act: Fabricated Evidence Makes
  LLM Agents Commit to the Unknowable'
title_zh: 校准到知而不校准到行：伪造证据使 LLM Agent 承诺不可知问题
authors:
- Pranav Aggarwal
affiliations:
- Independent Researcher
arxiv_id: '2608.27167'
url: https://arxiv.org/abs/2608.27167
pdf_url: https://arxiv.org/pdf/2608.27167
published: '2026-08-27'
collected: '2026-08-29'
category: Agent
direction: LLM Agent 决策校准与 SFT 修复
tags:
- LLM Agent
- Calibration
- Fabricated Evidence
- Decision Making
- SFT
- Act-Don't-act Gate
one_liner: 专业外观的市场面板大幅提升 LLM Agent 对不可预测问题的承诺率，定位为行动门控失效且可通过 SFT 修复
practical_value: '- 在电商/广告的 LLM Agent 决策链路中，对“不可预测”类问题（如未来销量、市场波动）增加显式门控：在行动前先让模型或一个小型分类器判断问题是否可答，避免被权威格式的不相关证据诱发错误承诺。

  - 对输入给 LLM 的指标/面板等证据进行可信度过滤：即使数据是伪造的，专业外观仍会显著提升模型承诺率，因此需验证数据来源，或通过 prompt 强调“仅使用问题本身信息，忽略装饰性面板”。

  - 可以使用少量合成数据 SFT 一个小模型（如 3B）来训练“拒绝不可知”的门控，实验显示 540 个案例即可将承诺率降至 0 并跨领域迁移，适合业务中快速构建风险控制模块。

  - 注意响应格式：为模型保留推理空间（如允许 chain-of-thought）是门控生效的关键，强制输出决策的刚性格式会导致模型自信犯错，因此在设计 agent
  prompt 时避免直接要求“是/否”而不给推理步骤。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM agent 在现实决策中可能因看似专业的证据（如市场面板）而过度自信，对不可预测问题做出承诺，导致高风险错误。

**方法关键点**：对 12 个前沿模型进行实验，比较无面板、真实市场面板、完全虚构面板三种条件下，对不可预测问题的方向性承诺率；同时测试匹配的可回答问题、概率校准、可回答性分类以定位失败；进一步对 3B 模型 SFT 训练 540 个合成案例（骰子、硬币、罐子、计时器），测试迁移与格式影响。

**关键结果**：承诺率从无面板的 6.5% 升至真实面板的 54.0%，虚构面板为 36.8%，与真实面板统计无差异；模型对可回答问题几乎总是回答且准确率高，概率校准差，可回答性分类正确但几乎不承诺；SFT 后承诺率降至 0.0% 并迁移到三个未见领域，但刚性格式（无推理空间）会使门控失效。
