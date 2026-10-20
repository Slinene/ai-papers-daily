---
title: 'Interlock: From Local Correctness to Task Completion in Long-Horizon Agents'
title_zh: Interlock：从局部正确到长程智能体任务完成
authors:
- Linji Hao
- Yanji He
- Zihan Wang
- Hansi Yang
- Jiayuan Zhang
- Hongyan Hao
- Qi Gu
- Yan Feng
- Han Wu
affiliations:
- Peking University
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
- Meituan
arxiv_id: '2610.19686'
url: https://arxiv.org/abs/2610.19686
pdf_url: https://arxiv.org/pdf/2610.19686
published: '2026-10-13'
collected: '2026-10-20'
category: Agent
direction: 长程 Agent 任务合成与完成过滤训练
tags:
- long-horizon agents
- task synthesis
- completion graph
- rejection sampling fine-tuning
- agent-as-judge
- executable verification
one_liner: 用 typed completion graph 约束长程任务合成，并以完成过滤的 RFT 提升 Agent 在外部基准上的完成率
practical_value: '- 用 completion graph 管理 Agent 工作流：在电商运营、广告投放、订单履约等长链路任务中，把“证据→决策→下游产物更新”显式建模为
  grounding / coupling / realization 关系，可以防止模型只做对局部决策但漏掉预算、排期、报表等连带更新。

  - 合成训练任务时做双重 review：source-coverage 保证原始义务不丢失，public-input critic 保证评估标准可由可见材料支撑。迁移到业务里，可用来生成大量带私有
  rubric 的 agent 训练任务，同时避免“只有标注者知道的信息”进入评估。

  - Agent-as-judge 比纯文本 LLM-as-judge 更有效：让裁判代理能读文件、写并执行验证脚本，只增加约 11% 的 judge token，就能显著提升过滤出的轨迹的训练价值。适合用来筛选线上
  agent 执行记录做 SFT。

  - 在固定轨迹预算下，扩大任务 domain 覆盖比重复采同一批任务更划算；对推荐/广告 Agent 也是提示：构造跨场景、跨品类的完成型任务，有助于学到可迁移的“把决策落地到所有受影响产物”的能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长程 Agent 常出现一种失败：单个决策或中间产物看起来正确，但最终任务并未完成。例如订票成功后漏改日程和预算，或修改分配后未同步更新排期、账目。其原因不是模型不会执行单步操作，而是没有保持证据、决策和所有必备下游效果之间的条件依赖关系。随着任务变长，这种“局部正确但不完整”的问题更加突出。

**方法关键点**  
- 将任务表示为 **typed completion graph**，包含三类边：grounding 连接公共证据/规则与决策；coupling 以超边约束多个组件必须共同满足某种条件；realization 连接决策与其必须落地的所有下游产物、状态或记录。  
- 每个效果带四个字段：证据来源、适用对象范围、适用条件和最终必须成立的条件，从而把“条件义务”结构化。  
- 生成流程用同一张 graph 编译出初始 workspace、公开 request 和私有 rubric；再做两轮互补 review：source-coverage 检查原始需求是否完整保留，public-input 检查 rubric 是否可由 solver 可见材料支撑。  
- 执行后用 **agent-as-judge** 检查最终文件、写并运行验证脚本，只有所有必需 criteria 通过的轨迹才被接受；每个 backbone 用自己的 accepted rollouts 做 rejection-sampling fine-tuning。  

**关键实验**  
用 Qwen3.6-27B 和 Qwen3.6-35B-A3B 各自在 3,278 个合成任务上采样，每个模型保留 8,957 条接受轨迹、约 154M token 做 SFT。在 AutomationBench、JobBench Main/Easy 和 Harvey LAB 上，两个模型均超过原始 checkpoint 和 ClawGym-SFT：AutomationBench 分别 +4.00 / +4.50 个百分点，JobBench Main +4.35 / +3.20，JobBench Easy +6.64 / +4.31，Harvey LAB +3.89 / +4.16。与纯文本 judge 相比，agent-as-judge 在相同训练预算下把 Qwen3.6-27B 的 AutomationBench 从 13.17 拉到 18.33。合成轨迹的执行长度也显著高于 ClawGym，平均 84,293 token、27.63 assistant turns、42.10 tool calls。

**最值得记住的一句话**  
任务完成不是单个决策正确，而是所有由证据触发的下游效果都被满足；用 typed completion graph 把这种条件义务固化下来，是训练可迁移长程 Agent 的关键。
