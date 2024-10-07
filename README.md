# For startup project

create .env file
1. POSTGRES_USER=username
2. POSTGRES_PASSWORD=password
3. POSTGRES_DB=database_name
4. DATABASE_URL=postgres://username:password@postgres_db:5432/database_name
5. SECRET_KEY=123
6. ACCESS_TOKEN_EXPIRE_MINUTES=30

For database you need to use tortoise orm and aerich
1. aerich init-db
2. aerich migrate
3. aerich upgrade