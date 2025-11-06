from httpx import AsyncClient
from app.main import app
import pytest

@pytest.mark.asyncio
async def test_run_ok():
    async with AsyncClient(app=app, base_url="http://t") as ac:
        r = await ac.post("/run", json={"language":"python","code":"print(1+1)"})
        assert r.status_code == 200
        assert "2" in r.json()["stdout"]
