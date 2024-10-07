import pytest
import bcrypt
from datetime import datetime
from httpx import AsyncClient, ASGITransport
from app.main import app  
from app.models.user_model import User
from app.core.config import settings
from tortoise import Tortoise
from app.core.security import create_access_token

global_token = None
global_kitten_id = None


@pytest.mark.asyncio
async def test_get_all_kittens():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": settings.MODELS}
    )
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        response = await client.get("/kittens/")
        assert response.status_code == 200
    await Tortoise.close_connections()


@pytest.mark.asyncio
async def test_create_kitten():
    global global_token  
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": settings.MODELS}
    )

    unique_email = f"test_{datetime.utcnow().isoformat()}@example.com"
    hashed_password = bcrypt.hashpw(b"testpassword", bcrypt.gensalt()).decode('utf-8')

    user = await User.create(username="testuser", email=unique_email, hashed_password=hashed_password)
    assert user is not None, "User creation failed!"

    token_data = {"sub": unique_email}  
    global_token = create_access_token(data=token_data)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000") as client:
        response = await client.post(
            "/kittens/",
            json={
                "name": "Fluffy",
                "color": "White",
                "age": 1,
                "description": "A cute fluffy kitten.",
                "breed_id": 2
            },
            headers={"Authorization": f"Bearer {global_token}"}
        )

        assert response.status_code == 200
        assert response.json()["name"] == "Fluffy"
        
        global global_kitten_id
        global_kitten_id = response.json()["id"] 

    await Tortoise.close_connections()

@pytest.mark.asyncio
async def test_update_kitten():
    global global_token, global_kitten_id  
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": settings.MODELS}
    )

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000") as client:
        response = await client.put(
            f"/kittens/{global_kitten_id}", 
            json={
                "name": "Updated Fluffy",
                "color": "White",
                "age": 2,
                "description": "An updated cute fluffy kitten.",
                "breed_id": 2
            },
            headers={"Authorization": f"Bearer {global_token}"}  
        )

        assert response.status_code == 200
        assert response.json()["name"] == "Updated Fluffy"

    await Tortoise.close_connections()


@pytest.mark.asyncio
async def test_delete_kitten():
    global global_token, global_kitten_id  
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        await Tortoise.init(
            db_url=settings.DATABASE_URL,
            modules={"models": settings.MODELS}
        )

        response = await client.delete(f"/kittens/{global_kitten_id}", headers={"Authorization": f"Bearer {global_token}"})  
        assert response.status_code == 200
        assert response.json()["id"] == global_kitten_id

    await Tortoise.close_connections()
