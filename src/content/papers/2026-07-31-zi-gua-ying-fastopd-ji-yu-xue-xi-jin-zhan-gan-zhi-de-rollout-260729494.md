---
title: 'Adaptive FastOPD: Progress-Aware Rollout Horizon Expansion for Efficient On-Policy
  Distillation'
title_zh: 自适应 FastOPD：基于学习进展感知的 rollout horizon 扩展, 实现高效 on-policy 蒸馏
authors:
- Qian Tan
- Huaifei Liang
- Xuanyu Zhu
- Lei Jiang
- Yuqiang Li
affiliations:
- University of Science and Technology of China
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2607.29494'
url: https://arxiv.org/abs/2607.29494
pdf_url: https://arxiv.org/pdf/2607.29494
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: On-Policy Distillation 自适应 rollout 调度
tags:
- OPD
- Adaptive Rollout
- Training Efficiency
- Plateau Detection
- Teacher-Student
- Progress-Aware
one_liner: 通过监测 OPD 训练进度并仅在边界区域进展停滞且充分利用当前长度时扩展 rollout horizon，自适应加速训练达 71.2% 并保持最优性能。
practical_value: '- **动态调度生成/推理长度**：在电商推荐或 Agent 在线采样中，批量内响应长度差异大，长尾拖慢整体。可借鉴自适应扩展机制，根据学习收敛信号（而非固定步数）动态决定是否增加采样长度，避免无效计算。

  - **多信号融合监测训练进展**：用 top-k 重叠、概率质量、共享贪婪优势、非共享惩罚四个互补信号归一化后取最大值，比单信号更鲁棒地判断当前阶段是否收敛，可应用于推荐模型的强化学习微调中，避免单一指标过早触发策略更新。

  - **长度利用率门控过滤长尾**：仅当足够比例样本到达当前 horizon 或边界时才扩展，防止少数超长响应主导批次时间。推荐系统中生成式召回的序列长度、对话
  Agent 的多轮交互深度均可采用类似门控，减少 straggler 影响。

  - **相对基线的归一化**：不对原始 teacher-student 一致信号设绝对阈值，而是以刚进入当前 horizon 时的值为基线，计算相对改进幅度。这种自参照设计可迁移到任何动态阶段训练任务，使超参数对模型和数据更稳健。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
On-policy 蒸馏 (OPD) 在线采样学生模型轨迹并用教师分布进行 token 级监督，训练成本随 rollout 长度增长，且批次内少数超长响应导致同步等待时间倍增。现有加速方法用固定预算或绝对一致性阈值控制长度，对不同模型和训练阶段需重新调参。为此提出 Adaptive FastOPD，一种进度感知的自适应 rollout horizon 扩展策略，旨在动态分配计算资源，在保持性能的同时大幅减少训练耗时。

**方法关键点**  
- 从短 horizon 开始，每步监测当前边界区域 \([H-\Delta H, H)\) 的四个教师-学生信号：top-k 重叠 (O)、共享概率质量 (P)、共享贪婪惩罚 (G)、未共享 token 惩罚 (U)。  
- 信号转换为非相似度指标后，以刚进入该 horizon 时的观测均值为基线进行归一化（对数相对值），再取最大值作为聚合得分，经 EMA 平滑得到 \(z_n\)。  
- 若 \(z_n\) 连续 \(K_{\text{pat}}\) 步不创新低则判定进展停滞，结合长度利用率门控（\(\bar{\eta}_{\text{hit}} \geq \tau_{\text{hit}}\) 或 \(\bar{\eta}_{\text{reach}} \geq \tau_{\text{reach}}\)）决定是否扩展 horizon。该门控确保边界区域有充足样本，避免少数长响应驱动无效扩展。  
- 扩展幅度 \(\Delta H\) 固定，最大 horizon 为 15360 tokens。全程无须预设每阶段的步数间隔或绝对信号阈值。

**关键实验与结果**  
在 DAPO-Math-17K 上训练，两个 teacher-student 对：(1) DeepSeek-R1-Distill-Qwen-1.5B / JustRL-DeepSeek-1.5B；(2) Qwen3-1.7B-Base / Qwen3-8B-Base。对比基准包括 OPD 7K/15K 固定长度、固定步数间隔的 FastOPD。
- **DeepSeek 对**：Adaptive FastOPD 获平均分 56.1，优于 OPD 15K (55.6) 和固定 FastOPD (55.7)，训练时间 6h16min，较 OPD 15K 节省 49.1%，较固定 FastOPD 节省 13.4%。  
- **Qwen3 对**：平均分 20.1，用时 2h37min，较 OPD 15K (19.1 / 9h) 节省 71.2%，较固定 FastOPD (19.4 / 5h) 节省 47.3%。  
- **消融实验**：固定步数间隔对性能影响大（表现跨度 9.1~9.8%），自适应策略在不同超参数下平均分波动仅 0.4~0.9%，鲁棒性强；去掉长度利用率门控在 Qwen3 上反致训练时间增加（2h37min → 6h06min）；仅用单一 overlap 信号速度更快但性能下降，多信号组合取得最佳平衡。

**核心启示**  
“一种进度感知、多信号融合且含长度利用门控的自适应 horizon 扩展框架，可作为训练加速与长尾抑制的通用范式，迁移至任何需要在线采样且存在批量长度差异的序列决策任务。”
