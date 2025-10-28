#!/usr/bin/env python3
"""
Simple MCP Server with Calculator Tools
This server exposes basic calculator operations through the Model Context Protocol.
"""

from mcp.server import FastMCP
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastMCP server instance
mcp = FastMCP("Calculator Server")

@mcp.tool(description="Add two numbers together")
def add(x: float, y: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        x: First number
        y: Second number
    
    Returns:
        Sum of x and y
    """
    result = x + y
    logger.info(f"ADD: {x} + {y} = {result}")
    return result


@mcp.tool(description="Subtract second number from first number")
def subtract(x: float, y: float) -> float:
    """
    Subtract y from x.
    
    Args:
        x: Number to subtract from
        y: Number to subtract
    
    Returns:
        Difference of x and y
    """
    result = x - y
    logger.info(f"SUBTRACT: {x} - {y} = {result}")
    return result


@mcp.tool(description="Multiply two numbers together")
def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        x: First number
        y: Second number
    
    Returns:
        Product of x and y
    """
    result = x * y
    logger.info(f"MULTIPLY: {x} × {y} = {result}")
    return result


@mcp.tool(description="Divide first number by second number")
def divide(x: float, y: float) -> float:
    """
    Divide x by y.
    
    Args:
        x: Numerator
        y: Denominator
    
    Returns:
        Quotient of x and y
    
    Raises:
        ValueError: If y is zero
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    
    result = x / y
    logger.info(f"DIVIDE: {x} ÷ {y} = {result}")
    return result


@mcp.tool(description="Calculate power of a number")
def power(base: float, exponent: float) -> float:
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
    
    Returns:
        base^exponent
    """
    result = base ** exponent
    logger.info(f"POWER: {base}^{exponent} = {result}")
    return result


@mcp.tool(description="Calculate square root of a number")
def square_root(x: float) -> float:
    """
    Calculate square root of x.
    
    Args:
        x: Number to find square root of
    
    Returns:
        Square root of x
    
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    
    result = x ** 0.5
    logger.info(f"SQRT: √{x} = {result}")
    return result


if __name__ == "__main__":
    logger.info("Starting Calculator MCP Server on http://localhost:8000/mcp/")
    logger.info("Available tools: add, subtract, multiply, divide, power, square_root")
    
    # Run the server with streamable HTTP transport
    mcp.run(transport="streamable-http", port=8000)
