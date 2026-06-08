---
title: 'M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions'
title_zh: M3Exam：真实用户-智能体交互的多模态记忆基准测试
authors:
- Zhengjun Huang
- Wenxuan Liu
- Zhoujin Tian
- Wei Chen
- Junle Chen
- Yuqian Wu
- Fangyuan Zhang
- Qintian Guo
- Xiaofang Zhou
affiliations:
- The Hong Kong University of Science and Technology
- Beijing University of Chemical Technology
- Harbin Institute of Technology (Shenzhen)
- Beijing Institute of Technology (Zhuhai)
- Tencent Hy
arxiv_id: '2606.07402'
url: https://arxiv.org/abs/2606.07402
pdf_url: https://arxiv.org/pdf/2606.07402
published: '2026-06-05'
collected: '2026-06-08'
category: Eval
direction: 多模态长期记忆评估与模态感知检索
tags:
- Multimodal Memory
- Agent Evaluation
- Modality-aware Retrieval
- Long-term Conversation
- Benchmark
- MLLM
one_liner: 首个多会话多模态记忆基准M3Exam及模态感知方法M3Proctor，按需使用原始视觉提升13%准确率且token减少70%以上
practical_value: '- **模态感知级联检索**：电商Agent可借鉴M3Proctor的查询模态偏向检测，先用文本替身回答，仅在需要时加载图片/文档，大幅降低多模态推理token成本。

  - **记忆索引优化**：将图片转为caption、文档转为digest作为文本替代品，并附加模态标签，结合偏向重排序提升跨模态检索精度，适用于多模态商品知识库的RAG。

  - **长会话记忆摘要**：通过紧凑的session summary维持跨会话线索，帮助电商智能客服在多轮对话中保持用户长期记忆，避免上下文断裂。

  - **隐式意图评估设计**：引入Implicit Inference和Thematic Reasoning题型，可移植到推荐系统长期用户理解的评测中，检验模型从非明确信息推断偏好与状态的能力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有智能体记忆基准假设人‑人对齐、图像稀疏、内容直白，忽视真实场景中多会话多模态碎片化信息和隐式用户意图推断。为此推出M3Exam，聚焦真实用户‑智能体交互，覆盖15种人格、239个多会话对话（3025轮）、1799个多模态附件和5150道评测题，新增跨模态推理和隐式推断两大难点题型，评估长期多模态记忆的三个维度：内容复杂度、推理复杂度和意图复杂度。

**方法关键点**  
- **基准构建**：基于人格与核心事件生成时间线，合成多轮对话，通过事件滑动窗口扩展会话并附加图片/文档；从八类题型（单会话SS、多会话MS、时序TR、多模态MR、找图FM、主题推理TH、隐式推断II、事实判断FJ）构建平衡题库，每题标注支撑事实轮次。  
- **M3Proctor记忆方法**：索引阶段将原始模态转换为文本替身（caption、图表转写、文档摘要）并附加模态标签；推理时先检测查询模态偏向，利用偏向向量重排序检索结果，然后采用成本感知级联——先仅用文本替身回答，若信心不足或模态偏向未满足则升级加载原始视觉源（图片、图表、文档），实现按需消费视觉。  

**关键实验**  
- 最强闭源MLLM（GLM‑5.1）在M3Exam上总分仅0.549，Agent记忆系统普遍弱于无检索的前沿MLLM，暴露跨模态推理（MR）和隐式推断（II）的明显短板。  
- M3Proctor以Qwen‑2.5‑VL‑7B为骨干，总分0.484，领先其他Agent记忆系统（次优0.456），在MR上的LLM‑Judge达到0.606，FM的EM达0.569。  
- 效率方面，M3Proctor的索引构建仅需72秒（MIRIX需43271秒），每查询token 4591（MIRIX需13491），且仅26.4%的查询触发了级联，视觉任务上的级联带来了+0.116 (FM) 和+0.092 (MR) 的显著增益。

**核心结论**：模态感知的按需视觉消费是解决多模态长期记忆效率与精度矛盾的有效途径，M3Exam可作为该方向的标准化评测框架。
