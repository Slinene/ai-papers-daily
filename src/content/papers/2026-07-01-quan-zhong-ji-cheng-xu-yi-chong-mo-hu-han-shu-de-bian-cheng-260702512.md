---
title: 'Program-as-Weights: A Programming Paradigm for Fuzzy Functions'
title_zh: 权重即程序：一种模糊函数的编程范式
authors:
- Wentao Zhang
- Liliana Hotsko
- Woojeong Kim
- Pengyu Nie
- Stuart Shieber
- Yuntian Deng
affiliations:
- University of Waterloo
- Cornell University
- Harvard University
arxiv_id: '2607.02512'
url: https://arxiv.org/abs/2607.02512
pdf_url: https://arxiv.org/pdf/2607.02512
published: '2026-07-01'
collected: '2026-07-04'
category: LLM
direction: 编译器-解释器范式 · 模糊函数编译为 LoRA
tags:
- Program-as-Weights
- Fuzzy Functions
- LoRA
- Hypernetwork
- Model Compilation
- On-device LLM
one_liner: 用 4B 编译器将模糊任务规格编译成小 LoRA 程序，0.6B 解释器执行可超 32B 模型提示且省 50× 内存
practical_value: '- **模糊函数本地化**：将需要反复调用的模糊判断（如意图分类、文案审核、查询质量过滤）编译为 0.6B + LoRA 小程序，在本地
  CPU/GPU 上以 30 tok/s 运行，摆脱对 API 的依赖，成本与延迟骤降。

  - **编译器-解释器架构**：借鉴其“编译一次，本地无限执行”的模式，对固定模糊任务（如搜索意图重排的打分函数）可事先用 4B 模型生成 LoRA 权重，后续调用只需加载
  23MB 适配器，无需远程调用。

  - **伪程序去噪**：他们在规格输入阶段用 4B 编译器将噪声规格重述为清晰伪程序，再喂给小解释器，大幅提升小模型对错别字、口语化规格的鲁棒性。在用户输入的任务描述不规范时可采用类似预处理。

  - **工具调用管道**：论文中将多个 PAW 程序串联实现复杂的工具路由（93% 准确率），可类比推荐系统中的多步预处理或过滤管线，每个环节编译为独立 LoRA，按需组合，灵活升级。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
日常开发中大量模糊任务（日志过滤、格式修复、搜索意图排序）无法用规则精确描述，常调用大模型 API，导致成本高、延迟大且不可复现。作者提出将模糊函数编译为小型神经程序，本地执行，把大模型的角色从“逐次求解”转变为“一次性工具构建”。

**方法关键点**  
- **编译器–解释器架构**：一个 4B 的 Qwen3 编译器将自然语言任务规格编译成混合程序，再由一个冻结的 0.6B 解释器加载执行。  
- **混合程序**：离散部分为“伪程序”（任务重述+示例），由现成 4B 模型生成，无需训练；连续部分为 LoRA 适配器，由经过训练的同尺寸 LoRA 编译器从自身隐藏态映射得到。  
- **LoRA 生成**：编译器在固定前缀令牌位置的隐藏态经平均池化后，通过 MLP 投影为混合系数，组合共享基矩阵得到 LoRA 权重，注入解释器所有注意力与 MLP 层。  
- **训练数据**：构建 FuzzyBench，含 1000 万条 (规格, 输入, 输出) 三元组，覆盖 800+ 类模糊任务，从文本处理到工具调用；用 GPT-5.2 自动生成，测试集经双模型一致性验证。  
- **训练目标**：只优化 LoRA 编译器，损失为解释器在生成目标输出时的对数似然，梯度穿过冻结解释器回传。

**关键实验**  
- 在 FuzzyBench 上，0.6B 解释器 + PAW 达到 73.78% 精确匹配，超过 32B 直接提示（68.70%），而推理内存仅约 1.2 GB（约为 32B 的 1/50）。  
- 量化后（Q6_K + Q4_0 LoRA）精度无损，在 MacBook M3 上生成 30 tokens/s，冷启动 0.48s。  
- 替换编译器为视觉模型后，同一解释器可处理图像模糊任务，在三个图表任务上超过 4B VLM 基线。  
- 五个案例验证：日志监控、意图导航、语义重排、工具调用（93%）、多语言猜词游戏。
