---
title: 'Latent-MOPD: Latent Multi-Teacher On-Policy Distillation'
title_zh: Latent-MOPD：隐空间多教师在线蒸馏
authors:
- Zhengyu Fang
- Seoyeon Hong
- Jie Yang
- Muyang Li
- Koyoshi Shindo
- Brandon Joseph Lwowski
- Jing Li
affiliations:
- Case Western Reserve University
- Zillow Group, Inc.
- University of Illinois at Chicago
- University of Florida
arxiv_id: '2610.02381'
url: https://arxiv.org/abs/2610.02381
pdf_url: https://arxiv.org/pdf/2610.02381
published: '2026-09-30'
collected: '2026-10-06'
category: Training
direction: 多教师在线蒸馏与表示对齐
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Representation Alignment
- LLM
- Model Merging
one_liner: 首个表示级多教师在线蒸馏方法，通过路由晚期隐藏状态对齐和逐教师 crossfade 融合多专家能力
practical_value: '- 多领域模型融合时，不要只蒸馏输出分布：在 token-level OPD 基础上增加学生与路由专家的 late-layer
  hidden states 对齐，能保留专家内部推理信息；电商搜索/推荐/广告多场景 teacher 融合可复用这一思路，避免简单平均 logits 稀释专家置信度。

  - 当学生与教师 hidden width 不同，用一个共享线性投影（或小 MLP）桥接，并用少量 student-teacher 状态对做 ridge 回归初始化投影，能降低训练不稳；业务中不同尺寸
  CTR/CVR 或生成式推荐模型合并时可直接借鉴。

  - 多专家训练时务必保持 domain-pure batches：同一 optimizer step 混入多个 teacher 的表示监督会导致表示 collapse，论文中
  interleaved 更新使 MATH-500 从 91.7 掉到 9.8；多场景推荐/Agent 能力融合应按场景分组更新。

  - 每个 teacher 使用独立 crossfade 时钟：前期表示监督、后期 token 蒸馏，能稳定多专家训练；若多个 teacher 同源同架构，可先用参数平均（model
  soup）作为学生初始化，再做少量在线蒸馏，电商多领域模型合并有直接参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM 多教师在线蒸馏只在输出分布层传递专家知识，但专家预测来自内部计算，隐藏表示包含中间推理信息。单教师表示蒸馏有效，但多教师如何选择表示目标、组织监督尚未解决。

**方法关键点**：
- 提出 Latent-MOPD，首个表示级多教师 OPD。每个 prompt 按 domain 路由到对应专家，同时用该专家的 token 分布和 hidden states 监督学生。
- 表示目标选择：同 family 教师与学生 CKA 在中后期高、输出层差异大，选最后 3 层；跨 family 在中间层 CKA 低，选最后一层，并用共享线性投影（ridge 初始化）桥接宽度差异。
- 训练组织：domain-pure batches，避免同一 update 混入多专家表示监督导致 collapse；per-teacher crossfade 让每个专家的监督从表示 loss 逐步切换到 token loss。
- 教师全部冻结，推理只保留学生，投影映射可丢弃。

**关键结果**：同 family 1.5B 学生蒸馏 3 个 1.5B 专家，在 math/code/logic 九项 benchmark 上全部超过 token-only、表示-only 和 uniform averaging 基线；其中 5 项超过最强单专家。相对 MOPD-style，Minerva 33.5→36.3，LiveCodeBench-easy 68.3→73.1，MuSR 50.7→52.4。跨 family 用 7B 教师蒸馏到 1.5B 学生，六项基准均超过单通道基线，Norm 从 0.16 到 0.26。从参数合并初始化再蒸馏，六项中五项提升，Norm 0.87→1.03。

**一句话**：把多个专家“怎么算”的晚期表示和“算什么”的 token 分布一起按域路由蒸馏，比只抄输出更稳更强。
