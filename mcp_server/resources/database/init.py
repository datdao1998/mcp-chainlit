from resources.database.utils import get_db_connection

conn = get_db_connection()

"""Creates a 'users' table if it doesn't exist."""
create_table_query = """
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
try:
    # Connect to the database
    cursor = conn.cursor()
    
    # Execute the create table query
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'users' initialized successfully.")
    
    # Verify table creation
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = 'users'
        );
    """)
    table_exists = cursor.fetchone()[0]
    if table_exists:
        print("Confirmed: 'users' table exists.")
    else:
        print("Table creation failed.")
    
except Exception as e:
    print(f"Error initializing table: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()