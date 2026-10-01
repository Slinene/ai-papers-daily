---
title: 'PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents'
title_zh: PivotOPD：多轮智能体从关键错误中学习恢复
authors:
- Yinghui He
- Yapei Chang
- Khushi Bhardwaj
- Daniele Molinari
- Tugrul Konuk
- Jan Kautz
- Ali Hatamizadeh
affiliations:
- Princeton University
- NVIDIA
- University of Maryland
arxiv_id: '2609.40285'
url: https://arxiv.org/abs/2609.40285
pdf_url: https://arxiv.org/pdf/2609.40285
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 多轮训练 · 关键错误恢复
tags:
- On-policy Distillation
- Pivotal Mistake
- Multi-turn Agents
- Recovery Distillation
- RL
- LLM
one_liner: 在关键轮做预防式 reverse KL、后续轮做恢复式 forward KL，大幅提升多轮 Agent 从关键错误恢复的成功率
practical_value: '- 多轮 shopping/search agent 中，用 teacher hindsight 检测 pivotal mistake，把密集蒸馏信号集中在关键轮及后续恢复窗口，比均匀蒸馏更划算；在
  WebShop 这类电商环境里，成功率提升明显大于部分得分，说明可把半途任务转化为完成订单。

  - 若没有环境 oracle，可直接用较大 LLM 回读轨迹，选 candidate turns 并给出 gold action，与 student 实际 action
  不一致就视为 pivotal；ALFWorld 上这种检测在 77.8% 失败轨迹中落在 oracle pivotal 附近，足够用于训练。

  - 目标构造可复用：frozen student + gold/recovery action hint 作为 privileged self-teacher，生成学生风格的
  token 级目标；预防用 reverse KL 压住错误动作，恢复用 forward KL 覆盖低概率恢复动作，两者放进同一个 PPO advantage 更新。

  - 恢复预算 K 按任务调：短链路取 K=1，长动作链恢复取 K=2；蒸馏 advantage 建议 clip，preventive weight 设小，恢复序列只保留可解析且不泄露
  hint 的回复。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
多轮 Agent 里一个错误动作会改变后续状态，误差逐轮累积。作者用 ALFWorld 的 symbolic oracle 分析 Qwen3 8B–235B 的失败轨迹，发现超过一半失败含有一个 pivotal mistake，且通常发生在早期；纠正该 step 后 replay 成功率从 8% 升到 59%，保留错误但用 oracle 动作引导后续两轮仍能到 58%，说明这类错误大多可恢复。标准 on-policy distillation 虽降低整体失败率，但 pivotal-turn 失败只下降 2.1%，因为 gold action 概率仍低于 1%，学生几乎采样不到，缺乏直接学习信号。

**方法关键点**  
- Pivot detection：teacher 回读整条轨迹与 outcome，选 candidate turns 并给出 gold action；student 实际 action 与 gold action 不一致时判为 pivotal turn。  
- Privileged self-teacher：frozen student 被 gold/recovery action 作为 hint 条件，生成学生自身风格的 token 级目标。  
- Preventive distillation：在 pivotal turn 用 reverse KL 拉向 hinted gold action，压住已犯错误。  
- Recovery distillation：teacher 在 pivotal turn 后 K 轮命名 recovery action，self-teacher 写出 hinted response，再用 forward KL 训练无 hint 的 student，覆盖其很少采样的恢复动作。  
- 与 group-based RL 合入单个 PPO update；preventive advantage 加在 rollout token 上，recovery sequence 只使用 clipped distillation advantage。

**关键实验**  
在 ALFWorld、WebShop、Search-based QA 上与 13 个 baseline 比较，Qwen3-1.7B 和 Qwen3-8B 学生均取得最强平均性能；1.7B 在 ALFWorld 上比最强 baseline 高 +5.5%，Search-based QA 高 +5.9%。WebShop 上 PivotOPD 相对 RLSD 的 score 只高 +1.2%，但 success rate 高 +14.1%。跨模型迁移到 Nemotron-3.5 学生、SWE-Bench Verified 上 resolve rate 提升 +3.2%，而标准 OPD 只 +0.2%。恢复分析中，PivotOPD 从同一 pivotal mistake 恢复的频率约为 base model 的 9 倍，且恢复轮数更少。

**一句话**  
失败往往由一个早期关键错误决定，训练时集中监督 pivotal turn 并显式覆盖后续恢复动作，比平均 reward/distillation 更能教会 Agent 从错误中走出来。
