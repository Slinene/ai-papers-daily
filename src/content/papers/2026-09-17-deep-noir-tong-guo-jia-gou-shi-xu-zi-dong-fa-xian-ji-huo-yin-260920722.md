---
title: 'Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in
  Transformer Models'
title_zh: Deep Noir：通过架构时序自动发现 Transformer 激活引导参数
authors:
- Frank E. Bobe
- Gregory D. Vetaw
- Darshan W. Bryner
- Matthew G. Cook
- Jose L. Salas-Vernis
affiliations:
- Naval Surface Warfare Center Panama City Division
arxiv_id: '2609.20722'
url: https://arxiv.org/abs/2609.20722
pdf_url: https://arxiv.org/pdf/2609.20722
published: '2026-09-17'
collected: '2026-09-19'
category: LLM
direction: LLM 推理时激活引导自动化
tags:
- activation steering
- mechanistic interpretability
- logit lens
- causal attribution
- prompt injection
- inference-time intervention
one_liner: 用 Logit Lens 收敛与因果头级归因自动定位 steering 层/头/幅度，实现跨任务激活引导
practical_value: '- **诊断优先的自动化 steering 参数搜索**：把 Logit Lens 收敛（模型何时从不确定到确定）与因果头级归因结合，可以替代手工调层、调头、调幅度。在电商/广告场景部署
  LLM 分类器或内容过滤器时，可复用这套 pipeline 自动化定位需要干预的层和头，降低维护成本。

  - **Head masking 是跨任务泛化的关键**：论文显示 RepE 不 mask head 在情感任务上无效，而 Deep Noir 的 head masking
  使所有模型都提升。实际做 steering 时，不要直接加全局方向向量，要先用因果归因找出对目标任务有贡献的 head 子集再干预。

  - **安全审查 Agent 的 prompt injection 风险量化**：steering 幅度越大，模型越容易被注入攻击。如果电商安全 Agent 或评论审核系统使用了
  steering 来控制输出，需要知道攻击面随 steering 强度单调上升，应在实际部署中限制 steering 强度或加入额外的注入检测层。

  - **架构时序作为可解释性工具**：Logit Lens 概率收敛曲线可以帮工程师理解模型在哪一层完成语义决策，这对优化推理截断、层剪枝、甚至识别哪些层对推荐/搜索
  query 理解关键有参考价值。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Activation steering 在推理时修改 LLM 行为有效，但手工选择干预层、头子集和幅度难以跨架构和任务扩展。现有自动化方法缺乏因果机制依据。

**方法关键点**：提出 Deep Noir 框架，核心是“Architectural Chronometry”——通过 Logit Lens 追踪 token 概率从不确定到确定的过程，测量模型在哪一层解决语义概念；再结合因果头级归因 patching，自动搜索完整的 steering 参数 (L, K, M, d)。与单独组件不同，组合 pipeline 实现跨任务泛化：RepE 无 head masking 在情感任务上不优于 baseline，而完整流程成功。

**关键结果**：在 1B×3、2-3B×2、7-9B×4 共 9 个模型上验证。Spam 任务 1B 模型提升 16.7 个百分点（标准差 4.7，39 次运行），7-9B 提升 21-42 个百分点；SST-2 情感任务零代码改动提升 13.1 个百分点。Deep Noir 对所有模型均有提升（p<0.01）。还揭示 steering 产生可预测的 prompt injection 攻击面，漏洞随 steering 幅度单调增加，这对部署 steered 分类器的 Agent 系统至关重要。
