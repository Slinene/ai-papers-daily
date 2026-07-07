---
title: 'DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive
  Generation'
title_zh: DSpark：半自回归生成与置信调度推测解码
authors:
- Xin Cheng
- Xingkai Yu
- Chenze Shao
- Jiashi Li
- Yunfan Xiong
- Yi Qian
- Jiaqi Zhu
- Shirong Ma
- Xiaokang Zhang
- Jiasheng Ye
affiliations:
- Peking University
- DeepSeek-AI
arxiv_id: '2607.05147'
url: https://arxiv.org/abs/2607.05147
pdf_url: https://arxiv.org/pdf/2607.05147
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: 推测解码 · 半自回归 · 置信调度
tags:
- Speculative Decoding
- Semi-Autoregressive
- Confidence Scheduling
- LLM Inference
- Throughput Optimization
- DeepSeek
one_liner: 半自回归架构缓解并行预测因果衰减，置信调度动态剪枝低信心后缀，系统吞吐与交互速度显著提升
practical_value: '- **半自回归草稿架构**：在并行骨干后追加轻量马尔可夫/RNN头，仅引入极低延迟开销（<2%），大幅缓解并行预测的多模态冲突和接受率衰减。类似思路可用于电商搜索推荐中的对话助手、自动回复生成等低延迟场景，在保持并行速度的同时提升生成连贯性。

  - **置信度驱动的动态调度**：通过置信头估计前缀生存概率，结合硬件吞吐曲线动态选择验证长度，让高并发下自动回收低信心token的计算资源。在推荐系统的消息推送、搜索词改写等LLM调用中，可借鉴此机制，根据服务负载动态调整生成预算，避免盲目固定长度造成的容量浪费。

  - **异步调度与核函数解耦**：生产部署中采用历史预测近似当前容量，延迟调度与CUDA图回放兼容，同时通过展平序列与标记张量实现变长验证的高效执行。工程上为推荐系统的LLM推理服务（如推荐理由生成、用户查询补全）提供了可行的低开销动态批处理方案。

  - **顺序温度缩放校准**：对累积置信度进行逐位置校准，使生存概率估计更准确，支撑硬件感知调度。该校准方法可直接复用于需要可靠概率输出的在线调度场景，如流量分发、个性化推送的置信过滤。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM推理的自回归特性导致高延迟和低GPU利用率，推测解码通过并行验证加速，但现有并行草稿模型因独立预测造成接受率快速衰减，且固定验证长度在高低负载下均无法高效利用资源，亟需兼顾草稿质量和系统吞吐的解法。

**方法**：
- **半自回归生成**：并行骨干（DFlash）一次预测所有草稿位置，追加极轻量的序列模块（马尔可夫头或RNN头）从左到右采样，引入token间依赖，缓解多模态碰撞与后缀衰减。`𝑇draft` 仍近乎与块大小无关，仅增加微秒级延迟。
- **置信调度验证**：附加置信头预测每一步的条件接受概率 `𝑐𝑘`，联合累积为前缀生存概率；硬件感知调度器以系统步骤吞吐 `SPS(𝐵)` 为代价表，贪婪选择全局最高生存概率的草稿 token 组成动态验证长度，最大化总吞吐 `Θ=𝜏·SPS(𝐵)`；并用顺序温度缩放校准累积估计。部署时采用异步调度与核函数解耦，兼容ZOS和变长计算。

**关键实验**：
- 离线：在Qwen3-4B/8B/14B、Gemma4-12B目标模型上，数学/代码/聊天任务平均接受长度较Eagle3提升约30%，较DFlash提升约18%。位置级分析表明初始位并行容量优势巨大，半自回归有效保持尾部接受率。
- 在线：部署于DeepSeek-V4生产系统，对比MTP-1基线，在匹配吞吐下V4-Flash生成速度提升60%–85%，V4-Pro提升57%–78%；严格SLA（120/50 TPS）下基线吞吐崩溃，DSpark仍维持有效容量，显著外推交互性 Pareto 前沿。

**核心结论**：并行草稿骨干的高容量与轻量串行依赖注入的结合，让推测解码首次在真实大流量服务中实现既不牺牲吞吐又显著加速交互，动态置信调度是释放这一潜力的关键。
