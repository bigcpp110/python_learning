import asyncio
import time


async def get_html(sleep_time):
    print("waiting")
    await asyncio.sleep(sleep_time)
    print("done after {}s".format(sleep_time))


if __name__=="__main__":
    tasks=[get_html(2),get_html(3),get_html(4)]
    loop=asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks=asyncio.Task.all_tasks()
        for task in tasks:
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()