import aiohttp

class APIImplementation:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    async def fetch_data(self, params):
        url = f"{self.base_url}{params}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, auth=aiohttp.BasicAuth(self.username, self.password)) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data: {response.status} - {await response.text()}")
                    return None
