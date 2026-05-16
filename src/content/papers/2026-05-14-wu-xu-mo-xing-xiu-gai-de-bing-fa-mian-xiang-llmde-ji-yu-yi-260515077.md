---
title: 'Concurrency without Model Changes: Future-based Asynchronous Function Calling
  for LLMs'
title_zh: 无需模型修改的并发：面向LLM的基于Future的异步函数调用
authors:
- Guangyu Feng
- Huanzhi Mao
- Prabal Dutta
- Joseph E. Gonzalez
affiliations:
- University of California, Berkeley
arxiv_id: '2605.15077'
url: https://arxiv.org/abs/2605.15077
pdf_url: https://arxiv.org/pdf/2605.15077
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- LLM
- Function Calling
- Asynchronous
- Future
- Concurrency
- Agent
one_liner: 提出AsyncFC，通过Future占位符解耦LLM解码与函数执行，实现无模型修改的异步工具调用并显著降低延迟
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM的工具调用（function calling）遵循严格的同步调用-返回协议：模型每发起一个函数调用，解码即被阻塞，直到该函数执行完毕并返回结果。这种串行化机制忽视了函数间的并行性，且导致端到端延迟随任务复杂度线性增长。尽管已有尝试通过暴露异步执行状态或修改模型协议来引入并发，但它们要么偏离标准协议，要么要求模型微调，部署成本高。

### 方法关键点
AsyncFC是一个纯执行层框架，通过在模型上下文中引入**符号Future占位符**，将函数调用的调度与执行彻底从解码循环中解耦，且无需改动模型或函数实现。
- **Future化协议转换**：自动将同步函数模式改写为支持Future值的输入/输出模式，并添加`await_future`函数供模型显式等待结果。调用函数时，运行时立即返回一个Future标识，满足协议要求，解码继续，函数在后台异步执行。
- **回合级结果集成**：在每次解码回合边界主动注入已完成函数的实际结果，减少模型显式等待的次数；检测到`await_future`调用时采用提前停用解码以降低等待开销。
- **依赖感知调度器**：开发者可选通过装饰器声明函数对分层资源（路径）的读写权限，调度器据此进行冲突分析，保守地序列化冲突调用，自动解锁安全的函数间并行。无注解时默认所有函数串行执行，但仍可重叠解码与执行。
- **错误传递与取消**：函数执行失败时，传递性取消所有依赖它的后续调用，并向模型注入明确的失败与取消信息。

### 关键结果
在BFCL v3多轮基准（150个案例，注入5秒函数延迟，GPT-4o）上，AsyncFC相对串行FC提速**1.26倍**，且与同步基线的准确率无显著差异（p>0.05）。在BFCL v4 Web Search真实后端延迟场景下，AsyncFC相对串行FC提速**1.26倍**，相对并行FC额外提速**1.12倍**。在SWE-bench Lite软件工程基准（SWE-agent，GPT-5.2，2倍工具延迟）上，AsyncFC实现**1.44倍**端到端加速，准确率保持。在HotpotQA多跳推理异步思考任务中，提速**1.24倍**。延迟分解显示，解码-函数执行重叠在低延迟区提供主要增益，而函数间并行在高延迟场景下贡献更大。

> 最值得记住的一点：LLM无需额外微调即可对表示未完成执行结果的符号Future进行原生推理，这为高效异步的模型-工具交互开辟了新范式。
