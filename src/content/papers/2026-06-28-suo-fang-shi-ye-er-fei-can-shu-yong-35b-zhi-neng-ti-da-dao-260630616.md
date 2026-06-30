---
title: 'Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance
  with a 35B Agent'
title_zh: 缩放视野而非参数：用 35B 智能体达到万亿参数性能
authors:
- Lei Bai
- Zongsheng Cao
- Yang Chen
- Zhiyao Cui
- Shangheng Du
- Yue Fan
- Shiyang Feng
- Zijie Guo
- Haonan He
- Liang He
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2606.30616'
url: https://arxiv.org/abs/2606.30616
pdf_url: https://arxiv.org/pdf/2606.30616
published: '2026-06-28'
collected: '2026-06-30'
category: Agent
direction: Agent 长时域扩展 · 多教师在线蒸馏
tags:
- Agent
- Long-horizon
- Knowledge-action graph
- Multi-teacher distillation
- MoE
- On-policy distillation
one_liner: 构建长轨迹知识-行动图与多教师在线蒸馏，让 35B MoE 智能体在科学、工程、搜索等长程任务上超越万亿参数模型
practical_value: "- **长轨迹过程监督：KAG 构建思路可复用**  \\\n  论文将搜索、工具调用、验证信号统一为知识-行动图（KAG），每条训练轨迹平均\
  \ 45K tokens，包含成功与失败的中间步骤。在电商搜索/推荐场景中，多轮对话推荐、深度商品调研等长程任务可借鉴此方式，把用户交互、工具调用、商品浏览记录构建为可训练的过程级监督数据，而非仅依赖最终答案。\n\
  - **多教师在线蒸馏的域路由设计**  \\\n  六个异构领域（搜索、工程、科学、指令跟随、工具调用）各训练一个领域教师，通过域路由的在线策略蒸馏（OPD）合并到单一\
  \ 35B 学生，避免不同领域梯度冲突。电商中不同品类、不同阶段（召回/排序）的专家模型可用同样方式蒸馏为统一部署模型，通过领域标签路由教师信号，保持各领域专长。\n\
  - **显著词汇对齐（SVA）提升蒸馏效率**  \\\n  SVA 仅约束教师高概率 token 子集（top-k 支持集）上的分布，避免全词汇表对齐引入噪声。在推荐生成式语义\
  \ ID 或文本答复时，可借鉴该技术，在蒸馏生成任务中聚焦关键 token，提高知识转移稳定性。\n- **RL 训练中的优势增强与数据复用**  \\\n \
  \ 工具调用 RL 中利用过程评分为失败轨迹提供分级奖励（仅负数样本使用过程奖励），并用数据复用（64 个 hard case 反复 rollout）在少量步数内达到高效提升。当业务有少量高质量困难任务时，可复用该策略进行\
  \ RL 微调，降低对庞大数据集的依赖。"
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
大规模语言模型通过扩展参数达到了强大的智能体能力，但万亿参数模型的训练与部署成本极高，且长程任务（如科学推理、深度搜索）中模型常因缺乏过程监督而积累错误。本文探索一条正交路径：扩展智能体的“视野”（horizon），即通过更长的轨迹和更丰富的交互学习，让小模型达到大模型的性能。核心挑战在于：（1）缺乏统一的知识-行动基础设施来生成可验证的长轨迹训练数据；（2）异构领域能力（搜索、工程、科学等）难以集成到单一模型。

## 方法
- **知识-行动图（KAG）**：将信息获取、工具调用、可执行迭代、证据验证、约束跟踪等原子能力建模为类型化的图结构（证据、行动、观察、验证结果），并通过自博弈搜索扩展 KAG，生成平均 45K tokens 的长轨迹训练数据。
- **三阶段训练**：
  1. 全领域监督微调（SFT）：在 100K 长轨迹上微调 Qwen3.5-35B-A3B，建立基础智能体能力；
  2. 领域教师训练：针对搜索、科学推理、指令跟随、工具调用等六个领域分别用 RL 或 SFT 训练专家模型；
  3. 多教师在线策略蒸馏（OPD）：学生生成 rollout，由对应领域教师提供逐 token 指导，采用域归一化损失和显著词汇对齐（SVA）仅约束教师高概率 token 子集，平衡各领域影响。
- **RL 训练细节**：搜索任务使用 GRPO，搭配效率惩罚和重复惩罚；工具调用采用非对称优势（仅在失败样本中加过程奖励），并用 64 个 hard case 的反复采样实现高效 RL。

## 关键实验
在多个长程智能体 benchmark 上，35B 的 Agents-A1 表现优于万亿参数模型 Kimi-K2.6 和 DeepSeek-V4-pro：SEAL-0 (56.4 vs 52.2/54.0)，IFBench (80.6 vs 73.0/75.9)，HiPhO (46.4 vs 43.3/41.1)，FrontierScience-Olympiad (79.0 vs 78.0/76.0)，MolBench-Bind (56.8 vs 21.6/37.8)，并在 SciCode (44.3)、HLE (47.6)、BrowseComp (75.5) 上保持竞争力。消融实验显示全领域 SFT 后各领域能力有基础提升，而领域教师 RL/OPD 带来了进一步显著增益。

> **核心结论**：通过构建长轨迹过程监督和领域路由蒸馏，35B 模型可以在多个长程智能体任务上达到万亿参数级别的性能，证明了“视野扩展”是一条可行且成本更低的路径。
