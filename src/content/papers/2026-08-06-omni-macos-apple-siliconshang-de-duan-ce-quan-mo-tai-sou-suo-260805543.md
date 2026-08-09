---
title: 'omni-macos: On-Device Omni-Modal Search on Apple Silicon'
title_zh: omni-macos：Apple Silicon上的端侧全模态搜索引擎
authors:
- Han Xiao
affiliations:
- Jina AI by Elastic
arxiv_id: '2608.05543'
url: https://arxiv.org/abs/2608.05543
pdf_url: https://arxiv.org/pdf/2608.05543
published: '2026-08-06'
collected: '2026-08-09'
category: Multimodal
direction: 设备端全模态隐私搜索
tags:
- on-device
- multimodal search
- vector indexing
- incremental encoding
- quantization
- privacy
one_liner: 在Mac本地运行全模态语义搜索引擎，数据不出设备，通过内存预算与增量索引保证实时交互。
practical_value: '- 隐私保护设备端索引：可将用户行为数据转为本地向量，构建个性化推荐索引而无需上传，适合电商用户端商品偏好建模。

  - 增量更新与内存预算：在推荐系统中对商品库动态变化采用只重编码差异块的策略，降低实时索引成本；设定内存上限防止服务抖动，可借鉴到大规模向量召回模块。

  - 量化+精确重排序：先用低精度向量快速检索，再用原始向量对 top-K 重排，平衡效率与精度，可直接用于推荐召回的二阶段优化。

  - 统一多模态嵌入空间：将商品标题、图片、描述嵌入同一语义空间，支持跨模态搜索与推荐，尤其适合多媒体商品信息处理。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有语义搜索依赖服务端，需上传文件和查询，隐私风险高。omni-macos 将全模态搜索引擎完全部署在用户 Mac 本地，文件、查询、向量均不外传，解决隐私痛点，同时需应对设备资源限制和实时性挑战。

**方法关键点**：
- 单进程集成编码器、索引与存储，利用 Apple Silicon 统一内存架构。
- 用户设置内存预算，系统动态分配：后台索引器持续监控文件变更，仅对编辑过的块增量重编码，避免全量重建。
- 交互搜索时，将大量文本拆分为小批次送 GPU 编码，防止界面卡顿；维护量化索引副本用于快速候选召回，再用精确向量对少量结果重排序，保证精度。
- 所有组件遵循同一内存上限，通过分配器统一控制，避免争抢资源。

**关键结果**：在 5 款不同配置的 Mac 上测试（GPU 核心数跨度 8 倍、内存跨度 32 倍），验证了机制有效性。系统在用户编辑同时保持搜索响应流畅，量化索引带来的精度损失可被重排序弥补，内存预算严格控制了最大资源占用。
