---
title: 'Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents,
  with an Affine-Typed Rust Mitigation as a Case Study'
title_zh: Token Budgets：63起LLM Agent预算超支事件实证目录与Rust仿射类型缓解
authors:
- Sajjad Khan
arxiv_id: '2606.04056'
url: https://arxiv.org/abs/2606.04056
pdf_url: https://arxiv.org/pdf/2606.04056
published: '2026-06-01'
collected: '2026-06-05'
category: Agent
direction: Agent 预算控制与类型安全
tags:
- LLM-Agent
- Token Budget
- Rust
- Affine Types
- Incident Catalog
- Cost Control
one_liner: 构建63起LLM Agent预算超支事件分类目录，并利用Rust仿射类型实现编译时防超支的token-budgets库
practical_value: '- **编译时防止预算误操作**：借鉴Rust仿射类型，将预算设计为不可克隆、不可别名、用后即焚（affine ownership），在编译期杜绝克隆、双重花费、use-after-delegation等错误。在Python/TypeScript等无所有权机制的语言中，可通过类型系统模拟（如unique指针、移动语义）或运行时静态分析，减少因operator误用导致的预算泄漏。

  - **多Agent委托场景的预算安全**：多个Agent委托任务时，预算传递若用简单计数器，并发下易重复扣除。直接迁移Rust的借用检查思想，对budget对象采用编译时唯一引用传递，避免运行时race
  condition。若不能换语言，可在框架层面实现类似“移动语义”的wrapper，确保同一时刻只有一个owner持有budget。

  - **事件分类指导防御手段设计**：论文给出八类预算超支故障模式（如retry-loop无限重试、无上限API调用、并发委托导致重复扣除等），可直接用于电商或推荐系统中Agent链路的审计清单，针对不同模式提前设置编译器检查或runtime
  guard。

  - **轻量级实现可嵌入现有Agent框架**：1,180行Rust代码（无unsafe）可作为库引入，或者将其理念转化为Lua/Python等胶水语言的类型约束层，为预算敏感场景提供零成本保证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent预算超支是生产环境中的常见故障，单次retry循环可能产生数千美元损失。现有解决方案多依赖运行时ad-hoc包装器，缺乏类型系统级保障，无法防止预算别名、双重花费、use-after-delegation等错误。

**方法**：
1. 构建一份包含63起已确认生产事件的经验目录，来自21个编排框架（2023-2026），每起事件均引用GitHub issue与损失金额。事件被归入8大故障模式（Cohen's κ=0.837），并附47条补充条目。
2. 基于该分类目录，实现名为token-budgets的Rust crate（1,180行，无unsafe），利用仿射所有权：预算对象不可克隆、不可别名、移动后失效，使得克隆、双重花费、已委托后继续使用均在编译时报错。金额封顶仍依赖运行时算术与估价假设，但仿射层确保该算术不可旁路。

**结果**：单Agent场景下，4行Python计数器同样可实现0/30不超支，区分度在于多Agent委托压力。11起事件中的委托扇出竞态在Rust中直接被借用检查器拒绝，而asyncio实现则30/30超支，三种改良方案为0/30。跨五个运行时、三家提供商、温度分层测试（N=160）中，零封顶违反与零误拒绝。静态预留时开销4-6x，自适应则降至2.11x。
