---
title: Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation
  on Live IOS Apps
title_zh: 在线稠密强化学习训练规划-接地智能体用于真实 iOS 应用 UI 导航
authors:
- Peitong Duan
- Khashayar Gatmiry
- Jeffrey Nichols
- Samy Bengio
- Emmanuel Abbe
affiliations:
- Apple
arxiv_id: '2610.39264'
url: https://arxiv.org/abs/2610.39264
pdf_url: https://arxiv.org/pdf/2610.39264
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: UI Agent 在线强化学习训练
tags:
- Online RL
- PPO
- LLM-as-a-Judge
- GUI Agent
- GiGPPO
- iOS
one_liner: 用在线 RL 训练解耦的规划与接地 UI Agent，结合稠密/终局奖励与 GiGPPO，使 8B 模型在真实 iOS 任务上接近或超越 Gemini
practical_value: '- 规划与 grounding 解耦：对话/导购 Agent 可把“策略决策”（是否推荐、是否反问、何时切换商品）与“执行层”（调用
  API、生成卡片、点击元素）拆开；RL 只训练前者，后者用 SFT/规则冻结，训练成本大幅下降，线上也便于独立迭代。

  - 稠密过程奖励 + 不对称折扣：用 LLM-as-a-Judge 对每一步的“业务进展”打分，但 dense 奖励要打折（如 γ=0.5），最终转化/成交奖励不打折。这能防止刷步骤分、拖时长，同时给稀疏转化提供中间信号。

  - ASK USER 动作与模拟用户：在导购/搜索推荐 Agent 里显式加入“反问用户”原语，训练阶段用轻量 LLM 模拟用户偏好和回答，能提升交互式偏好澄清与个性化能力。

  - critic warm-up 与高 critic lr：在 RL 训练推荐或对话策略时，先冻结策略训练 critic 15 步，再把 critic 学习率设为策略
  100 倍，可避免初期优势噪声导致策略崩坏；critic 最终丢弃，不必精调。

  - GiGPPO 思路可迁移到多并发 rollout 的搜索/推荐 Agent 训练：用状态相似度（如图像 hash 或 embedding）跨轨迹共享价值信号，尤其适合状态空间大、精确重复少的
  GUI/会话场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
前沿 VLM 做 UI 导航能力强但推理成本高；SFT 或离线 RL 的小模型容易记住静态轨迹，不会纠错，泛化差。在线 RL 能提供真实环境反馈，但单纯终局奖励稀疏，步级奖励又容易被策略拖时长利用。

**方法关键点**  
- 架构解耦：Planning Agent 基于 Qwen3-VL-8B，输出 CoT 推理、当前步骤和剩余计划；Grounding Model 为 3B 模型，只做动作与坐标映射，冻结不动，RL 只训练 planner。  
- 动作空间包含 ASK USER，允许请求偏好澄清；训练中用 Gemini-3.5-Flash 模拟用户回复。  
- 奖励：LLM-as-a-Judge 双通道。Dense 每步由 Gemini-3.5-Flash 判 success/fail/overcomplete，惩罚幻觉、重复无效动作、任务完成后继续操作；Terminal 由 Gemini-3.1-Pro 判 success/fail/blocked complete，对支付墙/CAPTCHA 等外部障碍给予部分奖励。  
- 优化：PPO + GAE。关键是非对称折扣：dense 用 γ=0.5 使价值目标局部可估，terminal 不打折，防止只攒步级分而拖延任务。  
- GiGPPO：用 64-bit perceptual hash 找同一任务并发轨迹中视觉最近状态，将邻接状态 embedding、其回报和 Hamming 距离喂给一个小 MLP 预测价值，避免 GRPO 组平均丢失时间结构，也避免 GiGPO 精确状态重复在 GUI 中基本不存在的问题。  
- critic 策略分离：先冻结策略训 critic 15 步；critic lr 1e-4，比 policy 1e-6 高两个量级。  
- 基础设施：512 并发虚拟 iOS 设备，VM 快照回滚约 10 秒。

**关键结果数字**  
- UINavBench：PPO Step 336 成功 32.4%，打平 Gemini-3.1-Pro，超过 Gemini-3.5-Flash(28.4%) 和 Qwen3.8-27B(19.6%)；SFT 仅 16.7%。  
- AndroidWorld：PPO Step 336 为 32.8% vs SFT 4.7%，近 7 倍，显示 OOD 泛化。  
- iOSWorld：GiGPPO Step 336 为 9.8% vs SFT 4.5%，超过 2 倍；合成 app 分布偏移导致整体偏低。  
- 稠密奖励加速：PPO Step 168 与 terminal-only Step 336 相当或更优；GiGPPO 在真实 iOS benchmark 上可提前达到同水平。

**最值得记住**  
把可复用的 grounding 冻结交给 SFT，只对需要开环推理和纠错的 planner 做在线 RL，用 LLM judge 提供局部稠密信号加不打折终局奖励，是 8B 小模型在真实 APP 上逼近大模型的关键。
