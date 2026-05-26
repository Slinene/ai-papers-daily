---
title: 'Soap2Soap: Long Cinematic Video Remaking via Multi-Agent Collaboration'
title_zh: Soap2Soap：多智体协作的长片电影重制框架
authors:
- Yiren Song
- Huilin Zhong
- Kevin Qinghong Lin
- Haofan Wang
- Mike Zheng Shou
affiliations:
- Show Lab, National University of Singapore
- University of Oxford
- Lovart AI
arxiv_id: '2605.17423'
url: https://arxiv.org/abs/2605.17423
pdf_url: https://arxiv.org/pdf/2605.17423
published: '2026-05-16'
collected: '2026-05-26'
category: MultiAgent
direction: 多智能体协作长视频生成重制
tags:
- Video Remaking
- Multi-Agent System
- Dual-Bridge Consistency
- Long Video Generation
- Identity Consistency
- Verification Agent
one_liner: 提出双桥一致性（语言JSON剧本+动态视觉锚）与闭环验证的多智体框架，解决长视频重制中的身份漂移与语义侵蚀。
practical_value: '- **双桥一致性解耦设计**：将语义结构（JSON剧本）与视觉外观（动态锚点）显式分离，可迁移到商品视频生成中，保持商品外观一致性的同时保证动作与场景的叙事连贯性。

  - **上下文动态内存分配**：按镜头级别构建最小必要上下文包，避免全局信息冗余和角色混淆，适合多角色虚拟主播或多商品展示场景，降低内存开销并提升生成稳定性。

  - **网格联合合成策略**：将同一场景的多镜头关键帧打包成网格一次生成，通过共享注意力强制身份与场景一致性，可用于生成商品多角度展示图或短视频，减少风格偏移。

  - **闭环验证与选择性重生成**：引入验证代理自动审计生成结果的多维度一致性，发现问题仅重新生成受影响片段，适合推荐系统中自动产出高质量内容，降低人工审核成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长片级电影重制（如角色替换、风格迁移）需在数百个镜头中严格保持角色身份、叙事结构和运动编排的一致性，但现有视频生成方法经常出现身份漂移、背景突变与语义侵蚀，原因在于缺乏显式的长期一致性控制机制。

**方法关键点**：
- 多智体框架：视频理解代理、视频生成代理、验证代理协同工作。
- 双桥一致性：语言桥（场景感知的JSON剧本）提供持久语义骨架，视觉桥动态分配场景/镜头级视觉锚点（环境、角色、服装参考图），确保生成条件始终绑定到结构化语义与视觉约束。
- 上下文内存分配：为每个镜头动态构建最小必要内存包，包含角色引用、场景描述、拍摄参数，避免全局上下文导致的混淆与退化。
- 锚驱动生成：关键帧阶段采用网格联合合成（2×2或3×3）在共享潜在空间中生成多帧，增强身份与背景一致性；视频阶段调用Veo 3执行I2V，输出4-8秒片段后拼接。
- 验证代理：对关键帧和视频片段进行质量、身份、环境、情节四维审计，检测不一致时生成反馈并选择性重新生成，形成闭环校错。

**关键实验**：在自建SoapBench（10部电影，607个镜头）上评估，对比Mocha、Kling O1、Runway Gen-4。Soap2Soap取得身份一致性VLM得分9.17（对比最佳基线8.11）、场景一致性8.84（8.37）、情节一致性8.67（8.60），CLIP-I身份相似度0.842（0.632），场景相似度0.819（0.751）。消融实验去掉动态内存分配使F1从0.936降至0.618，去掉验证环使ID-VLM从9.17降至8.91，验证了双重机制的关键作用。

> 最值得记住的一句话：将长期一致性从提示工程的 emergent 行为升级为可解释、可控制的架构目标，正是多智体系统与显式记忆桥接在生成式任务中的价值所在。
