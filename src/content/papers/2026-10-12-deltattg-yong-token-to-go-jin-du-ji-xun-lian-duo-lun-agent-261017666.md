---
title: 'DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter'
title_zh: DeltaTTG：用 Token-to-Go 进度计训练多轮 Agent
authors:
- Xuyan Ye
- Xiyan Fu
- Shengda Fan
- Jiawei Cui
- Yankai Lin
- Wei Lu
affiliations:
- Nanyang Technological University
- Renmin University of China
arxiv_id: '2610.17666'
url: https://arxiv.org/abs/2610.17666
pdf_url: https://arxiv.org/pdf/2610.17666
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 多轮 Agent RL · 过程信用分配
tags:
- RLVR
- Credit Assignment
- Process Supervision
- Multi-turn Agents
- Token-to-Go
- LLM
one_liner: 训练一个可复用的 Token-to-Go 进度计，将稀疏回合优势按步骤进步量重分配，提升多轮 Agent RL
practical_value: '- 在电商/搜索多轮 Agent 训练中，可直接复用 TTG 思路：把用户会话中“从当前搜索/推荐状态到最终下单/满意还需生成的
  token 数”作为剩余工作量监督，从线上日志低成本构建 progress meter，无需人工标注步骤好坏。

  - 冻结一个跨策略/跨模型共享的 progress meter，用 Δ_t = c_t - c_{t+1} 将回合级 outcome advantage 在步骤间重分配；保持
  trajectory advantage 符号和 token 均值不变，工程上只改 loss 中的 advantage 分配，容易接入现有 GRPO/DAPO
  等 RLVR 框架。

  - 采用 sign-aware 分配 + 均匀混合（ρ=0.2）+ token multiplier cap（M=5）可稳定训练，尤其是在多轮推荐/对话场景正负样本不平衡时；消融表明去掉
  sign-aware 或 uniform mixing 都会掉点。

  - progress meter 可用于线上推理的动作选择：在候选 query/商品/工具调用上试执行并用 meter 估计进步，选择进步最大的分支，论文显示在多个
  actor scale 上都能提升成功率并减少交互步数。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮 Agent 的 RLVR 只有稀疏的最终奖励，无法分辨中间动作的贡献；现有过程监督依赖外部标注、代价高昂的 judge 或任务特定启发式，难以泛化。

### 方法关键点
- **Token-to-Go (TTG)**：定义为一个轨迹中从当前状态到任务完成还需生成的 assistant token 数，作为剩余工作量的可观察代理；从多样化策略的轨迹中自动提取，无需人工标注。
- **进度计训练**：收集多模型（不同家族/规模）轨迹，每个前缀监督 completion label 和 TTG；用 SFT 初始化结构化输出 (b, v)，再用 GRPO 精炼；训练后冻结。
- **信用分配**：冻结 meter 给 actor 状态打分，Δ_t = c_t - c_{t+1} 表示进步/退步；sign-aware allocation：当优势 A>0 时进步获得更多正 credit，A<0 时退步获得更大负 credit；混合均匀份额 ρ=0.2，token 乘数 cap M=5；最终广播到 tokens 并对每个 trajectory 归一化，保持 reward 不变。
- 不改变 trajectory advantage 的 sign 和 token-average scale，只调整步骤间的优势分配强度。

### 关键实验结果
- 在 ALFWorld / PaperSearchQA / BFCLv3 上，Qwen3-4B 平均分 72.86 vs 最强 baseline 70.41；Llama-3.1-8B 平均分 66.49 vs 61.69。BFCLv3 提升最大（如 Multi-Turn +4.8，Non-Live/Live +7.6/+9.0）。
- 样本效率：ALFWorld Seen 约 75 步达 80% 成功率，GiGPO 需 125 步，减少约 40% 优化步数。
- 计算成本接近 GRPO；DAPO 是 GRPO 2.7x GPU-hours。
- 消融：替换 TTG 为 outcome value/logit/feasibility 均下降；去掉 sign-aware、meter training、uniform mixing 也下降。
- 进度计分析：AgentProcessBench 步骤质量准确率 56.91% vs direct prompting 50.83%；可在不同 actor scale 上引导测试时动作选择，提升成功率；跨域迁移到 PaperSearchQA 仍超过 GRPO。

### 最值得记住的一句话
用“剩余生成 token 数”作为过程进度监督，冻结共享进度计做 sign-aware 优势重分配，能以极低成本把稀疏 outcome reward 转化为步骤级信用。
