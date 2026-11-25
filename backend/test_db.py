import asyncio
import os

from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()


async def main():
    engine = create_async_engine(os.environ["DATABASE_URL"])
    async with engine.connect() as conn:
        result = await conn.execute(
            text(
                "select table_name from information_schema.tables "
                "where table_schema='public' order by 1"
            )
        )
        print([row[0] for row in result])
    await engine.dispose()


asyncio.run(main())