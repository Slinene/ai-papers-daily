---
title: 'From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating
  Full-Stack Web Applications from Requirements'
title_zh: 从可运行到可交付：多Agent测试驱动全栈Web应用生成
authors:
- Yuxuan Wan
- Tingshuo Liang
- Jiakai Xu
- Jingyu Xiao
- Yintong Huo
- Michael R Lyu
affiliations:
- The Chinese University of Hong Kong
- Columbia University
- Singapore Management University
arxiv_id: '2605.17242'
url: https://arxiv.org/abs/2605.17242
pdf_url: https://arxiv.org/pdf/2605.17242
published: '2026-05-16'
collected: '2026-05-20'
category: Agent
direction: 代码Agent测试驱动开发优化
tags:
- Test-Driven Development
- Code Generation
- Web Applications
- Coding Agents
- Multi-Agent
one_liner: TDDev框架通过自动化验收测试、浏览器交互验证与失败翻译，使全栈Web应用生成质量提升34-48个百分点，且协议必须匹配模型风格。
practical_value: '- **测试驱动的闭环反馈可用于生成式推荐或Agent管线**：将业务需求（如“推荐多样化商品”）自动转化为结构化验收用例（用户故事+交互步骤+预期结果），由LLM
  agent模拟用户行为在部署环境执行验证，再将失败点转化为代码修复信号，可复用至多步推理或工具调用场景。

  - **协议与模型生成风格匹配原则**：在Agent工作流编排中，对偏好整体重写的模型（如Sonnet）应赋予高自主权的agentic TDD（仅给予工具和流程提示，不强制步骤），对偏好增量修改的模型（如Qwen）应采用分步强制的incremental
  TDD；错配会完全抵消反馈增益，且token消耗数倍增加，这一规律可迁移至多Agent协作策略选择。

  - **浏览器交互验证的轻量化架构**：使用Playwright + 可访问性树作为页面状态表示，由同一个LLM逐步生成Playwright动作并根据历史轨迹给出通过/失败/部分通过的verdict，无需预知页面结构，实现低误判（100%缺陷召回率，仅有保守型假阴性），该设计可直接用于电商Agent的UI自动化测试或端到端功能回归。

  - **成本-质量权衡的量化方法**：通过计算每提升一个百分点的token消耗（tok/pp），为不同协议建立边际成本曲线，指导生产环境选型；实验中增量TDD对保守模型带来最高精度但token消耗是整体TDD的24倍，为类似Agent系统的算力预算提供参考。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**

现有coding agent生成的Web应用超过70%不符合功能需求，差距源于从自然语言需求到可交付应用之间存在三堵墙：需求模糊需人工澄清、正确性只能在浏览器中通过真实交互验证、浏览器中观察到的失败难以自动转化为可操作的修复信号。人工完成这些步骤既费力又阻碍自动化闭环研究。

**方法关键点**

TDDev框架分三步实现无人介入的测试驱动开发闭环：
1. **验收测试生成**：将高层需求转化为结构化测试用例。采用“肥皂剧测试”思路，让LLM先构想具体角色及目标，再细化出交互步骤与预期结果，实测对WebGen-Bench纯功能特征的覆盖率达91.9%，仅有全局导航类结构特性可能遗漏。
2. **浏览器交互验证**：部署应用后，基于Playwright与页面可访问性树的LLM testing agent按步骤动态生成操作并积累轨迹，最终输出Pass/Fail/Partial。agent判定准确性87.5%，对缺陷的召回率100%（无假阴性），偶有假阴性（错报正确应用为失败）仅触发不必要的重试，属于安全保守。
3. **失败翻译**：当测试不通过时，将交互轨迹与agent的自然语言观察转化为结构化报告，指明“哪个功能，在哪一步失败，观察到什么现象”，供coding agent直接修复。

框架支持四种开发协议：Non-TDD（基线，无任何TDD工具）、Incremental（逐个特征强依赖部署-测试-修复循环与回归套件）、Whole-Project（一次性实现后全特征测试修复）、Agentic（仅提供部署与测试工具，由agent自由决定工作流）。

**关键实验**
在WebGen-Bench和ArtifactsBench上，搭配Claude Sonnet 4.6和Qwen-3.5-397B模型，以及ClaudeSDK和OpenCode两款agent。
- TDD基础设施一致带来显著提升：与Non-TDD相比，至少一种TDD协议将准确率提升34~48个百分点（如Sonnet + Agentic-TDD 65.8% vs. 31.3%，Qwen + Incremental 71.4% vs. 23.3%）。
- 最优执行强度高度依赖模型生成风格：Sonnet偏好整体重写，Agentic-TDD匹配最好（单次65.8%），若强制使用Incremental则增益归零；Qwen偏好读后增量修改，Incremental最佳（71.4%），Agentic因长会话内补丁累积导致近半数应用崩溃。
- Whole-Project随着修复轮次大致翻倍精度，Incremental对风格不匹配的模型则迅速停滞。
- 匹配正确的配置边际成本极低，而错配协议消耗9.7百万token却零提升，甚至会付出25倍的token代价换取更差的精度。
- 用户调查显示TDDev将开发者手动介入时间降为0，工作量从持续提示工程转变为全自动反馈驱动修复。

**核心结论一句话**
测试驱动开发的有效性高度依赖协议与模型生成风格的匹配：匹配能为全栈代码生成带来翻倍以上的效果，错配则完全浪费全部重试预算。
