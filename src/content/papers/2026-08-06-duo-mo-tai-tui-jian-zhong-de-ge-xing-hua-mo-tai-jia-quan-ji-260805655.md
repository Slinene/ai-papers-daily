---
title: Is Personalized Modality Weighting Actually Personalized? A Controlled Audit
  of Per-User Weighting Claims in Multimodal Recommenders
title_zh: 多模态推荐中的个性化模态加权审计：每用户权重真的个性化吗？
authors:
- Jingyuan Zheng
- Xin Zhang
- Yang Gu
- Dongjing Wang
- Yuxiang Wang
- Xudong Shen
- Haiping Zhang
- Youhuizi Li
- Dongjin Yu
affiliations:
- Hangzhou Dianzi University
- Hangzhou Normal University
- NetEase Inc.
arxiv_id: '2608.05655'
url: https://arxiv.org/abs/2608.05655
pdf_url: https://arxiv.org/pdf/2608.05655
published: '2026-08-06'
collected: '2026-08-07'
category: RecSys
direction: 个性化声明审计 · 多模态推荐
tags:
- personalization audit
- multimodal recommendation
- modality weighting
- per-user weighting
- evaluation methodology
- recommender systems
one_liner: 通过两个受控对比审计六种每用户加权方法，发现全局模态权重已捕获全部增益，个性化加权无一致效用，且普通置换测试会给出虚假个人化信号
practical_value: '- **引入每用户模态权重前务必用全局权重作为基线**：在电商/视频推荐中，若想对不同用户动态调整模态（如图文/视频/标签）的信任度，优先尝试一个所有用户共享的
  global weight 并评估 PairAcc/NDCG/Recall。本文表明全局权重几乎吃掉所有内容增益，每用户加权不带来稳定提升。

  - **评价个性化效果时同时报告 real‑GM 和 real‑shuf**：仅用置换测试（shuffle control）会高估个性化程度，因为读取共享协同
  embedding 的门能够通过模型容量产生“看起来个性化”的假象。必须对比最强非个性化基线（global weight）上的 utility gap，才能确认额外收益。

  - **解耦门控输入，避免容量膨胀**：若必须使用 attention 或 hypernetwork 生成 user‑specific 权重，将其输入从协同 embedding
  改为独立 embedding（本文的 decoupled 变体），可消除虚假 identifiability gap，只保留真正的个性化信号。

  - **通过信号植入校准审计工具**：在启动一项复杂的个性化机制前，先向数据植入已知的用户模态偏好，检查模型能否单调恢复该信号。若自然数据上的效果远低于植入信号，可判断真实用户偏好信号不足。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态推荐中，许多系统声称用户对视觉、文本、声音等模态的偏好各不相同，因此引入每用户模态强度向量、注意力门或超网络来生成个性化权重。已有评估多通过与无模态基线对比来报告增益，并未隔离真正的用户特定信号与单一全局模态权重加模型容量的贡献。这一问题可能导致大量“伪个性化”设计被采纳。

**方法关键点**
- 在同一个矩阵分解协同过滤骨架上实现六种每用户加权头：自由查表（PUM）、双线性注意力门（ATT）、元权重超网络（MWN）、低秩引导权重（LRG）以及注意力门与超网络的解耦变体（ATTd、MWNd）。解耦变体将门输入从共享用户 embedding 换为独立 embedding。
- 设计两个配对对比：
  - **效用差（real‑GM）**：每用户头与全局权重（GM）的排名准确度差值。
  - **可识别性差（real‑shuf）**：冻结训练好的头，在评估时将用户-权重绑定打乱（同一活跃度分箱内置换），测量性能下降。
- 通过植入不同强度的合成用户模态偏好来校准工具灵敏度，要求性能随植入强度单调上升。

**关键结果**
- 在三个短视频语料（Tsinghua ShortVideo、KuaiRand‑27K、MicroLens‑100K）上，单个全局权重相比无模态基线带来+1.9～+3.6pp 的 PairAcc 增益，已几乎捕获全部内容收益。
- 没有任何一个每用户加权头在所有语料和所有指标上一致优于全局权重；少量正间隙≤0.9pp 且随数据集翻转。
- 可识别性与效用严重背离：KuaiRand‑27K 上的 ATT 头 real‑shuf 达到 +4.64pp（内容增益的 128%），但 real‑GM 为 −0.69pp。解耦门输入后该膨胀的 identifiability gap 降至 +0.02pp（0.6%），证明虚假信号来自门读取共享协同 embedding 引入的额外容量。
- 信号植入校准中，捕获 AUROC 随植入强度单调上升（如 0.25→1.00），证实审计工具能够检测真实用户特定结构，而自然数据中不存在该信号。
- 上述结论在电子商务语料 Amazon‑Baby 和 LightGCN 骨架上均被复制。

**核心洞见**：每用户模态权重在无额外监督（如缺失模态实验或会话级交互）时，其增益可被全局权重包含，置换测试的“个性化”假象源于模型容量而非真实模态偏好。
