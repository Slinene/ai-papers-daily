---
title: Are Causal Neuron Circuits Unique and Transferable?
title_zh: 因果神经元回路是否唯一且可迁移？
authors:
- Ömer Tekin Yavuz
affiliations:
- İletişim Yazılım
arxiv_id: '2611.13885'
url: https://arxiv.org/abs/2611.13885
pdf_url: https://arxiv.org/pdf/2611.13885
published: '2026-11-09'
collected: '2026-11-12'
category: LLM
direction: LLM 可解释性 · 神经元因果回路
tags:
- mechanistic interpretability
- activation patching
- causal intervention
- neuron redundancy
- LLM
one_liner: 系统检验 LLM 神经元组因果干预：关键少数即可改变输出，组内高度冗余，效应可迁移到改写但跨链弱。
practical_value: '- 业务模型可解释性/调试时，不要满足于“删掉一组特征/神经元后输出变了”：进一步做子集消融，定位最小必要子集和冗余神经元；例如对电商推荐模型的关键隐层单元做
  4096 子集搜索，识别哪些神经元真正承载 task 信号。

  - 用 activation patching 定位 LLM 生成推荐理由/搜索词时的错误来源：将目标 token 的激活替换为干净样本的激活，观察输出是否跳转到桥接实体或另一类别，从而判断错误在哪个
  MLP 层，便于做数据修复或 targeted fine-tune。

  - 注意“激活几乎不变”的神经元：它们在消融中可能表现重要，但可能只是常量/偏置门控，不携带样本特定内容；做模型剪枝、蒸馏或神经元级归因时，要结合跨样本激活方差区分语义神经元与偏置神经元。

  - 学术贡献为主，这些结论主要对内部机制分析有用；业务上可复用成本较高，建议仅在线上重大 badcase 归因时应用。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：可解释性演示常以“干预某组神经元改变答案”作为因果证据，但未回答该组多少神经元必要、是否存在其他可替代组、效果是否跨输入迁移。

方法：对 Qwen3-0.6B 双选项首都任务，枚举 12 个 MLP 神经元所有 4096 个子集做 zero-ablation；对两跳关系链（如 Lion King riddle），将 12 个神经元激活替换为第一跳问题的激活，观察 greedy answer 是否变成桥接实体；并测试同链改写与跨链。

结果：首都任务中消融选定 12 个神经元使答案 margin 下降 27%，随机神经元几乎无影响；但用其他问题的激活替换同组神经元也几乎无影响，说明这些激活在问题间近似常量，不携带问题特定内容。两跳链上 patching 后 greedy answer 以桥接实体开头：Qwen3-1.7B 9/11、Llama-3.2-1B 9/11、Gemma-3-1B 8/10；随机神经元为零。完整组很少必要：少数神经元常足够，许多链中不相交子集各自能独立翻转答案，且多发生在模型置信度较低时。组效应可迁移到同一链的改写，但跨链明显减弱。总体表明因果神经元组并不唯一，内部高度冗余，其效应部分可迁移。
