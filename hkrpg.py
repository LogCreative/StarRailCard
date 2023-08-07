from starrailcard import honkaicard 
import asyncio

async def mains():
    async with honkaicard.MiHoMoCard(lang="cn",save=True) as hmhm:
        r = await hmhm.creat(109814396)
        print(r)

asyncio.run(mains())
