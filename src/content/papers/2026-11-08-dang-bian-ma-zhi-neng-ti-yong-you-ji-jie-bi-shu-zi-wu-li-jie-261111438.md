---
title: 'When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary'
title_zh: 当编码智能体拥有机械臂：数字-物理边界的安全风险
authors:
- Yiming Sun
- Mi Zhang
affiliations:
- Fudan University
- JADE AI (Whitzard AI) Team
arxiv_id: '2611.11438'
url: https://arxiv.org/abs/2611.11438
pdf_url: https://arxiv.org/pdf/2611.11438
published: '2026-11-08'
collected: '2026-11-15'
category: Eval
direction: 编码智能体具身安全评测
tags:
- Coding Agent
- Robot Control
- Safety Benchmark
- Indirect Prompt Injection
- Embodied AI
one_liner: 首个系统性基准ArmedAgent，评估编码智能体零样本机器人控制中的鲁棒性、恶意使用与间接注入风险
practical_value: '- 间接提示注入是Agent系统共性风险：电商Agent常访问商品页面、用户评论、外部API，这些内容可能包含恶意指令，需引入类似ArmedAgent的鲁棒性测试集，验证推荐/搜索Agent是否会被劫持改变输出。

  - 评测维度可迁移：将安全风险分解为鲁棒性（对抗扰动）、恶意使用（能力滥用）、间接注入（外部内容劫持），适用于电商Agent（如自动选品、自动生成营销文案）的安全评估。

  - 零样本通用能力放大风险：前沿模型不经任务微调即可执行新任务，意味着一套通用Agent底座可能被用于未预期的危险操作，需对Agent能力边界做安全审计，尤其涉及支付、库存修改等数字/物理行动。

  - 数字-物理边界提醒：O2O电商（如即时零售、无人仓）中，Agent可能控制物理设备或影响现实世界（如自动下单、调度），需要模拟环境验证安全，避免将纯数字环境的Agent直接部署到涉及物理操作的场景。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：空间理解能力提升使前沿模型驱动的编码智能体能够零样本、端到端控制真实机械臂，无需任务特定演示或重训练。这带来两类新安全挑战：一是前沿模型广泛知识使智能体能执行早期VLA/WAM范式无法完成的任务，引发能力滥用；二是编码智能体访问网页、邮件等数字资源，间接提示注入威胁可能传递到物理世界。

**方法**：构建ArmedAgent基准，首个系统性评估编码智能体零样本机器人控制安全风险的基准。覆盖36个任务、5个场景，在仿真中评测并在物理机械臂上验证。任务包含鲁棒性、恶意使用、间接注入三类风险，其中部分任务针对早期VLA范式无法执行的有害行为。测试多个前沿模型（包括GPT-6-Astra）在常用Agent框架下的表现。

**结果**：发现当前系统存在重大安全风险，具体风险细节未在摘要中给出，但表明前沿模型在零样本机器人控制中存在可被利用的漏洞。
