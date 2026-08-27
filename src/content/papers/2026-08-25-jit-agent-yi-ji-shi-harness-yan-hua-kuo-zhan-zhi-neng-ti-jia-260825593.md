---
title: 'JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution'
title_zh: JIT-Agent：以即时 Harness 演化扩展智能体框架智能
authors:
- Guibin Zhang
- Leo Lu
- Fangzhou Xie
- Kang Zhu
- Junhao Wang
- Zhifei Xie
- Zhaochen Yu
- Zihang Liu
- Zhongxiang Sun
- Qiankun Li
affiliations:
- LV-NUS Lab
arxiv_id: '2608.25593'
url: https://arxiv.org/abs/2608.25593
pdf_url: https://arxiv.org/pdf/2608.25593
published: '2026-08-25'
collected: '2026-08-27'
category: Agent
direction: Agent harness 即时生成与演化
tags:
- Agent Harness
- Just-in-Time
- Preference Optimization
- Test-Time Evolution
- LLM Agents
one_liner: 训练 27B 元模型按任务即时生成/修复/演化 agent harness，使普通骨干模型超越更强基线与固定运行时
practical_value: '- **把推荐/搜索 Agent 的执行框架拆成可生成模块**：将 memory、planning、action、capability
  orchestration 四个模块协议化，用一个轻量 meta 模型按任务动态生成 harness，比固定 pipeline 更适配电商场景中深度研究、购物规划、多工具协同等异构任务。

  - **三阶段训练闭环可直接复用**：先用专家生成合法 harness 做 SFT+偏好对齐，再用失败修复轨迹教模型快速修 bug，最后用 Evo-GDPO 以历史最优为基线做在线偏好优化，保证
  reward 提升同时不牺牲 latency/cost。

  - **用“reward 提升且效率不退化”硬约束筛选候选**：偏好函数同时考虑 reward、latency、cost，避免靠堆 token 换分数；实验显示
  JIT harness 在性能提升的同时 token 成本平均降 36%，适合成本敏感的电商/广告 Agent 系统。

  - **引入 streaming archive 实现无参数持续进化**：线上任务执行后，只有突破 frontier 的 harness 才写入银行，后续任务检索相关历史
  harness 作为参考。这种轻量记忆库可迁移为搜索推荐 Agent 的跨任务经验积累。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent 能力不只由模型权重决定，harness（记忆管理、规划策略、动作协议、工具编排）往往主导最终表现。传统 Ahead-of-Time harness 依赖手工设计或离线搜索，难以适应实例级差异；不同任务需要不同的状态管理与控制结构，固定 harness 会限制模型上限。

**方法关键点**：
- 将 harness 形式化为可组合四模块协议 `h=(M,P,A,F)`：memory、planning、action、capability orchestration，并用 HarnessFactory 统一实现 13 种代表性脚手架作为种子。
- 训练 27B 元模型 JIT-Agent（基于 Qwen3.6-27B），推理时接收任务、协议、工具注册表与检索到的历史 harness，生成任务特化可执行 harness。
- 三阶段训练：Stage I 用更强教师生成合法 harness 做 SFT + 偏好学习，偏好约束为 reward 提升且 latency/cost 不退化；Stage II 把失败生成转化为最多两轮修复轨迹，教模型从编译错误、接口不匹配中恢复；Stage III 提出 Evo-GDPO，以 harness bank 中当前最优为基线，对候选组解耦 reward/latency/cost 优势并做 clipped PPO 更新，实现可训练的测试时演化。
- 推理支持 static（并行生成 N 个选最优）与 streaming（执行后按 frontier 规则更新 archive）。

**关键结果**：DeepSeek-V4-Flash + JIT-Agent 超过 GPT-5.6：DeepSearchQA +9.1、PinchBench +8.7、OdysseyBench +4.3；GLM-5.2 平均 +7.7、DeepSeek-V4-Flash 平均 +8.8，其中 DeepPlanning 子任务最高提升 +24.8。与 Claude Code/Codex/OpenCode 等固定 harness 控制对比，JIT 在 6 个 backbone-benchmark 中 4 个最优，token 成本平均降 36.0%，且跨 DeepSeek V4、Qwen3.6、Mimo-V2.5 三个模型家族 24/24 全提升，平均 +7.6。

**最值得记住的一句话**：Harness intelligence 是与模型权重、推理算力并列的第三维 scaling 维度，且可通过训练获得、跨模型迁移。
