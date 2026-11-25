import asyncio

from sqlalchemy import func, select

from app.db.session import SessionLocal
from app.models import Account, Case, Transaction, User


async def main():
    async with SessionLocal() as db:
        for model in (User, Case, Account, Transaction):
            count = (
                await db.execute(select(func.count()).select_from(model))
            ).scalar_one()
            print(model.__name__, count)


asyncio.run(main())