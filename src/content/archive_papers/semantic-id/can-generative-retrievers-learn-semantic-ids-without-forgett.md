---
title: "Can Generative Retrievers Learn Semantic IDs Without Forgetting How to Speak?"
authors: "Junchen Fu, Kleomenis Katevas, Vandana Rajan, Sofía Celi, Hamed Haddadi"
affiliation: "University of Glasgow × Brave"
date: 2026-09
venue: "arXiv (cs.IR)"
topic: semantic-id
topic_name: "Semantic ID"
topic_icon: "🗂"
idea: "把「SID 生成式检索会不会让 LLM 忘了怎么说话」当成一个独立问题来测：只做 SID 检索微调时，Qwen3-0.6B 的 WikiText PPL 在 25 步内从 31.69 涨到 6,956，最终 FKL 达 5.5–13.0，模型基本丧失自然语言能力。提出 SpeakGR，把「学 SID」和「保住说话能力」写成同一参数上的双目标：检索侧是层级受限的 SID 交叉熵，保持侧借用 on-policy distillation——学生屏蔽 SID token 自己采样续写，冻结的原始模型在同一前缀上给出下一 token 分布，在原文本词表上做 forward KL。Adaptive SpeakGR 再用 EMA 化的漂移量乘性调节正则权重 λ。六组 backbone×数据集上 FKL 下降 81–94%，召回基本保持，Adaptive 版在 5/6 组召回比固定权重版更好。"
paperUrl: https://arxiv.org/abs/2609.35430
codeUrl: null
tags: ["Semantic ID", "Generative Retrieval", "Catastrophic Forgetting", "On-Policy Distillation", "Adaptive Regularization"]
unverified: false
---

## 核心思路

把「SID 生成式检索会不会让 LLM 忘了怎么说话」当成一个独立问题来测：只做 SID 检索微调时，Qwen3-0.6B 的 WikiText PPL 在 25 步内从 31.69 涨到 6,956，最终 FKL 达 5.5–13.0，模型基本丧失自然语言能力。提出 SpeakGR，把「学 SID」和「保住说话能力」写成同一参数上的双目标：检索侧是层级受限的 SID 交叉熵，保持侧借用 on-policy distillation——学生屏蔽 SID token 自己采样续写，冻结的原始模型在同一前缀上给出下一 token 分布，在原文本词表上做 forward KL。Adaptive SpeakGR 再用 EMA 化的漂移量乘性调节正则权重 λ。六组 backbone×数据集上 FKL 下降 81–94%，召回基本保持，Adaptive 版在 5/6 组召回比固定权重版更好。

## 整体实现思路

```
Query ──► 学生 πθ (V_text ∪ V_SID) ──► 分级受限 CE ──► L_ret
                                                        │
语言 prompt x ──► 学生屏蔽 SID 采样续写 ŷ (stop-grad)     │
          │                                             ▼
          ├─► 冻结原模型 π0(·|x,ŷ<t) ─┐        L_t = L_ret + λ_t · L_Speak
          └─► 学生 πθ^V_text(·|x,ŷ<t) ─┴► forward KL ──► L_Speak
                                                        │
Adaptive: D_t → EMA K_t → e_t=clip(K_t/ϵ−1) → 死区 → λ_(t+1)=λ_t·exp(η·ẽ_t)
```

## 核心贡献

(1) 第一次系统测量 SID 检索特化对底座语言能力的破坏：3 个 backbone（Qwen3-0.6B/1.7B、Gemma-3-1B-IT）× 2 个数据集（MS MARCO、NQ）一致显示，纯 SFT 能学出有效检索，但语言分布会被迅速扭曲（WikiText FKL 5.5–13.0，PPL 最高到 1,362 万）；(2) 提出 SpeakGR：同一套参数上联合优化 SID 交叉熵与「speak-preserving」正则，正则是在学生自采样前缀上、限定原文本词表的 forward KL（teacher=冻结原模型），把检索当作新增能力而不是替换原有能力；(3) 提出 Adaptive SpeakGR：以训练中观测到的保持项 KL 的 EMA 与参考水平 ϵ 的偏差为信号，带死区和截断地乘性更新 λ，免去固定权重的选择；(4) 用语言漂移指标 Δ_lang（在原文本词表上重归一化后的 KL）把「SID token 抢概率」与「文本 token 内部分布变形」分开，并证明退化主要来自后者。

## 背景

生成式检索（DSI/NCI/TIGER 一脉）把每个文档编成 L 级离散 SID，扩展 LLM 词表后让模型从 query 自回归生成 SID。选 LLM 做检索器的一个重要理由是：同一个模型检索完还能回答、总结、引用、追问澄清，一个模型走完整个交互。但标准 GR 训练目标只优化 SID 生成，没有任何项约束文本 token 的分布，而且以往工作几乎只报 Recall，没人量过语言能力是否还在。如果检索微调把模型的语言能力毁了，那这些「统一接口 / 省掉单独 reader」的好处都无从谈起。相关工作里，ORBIT（Verma et al., 2026）在序列推荐上研究过遗忘，做法是监测参数符号漂移、超阈值就把权重与原模型 1:1 合并；经典防遗忘手段还有 EWC 类参数约束与 replay。本文的区别在于直接在目标函数层面正则语言分布，而不是改参数。

