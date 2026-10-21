---
title: Heterogeneous Agentic Coevolution
title_zh: 异质智能体共进化：专用基础模型与LLM Agent的互惠学习
authors:
- Wenqian Ye
- Ziwei Guan
- Zi Yang
- Shivani Modi
- Cici Cong Wu
- Yunlong He
- Yuxin Chen
- Zhengyu Zhang
- Liang Luo
- Venkatesh Ranganathan
affiliations:
- Meta AI
- University of Virginia
arxiv_id: '2610.16078'
url: https://arxiv.org/abs/2610.16078
pdf_url: https://arxiv.org/pdf/2610.16078
published: '2026-10-11'
collected: '2026-10-21'
category: Training
direction: 专用模型与LLM Agent共进化训练
tags:
- Heterogeneous Coevolution
- LLM Agents
- Reinforced Self-Training
- Recommendation
- Foundation Models
- Harness Search
one_liner: 提出 HACE 框架，让专用基础模型与 LLM agent 互惠共进化，在推荐、蛋白质功能、材料稳定预测上全面超越收敛后基线
practical_value: '- **用 LLM agent 做“经验筛选器”提升收敛后的推荐模型**：让 agent 基于当前 specialist 的预测生成候选，只保留贡献
  r_i = q_A - q_S > 0 的 verified response，再用这些 response 选择 specialist 的训练样本。电商推荐中可对已收敛的
  SASRec/HSTU/Wukong 类模型继续榨取提升，尤其长尾/冷门类目。

  - **融合打分公式很轻量，可直接上线实验**：joint prediction 使用 s_i(c) + λ a_i(c)，agent 分数按 log reciprocal
  rank 衰减，λ 通过交叉验证在固定网格上选择。这种 fusion 不改变 specialist 结构，适合快速接入现有排序链路。

  - **保留更新需做 paired validation，避免噪声回滚**：每次 specialist 或 harness 更新后，在同一 validation
  batch 上用当前 agent 做配对评估，只接受 ΔJ > 0 的 proposal。工程上可作为在线/离线模型迭代的安全门控。

  - **harness 进化搜索可自动发现上下文/课程策略**：论文中 harness 搜索会自动移除 genre metadata、隐藏候选排名、把课程指向
  hard cases。对应推荐系统可进化地决定给 agent 看哪些特征/上下文、以及哪些训练样本进入下轮 specialist 微调，减少人工试错。

  - **agent 与 specialist 不必同构，小 agent 也可能够用**：实验显示 Gemma-4 E4B 比更大的 26B-A4B 带来更稳定提升，说明业务中不必追求超大
  LLM agent，计算资源配置可优先给 specialist 微调。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

专用基础模型（如推荐系统 HSTU/Wukong、蛋白质语言模型 ESM-2、材料势函数 CHGNet）通过大规模预训练获得强领域能力，但一旦监督训练收敛，人工改进空间有限。同时，LLM agent 能基于反馈探索和自我改进，但一般通用模型缺乏领域深度。已有自进化系统大多只更新 agent 代码或 harness，不更新底层 LLM；而 agent 蒸馏类方法又固定 teacher 参数。论文提出：随着 specialist 能力提升，agent 需要学习新的弱点；agent 的探索反过来应影响 specialist 的训练数据。这种互惠学习（reciprocal learning）是核心挑战。

## 方法关键点

- **整体框架 HACE**：联合进化 Specialist S、Harness H、Agent A。每个 round 经历 harness 优化 → specialist 优化 → 联合选择 → agent 优化。
- **Agent 引导的经验选择**：agent 基于当前 specialist 的预测生成候选，不用标签；任务质量贡献 r_i(τ)=q_A_i(τ)-q_S_i，只有 r_i>0 且通过验证的 response 才用于选择 specialist 训练样本。
- **Specialist 监督学习**：用 agent 选择的实例做原始任务 loss 微调，不做 label 改写，只改变“在哪里训练”。
- **联合选择**：候选排序融合 s_i(c)+λ a_i(c)，λ 交叉验证；paired validation 仅接受 ΔJ>0 的更新。
- **Agent 的 on-policy 强化自训练**：在接受后的 specialist/harness 下重新采样 response，保留每个实例贡献最大的正贡献 response，用 ReST-EM 式 loss 微调 agent。
- **进化 harness**：搜索并优化信息交换、上下文、课程策略，让 agent 看到的候选视图和训练样本选择随能力进化。
- **理论保证**：给出从 adaptively selected experience 学习的风险界，将 specialist 风险分解为未充分暴露的源质量与已暴露经验上的最终 loss。

## 关键结果

- **推荐**：在 MovieLens 1M 和四个 Amazon 类目，覆盖 SASRec、HSTU、Wukong 三种架构，HACE 在所有 15 个设置上 HR@10 最高，相对 Base 平均提升 12.1%，最高 +18.5%；Wukong 在四个 Amazon 类目提升 12.9%–16.6%。
- **蛋白质功能预测**：CAFA 上 ESM-2 650M 的 NDCG 从 0.6285 提升到 0.6745，ProtT5-XL 从 0.6241 提升到 0.6739，远超其他自进化方法最多 0.0040 的提升。
- **材料稳定预测**：WBM 上 NDCG 从 0.6388 提升到 0.6541，超过最强对比方法 0.0028，且所有附加指标最优。
- **消融**：移除任意组件均掉点；agent 优化对 Toys 掉最多，specialist 优化对 WBM 掉最多，证明贡献按任务变化。
- **扩展性**：ESM-2 从 35M 到 3B，HACE 均带来约 +0.04 NDCG 增益；35M 微调后超过初始 3B 模型。

**最值得记住的一句话**：HACE 让 agent 的探索决定 specialist “在哪里继续学习”，而 specialist 的当前能力反过来决定 agent “哪些探索值得强化”，两者通过可进化的 harness 形成正向互惠闭环。
