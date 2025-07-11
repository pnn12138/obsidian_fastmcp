
---

# Obsidian MCP Server

## 简介

**Obsidian MCP Server** 是一个基于 FastMCP 框架的 API 服务，专为远程自动化管理 Obsidian 笔记库而设计。它通过 HTTP API（SSE）方式，提供了文件管理、内容读写、全文搜索等常用操作，适合与 AI Agent、自动化脚本等集成。

---

## 主要特性

- **列出文件**：获取 Obsidian 笔记库（Vault）中的所有文件或指定目录下的文件。
- **读取文件内容**：获取指定文件的完整内容。
- **追加内容**：向指定文件末尾追加内容。
- **覆盖写入**：覆盖写入指定文件内容（如文件不存在则自动创建）。
- **删除文件**：删除指定文件。
- **全文搜索**：支持全文检索笔记内容，返回相关片段和文件名。
- **API 设计**：所有操作均以工具（tool）形式注册，便于 AI Agent 自动发现和调用。

---

## 快速启动

1. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

2. **配置环境变量**

   在根目录下创建 `.env` 文件，内容示例：

   ```
   OBSIDIAN_API_KEY=你的API密钥
   OBSIDIAN_PROTOCOL=https
   OBSIDIAN_HOST=127.0.0.1
   OBSIDIAN_PORT=27124
   OBSIDIAN_VERIFY_SSL=false
   ```

3. **启动服务**

   ```bash
   cd src
   python server.py
   ```

   默认监听 `127.0.0.1:8000`，使用 SSE 协议。

---

## 主要 API 工具说明

| 工具名             | 说明                     | 参数示例                      |
|--------------------|--------------------------|-------------------------------|
| list_files         | 列出所有文件             | 无                            |
| get_file_contents  | 获取文件内容             | filepath: str                 |
| append_content     | 追加内容到文件           | filepath: str, content: str   |
| put_content        | 覆盖写入文件内容         | filepath: str, content: str   |
| delete_file        | 删除文件                 | filepath: str                 |
| obsidian_search    | 全文搜索                 | query: str, context_length: int（可选） |

---

## 代码结构

- `src/server.py`：MCP 服务主入口，注册所有工具并启动服务。
- `src/obsidian.py`：Obsidian API 封装，负责与实际 Obsidian HTTP 服务通信。
- `requirements.txt`：依赖列表。

---

## 典型用例

- **AI Agent 自动化**：通过 SSE 协议与本服务对接，实现智能问答、自动笔记整理等。
- **远程脚本管理**：用 Python/JS 等脚本远程批量管理 Obsidian 文件。
- **知识库检索**：通过 `obsidian_search` 实现全文检索和上下文提取。

---

## 进阶说明

- 支持自定义扩展工具，只需在 `server.py` 中用 `@mcp.tool` 装饰器注册新函数即可。
- 支持多种部署方式（本地、云服务器、Docker等）。
- 推荐配合 Obsidian REST 插件或自建 API 网关使用。

---

## 致谢

- [FastMCP](https://github.com/fastmcp/fastmcp)
- [Obsidian](https://obsidian.md/)
- [LangChain](https://python.langchain.com/)

---

如需更多帮助或定制开发，欢迎联系作者！

---

如需英文版或更详细的接口文档，请告知！

