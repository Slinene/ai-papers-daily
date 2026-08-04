---
title: 'Fetch-then-Explore: Decoupling Selection from Extraction over a Persistent
  Workspace for Search Agents'
title_zh: 先取后探：解耦搜索代理的选择与提取，基于持久工作区
authors:
- Qi Liu
- Yiqun Chen
- Zidan Chen
- Yan Gao
- Yi Wu
- Yao Hu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
affiliations:
- Renmin University of China
- Xiaohongshu Inc.
- National University of Singapore
arxiv_id: '2608.02097'
url: https://arxiv.org/abs/2608.02097
pdf_url: https://arxiv.org/pdf/2608.02097
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 文档访问接口设计
tags:
- Search Agent
- Document Interface
- Persistence
- Workspace
- Decoupling
- ReAct
one_liner: 将文档选择与证据提取解耦到文件系统工作区，搜索代理可反复回查已选页面，准确率大幅领先传统浏览接口
practical_value: '- **工具集分离思想可迁移至推荐 Agent 的知识检索**：在商品知识库问答或素材库检索中，可将“检索候选”与“提取证据”分成两个独立工具（如
  fetch 与 grep/read），避免一次性将整个商品描述塞入上下文，减少 token 消耗且允许事后反复查阅。

  - **文件系统工作区（Cache）模式可用于电商任务的多轮 Agent**：对于需要多次查阅商品详情、用户评价、活动规则的场景，可让 Agent 在对话开始时
  pull 一批候选页面到本地缓存，后续用 grep 按需检索具体字段，避免反复调用远程接口并保持状态稳定，适用于库存查询、竞品分析等长链任务。

  - **持久化与跨文档联合查询的设计可提升召回证据完整性**：在推荐或搜索聚合场景，可将多个候选商品的标题/属性/评价预先 fetch 到缓存，后续用正则表达式跨文件查询，避免漏掉关键信息（如同时搜索多个商品中是否包含某个成分），适合合规审核、特征比对。

  - **轻量缓存选择（仅返回 header）能显著降低上下文占用且不损失信息**：在实际推荐解释或商品比较 Agent 中，可借鉴只返回文件路径和长度的思想，让
  LLM 先“记住”有哪些可用素材而不将其全部内容压入 prompt，需要时再用 read 工具按行读取，平衡上下文窗口压力与信息完整度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
当前长周期搜索 Agent 普遍使用 **visit-and-read** 接口：打开网页时立即将内容（摘要或切块）注入消息历史，导致**页面选择与证据提取被绑定在一次操作中**，且一旦离开页面，已获取的内容就会丢失。另一种浏览接口虽然将两者解耦，但仅保持一个瞬态单页会话，无法跨文档累积证据。这导致 Agent 无法有效“回看”之前访问过的页面，错过需要多轮假设验证的关键事实。

## 方法关键点
- **解耦选择与提取**：设计 `fetch` 动作只记录页面到文件系统而不返回正文，只返回轻量 header；后续通过 `grep`（正则搜索）和 `read`（行窗口读取）按需提取证据。
- **持久工作区**：每个问题创建一个私有缓存目录 `C_q`，所有 fetch 的页面以纯文本文件保存，函数名由 URL 哈希确定，避免重复下载。工作区在整个轨迹中一直可用，允许跨文档联合检索。
- **工具集极简**：仅提供 `search、fetch、grep、read、list_fetched` 五种工具，其中 `grep` 默认搜索整个缓存（跨文件），能自动返回匹配行及上下文，`read` 允许按行偏移扩展阅读。
- **固定搜索与思考框架**：所有对比实验使用相同的 ReAct 循环、搜索后端（Serper API）、相同的 backbone 模型，仅改变文档访问工具集，确保性能差异可归因于接口设计。

## 关键结果
在 BrowseComp（深层事实查询）和 WideSearch（宽表填充）两个基准上，使用 Qwen3.5-35B/122B 和 DeepSeek-V4 三个 backbone，**Fetch-then-Explore 在 BrowseComp 准确率上全面领先**：
- 最强 backbone（DeepSeek-V4）上达到 70.5%，比最佳基线高 4.5pp，比 visit-and-read 类高出 6-7pp。
- 行为分析显示，**回查率（离开页面后再次提取）** 在 WideSearch 上达到 67-76%，是基线瞬态接口的 **8-12 倍**，而 BrowseComp 上回查率 12-20% 也明显高于基线（3-10%）。
- 消融实验证明，**跨文件 grep 是关键**：若将 grep 限制为一次只能搜索单个文件，准确率下降 5pp（BrowseComp）且搜索调用数反增 8 次，表明持久化必须搭配联合寻址才有效。

## 核心发现
搜索代理的真正瓶颈不是找页面，而是**如何反复利用已找到的页面**。持久工作区让证据积累成为可能，而跨文档的**联合查询能力**是释放这一潜力的关键。
