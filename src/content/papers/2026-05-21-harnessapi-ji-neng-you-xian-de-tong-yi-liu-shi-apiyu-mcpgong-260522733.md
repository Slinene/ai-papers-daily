---
title: 'HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools'
title_zh: HarnessAPI：技能优先的统一流式API与MCP工具框架
authors:
- Edwin Jose
affiliations:
- Western Michigan University
arxiv_id: '2605.22733'
url: https://arxiv.org/abs/2605.22733
pdf_url: https://arxiv.org/pdf/2605.22733
published: '2026-05-21'
collected: '2026-05-23'
category: Agent
direction: Agent 工具部署与统一API框架
tags:
- MCP
- FastAPI
- Streaming API
- Tool Use
- Boilerplate Reduction
- Code Generation
one_liner: 从单一技能文件夹自动派生流式HTTP端点、OpenAPI UI和MCP工具，减少74%样板代码
practical_value: '- **单源技能定义**：借鉴“技能文件夹 + Pydantic schema”模式，为每个业务能力（如推荐召回、订单查询）设置单一事实源，自动导出HTTP端点和MCP工具，避免双重维护，降低Agent工具与人工接口的偏离风险。

  - **双模响应协商**：同一handler通过Content-Type自动切换SSE流式与JSON响应，适合生成式推荐中流式生成结果与常规RPC调用，无需重写业务逻辑。

  - **全生态继承**：HarnessAPI子类化FastAPI，可直接复用现有中间件、依赖注入、鉴权和部署方案，工程落地成本低，适合在已有FastAPI服务上快速增加MCP工具暴露。

  - **动态代码生成保型**：通过动态生成模块确保Pydantic类型注解在MCP工具层正确传递，解决闭包注册时的类型丢失问题，对需要强类型校验的Agent工具链（如电商API参数校验）至关重要。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM工具通常需要同时暴露为HTTP端点（供人类客户端和CI）和MCP工具（供Agent运行时），两者共享业务逻辑但路由、验证、序列化、流式、模式维护等代码重复且易漂移，手动维护双栈（FastAPI + FastMCP）带来大量样板代码。

**方法**：提出HarnessAPI框架，以“技能文件夹”为单一事实源（包含handler.py和Pydantic schemas），自动派生流式HTTP端点（SSE）、OpenAPI/Swagger交互文档和零配置MCP工具，单进程同时服务。通过双模式内容协商，同一handler可处理SSE流式与JSON请求，无需修改逻辑。利用动态代码生成解决FastMCP从闭包注册时无法正确推断Pydantic类型注解的技术限制，确保MCP工具层类型安全。

**结果**：在6个代表性技能上，HarnessAPI将面向框架的样板代码减少74%（cloc度量），同时完全继承FastAPI中间件、依赖注入和部署生态。代码已开源，可通过pip安装。
