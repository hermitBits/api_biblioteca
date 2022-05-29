from os import getenv


class Settings:
    PROJECT_NAME: str = "Api Biblioteca"
    PROJECT_VERSION: str = "1.0.0"
    
    DATABASE_USER: str = getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = getenv('DATABASE_PASSWORD')
    DATABASE_NAME: str = getenv('DATABASE_NAME')
    DATABASE_SERVER: str = getenv('DATABASE_SERVER', "localhost")
    DATABASE_PORT: str = getenv('DATABASE_PORT', 3306)
    DATABASE_URL: str = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}"
    
    
settings = Settings()