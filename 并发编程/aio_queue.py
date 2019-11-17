import aiohttp
import asyncio
from asyncio import Lock,Queue


cache={}
queue=[]
lock=Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]

async def parse_stuff():
    stuff = await get_stuff(1)

async def use_stuff():
    stuff = await get_stuff(2)

tasks = [parse_stuff(), use_stuff()]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))