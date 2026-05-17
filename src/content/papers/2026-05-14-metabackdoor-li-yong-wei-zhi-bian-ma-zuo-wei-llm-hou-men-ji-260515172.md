---
title: 'MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface
  in LLMs'
title_zh: MetaBackdoor：利用位置编码作为 LLM 后门攻击面
authors:
- Rui Wen
- Mark Russinovich
- Andrew Paverd
- Jun Sakuma
- Ahmed Salem
affiliations:
- Institute of Science Tokyo
- Microsoft Azure
- Microsoft Security Response Center
arxiv_id: '2605.15172'
url: https://arxiv.org/abs/2605.15172
pdf_url: https://arxiv.org/pdf/2605.15172
published: '2026-05-14'
collected: '2026-05-17'
category: LLM
direction: LLM 安全 · 后门攻击
tags:
- backdoor attack
- positional encoding
- LLM security
- adversarial attack
- triggerless backdoor
one_liner: 提出基于位置编码的无内容触发器后门攻击，能泄露系统提示或自我激活恶意行为
practical_value: '- 在电商/推荐 Agent 的多轮对话中，警惕序列长度自然增长可能触发隐藏后门，需监控对话轮次与 token 长度，设置安全阈值。

  - 部署 LLM 前，应对位置编码相关的后门进行红队测试，不仅检测内容触发器，还要扫描与位置相关的异常行为。

  - 系统提示、工具调用等敏感逻辑应分层隔离，减少后门泄密面；即使输入文本干净，也可能被位置触发泄露。

  - 防御策略不能仅依赖文本可疑检测，应引入位置感知的防御机制，如限制上下文长度或对特定位置范围的输出加强审核。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 后门依赖基于内容的触发器（如特殊词、符号），需篡改输入文本，易被检测防御。本文发现 Transformer 强迫的位置编码可被用作一种“无内容”触发器，攻击者无需修改语意即可激活后门。  
**方法**：提出 MetaBackdoor，在模型训练时植入与序列长度相关的位置触发条件。例如，当对话 token 数超过阈值或落在特定位置区间时，模型行为改变：泄露系统提示、生成特定恶意输出或自动调用危险工具。甚至可实现“自我激活”：正常多轮对话自然累积长度，不自觉进入触发区域。攻击完全在语义干净的输入上生效，并能与内容触发器组合，增加隐蔽性。  
**结果**：在多种 LLM 场景下验证了攻击有效性，展示了三种新能力：① 泄露内部信息（如系统提示）；② 多轮交互自我激活恶意工具调用；③ 与内容后门正交组合，创造更难检测的复合触发器。攻击对现有基于文本检测的防御构成挑战，揭示位置编码是 LLM 安全中一个被忽视的攻击面。
