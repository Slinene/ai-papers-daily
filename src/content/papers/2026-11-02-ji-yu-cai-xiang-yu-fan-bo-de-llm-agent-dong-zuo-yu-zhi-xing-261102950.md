---
title: Action Verification through Conjecture and Refutation for Language Model Agents
title_zh: 基于猜想与反驳的 LLM Agent 动作预执行验证
authors:
- Minhyeon Oh
- Chiyeong Heo
- Geonwoo Noh
- Hoyoung Kim
- Jangwon Son
- Jungseul Ok
affiliations:
- Pohang University of Science and Technology
- National AI Research Lab
arxiv_id: '2611.02950'
url: https://arxiv.org/abs/2611.02950
pdf_url: https://arxiv.org/pdf/2611.02950
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 动作预执行验证 · 猜想与反驳
tags:
- LLM Agent
- Action Verification
- Refutation
- Pre-execution Verification
- AppWorld
- Self-correction
one_liner: 提出 BLACKSWAN：对每个会改变环境的动作，先预测效果、再生成可测试的怀疑并验证，执行前主动寻找反驳证据
practical_value: '- 对电商/广告/搜索推荐中的高危不可逆操作（下单、发送营销 push、修改商品价格、删除广告计划）可引入“预期-怀疑-测试”三阶段
  guard：在执行前让模型先写清预期效果，再列出可证伪的具体担忧，最后用只读 API 查询验证；任一担忧被证实即拦截并重写动作。

  - 把验证逻辑从“找支持证据”改为“找反驳证据”，并将怀疑预先注册、固定后再去测试，能避免模型先看到证据再反向修正假设，可复用到工具调用安全校验与 Agent
  风控中；实现时让怀疑绑定到具体代码元素（变量、API 参数），否则容易产生无关担忧。

  - 只对 state-mutating API 启用该机制，read-only 操作直接放行，能平衡安全与 token 成本；论文中 BLACKSWAN 的代价约为
  1.5–9.4 倍 ReAct，弱模型收益更大，适合中小参数模型在关键路径上的兜底。

  - 零样本/少样本条件下依然有效，说明不需要大量 in-context 演示即可迁移；如果业务中已有手工规则或 pre-defined 检查，可以替换为 LLM
  生成反驳假设 + 环境验证的软校验，减少硬编码漏报。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
LLM Agent 越来越多地代表用户操作外部环境，但用户指令往往是高层目标，大量任务与环境相关的关键信息隐含未说。执行错误动作会改变环境，比错误文本更难逆转。已有动作验证大多采用“确认导向”：寻找支撑动作成立的条件。论文指出这类方法存在盲区：错误动作可能通过所有“它是否正确”的检查。例如要求“按昨晚晚餐参与者分摊账单”，Agent 可能确认了账单金额与邀请名单，却没看到有人发消息取消了出席。因此需要改变验证方向：主动寻找反驳证据，而不是积累支持证据。

## 方法关键点
BLACKSWAN 以 Popper 的猜想与反驳思想为基础，对每个 state-mutating 动作执行 expect–suspect–test 流程：
- **Expect**：在执行前，让模型预测该动作会完成什么任务相关效果，形成一个 action-local 的可挑战声明；该声明在收集新证据前生成，避免被测试数据塑造。
- **Suspect**：基于当前上下文、动作代码和预期，生成具体、可测试的怀疑，覆盖“对象错误、集合不全、值或操作错误、隐藏状态、任务措辞不一致”五类失败；每个怀疑需要绑定到动作中的具体代码元素（变量、API 参数），保证可证伪且与动作相关。
- **Test**：用已有轨迹观察或发起只读探测来验证怀疑；全部怀疑被驳回或搁置才执行动作，任一确认则拦截并基于反驳证据重写动作。怀疑在测试前固定，类似科学实验的预注册，防止证据反向影响假设。

## 实验结果
在 AppWorld 的 challenge split 上，BLACKSWAN 取得 84.7 TGC，较最强 baseline 提升 14.9 个百分点（开启 thinking）；关闭 thinking 时提升 25.2 个百分点，且 BLACKSWAN 关闭 thinking 仍超过所有开启 thinking 的 baseline 11.7 个百分点。零 in-context 演示时，BLACKSWAN 也超过所有给定 3 个演示的 baseline 9.3 个百分点。在 WebShop 上，仅修改 prompts 为领域中立即可提升 12.7 个百分点；在 ALFWorld 上也有小幅提升。消融显示，反驳式怀疑与预注册固定怀疑二者同时使用才最有效；成本为 ReAct 的 1.5–9.4 倍，弱模型上收益更明显。

## 最值得记住的一句话
对会改变环境的动作，不要问“它哪里是对的”，而要问“它可能哪里是错的”，并在执行前用只读证据尝试驳倒它。
