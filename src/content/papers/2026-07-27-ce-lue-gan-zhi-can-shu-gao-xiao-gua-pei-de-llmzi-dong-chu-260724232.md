---
title: Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Bidding
title_zh: 策略感知参数高效适配的LLM自动出价框架
authors:
- Songyue Cai
- Lianyu Wang
- Shan Gu
- Ziru Xu
- Jian Xu
- Xiaofeng Zhu
- Bo Zheng
affiliations:
- Hainan University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.24232'
url: https://arxiv.org/abs/2607.24232
pdf_url: https://arxiv.org/pdf/2607.24232
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: LLM自动出价 · 策略感知参数高效微调
tags:
- Auto-Bidding
- LLM
- Parameter-Efficient Fine-Tuning
- Mixture of Experts
- LoRA
- Cross-Attention
one_liner: SAGE通过位置增强、文本对齐与约束门控LoRA，仅用不到10%参数实现策略感知的LLM自动出价最优决策。
practical_value: '- **位置增强模块可迁移到用户行为序列建模**：将序列中不同语义类型的token（如点击/购买/曝光）赋予独立语义嵌入，结合正弦时间编码，取代统一的绝对位置编码，提升序列区分度和长度扩展性，适用于推荐系统的会话理解。

  - **门控交叉注意力对齐多模态信息并压缩输入**：在处理用户行为轨迹与自然语言指令（如搜索query、广告文案）融合时，用轨迹作为Query、文本作为Key/Value进行交叉注意力，替代直接拼接，既实现有效跨模态对齐，又大幅缩短LLM输入长度，适合对话式推荐Agent或指令跟随出价。

  - **约束门控MoE LoRA实现低成本策略个性化**：将业务约束（如预算、CPA目标）编码为门控信号，驱动混合专家LoRA动态选择适配器，每个广告主或场景只需额外极少参数即可定制策略，工程上可冻结LLM主干，只训练轻量适配模块，显著降低训练和部署成本。

  - **整体框架可复用于多约束实时决策场景**：SAGE的冻结骨干、低秩适配、条件路由设计可直接应用于电商搜索排序中的动态出价、预算分配或Push消息的个性化约束优化，用10%的参数实现超越全量微调的效果。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在线广告自动出价需在动态拍卖中实时调整出价以满足CPA等多约束，传统方法（离线RL、序列建模）缺乏利用文本指令的能力，而现有LLM方法存在轨迹-文本交互浅、模态对齐差、全量微调成本高且易遗忘预训练知识等问题，急需一种参数高效且能感知约束策略的LLM适配方案。

**方法关键点**  
SAGE由三个模块组成，系统解决表征、融合和适配挑战：  
- **位置增强**：将位置嵌入分解为非参数正弦时间编码（支持变长轨迹）和可学习语义嵌入（为RTG、状态、动作三种token赋予不同角色），增强轨迹结构理解，参数极少。  
- **文本对齐**：使用门控交叉注意力，以轨迹嵌入为Query，任务描述文本嵌入为Key/Value进行融合，输出与轨迹等长，既对齐跨模态空间又避免拼接带来的超长输入，显著降低计算开销。  
- **约束门控LoRA**：冻结LLM主干，每层后以约束条件文本与轨迹隐状态进行交叉注意力获得门控信号，经MLP聚合后由Router选择MoE LoRA专家进行低秩适配，实现条件驱动的策略自适应，仅训练极少量参数（约9%）。  

**关键实验结果**  
在阿里AuctionNet稠密/稀疏两个版本上评估，SAGE在5个预算档位下均取得最优Score。稠密100%预算下，相比最强LLM基线LLM-DT，Score提升6.40%，相较Prompting提升22.03%；稀疏版本提升更显著（10.15% vs. LLM-DT）。消融实验移除位置增强或文本对齐，性能分别下降30.4%和7.2%。全量微调需更新380.6M参数，而SAGE仅需31.6M（不到10%），性能反而更优。

**核心记忆句**  
SAGE证明，通过解耦时间-语义位置编码、交叉注意力模态对齐和约束门控MoE LoRA，冻结的LLM仅需不到9%的参数量即可在复杂约束出价中超越全量微调，实现最优决策。
