---
title: 'Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation
  in Long-Video MLLMs'
title_zh: 选择、压缩、再投资：长视频多模态大模型视觉Token分配的控制研究
authors:
- Prakhar Khatri
affiliations:
- Independent Researcher
arxiv_id: '2609.03820'
url: https://arxiv.org/abs/2609.03820
pdf_url: https://arxiv.org/pdf/2609.03820
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 长视频MLLM视觉Token分配优化
tags:
- Visual Token Allocation
- Long-Video MLLM
- Frame Selection
- Orthogonal Matching Pursuit
- Token Compression
- Controlled Study
one_liner: 控制变量实验表明帧选择是长视频理解最大杠杆，经典OMP算法与专用选择器性能相当
practical_value: '- **预算固定的优化思路可直接迁移到多模态推荐/广告素材理解**：若系统只能用固定数量的视频帧或图像Token表示商品视频/广告创意，优先投资帧选择（比均匀采样提升显著），再考虑空间压缩，并把压缩节省的Token用于增加采样帧数，两步结合可带来2-3个点准确率提升。

  - **OMP等经典稀疏近似算法可作为轻量、无训练的特征/帧选择器**：在视频理解、商品短视频标签抽取、直播切片推荐等场景，无需训练专用选择器，直接用OMP挑选最具信息量的帧或片段，能匹配甚至超过专用模型，工程实现成本极低。

  - **对多模态模型评测/迭代：务必在同一统一框架内做控制变量**。论文发现相同规则在不同harness间有0.07-3.74点差距，自己的AKS基线也有实现bug，说明跨论文比较或直接套用他人结果风险高；业务中应构建内部统一的视觉Token分配评测管道，逐步替换单个变量（选择、压缩、分辨率）以定位真实收益。

  - **压缩必须配合再投资才有效**：单独压缩帧分辨率几乎是免费的（损失≤0.44点），但如果不把节省的Token花到更多帧上，就没有精度收益；该结论可指导资源受限场景下的多模态特征预算分配策略。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长视频MLLM无法处理全部帧（1小时@1fps=3600帧），系统只能保留少量固定帧。帧选择规则不是预处理细节，而是最紧的瓶颈。已发布的选择器因混改帧打分器、提示边界、分辨率策略和回答模型，难以公平比较。

**方法**：作者固定其他条件，逐一改变三个决策变量：帧选择、空间压缩、节省Token的再投资。在6种训练无关选择规则、3个长视频基准、2个回答模型上进行控制实验。

**关键结果**：
- 选择是最大杠杆：LongVideoBench的1小时组，8帧查询选择比16帧均匀采样高6.9分；经典OMP算法（未修改）在全部三个基准上与所有专用选择器持平或相差1分以内。
- 空间压缩几乎免费：固定时间戳下将每帧空间预算减半，最多损失0.44分。
- 再投资决定收益：将释放的Token用于双倍压缩帧（总成本不高于原始8帧），可再获2-3分提升；压缩只有在节省被再投资后才划算。
- 还发现AKS基线实现bug及两个harness运行相同规则在相同预算下存在0.07-3.74分差异，说明比较必须在统一评测框架内进行。
