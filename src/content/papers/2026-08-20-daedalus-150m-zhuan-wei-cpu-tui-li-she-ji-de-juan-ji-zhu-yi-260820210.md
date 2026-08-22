---
title: 'Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference'
title_zh: Daedalus-150M：专为 CPU 推理设计的卷积-注意力混合模型
authors:
- Christos Koutsiaris
arxiv_id: '2608.20210'
url: https://arxiv.org/abs/2608.20210
pdf_url: https://arxiv.org/pdf/2608.20210
published: '2026-08-20'
collected: '2026-08-22'
category: LLM
direction: 高效小型 LLM 架构 · 卷积-注意力混合
tags:
- CPU inference
- hybrid architecture
- small language model
- efficient inference
- quantization
one_liner: 用 12 个短卷积层替代多数注意力层，在 CPU 长文本解码时实现 1.76 倍加速且质量不降
practical_value: '- 对于需要在 CPU 或端侧低延迟推理的轻量级模型（如端侧 query 建议、实时 push 文案生成、边缘排序模型），可以尝试用短卷积替代大部分注意力层，减少
  KV cache 读取；在长上下文时加速显著，适合长 prompt 或长序列用户行为建模。

  - 目标驱动的架构设计：先固定部署环境（单用户、4-bit、普通 CPU），再反向选择模型结构，比“先设计大模型再压缩”更高效；推荐系统在边缘部署小模型时可复用这一思路。

  - 在模型选型时采用预先注册对照实验：固定训练数据和模型尺寸，比较不同架构，并事前确定胜利指标，避免事后挑选；业务团队做架构升级时值得借鉴。

  - 注意其报告的负面结果：4-bit 量化有不可忽视的质量损失，部分卷积通道实为冗余且难以修剪，词汇表不宜大于模型规模所需；这些小模型工程细节可直接避免踩坑。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：传统小语言模型沿用大模型架构，训练后再压缩部署到 CPU，但 CPU 单用户推理场景下 batch size 为 1，每 token 解码都需要重新流式加载权重，内存带宽成为瓶颈，注意力层的 KV cache 随上下文线性增长会加剧带宽压力。作者固定目标：单用户、逐 token、4-bit 权重、普通 CPU，针对这一目标设计架构。

**方法**：Daedalus-150M 共 18 个 block，仅其中 6 个保留 full attention，其余 12 个使用短卷积，其状态内存固定为两个时间步宽，与对话长度无关；因此三分之二的网络不会反复读取不断增长的 cache。模型从头训练，数据量为 59.9B tokens。

**结果**：五任务 benchmark 得分 47.31，超过预注册基线 42.20；击败 GPT-2 124M、Pythia-160M、OPT-125M、GPT-neo-125M（尽管它们用了 3-6 倍数据），也超过 MobileLLM-125M 的已发布得分（后者训练了 1T tokens）。验证集 bits-per-byte 为 0.8685。与同规模全注意力模型在相同数据上对照，混合架构质量指标赢 0.81%，下游任务持平，4-bit 文件小 6.3%，在 2048 token 上下文解码快 1.76 倍（对外部模型 2.08 倍）；速度优势随上下文长度增长，空上下文时接近零。带宽计算仅解释 1.17 倍加速，说明不只是内存量下降。另报告失败：4-bit 量化质量损失未缓解、约一半卷积通道惰性且无法移除、词汇表过大。
