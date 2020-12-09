import asyncio


async def usain_bolt_correr():

    print('Usain Bolt começou a correr')
    await asyncio.sleep(5.5)
    print('Usain Bolt terminou a corrida.')


async def flash_correr():

    print('Flash começou a correr')
    await asyncio.sleep(4.5)
    print('Flash terminou a corrida.')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(usain_bolt_correr(), flash_correr()))
