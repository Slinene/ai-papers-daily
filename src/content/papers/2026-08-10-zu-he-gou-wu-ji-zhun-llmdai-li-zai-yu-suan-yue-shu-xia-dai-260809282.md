---
title: 'ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping
  with Coupons'
title_zh: 组合购物基准：LLM代理在预算约束下带优惠券的篮子购物评估
authors:
- Adrian Li
- Kelong Mao
- Yudong Guo
- Heming Xia
- Xinwei Yang
- Lirui Luo
- Jace Wong
- Pu Yao
- Sulong Xu
- Simiu Gu
affiliations:
- JD.com
arxiv_id: '2608.09282'
url: https://arxiv.org/abs/2608.09282
pdf_url: https://arxiv.org/pdf/2608.09282
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: LLM Agent 购物评估基准
tags:
- Combo Shopping
- LLM Agent
- Benchmark
- Budget Constraint
- Coupon Optimization
- Basket Construction
one_liner: 提出ComboShoppingBench基准，评估LLM代理在跨商品兼容性、预算和优惠券约束下的组合购物能力，最强代理仅61.2%成功率。
practical_value: '- 电商购物助手可借鉴“隐藏见证”构建法：先生成可行篮子再反向创建任务，确保有解但不限制推荐多样性。

  - 混合评估框架（语义判断+确定性验证）可用于实际购物Agent评测，分离语义满足与交易可行性。

  - 优惠券最优选择是瓶颈，提示实际系统需要专门的组合优化模块，而非仅靠LLM推理。

  - 复杂组合约束下，Agent容易丢失个别条件，可通过提示工程或工具增强多条件跟踪。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有购物 Agent 基准主要面向单商品检索，而真实场景常需构建多商品组合篮子（如装机、订餐），需同时满足商品兼容性、预算、优惠券等联合约束。评估挑战在于存在多个可行解，难以枚举参考答案，且仅凭语义评估无法检测订单不可行或优惠券误用。为此，提出 ComboShoppingBench，构建解耦的“组合购物” Agent 任务，并采用混合评估框架。

**方法关键点**：
- 任务生成采用“解优先”流水线：先由探索 Agent 在模拟电商/外卖环境中构建并验证一个可行篮子（隐藏见证），再围绕该见证合成优惠券包、预算区间、用户查询和语义评分标准。确保每个任务至少有一个解，但见证不透露给受测 Agent，Agent 可返回任何有效篮子。
- 评估维度四合一：语义满足度（LLM 裁判按任务专属 rubrics 评估意图匹配）、规则验证（确定性校验 SKU 有效性、优惠券合法性/最优性、最终支付不超预算）、响应质量（表达清晰度、解释合理性）、声称忠实度（响应中价格、折扣等数值是否与重新计算结果一致）。整体成功率取四者交集。
- 环境包含 430 万商品、34 万外卖 SKU、5171 店铺，提供向量检索和受限计算器工具。任务跨纯商品、外卖/即时零售、混合域，共 291 个任务。

**关键结果**：
- 评估 11 个 LLM（含 GPT-5.5、Claude-Opus-4.6 等）在 Think/No-think 配置下，表现最佳的 GPT-5.5 (Think) 整体成功率仅 61.2%，次优 GLM-5.2 (Think) 52.9%。
- 失败主因：组合约束积累导致个别条件遗漏（每增加一条语义标准，任务级失败率明显上升）；互斥优惠券选择是核心瓶颈，Think 配置虽提升全局规划但仍有 8% 选错互斥券。
- LLM 语义评估与人类专家一致性高达 97.0–97.6%，验证了自动评估的可靠性。

**重要结论**：即使是当前顶尖 Agent，在需同时满足商品兼容、预算和优惠券最优的组合购物任务中表现远未可靠，复合约束满足是关键挑战。
