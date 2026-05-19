---
title: Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use
title_zh: 模型自适应工具必要性揭示LLM工具使用中的知行鸿沟
authors:
- Yize Cheng
- Chenrui Fan
- Mahdi JafariRaviz
- Keivan Rezaei
- Soheil Feiz
affiliations:
- University of Maryland, College Park
arxiv_id: '2605.14038'
url: https://arxiv.org/abs/2605.14038
pdf_url: https://arxiv.org/pdf/2605.14038
published: '2026-05-12'
collected: '2026-05-19'
category: Agent
direction: Agent工具使用决策·元认知检测
tags:
- Tool Use
- Meta-cognition
- Knowing-Doing Gap
- Representation Probing
- LLM Agents
one_liner: 基于模型能力重新定义工具必要性，发现LLM内部认知与实际行动脱节，错配主因在认知到行动的转换阶段
practical_value: '1. 在电商Agent/多智体场景中，评估工具调用必要性时应改用**模型自适应的阈值**，而非人工静态标注——用多个采样运行的一致性（如N=10,
  T=0.7）判断模型是否真正需要工具，更贴合实际部署。

  2. 可以通过**隐藏状态线性探测**快速诊断工具调用错配的根源：是模型认知不到必要（阶段1），还是认知到了但执行失败（阶段2）。若阶段2占比高，无需重新微调认知，重点应放在后期层对齐。

  3. 后期层中认知与行动方向近乎正交，提示可在**训练时加入对齐正则项**，或在推理时对最后几个token的残差流进行干预（如转向认知方向），强制知行一致，减少无谓工具调用。

  4. 系统设计里，与其依赖显式自我评估（会大幅改变行为），不如**直接监测内部状态**来触发工具，避免知行鸿沟，这对需要高可靠性的搜索、计算类工具尤其有用。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
当LLM需要自主决定是直接回答还是调用工具时，传统研究将工具必要性视为静态的、与模型无关的标注，忽略了一个关键事实：同一个问题对强模型可能无需工具，对弱模型可能必须借助外部能力。这种模型能力的差异造成了巨大的“知行错配”——模型的实际调用行为往往与真实需求不一致，严重影响Agent的可靠性。

**方法关键点**  
- **模型自适应必要性定义**：对每个模型，对同一查询在无工具下运行N次（N=10, T=0.7），若某次失败则标记为tool-necessary，全部正确才为unnecessary。  
- **两阶段分解**：将工具使用拆分为内部认知（是否认为需要工具）和执行（是否实际输出调用token）。通过线性探测器从隐藏状态中解码出两个信号，再计算它们的余弦相似度与错配分布。  
- **实验设置**：4个模型（Qwen3-8B/4B, Llama-3.1-8B-Instruct, Llama-3.2-3B-Instruct），在算术混合数据集和TruthfulQA上分别配置计算器与搜索API。  

**关键结果**  
- 端到端行为错配率高达26.5%~54.0%（算术）和30.8%~41.8%（事实QA），且错误模式随模型和域变化剧烈。  
- 认知与行动信号在后期层、最后token位置几乎正交，意味着模型“知道但做不到”。  
- 逐样本轨迹显示，多数错配发生在认知到行动的转换阶段（stage-two error），而非认知阶段本身，形成显著的**知行鸿沟**。  
- 显式自我报告与内部状态探测结果差异大，且自我报告会大幅改变模型行为（up to 49%样本的工具调用发生变化），不适合实用场景。

**核心结论**：提升Agent工具使用可靠性不仅需要更强的元认知，更关键的是弥合认知与行动之间的鸿沟，让内部“知道该不该用”畅通地转化为实际的调用/不调用决策。
