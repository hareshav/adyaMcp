import logging
from collections.abc import Sequence
from functools import lru_cache
from typing import Any
import traceback
from dotenv import load_dotenv
from mcp.server import Server
from mcp.types import (
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
import json

load_dotenv()

from . import tools_errors
from . import toolhandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-appsignal")

app = Server("mcp-appsignal")

tool_handlers = {}
def add_tool_handler(tool_class: toolhandler.ToolHandler):
    global tool_handlers
    tool_handlers[tool_class.name] = tool_class

def get_tool_handler(name: str) -> toolhandler.ToolHandler | None:
    if name not in tool_handlers:
        return None
    
    return tool_handlers[name]

# Register all tool handlers
add_tool_handler(tools_errors.SearchErrorsToolHandler())
add_tool_handler(tools_errors.GetAllErrorsToolHandler())
add_tool_handler(tools_errors.GetIncidentDetailsToolHandler())
add_tool_handler(tools_errors.GetAllIncidentsToolHandler())

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [th.get_tool_description() for th in tool_handlers.values()]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    try:        
        if not isinstance(arguments, dict):
            raise RuntimeError("arguments must be dictionary")
        
        tool_handler = get_tool_handler(name)
        if not tool_handler:
            raise ValueError(f"Unknown tool: {name}")

        return tool_handler.run_tool(arguments)
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.error(f"Error during call_tool: {str(e)}")
        raise RuntimeError(f"Caught Exception. Error: {str(e)}")

async def main():
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        ) 