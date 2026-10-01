---
title: 'AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks'
title_zh: AREX-2：通过长程反思任务推进自改进智能体
authors:
- Hongjin Qian
- Chaofan Li
- Kun Luo
- Wenqing Wei
- Jianlyu Chen
- Shuqi Lu
- Yuyang Hu
- Hongwang Xiao
- Hui Wang
- Chaozhuo Li
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2609.38288'
url: https://arxiv.org/abs/2609.38288
pdf_url: https://arxiv.org/pdf/2609.38288
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: 自改进 Agent · 长程反思训练
tags:
- Self-Improvement
- Long-Horizon Reflection
- Agent
- Test-Time Scaling
- Trajectory Synthesis
one_liner: 用长程反思轨迹训练 27B agent，在 ML/编程及深度研究基准上逼近更大模型
practical_value: '- 把“失败和恢复”写进训练轨迹，而不是只保留成功答案：在电商搜索/广告 agent 做 query 改写、创意优化时，可用离线仿真或历史日志构造多轮改进轨迹，保留负面反馈与后续修复步骤，loss
  只施加在产生进步的动作上。

  - 用 graded reward 替代 binary pass/fail：推荐/搜索中的 ranking 调优或选词不要只给“是否采纳”，可给连续指标（CTR、NDCG、转化率变化量），让每轮反馈都有信息量，延长有效迭代轮数。

  - 把 operational knowledge 做成可注入的 skills：在基座模型不变的情况下，将商品类目规则、广告政策、用户意图词典等做成紧凑文档放进
  context，能显著提升 agent 初始能力；实验中 base 从 28.8 到 68.2，说明业务知识注入比重新训练更便宜。

  - 在线上 agentic 工作流中预留 round budget，并用 best-so-far 指标评估：例如对高价值广告计划或搜索 query，可给 agent
  多次尝试与自评机会，按测试时消耗动态增加调用；但注意有效 horizon，超出 T* 后不再提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
解决难题不能靠单次尝试；现有 agent 训练数据多为“一次成功”快照，丢弃失败、反馈与修订，模型没有见过如何把一轮预算变成累计提升。自改进需要反思（每轮增益）与长程执行（保持多轮有效），两者是跨领域元技能。

### 方法
- 将自改进定义为测试时扩展：更多轮次应带来更好的 best-so-far score；分解为 reflection 与 long-horizon execution。
- 从 GitHub ML 仓库和在线评测题合成可验证环境，评分函数采用 graded score（如隐藏测试通过率）而非二值判定。
- 由 teacher agent 在数小时、数百次工具调用的预算内多轮迭代；保留 operational knowledge/skills 注入与每轮反馈。
- 整条轨迹入选条件只看最终分数高且过程合规，不筛掉失败轮/回退；监督时 loss 只施加在失败后产生进展的决策上。
- 用这些轨迹混合原有 deep-research 数据，微调 Qwen3.8-27B 得 AREX-2。

### 关键结果
- MLE-bench Lite 81.8（对比最高），Frontier-CS 70.7（开源最高）。
- 在未新增搜索数据的 deep research 上转移提升：BrowseComp 84.0、HLE 52.6、GAIA 92.2、DeepSearchQA 93.8。
- Frontier-CS 5h 内从 54.4 持续涨到 70.7；BrowseComp 无答案反馈时准确率从 64.8 随轮数升至 84.0，每轮增益约为上一代 3 倍。
- 消融显示：base 28.8 → +skills 68.2 → +trained model 多轮 81.8。

### 最值得记住的一句话
长程反思轨迹不仅保留成功，也保留失败与恢复，让模型学会在测试时把额外轮数持续转化为更好结果，并跨域迁移。
