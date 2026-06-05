---
title: Evaluating Large Language Models in Dynamic Clinical Decision-Making with Standardized
  Patient Cases
title_zh: 基于标准化病人案例的动态临床决策大语言模型评估
authors:
- Cheng Liang
- Pengcheng Qiu
- Ya Zhang
- Yanfeng Wang
- Chaoyi Wu
- Weidi Xie
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2606.05112'
url: https://arxiv.org/abs/2606.05112
pdf_url: https://arxiv.org/pdf/2606.05112
published: '2026-06-02'
collected: '2026-06-05'
category: Eval
direction: 临床代理动态交互评估基准
tags:
- Benchmark
- Clinical Agents
- Standardized Patients
- Interactive Evaluation
- LLM
- Multi-turn
one_liner: 提出 MedSP1000 交互式基准，用标准化病人闭环仿真评估 LLM 临床代理能力，暴露静态基准无法捕获的失败模式
practical_value: '- 在电商 Agent 评估中，可借鉴标准化用户脚本构建闭环仿真环境，让 Agent 与用户代理、环境控制器持续交互，用预先定义的评分细则评估每一步决策，而非仅看最终结果。

  - 过程级评价比单轮静态测试更能暴露 Agent 在信息收集不充分、规划缺失、状态适应等方面的失败模式，适合用于对话式推荐、客服 Agent 等场景的离线评测。

  - 用领域专家审核的脚本和评分标准（类似医学教学案例的书面评分细则）来构造评估数据，保证评测的客观性和可复现性，这比人工主观判断更可靠。

  - 实验发现增加测试时计算（如链式推理）对 Agent 性能提升有限，提示在推荐/对话 Agent 中，单纯堆叠推理步数可能不是最优解，需从训练数据或架构上增强长期规划和状态跟踪能力。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：静态单轮医学问答基准无法衡量LLM作为临床代理时的动态护理能力，如信息收集、治疗规划与适应患者状态变化。医学教育长期使用标准化病人（SP）进行训练与客观评估，因此借鉴SP方法构建交互式基准。

方法：提出MedSP1000，包含1638个SP案例和24602条轨迹级专家验证评分细则。将教学案例转化为可执行场景：临床代理与患者代理、环境控制器闭环交互，全程依据原始专家评分标准进行细粒度评价。

结果：在通用及医疗专用LLM上测试，最强通用模型GPT-5.5仅完成60.4%的专家指定操作，最强医疗模型仅达40.0%；增加测试时计算（推理链）无显著增益。表明当前LLM在动态临床决策中仍不可靠，且过程级SP风格评估能揭示单轮基准遗漏的临床相关失败模式。