## 方法

【问题设定】冻结原模型 π0（原词表 V_text），学生 πθ 从 π0 初始化并把词表扩到 V_text ∪ V_SID，各级 SID token 集 V_ℓ 互不相交；文档 SID 由 Qwen3-Embedding 文档向量经 RQ-VAE 得到（5 级 × 256 码本，SID 长度 5）。【检索目标】L_ret：在每一级只对 V_ℓ 内 logits 重归一化后算 CE，按 SID token 数归一化；EOS 做 teacher forcing 但不计损失。推理用分级动作空间 + 文档 trie 约束解码，碰撞桶（MS MARCO 仅 1.94%）用冻结 Qwen3-Embedding-0.6B 桶内重排。【漂移度量】Δ_lang = E_s[KL(π0(·|s) ‖ πθ^{V_text}(·|s))]，πθ^{V_text} 是把学生分布限制在原文本词表并重归一化，这样只衡量文本 token 之间相对概率的变化，不把「概率漏给 SID token」混进来；评测用 WikiText-2 test 的固定前缀。【Speak-preserving 正则】借鉴 on-policy distillation（Agarwal et al., 2024）：对语言 prompt 池 D_lang 中的 x，学生屏蔽全部 SID logits、只在 V_text 上采样续写 ŷ（温度 0.8、top-p 0.9、top-k 20、最多 32 token），采样结果视作常量不回传梯度；冻结原模型与学生读同一序列 (x, ŷ)，在每个续写位置 s_{i,t}=(x_i, ŷ_{i,<t}) 上算 Σ_v π0(v|s) log(π0(v|s)/πθ^{V_text}(v|s))，按总续写 token 数归一化。关键点：前缀由学生产生（学生当前会走到的状态），老师只给分布不给目标序列。选 forward KL 是因为在固定前缀上它等价于以老师分布为软标签的 CE，惩罚学生对老师偏好 token 给的概率不够（mode-covering）；其对学生文本 logits 的梯度就是 πθ^{V_text} − π0。【SpeakGR】L = L_ret + L_Speak（λ=1，两项各自按 token 归一化）。【Adaptive SpeakGR】每步 D_t = 当前保持 batch 的全局 token 平均 KL，K_t = αK_{t−1} + (1−α)D_t，e_t = clip(K_t/ϵ − 1, −c, c)，|e_t|≤δ 时置零（死区），λ_{t+1} = clip_{[λmin, λmax]}(λ_t·exp(η·ẽ_t))；当前步用 λ_t，观测 KL 决定下一步。默认 ϵ=1 nat/token、α=0.95、c=0.2、δ=0.05、η=0.05、λmax=1，Stage1 λ0=0.1、λmin=0.01。【训练流程】三阶段：doc→SID 索引 2k 步、docT5query 伪 query→SID 8k 步、真实 query→SID 2k 步；全参微调（含 embedding），每次优化更新配 6 条语言 prompt。语言 prompt 池 = 2,048 条 WikiText-2 train 续写前缀 + 2,048 条由训练段落/MS MARCO 问题/任务模板构造的指令型 prompt，WikiText-2 test 只用于评测。

## 实验设置与结果

数据：MS MARCO 子集 319,872 文档、NQ 子集 109,739 文档；R@1/R@10/MRR@10，trie 约束 beam（MS MARCO 10、NQ 100）；语言侧在 64 块 × 256 token 的 WikiText-2 test 上算 FKL、PPL、Top-1 一致率、SID 概率质量。主结果（R@10 / FKL / PPL）：MS MARCO·Qwen3-0.6B：SFT 0.6386/8.103/53,967，SpeakGR 0.6349/1.519/88.5，Ada 0.6498/1.728/105.9；MS MARCO·Qwen3-1.7B：SFT 0.6696/11.222/648,108，SpeakGR 0.6324/1.761/66.7，Ada 0.6745/1.841/70.7；MS MARCO·Gemma-3-1B：SFT 0.6337/13.005/1,362 万，SpeakGR 0.6361/0.809/88.2，Ada 0.6399/0.775/86.1；NQ·Qwen3-0.6B：SFT 0.7397/6.379，SpeakGR 0.6582/1.044，Ada 0.7285/1.116；NQ·Qwen3-1.7B：SFT 0.7507/5.545，SpeakGR 0.7172/1.042，Ada 0.7280/1.030；NQ·Gemma：SFT 0.7138/5.631，SpeakGR 0.7324/0.831，Ada 0.7189/0.743。FKL 相对下降 MS MARCO 81.3–93.8%、NQ 81.2–85.2%；Top-1 一致率从 SFT 的 0.1–17% 回到 43–58%。召回影响因设置而异：Qwen 在 NQ 上 SpeakGR 掉得最多（0.6B R@10 0.7397→0.6582），Adaptive 基本追回（0.7285）；Gemma 两组 SpeakGR 反而涨召回。基线对比（Qwen3-0.6B）：offline replay 在 MS MARCO FKL 8.672/R@10 0.5903，几乎没保住语言；ORBIT 强依赖阈值 τ——宽松 τ=0.10 召回 0.6584 但 FKL 7.391，严格 τ=0.007 FKL 0.273 但 R@10 跌到 0.1980；SpeakGR 落在两者之间的更优区域。ϵ 敏感性：ϵ∈[0.5, 2.0] 都在较好区域，最佳 R@10 0.6584@ϵ=1.5（FKL 1.566），过严 ϵ=0.25 反而召回 0.5458、FKL 2.507 双输，说明 ϵ 是训练参考值而不是 held-out 漂移的上界。机制分析：SID 概率泄漏只占 SFT 超额 NLL 的 0.58%，退化主体是文本 token 内部相对概率变形；共享概率质量 SFT 2.85% → SpeakGR 47.85%；残差流末层余弦漂移 SFT 1.61 vs SpeakGR 0.23，中后层方向漂移显著降低，但表征几何（CKA）结论对位置选择敏感，更像是「函数空间正则允许内部为检索适配」。

