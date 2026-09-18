---
title: In-Context Robot Learning with VLM Agents
title_zh: 基于VLM Agent的上下文机器人学习
authors:
- Dongzhou Cheng
- Taoran Yi
- Ye Fang
- Xingwu Zhang
- Fan Feng
- Yixuan Li
- Gengxiong Zhuang
- Rongze Wang
- Shuai Yang
- Wei Song
affiliations:
- Morphi Robot
- Shanghai Innovation Institute
- Huazhong University of Science and Technology
- Fudan University
- Hunan University
arxiv_id: '2609.19138'
url: https://arxiv.org/abs/2609.19138
pdf_url: https://arxiv.org/pdf/2609.19138
published: '2026-09-15'
collected: '2026-09-18'
category: Agent
direction: VLM Agent 机器人上下文学习
tags:
- VLM Agents
- In-Context Learning
- Robot Learning
- Embodied AI
- Context Compiler
- Constrained Controller
one_liner: GPT-Policy将VLM agent用于机器人上下文学习，通过context compiler与constrained controller把演示和反馈转为可执行动作，无需梯度更新
practical_value: '- 借鉴 context compiler：不要把所有用户行为或物料序列塞进 prompt，而是抽取任务相关 transition（如
  query→click→cart、曝光→点击→转化）压缩成示范对，降低 token 成本、减少噪声，提升 LLM agent 动作提案质量。

  - 在 LLM 生成推荐动作或查询改写后，增加一层 constrained controller/verifier：先做业务规则校验（类目、库存、价格、合规）再执行，并把执行结果回写上下文，形成闭环自纠错，适合电商
  Agent 可靠上线。

  - 弱监督示范可用：仅用无动作标签的人类行为序列（点击/加购/购买）作为 in-context 示例即可提升任务完成度；在标注数据不足时，可先大量使用无显式 label
  的序列构造上下文，再用少量对齐动作对（如 query-rewrite pair、next-item ID）提升高敏任务效果。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：有限机器人演示无法覆盖所有任务与场景，部署时需依靠上下文学习（ICL），但现有机器人策略难以实现；商用 VLM（如 GPT-6 Astra）的 agent 能力提供了新可能。

方法关键点：
- 提出 GPT-Policy 框架，由三部分组成：context compiler 保留任务相关视觉 transition；VLM 提出 robot-tool 动作；constrained controller 验证、执行每个动作并回报结果。
- 无需梯度更新或修改任务特定参数，从演示、示例和交互反馈中生成可执行且可验证的机器人行为。

关键结果数字：
- 真实机器人实验中，人类视频演示即使没有机器人动作标签也能提升任务完成度；对齐动作参考在接触敏感任务上进一步增益。
- 通过任务成功率、效率指标、多模型对比与 context 消融评估可靠性与局限；摘要未披露具体绝对值。
