---
title: Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational
  Music Recommendation
title_zh: 对话式音乐推荐的多模态语义扩展与受限LLM重排
authors:
- Naman Garg
- Sarika Jain
- George Fazekas
affiliations:
- National Institute of Technology Kurukshetra
- Queen Mary University of London
arxiv_id: '2608.23484'
url: https://arxiv.org/abs/2608.23484
pdf_url: https://arxiv.org/pdf/2608.23484
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 多模态检索融合与LLM约束重排的对话推荐
tags:
- Conversational Recommendation
- Multi-Modal Retrieval
- Reciprocal Rank Fusion
- LLM Reranking
- RAG
- Music Recommendation
one_liner: 三阶段多模态检索+轻量重排+LLM persona生成，融合7路embedding与BM25，Blind B综合0.3213，发现LLM注入仅在窄范围有效
practical_value: '- 多召回通道融合：采用加权RRF替代简单线性打分，并用差分进化在验证集上自动搜索权重；本工作MRR +19.5%，且行为/协同信号权重可远高于文本语义信号。电商搜索/推荐可对CF、语义embedding、BM25、属性match分别召回后加权RRF融合，离线调权。

  - LLM二次排序/改写采用“保守注入”：仅在正确item已部分出现但排名不足（例如top20内1-5条）时触发LLM干预；本工作无差别注入54会话导致nDCG
  -18.9%，而仅9会话介入得到+0.8%。工程上应设置严格触发条件并灰度验证。

  - 生成阶段用RAG绑定真实候选并强制提及，结合多persona轮转与presence/frequency penalty，可提升Distinct-2和Judge、减少模板重复与幻觉。电商导购/push文案可借鉴：让LLM从检索结果中选2个真实商品解释，并用不同人设轮转。

  - 端到端部署一致性：离线验证过的LLM与reranker不要轻易为降本替换；本工作GPT-4.1改GPT-4o-mini使响应质量损失约0.176复合分，省略reranker再损失约0.096。上线前需评估复合指标对组件替换的敏感度。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：对话推荐系统需要在多轮交互中综合理解偏好、检索相关物品并生成自然语言解释，但多模态信号覆盖、LLM幻觉边界与复合指标权衡使其非常脆弱。TalkPlayData 挑战（47,071 tracks，约15k会话）提供可量化测试场景。

方法关键点：
- 三阶段流水线：多模态检索、轻量重排、响应生成。
- 检索融合9路信号：track/user CF-BPR、Qwen3 metadata/lyrics/attributes、CLAP audio、SigLIP visual、BM25、artist substring match，使用加权RRF（k=60）融合；权重在500会话Devset上用差分进化搜索，MRR +19.5%。会话级 centroid 用历史track embedding 按 γ=0.85 指数衰减构建，冷启动用BM25 top5做PRF种子。
- 重排：历史过滤、流行度平滑、目录多样性惩罚为提交配置；开发未部署组件包括 album continuation、XGBoost LambdaMART、保守GPT注入。
- 响应生成：GPT-4o-mini十种persona轮转，RAG绑定top5检索结果并强制提及2个真实track，生成参数 temperature=1.0、presence/frequency penalty 调优以提升Distinct-2。

关键结果：
- 官方Blind B 综合0.3213（nDCG 0.232, Judge 2.60, LD 0.821, CD 0.031），排名37。
- Blind A 消融：BM25+CF 0.085 -> +多模态 centroid 0.120 (+41%) -> +artist substring bonus 0.277 (+131%) -> +album continuation 0.388 (+40%) -> +XGBoost 0.466 (+20%) -> +保守GPT注入（9会话）0.469 (+0.8%)。
- 关键敏感性：LLM注入仅在“目标artist已有1-5条在top20”的9个会话中带来+0.8%；无差别注入54个会话导致nDCG -18.9%。GPT-4.1 Mirroring prompt在开发集曾取得复合0.64，但由于成本未部署，部署简化与分布差异解释Blind B gap。

最值得记住的一句话：LLM rerank/injection 的收益高度依赖作用范围——“正确的item已部分出现在top-k但排名不足”才是安全区间，无差别LLM重排会因位置偏差摧毁已有排序。
