---
title: 'A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned
  On-Policy Self-Distillation for Reasoning'
title_zh: 只能打分的特权教师无法搜索：面向推理的批判条件化在线自蒸馏
authors:
- Mayug Maniparambil
- Ayush Rai
- Ekansh Verma
- Noel E. O'Connor
- Fergal Reid
affiliations:
- Fin.ai
- Dublin City University
arxiv_id: '2610.13744'
url: https://arxiv.org/abs/2610.13744
pdf_url: https://arxiv.org/pdf/2610.13744
published: '2026-10-09'
collected: '2026-10-13'
category: Reasoning
direction: Critique-conditioned self-distillation 用于推理错误定位
tags:
- self-distillation
- critique
- RLVR
- error localization
- reasoning
- token-level credit
one_liner: 证明参考解条件化的在线自蒸馏信号无法定位错误，提出先批判后条件化打分，使 token 级监督具有纠正性
practical_value: '- 在稀疏奖励场景（如 RLVR 只有最终结果正确/错误）中，若一组 rollout 全部失败，group advantage
  为零，可以借鉴 critique-conditioned 思路：先让模型对失败轨迹生成错误定位与解释，再以此作为额外上下文让 teacher 打分，获得 token
  级纠正信号，解决冷启动和长尾问题。

  - 验证了"定位错误是搜索问题，生成才能搜索"：在 Agent 多步决策、多轮对话等复杂任务中，单纯用参考解或最终状态做 reward model 可能无法提供有效信用分配，可以考虑增加一个
  critic 生成 critique，将生成结果作为 reward model 的额外输入，提升对错误步骤的敏感性。

  - 训练成本可控：用学生自己生成 critique（self-critique）仅增加 6% step time，但效果接近 oracle critic（OOD
  accuracy 0.593 vs 0.606），说明在计算预算有限时可以采用 self-critique 方案，且 quote 和 reason 的解耦（quote
  负责定位，reason 负责纠正）值得在 prompt 设计或模块拆分中参考。

  - Test-time 修复：将 critique 作为上下文插入 rollout 的截断处，可让模型回溯并纠正错误，在解决不了的问题上提升采样成功率（4.3%→9.3%），该思路可用于推荐对话系统或
  Agent 执行失败后的自动修复。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
On-policy self-distillation (OPSD) 试图用带特权信息的 teacher 对 student rollout 打分，替代 RLVR 的稀疏结果信号，提供 dense token 级信用。但密度不代表信用分配正确：作者发现参考解条件化的 teacher 信号在标注错误处既不集中（localization），也不降低错误 token 概率（correction），甚至不能区分同一问题的正确/错误 rollout。原因是定位错误本身是一个搜索问题，而打分 teacher 没有被要求进行搜索。

**方法关键点**  
- 定义两个信号：localization (KL_t(b)) 和 correction (Δ_t(b))，并用 error-span Z 相对 clean 区域标准化。  
- 提出 critique-conditioned self-distillation：先让 critic 对 rollout 生成 critique，包含错误句子的 verbatim quote 和 reason，再用该 critique 替代 reference 作为 teacher 的上下文进行打分。生成完成搜索，打分将找到的错误转化为 dense signal。  
- 训练时，将 critique 定位的错误句子及其后 50 tokens 的 corrective log-ratio 作为额外 advantage 项，与 GRPO 或 RLCSD 结合。

**关键实验**  
- 数据集：Knights & Knaves 逻辑题（4–8 人）、DeepMath L5-7/L7-10、ProcessBench。  
- 模型：Qwen3-1.7B、Olmo-3-7B-Think、Olmo-3-32B-Think 作为 student/teacher；critic 使用 gpt-5.2 (oracle)、Qwen3-8B、学生自己。  
- Error-span Z：reference-conditioned 在所有任务上不满足 localization 正、correction 负，而 oracle critique 全部满足，self-critique 也有较弱但一致的效果。  
- 训练结果：320 题 K&K 训练集上，RLCSD+critique (oracle) OOD accuracy 从 GRPO 0.509 提升到 0.606；self-critique 0.593；GRPO+critique 0.564。冷启动 4 题中，critique 解决 2 题，GRPO 仅解决 1 题。  
- Test-time：将 critique 插入截断处，模型采样解决不可解问题的比例从 4.3% 提升到 9.3%。

**最值得记住的一句话**  
定位错误本身是搜索问题；生成 critique 执行搜索，打分将其转化为密集 token 级信用。
