---
title: Real-Time Voice AI Hears but Does Not Listen
title_zh: 实时语音AI听得见声音却听不懂语气
authors:
- Martijn Bartelds
- Federico Bianchi
- James Zou
affiliations:
- Together AI
- Stanford University
arxiv_id: '2606.26083'
url: https://arxiv.org/abs/2606.26083
pdf_url: https://arxiv.org/pdf/2606.26083
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: 语音Agent情感智能评估
tags:
- real-time voice
- emotional intelligence
- perception-action gap
- prosody
- agent evaluation
- safety
one_liner: 主流实时语音AI在做决策时忽略声音情绪，仅依赖文字内容，形成“情感智能差距”
practical_value: '- 在语音客服或语音推荐Agent中，不能只依赖ASR转写的文本进行决策，必须将声音情绪特征（如语调、语速、重音）作为决策的额外模态输入，否则可能误判用户意图（比如愤怒用户说“没事”而机器人草率结束会话）。

  - 对于需要情感敏感的场景（如投诉处理、大额交易确认），可以加入声学情感分类器作为安全阀，当检测到声音情绪与文字语义冲突时触发人工介入或二次确认。

  - 评估语音Agent能力时，应专门设计“词汇-韵律冲突”的测试集，避免仅用文字上的准确率作为指标，从而暴露系统是否真正理解语音。

  - Prompt工程直接要求模型关注声音情绪有时能改善，但不稳定，更可靠的方案是架构层面融合独立的语音情感表征（如加入专门的prosody encoder），而不是期望单一模型兼顾。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：人类语音同时传递词汇内容和非词汇的副语言信息（语调、情绪等），但实际测试发现，当前领先的实时语音AI系统在做决策时常常忽略声音线索，仅依赖文字，可能导致严重后果（如误判求救电话）。

**方法**：评估了四个生产级实时语音系统——OpenAI GPT Realtime 2、Google Gemini 3.1 Flash Live、阿里Qwen3.5 Omni Plus和Omni Flash。设计了三个典型场景：1）哭泣者坚持说没事时系统是否会挂断；2）用恐惧声音授权转账时系统是否批准；3）用明显讽刺语气表示同意时系统是否错误注册。同时测试了直接询问情绪时的识别能力，以及口音、年龄估计中的偏见。

**关键结果**：所有系统在三个场景中均按文字含义行动，完全忽略声音情绪（挂断哭泣者、批准恐惧转账、接受讽刺同意），尽管直接提问时，四者中的三个能准确识别哭泣、恐惧和讽刺。在口音与年龄估计中，系统也倾向于跟随词汇偏见而非实际声音特征。将这种“感知-行动脱节”命名为情感智能差距。进一步实验表明，通过提示词引导模型关注声音只能部分改善，且效果不一致。

**结论**：当前实时语音AI的行为相当于将语音降级为文本转录，在需要情绪理解的应用中存在风险。
