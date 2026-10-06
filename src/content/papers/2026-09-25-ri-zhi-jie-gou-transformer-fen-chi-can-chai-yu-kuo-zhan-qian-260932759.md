---
title: 'The Extender: A Log-Structured Transformer'
title_zh: 日志结构Transformer：分离残差与扩展嵌入以压缩KV缓存
authors:
- Jakob Eriksson
affiliations:
- University of Illinois Chicago
arxiv_id: '2609.32759'
url: https://arxiv.org/abs/2609.32759
pdf_url: https://arxiv.org/pdf/2609.32759
published: '2026-09-25'
collected: '2026-10-06'
category: LLM
direction: Transformer架构改进 · KV cache压缩
tags:
- Transformer
- KV cache
- Long context
- Memory efficiency
- Architecture
one_liner: 提出日志结构Transformer，用每层32维扩展嵌入替代全宽KV缓存，使924M模型持久注意力内存减少104倍且长上下文更优
practical_value: '- 对于需要处理长用户行为序列或长文档上下文的电商/搜索推荐LLM，可借鉴双通道设计：将注意力KV输入改为低维log-structured扩展嵌入，回合间释放全宽KV缓存，显著节省显存，支持更长用户历史。

  - 架构改动仅影响注意力输入，与GQA、量化、层复用等现有压缩技术正交；论文显示Extender+GQA在参数更少情况下仍优于MHA Transformer，可直接叠加到现有推理优化栈。

  - 推理工程上可采用 ephemeral kv-cache 策略：持久保存x*缓存，按需重投影KV，适合多轮Agent或低频长上下文请求，避免长期占用大量显存。

  - 分离下一token预测残差流与注意力记忆通道的思想，可能提升长序列建模能力（如多key检索类任务），在用户行为建模或长文档理解场景值得验证。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
标准Transformer中，每一层的注意力KV缓存随模型宽度、深度和上下文长度线性增长，LLM推理时KV缓存可能超过100GB。现有方法如GQA、MLA、层复用、量化等主要降低推理期间的内存，但回合间持久内存仍然庞大。

**方法关键点**
- 引入双通道：残差流h继续用于下一token预测和FFN；新增加log-structured扩展嵌入x，每层输出一个极小的扩展向量εℓ（默认32维），拼接形成xℓ。
- 注意力KV投影只读取xℓ，q投影同时读取h和x。因此所有层共享同一个x*缓存，无需为每层保留全宽KV。
- 每层FFN同时输出残差更新δℓ和扩展εℓ；xℓ通过RMSNorm后拼接，hℓ通过加权残差更新。
- 默认滑动窗口取x的最后d_model维作为KV输入，第一层扩展宽度为64，ℓ_max = L-2。
- 推理时使用 ephemeral kv-cache：从x*缓存按需重投影KV，回合间可释放，避免重复计算开销。
- 与GQA、量化等技术正交，兼容叠加。

**关键结果**
- 在199M/436M/924M三个规模上，Extender在短上下文DCLM CORE基准上与Reference Transformer准确率持平。
- 在长上下文RULER基准上，Extender显著优于Transformer，尤其多key检索任务；上下文越长优势越大。
- 对于924M模型，64k上下文时持久注意力内存从5.67B特征（11.3GB）降至54.5M特征（109MB），减少104倍。
- 与GQA结合：813M Extender+GQA模型仍优于920M Transformer MHA。
- 蒸馏实验显示Extender学生可从Transformer或Extender教师有效学习。

**最值得记住的一句话**
用每层仅32维的log-structured扩展嵌入替代全宽KV缓存，可将持久注意力内存减少104倍且保持短上下文性能并提升长上下文能力。
