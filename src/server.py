from fastmcp import FastMCP
from obsidian import Obsidian
from dotenv import load_dotenv
# 你可以根据需要调整 API_KEY 的获取方式
import os
load_dotenv()
API_KEY=os.getenv("OBSIDIAN_API_KEY")
obsidian_client = Obsidian(api_key=API_KEY)
mcp = FastMCP("Obsidian MCP Server")

print("==== Obsidian MCP Server 启动 ====")

@mcp.tool(
    name="list_files",
    description="列出 Obsidian 笔记库中的所有文件。",
    tags={"vault", "list"}
)
def list_files() -> str:
    print("[TOOL CALL] list_files 被调用")
    try:
        files = obsidian_client.list_files_in_vault()
        if not files:
            result = "当前 vault 下没有文件。"
        else:
            result = "当前 vault 下的文件有：\n" + "\n".join(files)
        print("list_files 返回：", result)
        return result
    except Exception as e:
        print("list_files 错误：", e)
        return f"获取文件列表时出错：{e}"

@mcp.tool(
    name="get_file_contents",
    description="获取指定文件的内容。",
    tags={"vault", "read"}
)
def get_file_contents(filepath: str) -> str:
    try:
        content = obsidian_client.get_file_contents(filepath)
        return f"文件 {filepath} 的内容如下：\n{content}"
    except Exception as e:
        return f"获取文件内容时出错：{e}"

@mcp.tool(
    name="append_content",
    description="向指定文件追加内容。",
    tags={"vault", "write", "append"}
)
def append_content(filepath: str, content: str) -> str:
    try:
        obsidian_client.append_content(filepath, content)
        return f"已成功向 {filepath} 追加内容。"
    except Exception as e:
        return f"追加内容时出错：{e}"

@mcp.tool(
    name="put_content",
    description="覆盖写入指定文件的内容。",
    tags={"vault", "write", "overwrite"}
)
def put_content(filepath: str, content: str) -> str:
    try:
        obsidian_client.put_content(filepath, content)
        return f"已成功覆盖写入 {filepath} 的内容。"
    except Exception as e:
        return f"覆盖写入内容时出错：{e}"

@mcp.tool(
    name="delete_file",
    description="删除指定的文件。",
    tags={"vault", "delete"}
)
def delete_file(filepath: str) -> str:
    try:
        obsidian_client.delete_file(filepath)
        return f"已成功删除文件 {filepath}。"
    except Exception as e:
        return f"删除文件时出错：{e}"

@mcp.tool(
    name="obsidian_search",  # 避免用 search
    description="全文搜索 Obsidian 笔记库。",
    tags={"vault", "search"}
)
def search(query: str, context_length: int = 100) -> str:
    try:
        result = obsidian_client.search(query, context_length)
        if not result or not result.get('results'):
            return f"未找到与 '{query}' 相关的内容。"
        lines = [f"{i+1}. {item['text']} (文件: {item['file']})" for i, item in enumerate(result['results'])]
        return f"搜索 '{query}' 的结果如下：\n" + "\n".join(lines)
    except Exception as e:
        return f"搜索时出错：{e}"

# 你可以继续添加更多工具...

if __name__ == "__main__":
    mcp.run( transport="sse",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        )