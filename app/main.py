from core.config import settings
from database.utils import check_db_connected
from fastapi import Depends, FastAPI


def start():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    return app


app = start()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()
    
    
@app.get("/health")
def health():
    return {"health": "OK!"}
    