---
title: 'BaKron: Efficient Quantization with Kronecker-Factored Hessians'
title_zh: BaKron：基于Kronecker因式分解Hessian的高效量化加速
authors:
- Johann Birnick
- Rayan Saab
affiliations:
- University of California San Diego
- Department of Mathematics
- HDSI
arxiv_id: '2608.06291'
url: https://arxiv.org/abs/2608.06291
pdf_url: https://arxiv.org/pdf/2608.06291
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 神经网络量化加速
tags:
- quantization
- Kronecker-factored Hessian
- adaptive rounding
- GPTQ
- model compression
- efficient inference
one_liner: 利用双侧Kronecker-factored Hessian信息加速自适应舍入量化，复杂度与GPTQ同为立方级但精度更高
practical_value: '- 在电商/推荐系统中部署大模型（如LLM-based推荐）时，可尝试用双侧曲率信息（输出坐标相关性）替代GPTQ仅依赖输入激活的量化方式，提升量化后模型精度。

  - BaKron的递归分治与反斜对角并行策略可借鉴到自定义量化优化器中，将全矩阵量化成本从O(n⁴)降到O(n³)，尤其适用于推荐模型中中等规模投影层的高效压缩。

  - 方法对基础量化器（如四舍五入、格子量化）和Hessian估计器解耦，允许在工程中灵活替换更精确的曲率近似（如KFAC），平衡精度与计算开销。

  - 若直接在向量化权重上应用GPTQ式自适应舍入计算瓶颈过高，可采用BaKron的逐行/列交替更新框架，同时保持并行可行性，适配推荐系统在线serving的延迟要求。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：GPTQ等自适应舍入量化利用输入激活的Gram矩阵作为单侧曲率信息，忽略了输出维度的相关性；双侧Kronecker-factored Hessian能捕获输入-输出联合曲率，但直接扩展到向量化权重（O(m²n²)代价）不可行。  
**方法**：在BoA/YAQA的双侧自适应舍入框架下，提出BaKron。核心是反斜对角并行（anti-diagonal parallelism）与递归分治（divide-and-conquer），将原本需要O(m²n²)工作的全矩阵量化分解为O(m+n)个顺序步骤，总复杂度降至O(mn(m+n))，与GPTQ的立方级代价相当，同时保留了更丰富的二阶几何信息。求解器对底层量化方式（舍入策略）和Hessian近似方法解耦，可灵活组合。  
**结果**：实验验证了BaKron在使用不同Hessian估计（如经验Fisher、KFAC）下的量化效果，在保持与GPTQ相近效率的同时，因利用输出相关性而取得更优的扰动-量化精度权衡。
