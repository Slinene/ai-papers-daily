---
title: 'LazyWeights: Decode-on-Demand Edge LLMs'
title_zh: LazyWeights：边缘大模型的按需解码权重压缩
authors:
- Arnab Sanyal
- Gourav Datta
- Sandeep P. Chinchali
affiliations:
- The University of Texas at Austin
- Case Western Reserve University
arxiv_id: '2611.17108'
url: https://arxiv.org/abs/2611.17108
pdf_url: https://arxiv.org/pdf/2611.17108
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: 边缘 LLM 权重压缩与按需解码
tags:
- Edge LLM
- Huffman coding
- Quantization
- Lossless compression
- On-device inference
one_liner: 通过可压缩 GPTQ + Huffman 无损编码 + 按需解码硬件，在保持 GPU kernel 不变下将边缘 LLM 体积最多减 31.4%
  并降低延迟/能耗
practical_value: '- 借鉴「量化 + 熵编码」联合优化：在量化校准阶段让 GPTQ 知道后续有 Huffman 无损编码，有偏选择更可压缩的码本，在同等
  perplexity 预算下额外缩小模型体积。对需要把推荐/Agent 模型部署到端侧的场景，这比单纯降低 bit-width 更划算。

  - 系统架构可复用：在现有推理栈（llama.cpp / TensorRT-LLM）基础上，保持 GPU kernel 不变，只在 DRAM 与 L2 之间插入按需解码单元，用
  Huffman 编码减少 DRAM 带宽占用。适合边缘 Agent 或本地化搜索推荐服务，降低传输能耗。

  - 收益量化参考：论文结果显示 5.7–31.4% 体积缩减、Orin 下 36% 延迟/38% 能耗改善（speculation 下 54%/44%）、CPU
  下 53–57% 能耗节省。可作为是否引入类似压缩/硬件解码器的 ROI 评估基准。

  - 如果业务不跑边缘设备，核心价值在于细粒度 quant + 无损压缩兼容现有 kernel，可能主要适合权重存储/加载优化而非线上延迟；需要额外评估解码器面积与吞吐匹配。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：边缘设备内存容量与带宽决定能跑哪些 LLM，现有部署量化格式（GPTQ/AWQ/llama.cpp K/I-quants）对每个整数码固定位数，但权重分布不均匀，熵低于 bit-width，浪费带宽与存储。

**方法**：保留现有量化格式，但修改 GPTQ 量化目标，让码本更可压缩；对交错 lane 使用 Huffman 无损编码，将解码器放在 DRAM 与 L2 之间按需解码，因此 GPU 计算 kernel 无需改动，DRAM 只传输编码后的字节。

**关键结果**：在 1% 和 3.5% perplexity 预算下，Phi-3-mini、Mistral-7B、SmolLM-1.7B 编码后体积比最佳 llama.cpp 格式小 5.7–31.4%。在 Jetson Orin 上，0.21 mm² 7nm ASIC 解码器使每 token 延迟/能耗最多降低 36%/38%，配合 prompt-lookup speculation 达到 54%/44%；在 Jetson Nano 上，相比 CPU llama.cpp 推理时间减少 58–64%，能耗降低 53–57%，流式 Mistral-7B 在 3.89 bits per weight 下快 6.6 倍。
