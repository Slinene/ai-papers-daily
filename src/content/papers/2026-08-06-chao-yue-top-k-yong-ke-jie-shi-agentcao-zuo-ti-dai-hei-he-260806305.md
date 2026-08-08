---
title: 'Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations'
title_zh: 超越Top-K：用可解释Agent操作替代黑盒检索
authors:
- Sagar Tamang
- Ayush Vyas
- Tabarakul Hazarika
affiliations:
- Indian Institute of Technology Patna
- TwoSpoon
arxiv_id: '2608.06305'
url: https://arxiv.org/abs/2608.06305
pdf_url: https://arxiv.org/pdf/2608.06305
published: '2026-08-06'
collected: '2026-08-08'
category: Agent
direction: Agent驱动的结构化文档免嵌入检索
tags:
- RAG
- Agent
- Embedding-free retrieval
- Structured documents
- Model Context Protocol
- Interpretability
one_liner: 提出READ，一种免嵌入的agentic检索方法，在表格密集文档上准确率远超密集检索且可审计
practical_value: '- 对于包含大量表格/结构化字段的长文档（如商品参数、金融报告），分块嵌入检索常会破坏数值与单位/上下文的关联，可改用Agent按需读取原始文档，通过归一化词法搜索和结构导航确保精确提取。

  - 在检索环节中，嵌入并非万能：实验表明BM25与READ效果相当，因此对于数值密集场景，优先考虑强词法匹配而非密集向量。

  - 将检索接口设计为可审计的步骤序列（如MCP暴露工具），便于调试和信任，尤其适合高风险业务场景（如合规、财务审查）。

  - 若业务中需构建问答系统处理半结构化长文本，可借鉴READ的“保持文档完整、让Agent选择读哪里”的理念，避免提前分块带来的信息断裂。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：金融报表、审计报告等长文档中，86.8%内容为表格行，数值与表头（单位、财年）紧密关联，但传统RAG的分块嵌入检索会割裂这种关联——即使针对表格优化分块，仍有27-30%的数值块丢失财年信息。这导致检索错误可能高达两个数量级。

**方法**：提出READ（Reliable Embedding-free Agentic Document-search），一个Agent通过三个确定性操作与原始文档交互：归一化词法搜索（grep）、结构导航（outline，获取标题和行号）、有界跨度读取（read，返回指定行范围）。这些操作通过Model Context Protocol暴露，每一步生成可审计的引用行号，轨迹可复现。Agent自行决定下一步读什么，而非依赖黑盒相似度分数。

**结果**：在780页政府财务报告的51个验证问题上，READ准确率达58.8%，密集检索基线仅15.7%（p<0.001）。经调整分块大小和检索深度，密集检索最优为35.3%，READ仍领先23.5个百分点（p=0.017）。与BM25的46.4%无统计显著差异，说明优势源于免嵌入检索，而非迭代或Agent架构本身。
