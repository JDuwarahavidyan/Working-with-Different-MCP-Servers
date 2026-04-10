from mcp_servers.server_config import config
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from dotenv import load_dotenv

_ = load_dotenv()

import asyncio

async def main():
    
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    # Create MCP client
    client = MultiServerMCPClient(config)
    
    
    tools = await client.get_tools()
    
    tool_info = [tool.name for tool in tools]
    
    print(f"Available Tools: {tool_info}")
    
    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools,
    )
    
    # Run agent
    response = await agent.ainvoke({"messages": [{"role": "user", "content": "list allowed directories"}]})
    
    print(response['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())