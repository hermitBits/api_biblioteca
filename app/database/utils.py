from core.config import settings
from mysql import connector


async def check_db_connected():
    try:
        connector.connect(
            host=f"{settings.DATABASE_SERVER}",
            database=f"{settings.DATABASE_NAME}",
            user=f"{settings.DATABASE_USER}",
            password=f"{settings.DATABASE_PASSWORD}")
        return True
    except:
        return False
        
    