---
title: New LoRA Skills Should Read but Never Write
title_zh: 新 LoRA 技能应只读不写
authors:
- Zeyan Li
- Panqi Yang
- Qirong Guo
- Shengda Zhuo
- SIyuan Qiu
- Hu Xu
- Chun Li
- Jianfeng Xu
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiaotong University
- The Hong Kong University of Science and Technology (Guangzhou)
- Jinan University
arxiv_id: '2609.31600'
url: https://arxiv.org/abs/2609.31600
pdf_url: https://arxiv.org/pdf/2609.31600
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: LoRA 技能组合与参数高效训练
tags:
- LoRA
- Adapter Composition
- PEFT
- Skill Composition
- Read-only Expansion
one_liner: 提出 READ 只读扩展机制，冻结旧 LoRA 输出子空间并折叠组合更新，实现多任务 LoRA 增量组合且无推理开销
practical_value: '- 线上同时挂多个 LoRA（query 改写、类目预测、广告文案生成等）时，避免直接 weight-space merge；用
  READ 式只读耦合追加新技能，旧技能输出子空间不被写入，能减少跨任务干扰，适合增量上线。

  - 将每个 LoRA 先重写为 balanced canonical form，保持 ΔW 精确不变但对齐因子坐标，可作为 adapter 入库/发布前的规范化步骤，利于后续组合与版本管理。

  - 组合更新可折叠进 base weights，无额外推理开销、无 routing 规则，适合推荐/搜索高 QPS 在线服务，不需要为多任务维护多个前向路径。

  - 业务方管理大量 task adapters 时，可借鉴每次仅训练耦合矩阵中一行来追加新技能，训练成本极低，避免对历史任务数据全量重训。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：独立训练的 LoRA 适配器合并时，权重空间直接相加会产生干扰；全量重训成本高；多 adapter 路由又放弃单一组合模型。

方法关键点：
- 指出组合方法隐含两个选择：LoRA 等价分解的坐标选择、新旧技能耦合方向。
- READ 将每个 adapter 重写为 balanced canonical form，保持 ΔW 精确不变，但消除因子坐标歧义。
- 耦合单向增长：新技能可读旧技能的输入子空间，但不能写入旧技能的输出子空间，从而保护旧技能计算语义。
- 每次追加仅训练耦合矩阵中新技能对应的一行；组合更新可折叠进 base weights，无推理成本、无 routing、无任务特定规则。

关键结果：
- 在四个 benchmark suites、两个 model families 上逐技能增量添加。
- READ 在多个 family 的 suite 平均上超过同 adapter 构建的最强 published baselines：SuperGLUE 提升超 20 点，domain suite 提升超 7 点。
- 几乎所有完整添加序列的最终组合模型都超过所有 direct baselines。
