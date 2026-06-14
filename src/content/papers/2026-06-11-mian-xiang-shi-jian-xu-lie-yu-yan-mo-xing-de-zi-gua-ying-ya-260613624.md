---
title: 'Beyond Uniform Tokens: Adaptive Compression for Time Series Language Models'
title_zh: 面向时间序列语言模型的自适应压缩：超越统一Token处理
authors:
- Jialin Gan
- Xin Qiu
- Guangzhe Chen
- Xue Wang
affiliations:
- Zhejiang University
- Harbin Institute of Technology
- Shandong University
arxiv_id: '2606.13624'
url: https://arxiv.org/abs/2606.13624
pdf_url: https://arxiv.org/pdf/2606.13624
published: '2026-06-11'
collected: '2026-06-14'
category: LLM
direction: 时间序列LLM的Token压缩与推理加速
tags:
- adaptive token compression
- time series
- LLM
- inference acceleration
- frequency domain
- asymmetric token
one_liner: 从非对称Token视角提出自适应预算框架，在频域压缩时间序列Token并逐层削减提示Token，实现最高7.68倍推理加速与78%设置下的性能提升。
practical_value: '- **Token压缩思路可迁移到多模态LLM推理**：利用输入数据在频域/信息密度的非均匀性，设计自适应压缩模块，在电商图文理解、Agent对话历史管理等场景降低
  KV Cache 开销。

  - **动态Prompt Token削减策略**：观察到深层提示影响力衰减，可借鉴在 Agent 的 long-context 任务中，对不同深度层注入不同长度的
  System Prompt 或历史上下文，优化内存占用。

  - **训练时加入压缩预算约束**：在训练或微调阶段引入 Token 压缩目标，让模型学会保留关键信息，可应用于生成式推荐模型的用户行为序列建模，加速长序列处理。

  - **频域变换作为通用压缩手段**：将时序或序列信号变换到频域后根据能量分布进行压缩，可尝试用于电商点击序列的频域压缩表示，再送入推荐模型，在保证效果的同时减少序列长度。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 联合建模时序数值值与文本上下文时，通常将两者统一为 Token 序列，但时序 Token 和提示 Token 的信息结构差异显著，均匀处理导致效率低下。论文从非对称 Token 视角出发，发现时序 Token 在频域贡献高度不均（大量 Token 共享冗余频率模式，仅少数保留关键时序证据），且提示 Token 的影响随模型深度衰减，全层保留不必要的冗余。

**方法**：提出自适应 Token 预算框架。对时序 Token，通过频域变换（如离散余弦变换）将序列压缩到紧凑表示，保留高能量成分；对提示 Token，设计逐层减少机制，仅在浅层保留完整提示，深层用压缩后的简短提示替代。框架以微分化的预算分配实现端到端优化，可插拔集成到现有 TS-LLM 架构中。

**结果**：在预测、分类、补全、异常检测四类任务上，推理加速最高达 **7.68 倍**，并且 **78%** 的评估设置中获得性能提升，验证了非对称 Token 压缩对可扩展时序基础模型的有效性。
