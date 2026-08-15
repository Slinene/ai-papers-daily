---
title: 'SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction
  in Small Language Models'
title_zh: SKILLER：面向小语言模型可复用技能提取的语言级强化学习框架
authors:
- Chenhao Dang
- Siyuan Xiong
- Conghui He
- Weijia Li
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Harbin Institute of Technology, Shenzhen
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.10538'
url: https://arxiv.org/abs/2608.10538
pdf_url: https://arxiv.org/pdf/2608.10538
published: '2026-08-10'
collected: '2026-08-15'
category: Agent
direction: Agent 技能生成 · 语言级强化学习
tags:
- Agent Skills
- Language-level RL
- Small LVLM
- Skill Optimization
- Policy Iteration
- Cost-Effective Agent
one_liner: 用自然语言强化学习为小型 LVLM 自动生成定制化 agent 技能，不更新权重，成本降低 71-167 倍
practical_value: '- 离线用强模型（GPT-5.4）作为 actor/critic，将目标小模型（Qwen3.5-9B/4B）的 agent loop
  当作环境，通过可验证 reward 迭代优化 prompt/skill，线上只部署小模型，大幅降低推理成本。在电商客服、推荐解释生成等场景可直接复用此离线优化范式。

  - 将复杂多步推理流程固化到确定性脚本/工具中，skill 只负责调用和异常处理，避免小模型上下文过长、步骤遗漏或幻觉。对应推荐系统可将商品特征处理、规则过滤放在外部服务，LLM
  只做轻量决策。

  - 语言级 policy iteration 的 critic 定位最早因果错误并生成有界编辑（INSERT/REPLACE/CREATE/DELETE），actor
  实施局部更新并保留有效内容，防止灾难性遗忘。可用于 prompt 迭代优化：从失败 case 诊断原因，局部修改 prompt 而非全量重写。

  - 成本-性能权衡：SKILLER 生成技能成本约 $8.95，低于 SkillX $14.55 且性能更高；相比闭源部署成本低 71-167 倍。提示在预算有限时，针对
  executor 定制 prompt 比盲目堆大模型更高效。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Agent skills 是约束模型行为、保证重复高质量任务执行的重要机制，但现有技能多针对强闭源模型设计，直接移植到消费级 GPU 可部署的小模型时会出现模型失配：小模型容易幻觉参数、跳过验证、被复杂指令干扰。由于小模型推理成本极低，若能为它们自动生成定制化技能，可大幅降低 agent 部署成本。  

**方法关键点**  
- 将文本技能 K 视为可优化策略，冻结小模型 π，以 π 与任务环境交互的 agent loop 作为强化学习环境。  
- 每步状态为四元组 (x, τi, τ*, vi)：任务实例、当前轨迹、参考轨迹、verifier 诊断；奖励来自官方 verifier。  
- 强模型作为 critic，对比 τi 与 τ* 定位最早因果错误，生成有界修改建议 gi；replay memory 存储失败签名、批评历史、编辑结果，防止重复失败。  
- 强模型作为 actor，通过 Insert/Replace/Create/Delete 四种操作应用有界编辑更新技能；并合成 task-local helper 脚本，将确定性计算外化，降低小模型上下文负担。  
- 所有信息传递均通过自然语言完成，没有梯度更新。  

**关键实验**  
在 SkillsBench、SkillLearnBench、SWE-Skills-Bench、GAIA、EarthBench 五个基准上评估 Qwen3.5-9B 和 4B，对比 AutoSkill、EvoSkill、SkillX、Manus 和 human-authored skills。结果：9B 上 SKILLER 在 SkillsBench 达 73.91%，比最强开源基线 SkillX 高 13.04 个百分点；SWE-Skills-Bench 达 82.80%，高 24 个百分点；零样本 GAIA 49.59% 领先。4B 在 SWE-Skills-Bench 达 66.70%，超过 9B 使用 Manus 生成技能等基线。生成成本约 $8.95，低于 SkillX $14.55。  

**最值得记住的一句话**  
语言级 RL 把强模型的诊断与修复能力转化为小模型的可执行行为约束，让 4B/9B 模型在特定任务上接近甚至超越大模型，成本却低两个数量级。
