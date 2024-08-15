import asyncio
import aiohttp

# asynchronous function to fetch a URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

#asynchronous function
async def main():
    urls = [
        "https://yourlink.com",
        "https://yourlink.org",
        "https://yourlink.net"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)

    for i, page in enumerate(pages):
        print(f"Page {i+1}: {page[:100]}...")  # printing first 100 characters of each page

asyncio.run(main())
