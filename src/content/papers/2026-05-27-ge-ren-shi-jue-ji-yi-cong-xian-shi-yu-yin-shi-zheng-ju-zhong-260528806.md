---
title: Personal Visual Memory from Explicit and Implicit Evidence
title_zh: 个人视觉记忆：从显式与隐式证据中学习
authors:
- Viet Nguyen
- Thao Nguyen
- Vishal M. Patel
- Yuheng Li
affiliations:
- Johns Hopkins University
- University of Wisconsin-Madison
- Adobe Research
arxiv_id: '2605.28806'
url: https://arxiv.org/abs/2605.28806
pdf_url: https://arxiv.org/pdf/2605.28806
published: '2026-05-27'
collected: '2026-05-31'
category: Agent
direction: 多模态记忆 · Agent 长期记忆评估
tags:
- Visual Memory
- Personalized Agents
- Multimodal Memory
- Benchmark
- RAG
one_liner: 提出首个面向个性化AI助手的视觉记忆基准，并设计混合视觉-文本记忆架构显式保留身份与所有权
practical_value: '- **图片记忆不应沦为caption**：现有记忆系统将图像转为文本描述，丢失身份、所有权等关键视觉信息。你的电商/Agent场景若涉及用户上传图片（如服装、家居），应保留结构化视觉特征，而非仅存文本摘要。

  - **延迟提交机制值得工程化**：当图像信息不足以立即判断时，不急于提取结构化记忆，而是暂存pending状态，待后续多张图像累积证据后再统一解析。这一trick可迁移到用户多轮上传图片的商品识别、搭配推荐等场景。

  - **结构化视觉记忆的模块设计**：将记忆拆成relationship、entity、fact三个层级，分别存储社交关系、物体/宠物实例、持久化用户事实，按需路由。电商场景可类似设计：从用户晒图中抽取拥有的商品、偏好风格（实体/事实），而非仅用文本embedding。

  - **利用合成数据构建视觉记忆评估管线**：论文用一致化角色-场景-物体图像生成pipeline构建有多distractor的长会话，可借鉴用于Agent记忆能力的离线评测，避免隐私风险。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有长时记忆基准和系统以文本为中心，图像被转为caption，丢失身份、所有权等关键个人视觉证据。用户分享的照片中既包含显式实体（如宠物、个人物品），也包含可推理出的隐式事实（如养猫但不直说）。这些信息对个性化AI助手至关重要，但缺乏相关评测基准和记忆架构。  
**方法与架构**：
- **基准构建**：合成10个用户persona，包含社交图谱、拥有的物品/宠物；生成1,717个多轮对话事件，分为显式实体、隐式事实（纯视觉/多模态）和distractor三类；用主题一致性图像生成确保同一个人/物体/场景跨对话视觉连贯；最终产生696道选择题。
- **VISUALMEM架构**：分三步处理图像——①上下文引导解读：结合周围对话消歧图像归属；②延迟提交：若证据不足将图像挂起，待后续多张图像累积后重新解析；③结构化提取：将确认信息按关系、实体、持久事实三层存入视觉记忆，同时将事实文本化同步至文本记忆后端。
- **检索时路由**：实体相关问题走视觉记忆，事实/偏好走文本记忆或二者融合。  
**关键结果**：
- 视觉基准上，仅使用文本记忆的SOTA方法MemOS准确率56.0%，VISUALMEM达84.1%，在目标人物（95.0 vs 45.0）和目标资产（91.1 vs 59.9）提升巨大。
- 纯视觉记忆优于纯文本记忆，验证了图像信息的关键性；增加文本记忆可进一步提升隐式多模态事实。
- 移除延迟提交后整体下降2%以上，证明其必要性。
- 在标准文本记忆基准LOCOMO和PersonaMem上，VISUALMEM与MemOS持平，未破坏文本记忆能力。  
**核心结论**：个性化AI的长期记忆必须显式保留图像中的身份、所有权和用户事实，不能简单依赖caption。
