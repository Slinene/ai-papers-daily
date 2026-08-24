---
title: Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning
title_zh: 记忆增强解锁高效思维链推理
authors:
- Simeng Zhang
- Yilong Chen
- Wenyuan Zhang
- Zhenyu Zhang
- Yao Chen
- Junyuan Shang
- Tingwen Liu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- Baidu Inc.
- Tencent Inc.
arxiv_id: '2608.21265'
url: https://arxiv.org/abs/2608.21265
pdf_url: https://arxiv.org/pdf/2608.21265
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM 推理加速 × 记忆增强压缩
tags:
- Chain-of-Thought
- Prompt Compression
- Memory Augmentation
- Inference Efficiency
- LLM
one_liner: 提出训练无关的记忆增强压缩框架，用历史推理模式作为预填充支架补偿思维链压缩的信息损失
practical_value: '- 在电商/推荐场景中，若用 LLM 做复杂推理（如商品属性抽取、多步排序、用户意图理解），可将完整 CoT 改为 Chain-of-Draft
  风格短推理链降低延迟；同时构建可检索的“推理记忆库”，从历史正确推理中总结关键约束、公式和操作序列，作为 prompt 前缀注入，补偿压缩带来的准确率损失，无需训练，直接可用。

  - 记忆的生成与使用可以借鉴 RAG 架构：将历史推理轨迹离线总结为结构化短记忆（如规则、公式片段）并建索引，线上根据问题检索最相关记忆，加入 system 或
  prefix；注意实验表明增益来自记忆相关性，单纯拼接长上下文无效，所以向量相似度和相关性过滤要重点设计。

  - 对推荐系统中的 query 改写、排序解释、广告文案生成等需要推理但追求低延迟的任务，可以采用“压缩+记忆”的组合：短输出 + 预填充的关键决策因子，达到速度与效果平衡，特别是线上高
  QPS 场景。

  - 该方法训练无关，兼容 token 级、推理轨迹级、推理状态级压缩，可作为现有 LLM 推理加速方案的轻量插件，适合快速验证对业务指标的影响。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在复杂任务上依赖思维链（CoT）推理，但冗长的推理轨迹带来显著推理开销。CoT 压缩可以减少生成量，但过度压缩会破坏逻辑连贯性、降低性能。论文将这一权衡形式化为“上下文-生成替代定律”：显式推理上下文可以替代部分解码期生成。

**方法关键点**：基于该定律，提出 **Memory-Augmented Compression**，一个训练无关框架。它从历史推理轨迹中构建可复用的推理记忆，这些记忆总结推理模式、关键约束和关键操作，并在预填充阶段作为 scaffold 检索注入，而不是使用原始演示。该方法兼容 token 级、推理轨迹级和推理状态级压缩机制，并可与 Chain-of-Draft（CoD）等提示压缩方法结合。

**关键结果**：在数学推理（GSM8K、MATH）、复杂推理（BBH）和科学问答（MMLU-Sci）四个基准上，Memory 将 CoD 的准确率分别提升 21.4、28.0、29.5、6.61 个百分点，同时相对标准 CoT 实现 1.14–1.49× 的延迟加速。进一步分析表明，性能增益来自检索到的相关推理记忆，而非简单增加上下文长度。
