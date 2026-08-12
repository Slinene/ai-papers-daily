---
title: 'What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in
  Conversational Systems'
title_zh: 视觉对齐的图像编辑跟随建议：三阶段学习框架
authors:
- Zhijing Zhang
- Jinpeng Yu
- Xin Song
- Bingnan Li
- Chuyue Li
- Changhui Du
- Xiaolin Fang
- Jiaming Liu
- Ruihua Huang
affiliations:
- Alibaba Qwen Business Unit
- Southeast University
arxiv_id: '2608.07565'
url: https://arxiv.org/abs/2608.07565
pdf_url: https://arxiv.org/pdf/2608.07565
published: '2026-08-02'
collected: '2026-08-12'
category: QueryRec
direction: 多模态 query 推荐 · RL 对齐
tags:
- multimodal recommendation
- image editing
- visual grounding
- reinforcement learning
- click preference
- GRPO
one_liner: 三阶段框架结合人工意图、点击偏好与源-目标视觉验证，将视觉不一致率从3.7%降至0.9%，在线CTR提升32.70%
practical_value: '- **位置感知点击偏好对**：利用点击建议仅与上方未点击建议配对，减少展示位置偏差，适合任何有曝光顺序的推荐场景（如电商搜索推荐）。

  - **多目标GRPO优化**：组合点击偏好、格式有效性、PPL、内容感知长度、列表内多样性五维奖励，使用动态文本侧权重调整长度与多样性压力，可迁移至生成式推荐列表的强化对齐。

  - **图像优先源-目标验证**：将编辑指令拆解为所需源（必须存在）与目标（不应已满足），分步检查视觉条件，可作为多模态Agent的动作校验器，避免幻觉推荐。

  - **SFT数据构建流水线**：从真实会话与人工意图表中用大模型生成候选，再经多级验证形成监督信号，解决了缺乏推荐标签时的冷启动问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
对话式图片创作中，80.1%的跟随编辑请求依赖于最新图像内容，纯文本建议无法满足需求。现有系统要么只做文本查询推荐，要么仅执行编辑指令，缺少一种既对齐用户偏好又保证编辑可行性（视觉一致性）的推荐方法。  

**方法关键点**  
- **三阶段渐进式监督**：Stage 1 利用在线真实会话与人工审核的编辑意图表，由大模型生成候选并严格验证，构建SFT数据；Stage 2 从用户点击反馈中抽取位置感知偏好对训练奖励模型，结合格式有效性、PPL、长度、多样性共五个奖励进行GRPO优化；Stage 3 引入图像优先源-目标视觉验证器，检查每条建议所需的源是否存在、目标是否已满足，作为第六个奖励强化视觉一致性。  
- **奖励设计**：点击偏好采用Bradley-Terry建模，长度奖励按内容密度分级分配预算，多样性用最大余弦相似度惩罚，视觉一致性通过验证器的结构化输出计算。  
- **训练与部署**：策略模型仅为8B Qwen3-VL，验证器仅在训练中使用，在线推理无额外时延。  

**关键实验**  
- 离线：视觉不一致率从3.7%（Stage 2）降至0.9%（Stage 3），且专家GSB评分从+405升至+446。  
- 在线A/B测试（14天，百万级用户）：相对初始prompt策略，CTR提升32.70%，图片保存率提升16.32%，平均对话轮次提升39.90%（p<0.05）。  
- 消融：位置感知配对将点击奖励模型准确率从0.619提至0.690；源-目标结构化验证器召回率达78.7%，误拒率仅0.6%，优于单轮基线（47.5%/22.2%）。
