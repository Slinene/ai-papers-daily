---
title: A Self-Triggered Agentic Push Recommendation System
title_zh: 自触发式Agent推送推荐系统
authors:
- Zhao-Yu Zhang
- Qingying Chen
- Chunyuan Zheng
- Jing Zhou
- Jian Sun
- Siqi Chen
- Leiying Chen
- Chuan Zhou
- Huiyou Jiang
- Xin Tao
affiliations:
- ByteDance
- Peking University
arxiv_id: '2608.01949'
url: https://arxiv.org/abs/2608.01949
pdf_url: https://arxiv.org/pdf/2608.01949
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 自触发Agent推送推荐
tags:
- Agentic Recommender
- Push Notification
- Decision Transformer
- Ordinal Regression
- Computational Efficiency
- Bellman RTG
one_liner: 将推送推荐建模为自触发闭环决策，用DT联合优化时机与是否推送，显著提升活跃度并降低计算开销
practical_value: '- **时机与动作联合优化**：将推送的“何时触发”与“是否推送”统一为自触发闭环Agent，可迁移至电商广告的触达、消息提醒等场景，避免固定间隔预测的资源浪费。

  - **序数回归稳定预测时间**：用等频分桶将连续时间预测转化为序数回归，搭配门控RTG注入条件，解决高噪声下模型忽略RTG信号的问题，适用于任何需要预测最优间隔的推荐或排序场景。

  - **轻量过滤代理节约计算**：在执行重排序前用仅依赖用户和上下文特征的MLP过滤低价值请求，可显著降低下游排序的QPS成本（达79%），对大规模工业推荐系统尤其有借鉴意义，如电商推荐流/广告候选生成前的粗筛。

  - **Bellman RTG纠正离线日志偏差**：用贝尔曼方程重新计算回报并重赋权动作，缓解离线数据中次优行为的影响，适合在利用DT优化长期指标的业务中直接复用。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
推送推荐系统的核心挑战是“是否推送及何时推送”，需在严格资源约束下最大化用户长期活跃。传统预规划频率方法忽略实时上下文，固定间隔触发则面临计算开销与最优时机捕捉的矛盾。为此，论文重新定义推送为**自触发Agent决策过程**，由系统自主决定何时唤醒自身并执行推送。

**方法关键点**  
- **整体框架**：STEPS 由三个Agent构成闭环——规划Agent预测下次系统调用时间Δ𝑡，执行Agent在Δ𝑡到达时判断是否推送，过滤Agent在计算前剔除低价值请求。  
- **规划Agent**：采用决策变换器结构，提出**门控RTG**将目标回报通过哈达玛积注入状态嵌入，避免RTG被高维特征淹没；对连续时间进行100桶等频分桶的**序数回归**，预测Δ𝑡大于各边界的概率，提升长尾时间分布的稳定性。  
- **执行Agent**：采用**价值引导决策**，用贝尔曼方程学习𝑄值并计算优势权重，修正离线日志中的次优动作，对高𝑄值动作赋予更高采样概率。  
- **过滤Agent**：一个仅依赖用户和环境特征的3层MLP，蒸馏执行Agent的知识，提前过滤低价值或冗余请求，避免下游重排序的资源消耗。  
- **训练与推理**：训练时动态采样λₙ以学习目标平衡，损失函数综合下一时间预测、𝑄值回归和带权动作交叉熵；在线时可通过λₙ实时调整业务目标。

**关键结果**  
在抖音（超10亿用户）全量部署的在线A/B测试中，相比预规划频率基线：  
- 用户活跃天数提升 **+0.2843%**；  
- 推送权限关闭率降低 **-1.9089%**；  
- 过滤Agent使计算开销减少 **79.42%**。  
消融实验表明规划Agent对核心指标贡献最大，序数分桶等频策略优于等宽，门控RTG使模型有效学习条件生成。

**最值得记住的一句话**：推送系统应像智能体一样主动规划自我唤醒时机，而非被动等待固定调度，这能同时实现业务效果与计算效率的跨台阶提升。