## 思考与可参考价值

### 优点

① 问题问得准：GR 社区长期只看 Recall，这篇把「检索器还能不能说话」变成一个可量化的指标（限定原词表重归一化的 FKL），并且把 SID 泄漏与文本分布变形拆开，结论（主因是后者）有信息量；② 方法简单、可嫁接：保持项只需要一个冻结老师 + 学生自采样的短续写（≤32 token），不改模型结构、不需要额外标注，任何「给 LLM 加新 token 做特化」的训练都能直接加；③ on-policy 前缀 + forward KL 的组合比 offline replay 合理——正则施加在学生当前实际会走到的状态上，实验上 replay 在同预算下几乎无效，对比很说明问题；④ 与 ORBIT 的对比揭示了权重合并类方法「要么保语言要么保召回」的阈值困境，目标函数层面的正则更平滑；⑤ 实验控制好：同 SID 分配、同初始化、固定 held-out 集，六组设置 + 敏感性 + 机制分析齐全，作者对结论边界（WikiText≠完整语言能力）表述克制。

### 局限

① 「会说话」只用 WikiText-2 上的下一 token 分布来衡量，没有任何下游生成任务（问答、总结、澄清追问、基于检索结果的回答）评测，而论文动机恰恰是这些交互场景——分布接近不代表能用；② 即便有正则，PPL 仍从 31.69 升到 88–106（0.6B），FKL ~1.5 nat/token 并不小，离「不遗忘」还有距离，标题的答案更像是「能少忘很多」；③ 召回代价不稳定：固定权重的 SpeakGR 在 NQ·Qwen 上 R@10 掉 8 个点，需要 Adaptive 才能追回，而 Adaptive 又引入 ϵ/α/c/δ/η/λ 范围六个超参，且不同 backbone 的 stage 间重置策略不同（1.7B/Gemma 在 Stage 2 重置 λ=0.25），有调参痕迹；④ 规模只到 1.7B、语料只到 32 万文档，绝对召回也不是 SOTA（作者明说不追 SOTA），大模型、千万级库上的结论未知；⑤ 训练成本没报：每步都要学生采样续写 + 老师前向，在线开销和吞吐影响没讨论；⑥ 代码为匿名仓库，正文未给出可访问链接。

### 对搜索推荐/Agent方向的可借鉴点

(1) 对我们做 SID 生成式推荐/搜索（如 Qwen3-0.6B + SID 的协同训练）很直接：如果希望同一个模型既出 SID 又保留语言能力（生成推荐理由、query 改写、CoT 后出 SID），纯 SFT 会把文本分布打坏，可以直接加一项「屏蔽 SID 采样续写 + 冻结 base 的 forward KL」作为廉价正则，prompt 池可以用业务语料（商品标题/query）而不是 WikiText；(2) 「在原文本词表上重归一化的 FKL + SID 概率质量」这对指标可以作为 SID 训练的常驻监控，比只看 PPL 更能定位问题是 SID 抢概率还是文本分布变形；(3) Adaptive λ 的 EMA + 死区 + 乘性更新是一个通用的「目标 KL 控制器」，可以迁移到任何需要把辅助约束控制在目标水平的多任务训练（例如 RL 里控制对 reference 的 KL）；(4) 反面提示：replay 在同预算下几乎无效、ORBIT 类权重合并存在阈值困境，做防遗忘时优先考虑 on-policy 的分布级约束；(5) 值得补的实验：在电商场景评测「检索后生成」的真实下游能力，以及 SID 泄漏是否在更大 SID 词表（百万级商品）下变成主要矛盾。

## 一句话总结

SID 检索微调会迅速毁掉 LLM 的语言分布（FKL 5.5–13），SpeakGR 用「学生自采样前缀 + 冻结原模型 forward KL（限原词表）」作为和 SID 交叉熵并列的第二目标，把漂移降 81–94% 且召回基本不掉，Adaptive 版用 EMA 控制器自动调权重。一句话：想让同一个模型既出 SID 又能说话，就把「保住说话能力」写进损失函数，而不是事后合并权重或做 replay。
