---
title: 'Ψ-Bench: Evaluating Persona-Sensitive Influencing in Persuasive Dialogues'
title_zh: 'Ψ-Bench: 评估基于画像的个性化说服对话能力基准'
authors:
- Peixuan Han
- Hongyi Du
- Jiayu Liu
- Yihang Sun
- Yutong Liu
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.02754'
url: https://arxiv.org/abs/2606.02754
pdf_url: https://arxiv.org/pdf/2606.02754
published: '2026-06-01'
collected: '2026-06-03'
category: Agent
direction: 个性化代理 · 说服性对话评估
tags:
- LLM Evaluation
- Persuasion
- Persona
- Benchmark
- RL Profile Analyzer
one_liner: 提出Ψ-Bench，通过模拟个性化客户评估LLM在说服性对话中的画像敏感影响能力
practical_value: '- 电商客服或营销对话中可借鉴画像驱动的评估框架：用合成用户画像模拟真实客户，并用LLM裁判评估对话的个性化和说服效果，替代或补充人工评估。

  - 在对话推荐或主动推送中，可部署轻量级画像分析器（如RL训练的小模型）从用户历史对话中实时推断偏好，动态调整话术，提升转化。

  - 发现即使强模型在缺乏用户特定信息时说服力有限，意味着在生成式推荐或对话代理中，显式用户建模（如行为序列、长期偏好）比单纯提升生成质量更关键。

  - 评估指标设计上，将“个性化响应水平”作为中间指标，与最终效果强相关（ρ=0.77），可在业务中用作可解释的离线代理指标，降低线上实验成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
当前个性化LLM代理多是被动响应用户偏好，但实际场景（如辅助决策、主动建议）要求代理能主动影响用户。现有说服评估忽略目标用户的个性化特征，导致评判偏向模型默认偏好，而非真实用户反应。Ψ-Bench旨在系统性评估LLM基于用户画像的主动说服能力，推动更贴近现实的个性化交互研究。  

**方法关键点**  
- 设计三种说服场景：**观点辩论**（来自Reddit CMV数据，500个测试话题）、**心理咨询**（90个来自CounselBench的心理咨询问题）、**日常请求**（100个合成请求），共约690个查询。  
- 为每个查询配对一个**合成人物画像**（包括性格、说话风格、政治观点等），画像基于真实对话历史生成（辩论场景用LIWC语言特征），用于实例化模拟客户。  
- 评价采用三个LLM裁判指标（9分制）：**对话质量**、**个性化响应水平**、**说服效果**，裁判提示包含详细评分准则，并与人类标注显著相关（辩论效果AUC=96.0）。  
- 还提出一个基于**强化学习（GRPO）**的画像分析器（Qwen3-4B-RL），从对话历史中预测客户画像，以在画像隐藏时提升说服表现。  

**关键实验结果**  
- 评测10个前沿LLM：GPT-5.1平均效果分最高（5.79/9），Qwen3-8B最低（4.05/9），所有模型效果分均低于6，表明个性化说服仍是难题。  
- 提供完整客户画像（Oracle设置）使所有模型平均效果提升**18.24%**，个性化分提升**41.19%**，揭示信息准确性是瓶颈。  
- Qwen3-4B-RL画像分析器在辩论场景画像相似度达55%，应用到说服对话中使效果提升**9.1%**（强于零样本DeepSeek-v3.2的6.4%），且仅用4B参数便接近Oracle上限，验证了推断式画像建模的实用价值。
