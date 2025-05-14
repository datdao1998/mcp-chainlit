# server.py
from mcp.server.fastmcp import FastMCP
from psycopg2.extras import DictCursor

from resources.database.utils import get_db_connection
from tools.get_cat_facts import get_facts

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def get_cat_facts() -> str:
    """Get random cat facts via text message every day."""
    return get_facts()


@mcp.tool()
def insert_user_info(username: str, email: str) -> str:
    """Insert user information to PostgreSQL database
    Args:
        username (str): Username of the user.
        email (str): Email address of the user.
    """
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute("""INSERT INTO public.users (username, email) VALUES (%s, %s)""", (username, email))
    conn.commit()
    return "Insert user data successfully"


@mcp.prompt()
def summarize_paragraphs(para: str) -> str:
    """Summary paragraph"""
    return f"Please summary this paragraphs : {para}"

