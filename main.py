import asyncio
from application.api_service import APIService

async def main():
    service = APIService()
    await service.fetch_data()

if __name__ == "__main__":
    asyncio.run(main())
