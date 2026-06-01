---
title: UserGPT Technical Report
authors: Yunyi Xuan, Hao Yi, Fengling Mao, Daye Cai, Leikun Liang, et al. (11 人)
affiliation: Alibaba Group
date: 2026-05
venue: arXiv (Tech Report)
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 把 user profiling 从 "判别 + 离散标签" 改为 LLM 生成 narrative summary。配套四模块用户行为仿真引擎（BDI 三层 Persona-Need-Intent + Markov 状态机 + 跨平台 Tool Graph + QA 校验）造合成轨迹，再用 Curriculum SFT + DF-GRPO 训 8B；HPR-Bench 上 Avg@10 0.7325 / AccEx 0.7528，行为序列压缩 97.9%。
paperUrl: https://arxiv.org/abs/2605.08766
codeUrl: null
tags:
- Persona Simulation
- DF-GRPO
- Profile Generation
- Curriculum SFT
- E-commerce
unverified: false
detail:
  contribution: |
    ① 提出 User Behavior Simulation Engine：四模块（Persona-Driven Agent / Environment & Interaction Agent / Simulation Engine with Persona Evolution / Quality Assurance）合力生成长期、跨平台、persona-evolving 的合成用户轨迹，解决真实长期行为数据稀缺；② Data-Centric Semantization：Entity Refinement（micro 级去噪）+ Behavioral Corpus Construction（macro 级结构化 + behavior compression）把异质 raw log 转成 LLM 可消化的语义化输入；③ Curriculum-Driven Post-Training：多阶段 SFT + 新 RL 算法 DF-GRPO（sample-level + group-level 双层过滤），训 8B Qwen3-Thinking 在 tag prediction / summary generation 双任务接近百倍参数量 SOTA；④ 构建 HPR-Bench，覆盖 atomic portrait tag infer 与 composite profile summarization，并配 grounding + quality + 人工 4 维评分体系。
  background: |
    传统 user profiling 走判别 + 人工特征工程，输出离散标签碎片化、跨长尾行为泛化差、profile 内部逻辑常不一致；直接换 LLM 又撞两堵墙——(1) 真实长期行为数据稀缺无法 supervise，(2) 即便 SOTA LLM，对 implicit / complex persona reasoning 仍力不从心。UserGPT 同时补上 "数据侧仿真" 与 "模型侧后训练" 两块。
  method: |
    **Data Simulation（§2.1）**：BDI-inspired Persona-Driven Agent 维护 Persona–Need–Intent 三层（90 维 AlignX 偏好 + 15 维 SocioVerse 标注 + LifeSim Desire Pool）；Environment & Interaction Agent 模拟时空（618 / 双 11 / 春节）+ Cross-Platform Tool Graph（电商/外卖/OTA/POI）；Simulation Engine 用 MDP 做行为状态转移（idle → browsing → searching → ordering）+ Persona Evolution（event-driven 大变化 + behavior-driven 月度微调）；Quality Assurance 含逻辑校验 + 噪声注入 + 人工抽检。**Data-Centric Semantization（§2.2-2.3）**：Entity Refinement 在 entity 级标准化/去噪；Behavioral Corpus Construction 做长序列结构化并引入 behavior compression 适配 context window。**Curriculum-Driven Post-Training（§3.3）**：多阶段 SFT（stage1 atomic tag → stage2 composite → stage3 summary）+ DF-GRPO：reward = Atomic Accuracy + Summary Quality（judge model 评 4 维：完整 / 一致 / 简洁 / 美感），two-tier filter——sample-level 丢截断/格式错样本，group-level 用 ε_low / ε_high 阈值丢平均 reward 太低或太高的组；8B base = Qwen3-8B-Thinking，max seq 40K，RL lr 1e-6 bs 128。
  experiments: |
    全部在自建 HPR-Bench 上：**Tag prediction (HPR-Benchtag)** UserGPT-SFT (8B) Avg@10 = 0.7325，几乎追平 Qwen3.6-Plus 0.7329；相对 backbone Qwen3-8B-Thinking 0.5035 提升 +45%。**Summary generation (HPR-Benchsum)** AccEx 0.7528（vs Qwen3-235B-A22B-Thinking-2507 0.7014，+50.47% 相对），COVEx 0.9747；人工评分 completeness 6.36 / consistency 9.90 / conciseness 6.59 / aesthetics 6.05。**Compression** 平均输入 15K token 序列压缩 up to 97.9%。**Ablation** 多阶段 Curriculum SFT 缺一阶段 Pass@1 跌 4%+；DF-GRPO 相比 vanilla GRPO 在 AccEx 上 +9.12%。
  pros: |
    ① 把 "用 LLM 模拟用户 → 用合成数据训 LLM" 形成完整闭环，与 user-simulation 主线契合且 simulator-as-trainer 这一深度链路罕见；② BDI 三层 cognition + Cross-Platform Tool Graph + Persona Evolution 是当下最系统的 e-commerce user simulator 设计模板；③ DF-GRPO 的 group-level 双阈值过滤是对 GRPO 稀疏 reward 下数据效率问题的直接补丁，可拆出来复用；④ 8B 反超百倍参数 SOTA，对工业部署极友好；⑤ HPR-Bench + grounding/quality/aesthetics 四维评分给社区可复用基础设施。
  cons: |
    ① 所有 SOTA 数字均来自自建 HPR-Bench（与训练数据同源仿真生成），缺少跨 benchmark 外部验证，存在 simulator-train / simulator-eval 同源风险；② Simulation 高度针对中国电商场景（618 / 双 11 / POI / 中国人口统计对齐），跨域跨地区迁移不明；③ 未公开代码与权重（technical report），社区难独立复现；④ 与 Persona-Sim-RL / UGST 的 persona-drift / goal-drift 优化方向无对照实验；⑤ "97.9% 压缩 + 性能不掉" 在 HPR-Bench 任务上成立，对长尾 fine-grained behavior 是否真无信息损失存疑。
  inspiration: |
    ① user simulator 不止 "训/评 agent 的外部环境"，可反过来作为 LLM persona 后训练的核心数据源——这种 simulator → synthetic trajectory → SFT+RL 闭环值得迁移到推荐/搜索的用户表征 LLM；② DF-GRPO 的 sample-level + group-level 双层过滤是 GRPO 在数据质量参差任务上的通用 patch，可直接套到任何 long-form generation RL；③ "把多月行为压成 narrative summary" 提供新的用户表征接口，下游推荐/搜索可以直接拿 summary 当 context，替代传统 user embedding；④ Persona–Need–Intent 三层 cognition + Persona Evolution 设计可迁移到任何长期 user-modeling 场景（健康 / 教育 / 内容消费），不限电商；⑤ HPR-Bench 的 atomic tag + composite summary 双任务模板可作为后续 persona reasoning 评测的通用脚手架。
  takeaway: |
    Alibaba 把 user simulator 从 "训/评 agent 的工具" 升级为 "训 user-LLM 自身的数据引擎"，配 Curriculum SFT + DF-GRPO 后训练，让 8B narrative-summary 模型超越百倍参数 SOTA——目前最完整的 e-commerce user simulator + persona LLM 闭环系统。
---
