---
title: StepAudio 3 Music Technical Report
title_zh: StepAudio 3 Music 音乐生成技术报告
authors:
- Chengli Feng
- Zhiyue Wu
- Jiahao Song
- Zheqi Dai
- Boyang Wang
- Ruibin Yuan
- Junming Gong
- Wenxiao Zhao
- Jing Guo
- Gang Yu
affiliations:
- StepFun
- ACE
- The Chinese University of Hong Kong
- University of California San Diego
arxiv_id: '2609.16034'
url: https://arxiv.org/abs/2609.16034
pdf_url: https://arxiv.org/pdf/2609.16034
published: '2026-09-10'
collected: '2026-09-18'
category: Multimodal
direction: 音乐生成 · ABC-CoT 显式规划
tags:
- music generation
- flow matching
- DiT
- MoE
- DPO
- audio tokenizer
one_liner: 支持 ABC-CoT 显式音乐规划与离散-连续表示的 5 分 30 秒级音乐生成模型
practical_value: '- 显式中间规划再做最终生成：在推荐理由、push 文案、对话式导购等场景中，可以先产出结构化计划（如类目、卖点、风格、约束）作为部分上下文，再生成最终文案，提升可控性和结构一致性。

  - 离散 token + 连续 latent 混合生成路径：生成式召回或内容生成中，可用 Semantic ID 作为离散 token，配合 diffusion
  生成连续隐变量，兼顾语义可控与高保真重建。

  - 低帧率大码本 single codebook：50Hz、65536 码本降低序列长度和解码成本；在 item/query 表示 tokenization 时可借鉴“低频帧
  + 大码本 + 语义辅助多任务训练”。

  - 用 DPO 直接优化业务偏好指标：AudioBox 的 enjoyment、usefulness、production quality 均在 DPO 后提升，说明推荐文案、搜索
  query 生成等任务可以在 SFT 后用真实业务偏好做偏好优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长时音乐生成需要同时解决结构规划与高保真音频合成，纯离散或纯连续方法各有瓶颈。StepAudio 3 Music 面向显式音乐规划与开放域文本控制，目标提升长序列音乐的结构一致性、可用性与听感质量。

**方法关键点**：音频 tokenizer 输出 50Hz、单码本 65536 的 token 流，以语义自监督和多任务训练保留音乐结构；flow-matching DiT 预测连续 VAE latent，再由解码器生成 48kHz 音频。显式规划部分用 MoE 自回归模型先以 ABC notation 产生中间编排计划（ABC-CoT），再预测音乐 token，将和声、节奏、旋律结构纳入上下文。渐进式训练课程与 SFT 支持歌曲/器乐生成、干声伴奏与 cover 合成，最长 5 分 30 秒；最后引入 DPO 做偏好优化。

**结果**：最终模型在 AudioBox Content Enjoyment、Content Usefulness、Production Quality 及 MuQ-MuLan 相似度上取得评测系统最高分，SongBench 具有竞争力；在 Artificial Analysis Music Arena Vocals 初步榜上 Quality Elo 1105，仅次于 Suno V5.5 与 Mureka，超过 Suno V5 和 MiniMax 等。
