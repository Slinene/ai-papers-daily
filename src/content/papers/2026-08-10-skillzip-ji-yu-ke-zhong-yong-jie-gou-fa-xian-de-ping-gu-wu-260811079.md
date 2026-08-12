---
title: 'SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering
  Reusable Structure'
title_zh: SkillZip：基于可重用结构发现的评估无关技能压缩
authors:
- Xiaofan Bai
- Hongqiang Lin
- Chao Liu
- Yantao Zhang
- Xuan Jin
- Xipeng Cao
- Yuhong Li
affiliations:
- Alibaba Group
- Zhejiang University
- Duke University
arxiv_id: '2608.11079'
url: https://arxiv.org/abs/2608.11079
pdf_url: https://arxiv.org/pdf/2608.11079
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: Agent 技能压缩 · 评估无关结构化精益
tags:
- Skill Compression
- Self-Evolving Agents
- Prompt Compression
- Minimum Description Length
- Structured Contracts
- Zip-on-Write
one_liner: 用“一次性解释，多处引用”原则，在不依赖下游评估的条件下压缩自进化Agent的冗余技能文本。
practical_value: ' - **长期维护的Agent系统可直接套用**：将Agent技能视为类型化合约（接口、工作流、工具协议、规则、输出模式），通过共享规则、上提公共规则、工作流复用和异常编码实现文本压缩，减少每次调用的上下文token成本。

  - **避免评估集过拟合的压缩范式**：SkillZip 完全不依赖任务实例、奖励或验证器，仅从技能自身结构提取合约并强制覆盖所有要求，可杜绝因评估集偏差导致的技能退化，适合需要频繁更新的推荐/搜索Agent。

  - **增量压缩模式适于在线进化系统**：Zip-on-Write 在Agent每次自我进化时仅对比受影响局部，以ABSORB/REFINE/EXTEND/REFACTOR四类操作更新合约，零重放任务，可嵌入在线学习推荐Agent的实时优化流程。

  - **最小描述长度( MDL )可直接指导提示精简**：公式(4)定义的“最短忠实解释”目标，以及计算收益阈值（如规则提升、工作流复用）的显式条件，可迁移到对话策略、Query改写等复杂提示的自动去重与结构化重构中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：自进化Agent通过追加成功/失败经验累积技能，导致文本膨胀（5.2倍以上），但实质性的新需求已饱和。冗余以重复规则、重复工作流、多层异常的形式存在，既增加上下文成本，又模糊核心指令。现有提示压缩基于查询或答案条件测度重要性，不适合可跨任务复用的技能；评估引导压缩依赖任务采样，易引入偏差且成本高。为此，论文提出评估无关的压缩方法SkillZip，仅从技能自身结构出发做精简。

**方法关键点**：
- **技能作为类型化合约**：将技能解析为接口、工作流、工具协议、规则、输出合同和证据六类单元，保留来源锚定。不确定片段锁定为残留，禁止删除。
- **最短忠实解释目标**：基于MDL原则，最小化合约库与残留的渲染token成本，且硬性要求每个提取出的规范单元必须被覆盖（命题IV.1，推论IV.2）。
- **四类可重用结构**：等价要求合并、跨作用域规则提升、重复工作流提取为共享过程、关联从句写成共同规则+异常差量，每类决策均有明确的长度阈值条件。
- **两种压缩模式**：One-shot模式通过一次结构化抽取+确定式优化实现批量压缩；Zip-on-Write模式在自进化过程中就地吸收补丁，仅进行局部类型‑作用域检索与更新，定期全局重排以回收跨补丁重用。压缩过程无任务、奖励或轨迹，确定性渲染为纯文本技能文件。

**关键结果**：在BFCL-v4、LiveMath、SpreadsheetBench上，以Qwen3.7-Max/Qwen3.6-Plus/Kimi K2.6为Agent骨干，SkillZip压缩率达27.1%–36.9%（平均31.2%），性能不降反微升（平均0.577 vs. 进化技能0.570），且显著优于SkillReducer（平均压缩9.2%，性能0.544）。一次性压缩速度比SkillReducer快3.5倍，不需任何任务Rollout。跨模型泛化保持率0.97（LiveMath），Zip-on-Write持续压缩可将技能长度保持在1.6–1.9倍种子长度，且从进化一开始启用效果最佳，不会牺牲准确率。

**最值得记住的一句话**：自进化Agent技能膨胀的根源是“表象重复”而非“内容无用”，因此应通过结构化合约共享隐性相同点，而非仅仅删减文本。
