---
title: 'LERA: LLM-Enhanced RAG for Ad Auction in Generative Chatbots'
title_zh: LERA：面向生成式聊天的两阶段LLM增强RAG广告拍卖
authors:
- Haoran Sun
- Xinrui Song
- Xinyu Zhang
- Zhaohua Chen
- Xu Chu
- Zhilin Zhang
- Chuan Yu
- Jian Xu
- Bo Zheng
- Xiaotie Deng
affiliations:
- Peking University
- Alibaba Group
- Shandong University
arxiv_id: '2605.16474'
url: https://arxiv.org/abs/2605.16474
pdf_url: https://arxiv.org/pdf/2605.16474
published: '2026-05-15'
collected: '2026-05-19'
category: GenRec
direction: 生成式推荐 · 广告拍卖机制设计
tags:
- LLM-based-ad-auction
- RAG
- Two-stage-ranking
- Logit-scoring
- Incentive-compatibility
- Generative-chatbot
one_liner: 先由关键词嵌入粗筛，再用LLM logits精排，并以临界值支付保证激励相容，实现高效精准的聊天广告插入。
practical_value: '- **两阶段LLM排序可用于电商推荐/广告**：先用轻量检索（如关键词嵌入）粗筛Top-K，再调用LLM logits精排。既保持效率，又能捕获复杂意图，尤其适合高并发在线服务。

  - **用logits而非文本输出做排序**：在SGLang等推理引擎中，可通过并行pre-filling提取候选标签的log概率，比文本生成更稳定、可解耦，方便与出价等数值信号融合，适合实时竞价。

  - **临界值支付规则适配多阶段筛选**：胜出者支付两阶段门槛的最大值，可移植到带粗排-精排的推荐广告混排系统，保证广告主真实报价，降低经济设计风险。

  - **多广告插入的段落化生成策略**：在长回复或对话中分段重新拍卖，利用KV-cache重用控制延迟，可应用于多轮对话广告位、直播带货字幕广告等场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在LLM驱动的聊天机器人中插入广告面临两难：纯嵌入相似度检索（如现有RAG-based auction）难以捕捉意图转移、否定偏好等语义细节；直接用LLM对全量广告商打分则计算开销过大，且需合理的拍卖规则适配战略出价。  

**方法关键点**  
- **两阶段评分**：第一阶段用LLM生成2-3个意图关键词，再计算关键词嵌入与广告描述的余弦相似度，按「相似度×出价」选出Top-K（K=5或8）进入候选集；第二阶段将候选列表连同“不插入”选项喂给LLM，提取对应标签的logits经softmax归一化作为有机相关性分数，再乘以出价决定胜者。  
- **临界值支付**：胜者支付max{进入Top-K所需的最低出价，击败第二阶段次高竞争者所需的最低出价}，同时满足两阶段约束，保证在贝努利点击/估值独立且无偏假设下出价真实最优。  
- **多广告插入扩展**：在长回复中分段生成，每段前缀重用了SGLang的RadixAttention缓存，仅在每段开始时执行一次两阶段拍卖，控制额外延迟。  

**关键实验**  
- 在100个广告商、8品类的合成基准上，构造240条单广告查询（含复杂意图、意图转移、否定细化场景）。LERA在各模型尺度上显著优于纯嵌入基线：4B模型准确率94.6% vs 62.93%；30B达98.7%；235B达97.5%（因保守不插入有些损失）。直接LLM-only在小模型上反而更差，证明粗筛必要。  
- 多广告动态插入（50个查询，每查询需覆盖3类需求）：LERA的类别覆盖率比嵌入基线高20+个百分点（4B：72% vs 46.67%；30B：80% vs 42%）。  
- 吞吐-延迟分析显示，LLM-only在高并发下迅速瓶颈，而LERA在concurrency≤4时延迟可控，K=8时达到较好折中。  

**核心结论**  
将LLM的logits作为相关性信号引入拍卖，仅在粗筛后的小集合上计算，是平衡上下文理解与推理效率的有效设计；配合多段插入和临界值支付，可为生成式聊天广告提供扎实的工程与机制基础。
