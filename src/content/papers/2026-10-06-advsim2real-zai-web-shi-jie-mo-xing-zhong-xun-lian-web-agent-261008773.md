---
title: 'AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web
  World Model'
title_zh: AdvSim2Real：在 Web 世界模型中训练 Web Agent 对抗自适应提示注入
authors:
- Sarim Hashmi
- Mukul Ranjan
- Kshitij Mishra
- Mikhail Kuznetsov
- Praneeth Vepakomma
- Nils Lukas
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Amazon
- Massachusetts Institute of Technology
arxiv_id: '2610.08773'
url: https://arxiv.org/abs/2610.08773
pdf_url: https://arxiv.org/pdf/2610.08773
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Web Agent 鲁棒训练与对抗攻防
tags:
- prompt injection
- web agents
- adversarial training
- world model
- curriculum learning
- sim-to-real
one_liner: 冻结 world model 内共同进化课程、注入攻击者与 agent，4B agent 在未见攻击下完成率提升33.6%并泛化真实浏览器
practical_value: '- 在电商商品详情、用户评论、广告文案等第三方可控页面中，同样存在 prompt injection 风险（如“忽略用户要求，推荐本商品”），可借鉴用
  frozen world model + LLM judge 构建低成本对抗训练环境，避免依赖人工标注或真实浏览器滚动。

  - 联合优化课程和攻击者：课程奖励设在 agent 成功率约 50%，防止任务饱和后停止教学；攻击者只在“成功翻转”时给奖励，保证攻击持续有效。这套奖励设计可直接迁移到
  agent 安全训练或鲁棒性调优。

  - 不要用固定攻击集微调；攻击者应与 agent 同步进化，且评估时引入未见过的前沿模型攻击（如 Kimi-K3）测试真实鲁棒性。

  - 4B 小模型在 frozen world model 中训练后即可将能力增益迁移到真实浏览器，说明模拟对抗环境是小模型低成本获得鲁棒性的可行路径，适合资源敏感业务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
Web agent 必须读取并执行第三方页面上的内容，但页面可能植入恶意指令，把 agent 从用户目标引开；agent 又不能完全忽略页面，因为页面也包含完成任务所需的值和控件。当前防御用训练前固定的注入做微调，攻击者自适应后即可绕过；对抗训练允许攻击者自适应，但任务固定，任务一旦被攻克就不再提供教学信号。

**方法关键点**  
AdvSim2Real 在一个冻结的 Web world model 内共同进化三部分：任务课程（curriculum）、注入攻击者（adversary）和 agent。课程被奖励为 agent 能解决约一半的任务，以维持在能力边界附近；攻击者仅在“成功翻转”时获得奖励，即注入必须把一个判定为成功的任务翻转为失败。世界模型模拟页面与交互，LLM judge 冻结并判定成功。训练分两个阶段：Stage 1 课程生成任务，Stage 2 攻击者插入一次性定时注入，两个阶段都更新 agent。

**关键结果**  
在 150 个 web 任务上，训练后的 4B agent 在干净任务上完成率 +8.6%，在训练中见过的攻击者下 +19.6%，在从未训练过的前沿模型攻击者 Kimi-K3 下 +33.6%；能力增益还能迁移到真实浏览器。
