#!/usr/bin/env python3
"""
MCP Client with Strands Agent
This client connects to the MCP Calculator Server and creates an AI agent
that can use calculator tools through natural language.
"""

from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_transport():
    """
    Create a streamable HTTP transport to connect to the MCP server.
    
    Returns:
        Transport client connected to localhost:8000
    """
    return streamablehttp_client("http://localhost:8000/mcp/")


def create_agent_with_mcp_tools():
    """
    Create a Strands agent connected to the MCP calculator server.
    
    Returns:
        Tuple of (MCPClient, Agent)
    """
    # Create MCP client
    mcp_client = MCPClient(create_transport)
    
    # Connect to server and get tools
    with mcp_client:
        tools = mcp_client.list_tools_sync()
        logger.info(f"Connected to MCP server. Available tools: {len(tools)}")
        
        # Print available tools
        for tool in tools:
            logger.info(f"  - {tool.name}: {tool.description}")
        
        # Create agent with MCP tools
        agent = Agent(tools=tools)
        
        return mcp_client, agent


def interactive_mode():
    """
    Run the agent in interactive mode where users can ask questions.
    """
    print("="*70)
    print("🤖 MCP CALCULATOR AGENT")
    print("="*70)
    print("\nConnecting to MCP Calculator Server...")
    
    # Create MCP client
    mcp_client = MCPClient(create_transport)
    
    try:
        with mcp_client:
            # Get tools from server
            tools = mcp_client.list_tools_sync()
            print(f"\n✅ Connected! Available tools: {len(tools)}")
            print("\nTools:")
            for tool in tools:
                print(f"  • {tool.name}: {tool.description}")
            
            # Create agent
            agent = Agent(tools=tools)
            
            print("\n" + "="*70)
            print("💬 Ask me math questions! (Type 'exit' to quit)")
            print("="*70)
            print("\nExample questions:")
            print("  - What is 125 plus 375?")
            print("  - If I have 1000 and spend 246, how much do I have left?")
            print("  - What is 16 times 16?")
            print("  - What is the square root of 144?")
            print("  - What is 2 to the power of 10?")
            print()
            
            # Interactive loop
            while True:
                try:
                    # Get user input
                    user_input = input("\n🧮 You: ").strip()
                    
                    # Check for exit command
                    if user_input.lower() in ['exit', 'quit', 'q']:
                        print("\n👋 Goodbye!")
                        break
                    
                    # Skip empty input
                    if not user_input:
                        continue
                    
                    # Process with agent
                    print("\n🤔 Agent: Thinking...\n")
                    response = agent(user_input)
                    print(f"💡 Answer: {response}\n")
                    
                except KeyboardInterrupt:
                    print("\n\n👋 Goodbye!")
                    break
                except Exception as e:
                    logger.error(f"Error processing query: {e}")
                    print(f"\n❌ Error: {e}\n")
    
    except Exception as e:
        logger.error(f"Failed to connect to MCP server: {e}")
        print(f"\n❌ Failed to connect to MCP server!")
        print("Make sure the server is running: python mcp_server.py")
        sys.exit(1)


def test_mode():
    """
    Run predefined test queries to verify the agent works.
    """
    print("="*70)
    print("🧪 MCP CALCULATOR AGENT - TEST MODE")
    print("="*70)
    
    # Create MCP client
    mcp_client = MCPClient(create_transport)
    
    # Test queries
    test_queries = [
        "What is 125 plus 375?",
        "If I have 1000 and spend 246, how much do I have left?",
        "What is 16 times 16?",
        "What is 100 divided by 4?",
        "What is 2 to the power of 8?",
        "What is the square root of 144?"
    ]
    
    try:
        with mcp_client:
            # Get tools
            tools = mcp_client.list_tools_sync()
            print(f"\n✅ Connected! Available tools: {len(tools)}\n")
            
            # Create agent
            agent = Agent(tools=tools)
            
            # Run test queries
            for i, query in enumerate(test_queries, 1):
                print(f"\n{'='*70}")
                print(f"Test {i}/{len(test_queries)}: {query}")
                print('='*70)
                
                try:
                    response = agent(query)
                    print(f"✅ Answer: {response}")
                except Exception as e:
                    print(f"❌ Error: {e}")
            
            print(f"\n{'='*70}")
            print("✅ All tests completed!")
            print('='*70)
    
    except Exception as e:
        logger.error(f"Test mode failed: {e}")
        print(f"\n❌ Failed to connect to MCP server!")
        print("Make sure the server is running: python mcp_server.py")
        sys.exit(1)


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run in test mode
        test_mode()
    else:
        # Run in interactive mode
        interactive_mode()
