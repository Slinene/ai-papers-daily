---
title: 'WebChallenger: A Reliable and Efficient Generalist Web Agent'
title_zh: WebChallenger：基于结构化页面表示与分治策略的高效通用 Web Agent
authors:
- Jayoo Hwang
- Xiaowen Zhang
- Vedant Padwal
affiliations:
- ML Collective
- longsurf.ai
- Independent
arxiv_id: '2606.10423'
url: https://arxiv.org/abs/2606.10423
pdf_url: https://arxiv.org/pdf/2606.10423
published: '2026-06-08'
collected: '2026-06-13'
category: Agent
direction: Agent 架构优化 · 认知脚手架
tags:
- Web Agent
- PageMem
- Divide-and-Conquer
- Compound Actions
- Exploration
- Open-Source
one_liner: 通过 PageMem 页面结构化表示与三大认知机制，用开源小模型无微调达到逼近闭源大模型的 Web 任务成功率
practical_value: '- **结构化页面表示 PageMem 可直接复用到电商 Agent**：将商品列表页拆分为导航栏、商品卡片列表、筛选面板等语义段，每段缓存摘要和交互元素，后续任务复用，大幅降低重复解析成本。

  - **分治观察流水线**：先让 Agent 浏览段摘要，只选择任务相关区域展开详细信息；在推荐业务中可避免把整个商品详情页 token 堆进 prompt，聚焦价格、评价、库存等关键信息。

  - **离线探索 + 持久记忆**：对目标网站预先遍历构建 PageMem 地图和元素行为记录，Agent 在执行任务时直接拿书签和菜单跳转信息，类似 RAG
  中的预先索引；适用于长期运行的购物比价 Agent。

  - **复合动作工作流**：将下拉选择、表单提交等多步交互封装为单个 Agent 动作，内部自动处理局部状态变化（如菜单展开），避免每步重新观察全页；在电商搜索、下单、多轮筛选场景能显著减少决策步数和
  LLM 调用'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
人类浏览网页高效依赖三个认知优势：选择性关注相关区域、持久记忆网站结构、对常用交互模式形成程序化流畅操作。现有 LLM Web Agent 却将整页文本扁平输入，缺乏跨会话记忆，每做一步原子操作都要重新理解全页，导致性能瓶颈和推理成本高昂。论文认为差距不在于模型智能，而在于缺乏合适的观察、记忆和行动脚手架。

**方法关键点**  
1. **PageMem 结构化页面表示**：基于 DOM 递归分割，将页面拆分为语义段（如导航栏、列表、表单），每段携带摘要、交互元素、位置等元数据，作为统一抽象层供各组件使用。  
2. **分治观察流水线**：Agent 先浏览段摘要选择任务相关区域，再从选定区域提取细节，最后合成紧凑页面摘要，避免全页 token 爆炸，让 32B 模型也能处理长页面。  
3. **离线探索与记忆**：任务前对网站做确定性遍历，记录页面、路径、元素交互结果，建成 WebSiteMem；任务中 Agent 可加载书签和下拉菜单信息，实现零样本站点先验。  
4. **复合动作工作流**：将下拉选择、表单填写、搜索等多步交互封装为一个高层动作，内部用子 LLM 调用和 Playwright 操作自动处理局部状态变化，Agent 决策只在页面跳转等语义转变处进行，大幅减少步数和 token。

**实验与结果**  
使用 GLM-4-32B 作为主控模型，Qwen2.5-VL-7B 作为视觉模型，无任何微调。在 WebArena 达 56.3%（超过之前最强开源微调方案 48.4%），VisualWebArena 48.7%，Online-Mind2Web 51.0%，WorkArena 70.9%，均为开源模型新 SOTA，成本远低于闭源 GPT-5 等方案。消融显示：移除观察流水线性能暴跌 17.6 点，复合动作移除降 9.7 点，记忆移除降 7.6 点。将 GLM-4-32B 放入基础 GenericAgent 仅得 19.4%，而 WebChallenger 框架带来 +39.4 点的提升。

**核心启示**  
“当前 LLM 已具备足够的网页理解能力，缺的是正确的观察、记忆和行动框架，架构设计可以弥补模型规模的差距。”
