---
title: 'Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces'
title_zh: 基于 UI 行为痕迹的 LLM 浏览器智能体指纹识别
authors:
- William Lugoloobi
- Samuelle Marro
- Jabez Magomere
- Joss Wright
- Chris Russell
affiliations:
- University of Oxford
arxiv_id: '2605.14786'
url: https://arxiv.org/abs/2605.14786
pdf_url: https://arxiv.org/pdf/2605.14786
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- LLM Agent
- Browser Fingerprinting
- Behavioral Trace
- Side-Channel Attack
- XGBoost
one_liner: 仅通过页面动作时序,即可识别浏览器智能体的底层模型,F1 最高 96%,随机延迟防御可被自适应分类器破解
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

**动机**：LLM 驱动的浏览器智能体正被快速部署，但每次访问都可能被页面捕获行为痕迹。传统靶标识别是攻击的第一步，若网站能被动推断出底层模型，便可针对已知漏洞实施定向攻击（如模型特定 jailbreak）。本文首次探究仅利用页面 UI 交互痕迹（点击、滚动、按键）及其时序，能否识别出 14 个前沿 LLM 中的具体模型。

**方法**：统一使用 Midscene.js 纯视觉 harness 在 Wikipedia 和 Amazon 等真实网站执行信息检索与购物任务，通过注入的 JavaScript 追踪器记录毫秒级精度的 DOM 事件。从每个交互会话中提取 41 个行为特征，包括动作间隔均值/标准差/分位数、点击空间散布、导航比例、按键结构比等。在闭集（14 类）和开集（留一模型）设置下，训练 XGBoost、随机森林等分类器。进一步通过 SHAP 分析特征重要性，并模拟注入随机延迟测试防御效果。

**关键结果**：闭集宏 F1 最高达 96.6%（FRAMES 上 Seed-2-lite），大部分模型 F1 超 70%。开集检测 AUROC 普遍 >0.6。时序特征（如点击 IEI 标准差）贡献最大，但注入均匀延迟后分类器性能骤降；然而，若重训练于延迟轨迹，分类器转而依赖动作结构特征（如按键比率、点击位置），性能基本恢复。仅需 1/3 训练轨迹或前 40% 测试动作即可实现有效识别，表明指纹在早期即显现且样本高效。本次研究揭示了新任一种被动识别面，为未来的智能体安全防御提供了新思路：不是区分人机，而是识别哪类模型在操控。
