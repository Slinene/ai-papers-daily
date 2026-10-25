---
title: 'What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise
  Document Ingestion'
title_zh: 作者写了什么，Agent 读了什么：企业文档摄取中的静默线索丢失
authors:
- Yikai Zhao
- Saurabh Pandey
- Pradeep Kumar Misra
affiliations:
- Amazon
arxiv_id: '2610.30026'
url: https://arxiv.org/abs/2610.30026
pdf_url: https://arxiv.org/pdf/2610.30026
published: '2026-10-21'
collected: '2026-10-25'
category: Agent
direction: 企业文档摄取与格式线索保留
tags:
- document ingestion
- formatting cues
- enterprise agents
- OOXML
- RAG
- evaluation
one_liner: 企业文档摄取层丢失高亮和颜色等视觉格式线索，使 Agent 对关键义务识别 F1 骤降且自信犯错
practical_value: '- 在 RAG/Agent 文档解析链路中优先保留高亮和颜色：实验显示 docling/plain text 格式盲摄取使义务识别
  micro F1 从 0.690 降至 0.150/0.075，而高亮贡献 +0.302、颜色 +0.262；建议在 OOXML 解析阶段提取 highlight/color
  属性并转为显式标记（如 `<highlight>...</highlight>` 或文字说明），而不是只输出纯文本。

  - 不要过度依赖粗体、斜体等常见格式：本文中 bold/italic/monospace/strikethrough 对义务抽取增益均在 ±0.003 内，真正有效的是高亮和颜色；在合同、政策、促销规则等业务文档中应重新权衡格式线索的优先级。

  - 把格式线索显式键入提示比仅隐式保留更强：预注册测试显示额外 +0.085 F1（p=0.049），可在 ingestion 层自动生成“原文中以下内容被高亮/着色，可能为关键义务”的上下文提示，代价低且可量化。

  - 用 OOXML 属性做确定性 ground truth 匹配器，无需 LLM 裁判即可监控解析器对格式信息的保真度，适合持续集成评测，避免文档解析中静默退化。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

## 动机
企业 Agent 依赖摄取层将 Word/PDF 转成 tokens 后理解文档。但常见转换器只恢复文本、表格和结构，作者通过文字外观（高亮、颜色等）编码的语义信息被静默丢弃，导致 Agent 对关键义务自信犯错而非可见缺漏。

## 方法
构建自 76 份真实政策文档的任务：恢复作者特别标出的要求，使用文件自身 OOXML 属性做确定性匹配器评分，避免 LLM 裁判。对比格式盲摄取（docling、纯文本）与保留格式的基线，跨六个模型（五款 Claude 不同档位和 GPT-5.6）验证。通过 span-level leave-one-out 定位单个格式线索贡献，在 PDF 上重复实验，并统计 6,460 份文档中颜色/高亮出现率。用渲染页面图像独立验证标签（κ=0.72），并测量仅靠措辞的 AUC 上限（0.664）。

## 关键结果
格式盲摄取使 micro F1 从 0.690 暴跌至 0.150（docling）和 0.075（纯文本）；docling 在作者未标记要求上的误报率是基线的四倍。高亮贡献 +0.302，颜色贡献 +0.262，均 Holm-adjusted p<1e-4；粗体、斜体、等宽、删除线几乎无影响。32.8% 的文档包含刻意颜色或高亮，其中 10.3% 出现在义务类内容。显式把线索键入给 Agent 比仅保留格式额外 +0.085（p=0.049）。
