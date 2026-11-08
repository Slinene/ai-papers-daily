---
title: 'Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex
  Speech Language Models'
title_zh: 先解码后聆听：分块交织全双工语音语言模型的推测性聆听
authors:
- Yutong Bian
- Yanglin Zhang
- Yuxiang Wang
- Luoyuan Zhang
- Rongshen He
- Zihao Wang
- Junwen Qiu
- Jiaqi Li
- Zhizheng Wu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Amphion Technology Co., Ltd.
arxiv_id: '2611.06982'
url: https://arxiv.org/abs/2611.06982
pdf_url: https://arxiv.org/pdf/2611.06982
published: '2026-11-03'
collected: '2026-11-08'
category: LLM
direction: 全双工语音语言模型 · 推测解码加速
tags:
- Speculative Decoding
- Speech Language Model
- Full-Duplex
- Low Latency
- Tool Call
- Inference Acceleration
one_liner: 利用静音假设在空闲期对下一音频块做自推测解码，无损加速全双工语音模型，响应前延迟降低73%
practical_value: '- 在实时语音客服/语音搜索等场景，可用「静音/空输入」作为假设，在系统等待音频或用户停顿时用空闲算力预生成草稿，真实输入到达后再验证；该方法训练无关、无损，可直接用于已有语音交互
  Agent 的推理加速。

  - 观察「95.3% 的下一块不改变输出、88% 变化在首 token」提示首 token 不确定性是预测式生成的主要瓶颈；在 Agent 工具预调用或 query
  补全中，可只维护 top-1 / runner-up 首 token 两个草稿分支，以极小开销提升 speculative 命中率。

  - 跨块假设池与一次性验证机制可迁移到多轮对话/Agent 工作流：等待用户输入或工具返回时预生成多个候选回复或候选动作，输入到达后批量验证，降低用户感知延迟；对
  batch 推理服务也可复用「空闲槽位预填充」思想。

  - 注意该方法依赖语音块边界与输入时序；若业务输入高度随机（如电商推荐请求），静音假设不一定成立，需先统计输入对输出的影响比例再决定是否引入。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
分块交织全双工语音语言模型按固定时间块听与说，每个块须在下个块到达前处理完。实际负载不对称：听块等待音频时计算空闲，说块和工具调用块需串行生成，造成响应与工具调用延迟。核心问题是如何利用空闲计算提前解码下一块。

### 方法关键点
采用静音作为假设输入，在四个模型上观察到：95.3% 的块中下一块音频不改变输出；88% 的变化始于第一个输出 token。据此提出 Speculative Listening：训练无关、无损的输入时自推测解码。空闲时模型在静音下为下一块草拟输出；若变化发生在首 token，还从 runner-up 首 token 生成第二分支。所有草稿保留在跨块假设池中，音频到达后验证接受或回退。

### 关键结果数字
在八任务基准 TickTock-Bench 上，说块加速 2.6–2.8 倍，工具调用块最高加速 23.4 倍；响应开始前的解码延迟平均降低 73% 至 74–241 ms，接近人类轮流间隔 200 ms；实时最大滞后降低 94.4%。
