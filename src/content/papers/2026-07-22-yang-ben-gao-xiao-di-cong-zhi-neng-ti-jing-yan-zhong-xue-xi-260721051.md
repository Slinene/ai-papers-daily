---
title: Sample-Efficient Learning from Agent Experience
title_zh: 样本高效地从智能体经验中学习
authors:
- Chenhui Gou
- Haoqin Tu
- Yunhao Fang
- Jianfei Cai
- Hamid Rezatofighi
affiliations:
- Monash University
- ByteDance Seed
arxiv_id: '2607.21051'
url: https://arxiv.org/abs/2607.21051
pdf_url: https://arxiv.org/pdf/2607.21051
published: '2026-07-22'
collected: '2026-07-25'
category: Agent
direction: Agent 经验蒸馏 · 样本高效学习
tags:
- Experience Distillation
- Sample Efficiency
- In-Context Learning
- Agent Learning
- Context Distillation
- Branch Packing
one_liner: 提出经验蒸馏，无需额外环境交互即可将 ICL 增益蒸馏到模型权重，保留 64.8% 增益，比 SFT 高 17 倍，比 RL 节省 9.6 倍样本
practical_value: '- 在对话式推荐或 Agent 系统中，利用用户历史交互作为上下文进行 ICL，再通过单步经验蒸馏将改进的行为固化到模型权重，可大幅减少线上推理时的上下文长度和成本。

  - 分支打包技术能够在单个训练序列中高效利用长交互历史中的多个决策点，可迁移至用户行为序列建模，如将多次推荐点击/转化作为监督信号紧凑打包训练。

  - 模型自由的单步蒸馏避免了世界模型误差和额外的线上交互，适用于推荐场景中的离线日志训练，无需重新部署模型到线上试验即可提升策略。

  - 可借鉴多任务经验蒸馏实现零样本或小样本任务泛化，通过多用户群体的历史经验蒸馏提升模型对新用户的冷启动表现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
真实智能体任务（如代码修复、文本游戏）的环境交互成本高昂，传统强化学习需要大量样本。In-Context Learning（ICL）虽能通过上下文实现样本高效学习，但增益在上下文移除后消失。如何在不增加额外环境交互的前提下，将 ICL 学到的能力固化到模型权重，成为一个关键问题。

**方法关键点**  
- **问题定义**：Experience Distillation，将智能体从交互历史中通过 ICL 获得的决策改进蒸馏到模型权重。
- **核心思路**：采用**模型自由的单步分支展开**，在已记录的历史点上，用经验上下文条件 teacher 重新采样下一个决策，作为 student 的监督信号，无需世界模型，也无需额外环境交互。
- **关键实现**：  
  (1) **经验预处理**：对长历史进行摘要或改写，压缩噪声，提升 teacher 推理密度。  
  (2) **增强教师推理**：通过提示让 teacher 在生成决策前进行详细推理，提升蒸馏目标质量。  
  (3) **分支打包**：将同一轨迹上多个分支点的 teacher 决策串联为单一训练序列，大幅减少重复 prefix 计算，提升监督密度和训练效率。  
- **损失函数**：对 teacher 采样的决策 token 做 next-token prediction 交叉熵损失。

**关键结果**  
- 在 **749 个软件工程任务**上，Experience Distillation 将 pass@1 从 5.3%（零样本）提升至 51.4%，保留 **64.8%** 的 ICL 增益，而直接 SFT 仅保留 3.8%。  
- 在 **6 个文本冒险游戏**上，保留 **93.4%** 的 ICL 增益。  
- 与 PPO/GRPO 等 RL 基准相比，达到匹配性能所需环境样本**减少 9.6 倍**。  
- 分支打包将训练实例数从 4096 降至 128，训练时间缩短**超过 10 倍**。  
- **OOD 泛化**：在多任务蒸馏后，对未见过的软件工程任务 pass@1 从 4.62% 提升至 8.84%。  
- **连续蒸馏**：重复收集-蒸馏循环，性能持续累积，五次循环后平均得分从 7.1 升至 47.0。  

**本质洞见**：仅在已记录的交互历史点上重采样教师的下一步决策，就足以将 ICL 的行为增益有效蒸馏进模型参数，为样本高效的 Agent 持续学习提供了一条实用路径。
