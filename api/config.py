DB_USER = "backend"
DB_PASSWORD = "FNaF1122"
DB_NAME = "hhtp418"
DB_HOST = "185.178.45.234"
DB_PORT = "5432"
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

JWT_SECRET_KEY = "secret_jwt_words"