class Config:
    def __init__(self):
        self.postgresql_user = "admin"
        self.postgresql_password = "admin"
        self.postgresql_dbname = "mcp"

        self.db_config = {
            "host": "0.0.0.0",
            "database": self.postgresql_dbname,  
            "user": self.postgresql_user,          
            "password": self.postgresql_password,      
            "port": "5432"
        }

config = Config()
