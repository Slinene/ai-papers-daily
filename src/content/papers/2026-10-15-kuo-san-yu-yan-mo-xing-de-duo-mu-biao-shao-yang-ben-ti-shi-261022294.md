---
title: Multi-Target Few-Shot Prompting with Diffusion Language Models
title_zh: 扩散语言模型的多目标少样本提示
authors:
- Anton Xue
- Alan Li
- Rahul Saha
affiliations:
- University of Texas at Austin
arxiv_id: '2610.22294'
url: https://arxiv.org/abs/2610.22294
pdf_url: https://arxiv.org/pdf/2610.22294
published: '2026-10-15'
collected: '2026-10-18'
category: LLM
direction: 扩散语言模型 · 少样本多目标填充
tags:
- Diffusion Language Models
- Few-Shot Prompting
- Infilling
- Likelihood-Ratio Reward
- Text Editing
one_liner: 用扩散语言模型在共享画布中同时填充多个掩码区域，并通过似然比奖励提升少样本示例跟随能力
practical_value: '- 在电商文本结构化改写（如根据 2-3 个示例将商品描述转换成标题+卖点+属性标签等多字段）中，可借鉴扩散 LM 的多目标掩码填充：一次生成多个字段，利用左右上下文约束，比自回归逐
  token 生成更连贯且避免重复。

  - 选择性掩码+似然比奖励的思路可以迁移到 LLM 解码或 prompt 设计：只对关键槽位计算「有示例支持 vs 无示例支持」的概率比，作为过滤或重排分数，提高生成结果对
  few-shot 示例的忠实度，减少随意发挥。

  - 在需要格式转换/API 迁移的工程任务（如商品数据批量清洗、旧接口字段映射新接口）中，可以把每个字段当作一个掩码目标，展示少量成对示例后让扩散 LM 同时填充多个目标，减少多步串行生成的误差累积。

  - 若团队已在探索生成式推荐中使用 diffusion LM 生成 Semantic ID 或多属性 token，这种共享画布的多目标填充可用来同时预测多个 token（如类目+属性+ID），相互提供上下文。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

## 动机
少样本提示适用于难以用指令和奖励描述的任务，例如“按示例编辑”——将演示的格式变更或 API 迁移应用到多个位置。这类编辑通常同时依赖左右上下文，因果自回归模型只能单向生成，处理多目标填充不自然。

## 方法关键点
- 提出多目标少样本提示：用扩散语言模型在共享画布中对多个掩码区域同时进行填充，示例作为条件指导。
- 针对少样本提示中模型难以可靠遵循示例的已知问题，利用画布的选择性掩码，推导出似然比奖励，偏好那些被示例支持而非仅由语言模型先验驱动的填充。
- 扩散过程分多轮进行，已揭示的 token 可为其他掩码位置提供上下文，形成迭代协同填充。

## 关键结果
在少样本提示基准和软件重构案例中，演示能提升填充准确率；加入基于似然比的示例指导后，在多个设置上取得了进一步增益，验证了多目标协同填充和选择性掩码奖励的有效性。
