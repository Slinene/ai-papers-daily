---
title: 'Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access
  to User''s Digital World'
title_zh: Claw-Anything：评测始终在线的个人助手在全访问数字世界中的能力
authors:
- Yusong Lin
- Xinyuan Liang
- Haiyang Wang
- Qipeng Gu
- Siqi Cheng
- Jiangui Chen
- Shuzhe Wu
- Feiyang Pan
- Lue Fan
- Sanyuan Zhao
affiliations:
- Beijing Institute of Technology
- Huawei Technologies Co., Ltd
- Peking University
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2605.26086'
url: https://arxiv.org/abs/2605.26086
pdf_url: https://arxiv.org/pdf/2605.26086
published: '2026-05-24'
collected: '2026-05-26'
category: Agent
direction: 个人助手评测 · 长周期上下文与主动式帮助
tags:
- personal assistant
- long-horizon event stream
- cross-service coordination
- multi-device interaction
- benchmark
- data generation
one_liner: 首次构造涵盖长周期事件流、跨服务依存、多设备协同的个人助手基准，暴露当前模型仅34.5% pass@1的差距，并利用数据生成管道将基线提升23.7%。
practical_value: '- **长周期事件流的模拟与注入**：电商/推荐系统可借鉴该方法，通过多轮事件注入自动生成用户长期行为序列（浏览、购买、比价），构造带有噪声和冲突的真实上下文，训练具备长期记忆的推荐Agent。

  - **跨服务信息协调与冲突消解**：用户画像往往分散在搜索、邮件、日历等多源数据中，存在不一致。该基准中的冲突检测与推理机制可直接用于推荐场景，提升Agent对跨渠道信息的一致性判断。

  - **自动化环境与任务生成管道**：从种子 persona 开始迭代合成数字世界+可执行验证器的方案，可作为生成式推荐中构造多样化训练环境的脚手架，实现大规模自动标注与
  curriculum 设计。

  - **主动式推荐评测的设计**：任务中包含无需显式请求的主动式协助，且当前模型在此项上得分很低（pass@1仅6.7%）。电商中可迁移其评估思路，衡量“何时推送推荐”的时机与上下文理解能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有个人助手评测仅暴露狭窄、静态的用户状态片段，忽略长周期活动历史、跨服务依赖和多设备交互，导致高估模型性能。为衡量始终在线的助手在真实数字世界中的能力，需要扩展上下文的广度与深度。  

**方法**  
- 构建 **Claw-Anything** 基准，沿三个维度扩展Agent可感知与操作的范围：
  1) **长周期事件流**：模拟三个月的系统与服务日志，提供细粒度历史记录；
  2) **多后端服务**：覆盖生活、工作等领域40+服务的持久状态与专用历史；
  3) **跨设备交互**：结合 CLI 和 GUI（Android）界面，要求跨设备协同完成任务。
- 开发**自动化数据生成管道**：从稀疏 persona 出发，通过多轮事件注入（含任务种子与噪声模板）逐步演化为复杂数字世界，捕获不一致信号与无关事件；在指定轮次快照环境并生成自然语言查询、可执行验证器与参考解；经自动过滤与人工核验最终产出200个评测任务和2000个训练环境。
- 评测同时覆盖**反应式与主动式任务**，后者要求Agent无明确请求时从上下文推断需求。

**实验结果**  
- GPT-5.5 仅获 **34.5% pass@1**，Claude Opus 4.7 仅 **31.8%**，远低于此前基准上的表现，说明更广的操作范围暴露了根本性缺陷。
- 用管道生成的1500条成功轨迹微调 Qwen3.5-27B，pass@1 从9.8%提升到 **33.5%（+23.7%）**，超越所有开源模型，证明管道具有可扩展的数据生产能力。
- 消融实验：移除事件流后成功率归零；跨服务工具掩码后同样归零；跨设备协同任务在仅 CLI 时基本不可解。上下文中噪声比例、仿真轮数和冲突数量增加均导致性能持续下降，验证了场景的真实难度。
- 主动任务 pass@1 仅 **6.7%**，表明时机判断与上下文推理仍是短板。  

**核心结论**  
更广的数字世界访问虽能解锁更多任务，但也急剧提升了上下文信噪分离、跨服务协调与执行精度的要求，当前最前沿模型与理想个人助手间存在显著差距，且该差距随上下文尺度增大而加剧。
