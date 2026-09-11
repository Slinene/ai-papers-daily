---
title: 'NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models
  through Next Concept Prediction'
title_zh: 通过下一概念预测迈向隐空间语言模型
authors:
- NCP Team
- Jiaqi Cao
- Chiyu Chen
- Shuang Cheng
- Xu Cheng
- Beiya Dai
- Yufan Feng
- Kewen Ge
- Ruijun Ge
- Jiayi Huang
affiliations:
- Shanghai AI Lab
- LUMIA Lab, Shanghai Jiao Tong University
arxiv_id: '2609.10715'
url: https://arxiv.org/abs/2609.10715
pdf_url: https://arxiv.org/pdf/2609.10715
published: '2026-09-08'
collected: '2026-09-11'
category: Training
direction: 下一概念预测 · 隐空间语言模型
tags:
- Next Concept Prediction
- Latent Space LM
- Product Quantization
- Pretraining Efficiency
- Speculative Decoding
- Domain Adaptation
one_liner: 在 8.9B 参数规模验证 NTP 与 Next Concept Prediction 联合训练，用 51.3% tokens 达到 OLMo-3-7B
  最终 loss
practical_value: '- 将 product quantization 作用于 hidden states 构建离散概念 vocab，可类比生成式推荐里的
  Semantic ID，对 item/category/query 做多粒度 token-context 联合建模，让 LLM 在生成物品或搜索词时既有 token
  级流畅度又有概念级语义约束。

  - 只更新 17M 的 VQ module 即可实现域适配，适合电商多品类、多场景快速切换：固定底座，仅调整 codebook/概念映射，省去全参微调，便于线上迭代和
  A/B 测试。

  - 把 concept representations 注入 draft model 做投机解码，mean accepted length 提升 4.17% 且开销可忽略；在
  Agent 工具调用、推荐理由生成等长文本输出场景可低成本加速推理。

  - 联合 NTP + NCP 在同等算力下逼近或超过更强 baseline，提示大模型底座或领域微调时可加入概念级辅助目标，提升样本效率和 downstream
  指标。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：标准 next-token prediction 只建模 token 级关系，缺少显式概念级目标；隐空间语言模型通过离散概念实现高层压缩与预测，但此前缺乏大规模验证。

方法关键点：
- 在 NTP 之外引入 Next Concept Prediction（NCP），从模型 hidden states 使用 product quantization 构建离散 concept vocabulary，概念可跨多个 token。
- 新增 Concept Module 预测未来概念，并将 concept 表示反馈到 token level 引导后续生成，NTP 与 NCP 端到端联合训练。
- 规模：8.9B 参数，Dolma-3 数据集 5.73T tokens。

关键结果：
- 仅消费 51.3% 训练 tokens，即达到 OLMo-3-7B 的最终 pretraining loss；完整预训练后下游宏平均超过 OLMo-3-7B 2.45 点，其中 GSM8K 提升 5.99 点。
- 使用 85% 标准算力可逼近严格参数对齐的 8.9B baseline。
- 预训练后隐空间仍有用：只更新 17M VQ 模块实现轻量域适配；将概念表示注入 DFlash2 drafter，mean accepted length 提升 4.17%，开销可忽略。
