---
title: 'ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation
  of Verified Experience'
title_zh: ASCENT：通过验证经验自蒸馏实现在线测试时训练长程智能体
authors:
- Haodong Lu
- Dong Gong
affiliations:
- University of New South Wales (UNSW Sydney)
arxiv_id: '2610.05303'
url: https://arxiv.org/abs/2610.05303
pdf_url: https://arxiv.org/pdf/2610.05303
published: '2026-10-03'
collected: '2026-10-06'
category: Agent
direction: Agent 在线测试时训练 · 自我蒸馏验证经验
tags:
- Test-Time Training
- Self-Distillation
- LLM Agents
- Online Learning
- LoRA
- Long-Horizon
one_liner: 用冻结初始模型将验证成功的轨迹蒸馏为 LoRA 软目标，使长程 Agent 在单次任务流中稳定在线进化
practical_value: '- 在线学习方案：在对话式导购/客服/智能投放等长程 Agent 场景，可以用冻结 base 模型 + LoRA 快权重持续训练。每次成功会话（成交/点击等强验证）做一次自蒸馏，失败跳过更新，无需
  replay buffer，工程成本低。

  - 特权信息构造：将成功会话的动作有效部分（排除 parse 失败或环境未执行的动作）与推理文本保留，去掉 observation（按模型规模调整），作为 teacher
  的 hindsight 上下文。教师看到完整成功轨迹后产生全词表 soft target，学生只在当前 prefix 学习，可减少冗余 detour 动作、提升
  turns 效率。

  - 蒸馏目标选择：用 forward KL 匹配全词表分布，而不是最大化生成 token 概率或 REINFORCE 梯度；这能抑制策略对自身输出的过拟合，避免熵崩溃和无效动作增加，尤其适合单条轨迹在线流。

  - 与 in-context memory 互补：小模型可能被检索记忆干扰，可单独用权重更新；大模型可以叠加 retrieved memory 与 ASCENT
  权重，形成 co-evolution。动作有效性过滤可免费从环境响应中解析得到，可作为轨迹清洗信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：部署的 LLM Agent 长时间在线运行，每个任务只有一次交互和终止时的稀疏验证，但现有在线适应多用 in-context 记忆（依赖检索与冻结策略），单 episode TTT 重置参数，RL/自训练通常需要多次采样或离线阶段。直接模仿或强化自己生成的单条轨迹会导致策略崩溃：第一响应熵下降、有效动作率降低、成功率跌破 base。

方法关键点：
- OaTTT 协议：任务流单遍、每任务一次尝试、稀疏 episode 验证；更新持久 LoRA 快权重。
- ASCENT 自蒸馏：验证成功的轨迹作为特权信息传给冻结初始模型（teacher），teacher 在每个学生 prompt prefix 上输出全词表 next-token 分布；用 forward KL 将这些分布蒸馏到 LoRA 权重，失败则跳过更新。
- 动作有效性过滤：从 teacher 特权 context 中移除环境未执行的无效动作 turn，但学生仍在这些位置训练；默认只用 reasoning+action，不加 observation。
- 与 hard token 模仿/REINFORCE 对比：梯度为 p_φ−q 而非 p_φ−e_y，避免只抬高自己生成 token、覆盖 teacher 偏好 token。

关键结果：
- ALFWorld seen：Qwen3.5-4B 成功率 46.4→69.5（+23.1 点），9B 55.0→77.4（+22.4 点）；平均 turns 35.1→26.3、32.6→21.0。
- WebShop：4B strict SR 17.8→41.9、mean score 25.9→62.4；9B 17.2→41.5、27.8→56.8；turns 均大幅下降。
- 未见场景迁移：4B/9B 分别 78.6%/90.0%，Base 43.3%/49.3%；持续在线更新仍有效。
- 消融：reasoning 是关键，action-only 几乎无效；4B 倾向较短过滤 context，9B 可含 observation；forward KL 总体最稳。

最值得记住：用冻结初始模型作为 teacher，把验证成功轨迹的后续信息变为全词表软目标，再以 forward KL 蒸馏到 LoRA，是在单条轨迹、稀疏验证下稳定在线进化的核心 trick。
