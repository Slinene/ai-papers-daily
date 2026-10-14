---
title: Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL
  Constraints
title_zh: 面向小语言模型工具学习的教师引导策略优化
authors:
- Haoxuan Gao
- Qin-Wen Luo
- Xiang Chen
- Yu Tian
- Zequn Sun
- Xiaofeng Cao
- Jiangchao Yao
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- 360 Security Capability Center
- Nanjing University
- Tongji University
- Shanghai Jiao Tong University
arxiv_id: '2610.18459'
url: https://arxiv.org/abs/2610.18459
pdf_url: https://arxiv.org/pdf/2610.18459
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agent 工具学习 · 双向 KL 约束
tags:
- SLM
- Tool Learning
- GRPO
- Knowledge Distillation
- Bidirectional KL
- Teacher Guidance
one_liner: 提出 SeTPO，在 GRPO 中按奖励门控注入教师 token 级反向 KL 信号，并用教师演示前向 KL 保留结构，提升 SLM 工具调用
practical_value: '- 在 RL 训练 SLM 工具调用/函数调用时，不要对所有轨迹都上教师蒸馏；按任务奖励门控只对低奖励轨迹注入教师 token
  级修正（用 log p_student - log p_teacher 修正 GRPO advantage），可保留高奖励轨迹的纯 task-driven 更新，避免过度约束。

  - 持续保留一个小的 auxiliary SFT/演示损失（如权重 0.1）在 RL 过程中：用冻结教师生成的完整参考轨迹做交叉熵，能稳定输出格式（<tool_call>
  等结构），防止 reward 上升但格式坍塌；这对生产环境结构化输出尤其重要。

  - 教师模型容量不是越大越好：论文显示 0.5B 学生配 1.5B 教师优于 3B/7B；迁移能力与容量差距存在倒 U。业务选教师可优先选与学生同架构、容量适中的模型，降低分布差异。

  - 若工具/API 场景有确定性 checker，可把 composite reward 设为格式奖励 + 正确性奖励（工具名/参数名/参数值 Jaccard+exact
  match），配合 γ 接近最大奖励的门控，让低奖励轨迹获得教师修复信号。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小模型（SLM）通过外部工具扩展能力是端侧/资源受限场景的实用路线，但面临三个障碍：SFT 演示与模型自生成分布不匹配；纯 RL 奖励稀疏，SLM 难以自主发现成功轨迹；在线蒸馏（OPD）可能传递教师错误偏好，且师生容量差异导致知识迁移低效。论文针对工具调用任务，提出 SeTPO。

### 方法关键点
- 在 GRPO 基础上，按轨迹奖励 R_j<γ 门控，只对低奖励学生轨迹请求教师；教师对学生前缀下已采样 token 计算 log p_old - log p_teacher，作为单样本 reverse KL 估计，修正该 token 的 advantage：A'_{j,t}=A_j - I_j β d_{j,t}。
- 同时保留 auxiliary SFT：冻结教师为每个训练 prompt 生成完整参考轨迹，持续最小化交叉熵，等价于最小化前向 KL(q_D || π_θ)，防止格式崩溃并保留教师演示行为。
- 理论上，在理想双向 KL 目标 F(p)=E_p[R]-a D_KL(p||q)-b D_KL(q||p) 下，最优策略期望奖励不低于教师，且对任意响应集 E 保留至少 b/(b+ΔR) 的教师概率质量。

### 关键结果
在 BFCL-v4 和 API-Bank 上，Qwen2.5-0.5B/1.5B/3B 学生均取得最佳综合成绩，超过 SFT、GRPO、SFT+GRPO、KD、OPD。0.5B 学生 BFCL-v4 上 SeTPO 为 18.99，GRPO 为 10.67、OPD 为 16.17；3B 学生在 API-Bank 上 63.82 超过其 14B 教师 62.48。消融显示去掉 token 级 teacher signal 掉点最大（BFCL-v4 -11.20，API-Bank -13.56）；去掉 auxiliary SFT 导致格式奖励崩溃。

### 最值得记住的一句话
“用 reverse KL 修正学生低奖励探索中的 token 决策，用 forward KL 持续保留教师演示结构，二者双向约束能在不牺牲教师行为覆盖的前提下提升任务奖励。”
