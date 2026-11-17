---
title: 'LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers'
title_zh: LoopFill：用于循环 Transformer 的流水线多 token 投机解码
authors:
- Siqi Zhu
- Suozhi Huang
- Yi Zhao
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Princeton University
arxiv_id: '2611.19649'
url: https://arxiv.org/abs/2611.19649
pdf_url: https://arxiv.org/pdf/2611.19649
published: '2026-11-13'
collected: '2026-11-17'
category: LLM
direction: LLM 推理加速 · 投机解码
tags:
- speculative decoding
- looped transformers
- inference acceleration
- draft tree
- LLM serving
one_liner: 将多 token 后缀草稿与浅层循环预测结合到单一草稿树，无损加速 Looped Transformer 解码达 5.85 倍
practical_value: '- 业务上若采用循环/权重共享 Transformer 做生成式推荐或 query 改写，可直接用 LoopFill 这类训练无关、无损的投机解码方案降低线上延迟，尤其适合对输出分布一致性要求高的广告文案、搜索
  suggestion 场景。

  - 多 token 后缀草稿树可借鉴到通用 LLM 推理：用高频 n-gram cache（如用户历史 query、商品标题片段）构建后缀查找，与模型浅层草稿合并成树，提高投机解码接受率与
  batch 并行度。

  - 流水线调度思路值得在 LLM serving 中复用：将处于不同草稿深度的请求合并到一个 batch 计算共享 block，提升小 batch 下的 GPU
  利用率，适配搜索推荐系统高并发、低延迟请求。

  - 该方法无需微调，工程落地成本低，可作为现有自回归生成服务的推理加速插件，先在线下评估 speedup 与输出一致性再灰度上线。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Looped Transformer 通过重复应用同一组层提升参数效率，但自回归解码时每 token 需多次串行经过共享 block，延迟高；现有流水线 self-speculative 方法要求每个 token 必须达到草稿深度后才能让下一个 token 进入流水线，限制了并行度。

方法关键点：LoopFill 训练无关，将多 token 后缀草稿与浅层循环预测融入同一棵草稿树。后缀 lookup 可立即扩展浅层预测，使多个未来 token 一起进入流水线；共享 block 在同一个 batch 中计算不同循环深度的最高分草稿候选，最终由 full-depth verification 保证与自回归模型输出分布一致。

关键结果：在 7 个 benchmark 上，相对 greedy 自回归解码平均加速 5.85×（Ouro-2.6B）和 5.13×（Huginn-3.5B），比最强基线 LoopAhead 分别提升 40% 与 25%。
