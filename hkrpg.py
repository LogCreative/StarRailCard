from starrailcard import honkaicard
from starrailcard.src.tools.pill import get_dowload_img
import asyncio
import os, shutil

uid       = 109814396
outputdir = "RailCard"
lang      = "cn"
preserve  = True

if os.path.exists(outputdir):
    if not preserve:
        shutil.rmtree(outputdir)
os.makedirs(outputdir, exist_ok=True)

async def main():
    async with honkaicard.MiHoMoCard(lang=lang) as hmhm:

        # avatar
        user_profile = await hmhm.API.get_full_data(uid)
        for character in user_profile.characters:
            character_avatar_filename = "avatar-{}-{}.png".format(character.name.replace(' ','_'), character.rarity)
            character_avatar = await get_dowload_img(character.icon)
            character_avatar.save(os.path.join(outputdir, character_avatar_filename))

        # card
        r = await hmhm.creat(uid=uid)
        for character_card in r.card:
            character_fullname = "{}-{}".format(character_card.name.replace(' ','_'), character_card.rarity)
            character_card_filename = "card-{}.jpg".format(character_fullname)
            character_card.card.convert('RGB').save(os.path.join(outputdir, character_card_filename))

asyncio.run(main())
