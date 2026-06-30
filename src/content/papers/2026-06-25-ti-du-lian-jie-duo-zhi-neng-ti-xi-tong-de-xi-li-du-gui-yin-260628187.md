---
title: 'GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems'
title_zh: 梯度连接：多智能体系统的细粒度归因与提示优化
authors:
- Xiaocheng Yang
- Abdulrahman Alrabah
- Dilek Hakkani-Tür
- Gokhan Tur
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.28187'
url: https://arxiv.org/abs/2606.28187
pdf_url: https://arxiv.org/pdf/2606.28187
published: '2026-06-25'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体细粒度归因与提示优化
tags:
- multi-agent systems
- gradient-based attribution
- credit assignment
- prompt optimization
- LLM
one_liner: 将多智能体系统建模为计算图，利用梯度连接权重实现token级影响量化，精准定位错误并优化提示。
practical_value: '- **多智能体链路可解释性与调试**：在电商搜索/推荐的多智能体系统中（如查询改写→召回→排序→生成解释），可借鉴GBC构建计算图，用梯度反向传播计算每个智能体输出的token级贡献，快速定位“哪个智能体哪一步说错了话”，代替人工逐链排查。

  - **自动化提示词优化**：通过归因图识别错误节点后，直接对相应智能体的提示进行针对性修改（如强化缺失信息、调整角色定义），无需依赖粗粒度宏观调参。对于频繁迭代的对话式购物助手，可嵌入自动优化管道。

  - **高效实现AgentChord**：论文提出的prefix-based梯度缓存与重计算策略，可降低大规模Agent拓扑下的归因成本，适合在线服务或离线评估时对Agent链路进行细粒度审计。

  - **任务导向对话与协商场景**：在广告投放的竞价协商、多部门联合推荐等仿照MultiWOZ的任务型多轮对话中，GBC可提升信息传递效率，减少协调失败。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多智能体系统虽能分解复杂任务，但常因协调失误和缺乏细粒度信用分配而表现不佳。现有反馈多为粗粒度，难以判断哪个智能体或交互步骤出错。

**方法**：GBC将多智能体系统抽象为计算图，在每个连接处引入**基于梯度的连接权重**，量化上游智能体输出对下游推理的token级影响。通过构建归因图并反向传播特定任务的损失信号，可精确定位错误源头。在此基础上，对相应智能体的提示词进行针对性优化，而非全局调整。为提升效率，提出AgentChord，利用前缀缓存和梯度重计算减少开销。

**结果**：在MultiWOZ和τ-bench两个多轮任务对话数据集上，GBC优化后的多智能体系统战胜了强单智能体和多智能体基线，且归因质量越高，优化效果越显著。
