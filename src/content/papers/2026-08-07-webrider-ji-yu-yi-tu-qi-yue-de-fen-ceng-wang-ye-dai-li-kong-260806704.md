---
title: 'WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance'
title_zh: WebRider：基于意图契约的分层网页代理控制
authors:
- Zhi Li
- Tao Zhou
- Yeqing Li
- Eugene Ie
- Demetri Terzopoulos
affiliations:
- University of California, Los Angeles
- Google
arxiv_id: '2608.06704'
url: https://arxiv.org/abs/2608.06704
pdf_url: https://arxiv.org/pdf/2608.06704
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent分层控制与意图契约驱动的网页任务执行
tags:
- Web Agents
- Hierarchical Control
- Intent Contracts
- Persona Policy
- Trajectory Auditing
- Live-Web Evaluation
one_liner: 分层架构与意图契约让网页代理的路径可审计，揭示高任务完成率背后仅38.8%的合约忠实度。
practical_value: '- 将用户委托中的硬约束、证据义务显式化为意图契约，可审计每一步是否忠实执行策略，避免最终推荐看似正确但中间偏离。

  - 分层控制器分离“证据充分性和停止决策”与“页面级动作选择”，高层管理状态，低层生成可执行动作，增强可控性并便于训练替换动作策略。

  - 引入 guard 机制确保动作语法正确并拦截无效操作，可在电商代理中防止错误点击或状态循环，提高鲁棒性。

  - 利用合约状态和 guard 过滤后的轨迹训练中间层动作策略，使动作实现可学习，对业务落地中的策略迭代具有参考价值。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**
当前网页代理仅以最终任务成功（如找到商品）评估，忽略用户委托中隐含的策略约束（如必须检查退货政策、验证卖家信誉）。强基线代理完成率可达99.2%，但遵守所有策略约束的合约门控成功（CGS）仅38.8%，大量轨迹虽然到达终点但已违背原始约束。因此，需要一种机制使「路径」可审计，确保代理在执行过程中保持委托忠诚度。

**方法关键点**
- **意图契约**：将用户委托形式化为稳定记录，包含目标、硬约束、软偏好、证据义务、阻塞条件和答案格式，保证条件在执行前已知、执行后可审计。
- **分层架构**：顶层控制器维护合约状态，决定继续浏览、提问、回答或停止；中间层将当前意图结合页面状态和Persona策略，生成**单个受 guard 保护的可执行 JSON Action AST**，禁止自行判断证据充分性或终止；底层执行器操作浏览器、搜索或地图。
- **Persona策略**：定义为任务局部的控制规则（如信任优先验证、不确定性回避问询），可在同一请求和硬约束下通过对策论实验改变搜索广度、验证深度、排序或停止行为。
- **RiderBench基准**：包含768个基础任务、15种Persona策略、4096个合约，跨42个真实站点；评估包括合约门控成功（CGS）和人类评估的步骤级一致性及委托舒适度。

**关键结果**
- 强控制器 Full-Pro（Gemini 3.1 Pro）终止率达99.2%，但CGS仅38.8%，证据门和答案门是主要瓶颈。
- 具有持久意图和单 guard 动作的 IntentCore 结构相较纯文本提示提升CGS +5.6pp（46.8% vs 41.2%），证据满意度从60.5%提升至72.1%。
- 人类评估中，IntentCore 的Persona一致性得分86% vs 基线70%，净舒适偏好优势+42.5%。
- 训练的中间层动作策略 MidSFT-8B（Qwen3-VL-8B）在固定顶层下取得CGS 50.8%（干净条件下52.0%），远超可执行基线约32.9%，且证据满足率达78.1%。

**结论一句话**
高完成率可与低合约忠实度并存，使路径本身成为任务的一部分，意图契约让路径可审计、可学习、可被人类评判。
