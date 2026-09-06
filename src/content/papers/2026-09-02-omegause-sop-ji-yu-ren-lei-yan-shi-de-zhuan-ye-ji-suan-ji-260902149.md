---
title: 'OmegaUse-SOP: SOP Engineering for Professional Computer Use from Human Demonstrations'
title_zh: OmegaUse-SOP：基于人类演示的专业计算机使用SOP工程
authors:
- Yixiong Xiao
- Lang An
- Hucheng Yang
- Pinxue Ma
- Yongquan Chen
- Jingjia Cao
- Yusai Zhao
- Ting Wang
- Ting Liu
- Siqi Bao
affiliations:
- Baidu, Inc.
- Ningxia Electric Power Engineering Co., Ltd.
arxiv_id: '2609.02149'
url: https://arxiv.org/abs/2609.02149
pdf_url: https://arxiv.org/pdf/2609.02149
published: '2026-09-02'
collected: '2026-09-06'
category: Agent
direction: GUI Agent 技能工程化
tags:
- GUI Agent
- SOP Engineering
- Human-in-the-loop
- Multimodal Trace
- Verification
- Professional Software
one_liner: 提出SOP Engineering系统OmegaUse-SOP，将人类专业软件操作演示转化为可复用GUI Agent技能，提升专业SOP任务可靠性
practical_value: '- 对电商运营自动化（如自动操作广告投放后台、商家后台、ERP）的Agent，可借鉴Observe-Reason-Configure-Execute四阶段：先录制人类专家操作轨迹，再抽象成语义级步骤，配置领域规则，最后执行时逐步grounding+验证，而不是让LLM一次生成全部操作，能显著提高可靠性。

  - 将SOP与Agent分离，类比prompt engineering，把“专业技能”作为可迭代资产：每次执行失败或人工修正后，回流更新演示和规则，形成企业专属的Agent技能库，类似推荐系统中的用户行为反馈闭环。

  - 步骤级验证（step-wise verification）思路可迁移到多步Agent任务中，例如在电商选品、广告调价等流程中，每一步生成后由规则或轻量模型校验中间状态，避免错误累积导致任务失败。

  - 多模态轨迹（截图+事件流）可作为训练/微调数据，尤其适合缺乏API的专业软件场景；在电商内部工具中，若某些操作只能通过GUI完成，此方法可低成本积累领域专家知识。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM正从对话助手进化为能操作外部数字环境的Agent，GUI Agent是关键载体。但专业领域的标准作业流程（SOP）隐含领域知识、软件专用约定和任务级验证要求，通用计算机使用基准难以覆盖。

**方法**：提出OmegaUse-SOP，一个人机协同的SOP Engineering系统，将人类专家在专业软件上的操作演示转化为可复用的GUI Agent技能。系统包含四个模块：Observe记录专家操作的多模态GUI轨迹；Reason把低级事件抽象成语义步骤级指令；Configure融入领域规则与任务参数；Execute在真实GUI环境中执行，包含逐步grounding、动作生成与验证。整体类比prompt engineering，通过迭代优化演示、执行规则和领域知识，形成可复用的技能资产。

**结果**：与电力行业客户合作，在光伏仿真软件PVsyst 7.2的工作流上进行测试，结果表明OmegaUse-SOP能提升GUI Agent在专业SOP任务上的可靠性，展示了在领域专用软件中部署GUI Agent的可行路径。
