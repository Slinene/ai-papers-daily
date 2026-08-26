---
title: RecGPT-Mobile-V2 Technical Report
title_zh: RecGPT-Mobile-V2 技术报告：端侧个性化 Query 预测的质效联合优化
authors:
- Lingqing Zhang
- Bin Zhang
- Weipeng Huang
- Chengfei Lv
- Chengyu Lai
- Chuxin Chen
- Dimin Wang
- Han Zhu
- Hongtao Cheng
- Jialin Zhu
affiliations:
- Alibaba
arxiv_id: '2608.24295'
url: https://arxiv.org/abs/2608.24295
pdf_url: https://arxiv.org/pdf/2608.24295
published: '2026-08-25'
collected: '2026-08-26'
category: QueryRec
direction: 个性化 Query 预测 · 端侧 LLM 自适应推理
tags:
- Query prediction
- On-device LLM
- Adaptive reasoning
- GRPO
- Semantic ID
- Model compression
one_liner: 面向端侧个性化 Query 预测，提出质量门控自适应推理与压缩部署的端到端框架。
practical_value: '- 行为轨迹压缩可先做确定性工程再上模型：按“搜索/购买>加购/收藏>点击/内容种子>曝光/页面噪声”分层，去爆、去重、语义富化、分段序列化，将
  ~300 原始事件压到 100-300 token 的 LLM 可读上下文；电商推荐/搜索场景下，这是低成本、可审计的输入治理方式。

  - 训练顺序建议 PT→SFT→RL：先用 domain CPT 注入层级 Semantic ID、共现/互补/替代关系和购后转移，再通过 SFT 固定输出契约（单
  Query、独立 rationale 区域、禁止解释和候选列表），最后才做 RL；业务迁移时先确保基座懂领域和输出格式合法。

  - RL 奖励设计不要用全局长度惩罚，而是质量门控：分组 rollout 中仅对质量合格且长度可比的轨迹计算输入分位数预算，采用 one-sided 超额成本
  + 乘法折扣 Q*exp(-λC)，并保留 rank protection；这能避免模型刷短 query 或牺牲 grounding。

  - 端侧部署可分离 teacher 显式 CoT 与 student 隐式 latent 推理：teacher 保留完整 rationale 用于监督/审计，student
  只输出最终 Query；结合 INT8/INT4 量化、结构化剪枝、蒸馏和端云路由，适合移动端低延迟场景。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商平台从点击、收藏、购买等隐式信号推断用户下一步检索意图，个性化 Query 预测在端侧部署有隐私和响应优势。但行为轨迹噪声大、多尺度，且同一轨迹可对应多个合法 Query；长 CoT 模型在简单样本上浪费计算，强压短输出又会丢失复杂跨类目推理所需的证据组合。问题本质是：在质量约束下分配最小充分推理，而非统一缩短。

**方法关键点**
- **行为轨迹压缩**：五层确定性 pipeline（信号过滤→动作感知去重→语义富化→意图分层→分段序列化），将典型用户 ~300 原始事件压缩到 ~25 意图事件、100-300 token；高活跃 p99 从 2,858 事件降到 200-400 token，强意图信号（搜索/购买/加购/收藏）最后被截断。
- **推荐 native 底座**：基于 Qwen3.5-0.8B 混合 backbone（3×Gated DeltaNet + 1×Gated Attention 每组，共 24 层），选择性热启动早期和中期组；domain CPT 学习层级 Semantic ID、行为转移和购后关系，SFT 固定输出契约并引入证据优先短 rationale。
- **质量门控自适应 RL**：分组 rollout，仅对质量合格且长度可比的轨迹做长度优化；输入特定分位数预算，one-sided 超额成本，乘法奖励 Q·exp(−λC)，rank protection 防止短劣 query 抢占优势；λ 随超额成本动态调整。
- **部署**：教师显式 CoT 蒸馏到隐式 latent 状态学生，结合 INT8/INT4 量化、结构化剪枝和端云路由。

**关键结果**
- CoT 信息消融：证据聚焦短 rationale 将 ROUGE-L 从 0.228 提升到 0.315，Jaccard 从 0.174 提升到 0.248，略优于五阶段全 rationale。
- 受控 RL 对比：完整奖励将 Query 质量从 quality-only RL 的 73.2% 提升到 78.6%，硬失败率从 3.6% 降至 1.6%，中位 CoT 长度从 62 token 降至 14 token。
- 在线检索分析表明 Query 召回通道与既有召回通道互补。

**最值得记住的一句话**：效率不等于统一短推理，而是为每个请求分配最小充分计算；质量先于效率，brvity 只有在质量得到保障后才有价值。
