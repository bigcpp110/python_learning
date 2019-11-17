import re
import asyncio
import aiohttp
import aiomysql
from pyquery import PyQuery

# https://www.lfd.uci.edu/


stop_flag = False
start_url = "http://www.jobbole.com/"
waitting_urls = []
seen_urls = set()
sem = asyncio.Semaphore(3)


async def fetch(url, session):
    """
    发送http请求
    :param url:
    :return:
    """
    async with sem:                 # 并发度控制
        await asyncio.sleep(1)      # 爬取速度控制
        try:
            async with session.get(url) as resp:
                print('url statis: {0}'.format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):
    """
    从请求页面中获取下次要请求url
    :param html:
    :return:
    """
    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        if url and url.startswith('http') and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def article_handler(url, session, pool):
    """
    获取文章详情并解析入库
    :param url:
    :param session:
    :return:
    """
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq('title').text()  # 省略其他字段
    print(title)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("sql")
            insert_sql = """
                INSERT INTO xxx
            """
            print(cur.description)
            await cur.execute(insert_sql)


async def init_urls(url, session):
    """
    解析页面，
    :param url:
    :param session:
    :return:
    """

    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def consumer(pool, session):
    # async with aiohttp.ClientSession() as session:      # 发送http请求需要的session
    while not stop_flag:
        if len(waitting_urls) == 0:
            await asyncio.sleep(0.5)
            continue
        url = waitting_urls.pop()
        print('start get url: ' + url)

        # 详情页协程，解析页面内容、入库
        if re.match('http://.*?jobbole.com/\d+/', url):
            if url not in seen_urls:
                asyncio.ensure_future(article_handler(url, session, pool))

        # 非详情页协程，进一步提取出详情页的url
        else:
            if url not in seen_urls:
                asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    # 等待Mysql连接池建立
    pool = await aiomysql.create_pool(
        host='', port='', user='', password='', db='mysql', loop=loop, charset='utf8', autocommit=True
    )
    async with aiohttp.ClientSession() as session:      # 发送http请求需要的session
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)

        # consumer协程从url获取，动态向asyncio提交article_handler和init_urls协程
        asyncio.ensure_future(consumer(pool, session))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()