---
title: Post-Training Language Models for Gold-Medal Performance in Coding Competitions
title_zh: 面向竞赛编程金牌表现的后训练语言模型
authors:
- Aleksander Ficek
- Sean Narenthiran
- Mehrzad Samadi
- Somshubra Majumdar
- Boris Ginsburg
affiliations:
- NVIDIA
arxiv_id: '2609.02849'
url: https://arxiv.org/abs/2609.02849
pdf_url: https://arxiv.org/pdf/2609.02849
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: LLM 后训练 + 测试时扩展
tags:
- post-training
- test-time compute
- GRPO
- synthetic data
- competitive programming
- NVFP4
one_liner: 端到端后训练+GenCorrect 迭代测试时计算，IOI 2026 得分 535.4 超人类冠军
practical_value: '- **强 teacher 蒸馏 + 难例/自修正 trace 更划算**：用大模型为 hard query、长尾 item 或复杂
  Agent 任务生成推理与自我修正轨迹，SFT 能带来大部分单次推理提升；预算有限时优先 SFT，RL 作为补充，且不要只用 terminal binary reward，可引入过程奖励或分步反馈。

  - **GenCorrect 式反馈闭环适合 query 推荐 / 文案生成**：并行采样 100-200 条候选，用 token-shingle/embedding
  聚类选 10 个多样性代表，再通过 offline/online evaluator 获取分目标得分，维护累计最佳指标并回填 prompt。适合 API/submission
  预算受限、需要多样性覆盖的场景。

  - **测试时扩展比继续训练模型更有效**：论文中 5 轮 GenCorrect 带来 +107~158 分，远超 RL 的个位数百分点。电商搜索结果页、广告文案或推荐解释可先生成大量候选，再用执行反馈或用户信号筛选，而不是一味增大模型规模。

  - **NVFP4 + MTP 的吞吐-质量权衡可复用**：在固定 inference 窗口内，FP8 KV cache + 关闭 prefix caching
  + MTP=5 使吞吐 3.7x，质量仅小幅下降。若 Agent 需秒级生成大量候选（如自动出价理由、推荐解释），可先做量化/投机解码保吞吐，再用采样多样性补质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：竞赛编程是 LLM 推理能力的重要试金石，但达到金牌的系统往往混合数据、后训练、模型规模和测试时计算，各组件贡献难以拆解。该工作构建端到端管道，系统评估 SFT、RL 与测试时计算对 IOI/ICPC 表现的影响。

**方法关键点**：
- 数据：从 16 个竞赛家族和在线平台筛选 22,000 题，构建可执行评测环境；用 DeepSeek-V4-Flash 为 Nano 生成 1.2M 条推理轨迹、为 Ultra 生成 477k 条，难题和自修正轨迹占比更高。
- SFT：Nano 训 3 epochs，Ultra 训 1 epoch，支持 262K token 序列打包。
- RL：仅对 Nano 做 GRPO，3,219 道可执行题，每步 1,024 个 rollout，只给编译执行后满分 1 / 否则 0 的 terminal reward，无 KL 惩罚。
- GenCorrect：5 轮迭代；每轮生成 200 个候选，编译过滤后用 token-shingle 聚类选 10 个代表提交，累积子任务得分作为反馈，下一轮用最佳子任务向量 + 3 个互补参考继续生成。

**关键结果**：
- IOI 2025：Nano Score@1 从 130 提升到 SFT 后 280、RL 后 291；GenCorrect 5 轮达 468，超过金牌线 438.3；Ultra-CC 达 502。
- ICPC 2025 Pass@1：Nano 从 16.9% 提升到 51.0%；LCB Pro 从 17.6% 提升到 71.6%。
- IOI 2026 live：竞赛专用 Ultra-CC 在真实时间/提交/断网约束下得分 535.4/600，超过金牌线 361.12 和人类冠军 498.27。
- 竞赛专用优化：用 GLM-5.2 轨迹替代 DeepSeek 轨迹做 SFT；NVFP4 量化后吞吐 736.8 tokens/s/GPU，约为 BF16 的 3.7 倍，分数仅降 6.6 个百分点；最后轮生成 1,000 候选并用执行生成测试用例排序。

**最值得记住的一句话**：SFT 带来最大的单次推理提升，RL 只提供小幅增量；真正拉开竞赛差距的是 GenCorrect 这类反馈驱动的迭代测试时计算，而不是继续堆模型或训练阶段。
