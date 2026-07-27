---
title: 'ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders'
title_zh: ICAE-Bench：交互式项目构建编程代理评估基准
authors:
- Zhongyuan Peng
- Dan Huang
- Chuyu Zhang
- Caijun Xu
- Changyi Xiao
- Shibo Hong
- David Lo
- Lin Qiu
- Xuezhi Cao
- Jiyuan He
affiliations:
- Fudan University
- Meituan Group
- Singapore Management University
- Shanghai Innovation Institute
arxiv_id: '2607.21217'
url: https://arxiv.org/abs/2607.21217
pdf_url: https://arxiv.org/pdf/2607.21217
published: '2026-07-22'
collected: '2026-07-27'
category: Agent
direction: 交互式编程Agent评估与用户模拟
tags:
- Coding Agents
- Interactive Evaluation
- User Simulation
- Benchmark
- Project Building
one_liner: 提出首个从模糊需求出发交互式构建项目的编程代理评估基准，包含480个任务与自动用户模拟
practical_value: '- **用户模拟器设计思路可迁移至对话式推荐**：使用预定义的“用户数据”来约束模拟过程，避免人为虚构需求或泄露答案，确保交互可重现。搜索/推荐Agent评测中可借鉴此法，用历史行为序列生成模糊意图并模拟用户追问。

  - **多维黑盒评估范式适用于Agent推荐**：除功能正确性外，还细粒度评估语义相似度、结构保真度、交互质量等，可指导构建推荐/搜索Agent的全面评估体系，防止仅看单一指标导致误判。

  - **将模糊需求锚定到具体真实代码库**：在电商导购Agent场景，可用真实商品库或业务接口作为“可执行基准”，评估Agent能否将模糊意图（如“帮我找个性价比高的蓝牙耳机”）逐步澄清并落地为具体推荐/搜索动作。

  - **通过隐藏约束与边界情况暴露Agent短板**：评测表明当前模型擅长表层复现，但对隐藏业务规则、异常分支处理不足。在推荐系统中，可专门设计需要常识推理、用户长尾偏好、促销规则链的测试集，以检验Agent的深层理解与交互决策能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：随着vibe-coding的兴起，编程代理不再局限于完成明确指令，而需将模糊的产品意图转化为可工作的软件，这要求其具备需求澄清、工具使用、调试和仓库级构建等综合能力。然而现有基准仍停留在静态、完全指定的任务上，无法评估代理在交互式项目构建中的表现。

**方法**：ICAE-Bench从一个模糊的产品需求出发，利用一个自动化的User Agent模拟动态交互过程。为保证真实性与可评估性，设计三大关键机制：① 每个任务的模糊性源自一个精确的真实开源仓库，以其可执行行为作为锚点，避免无约束模糊需求的歧义；② 通过预定义的User Agent数据约束交互，使模拟用户能逐步揭示隐藏约束，而不凭空捏造新需求或泄露实现细节；③ 采用标准化的黑盒测试搭配多维诊断指标，包括功能正确性、语义与API相似度、结构保真度、设计质量及交互质量。

**结果**：基准涵盖12种编程语言、480个任务，在6个主流编程模型与2个代理框架上评估。实验表明，模糊项目生成对当前模型仍极具挑战：代理通常能复现可见行为，但在隐藏约束、边界案例和长程集成方面频繁失败，交互质量也有明显不足。多维分析显示，即使最终功能达标，内部结构与参考实现也可能存在显著差异。
