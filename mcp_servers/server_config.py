config = {  
    "filesystem": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            r"D:\WSO2 Learnings"
        ],
        "transport": "stdio"
    },
    
    "math": {
        "command": "uv",
        "args": ["run", "mcp_servers/math_server.py"],
        "transport":"stdio"
    },
    
    "research": {
        "url": "http://localhost:8001/sse",
        "transport": "sse"
    },
    
    "internet_search": {
        "url": "http://localhost:8002/mcp",
        "transport": "http"
    },
    
    "fetch": {
        "transport": "stdio",
        "command": "uvx",
        "args": ["mcp-server-fetch"],
    },
    
    "time": {
      "command": "python",
      "args": ["-m", "mcp_server_time"],
       "transport": "stdio"
    }
    
}
  