from .. import utils, loader
from asyncio import sleep
import random
from datetime import timedelta
import os

shablon1 = ('﻿твою мамашку ебал на тихих холмах а после этого похоронил ее под перевернутым крестом',
'с сатаной хуярим кагор и ебем твою мамашку',
'еблище твое ломом отхуярим так что ты из себя ничего кроме как куска мяса ничего представлять не будешь',
'твоей беременной мамаше по коленям хуем ебанул и она шалава ебучая сразу сосать принялась',
'кончил в твою мать из нее вышла саламандра',
'я наколол себе пентаграмму и твою голову на кол',
'твою мамашку ебалом засунул в решетки полыхающего храма',
'расхуярил твою мамашку а ты так и остался пидорасом',
'оторву голову твоей мамаше и насажу на забор ',
'сброшу тебя с небоскреба на штык',
'я тебе пиздень порву сын шлюхи',
'ноу нейм я твою мать ебал закрой нахуй свое еблище',
'я тебе рылище переломаю сын шлюхи ты ебучий',
'член мой бери в руки и дережируй ебать',
'еблище тебе порву сын шлюхи ебучий',
'ебало тебе сломаю сын шлюхи закрой ебало',
'членикс бери в руки сынок шлюхи',
'я тебя за уши на свой хуй натяну шлюха позорная',
'вырвем тебе уши сын шлюхи ебаный',
'я твою шлюхоматерь ебал закрой еблище свое нахуй',
'рылище тебе переломаем сынок осла ебаный',
)
shablon2 = " отсоси"
shablon3 = 'che sosi'
shablon4 = " усоси"
shablon5 = "уу"
shablon6 = " сс"
shablon7 = " ввв"
shablon8 = " член берешь"
shablon_all = [shablon1, shablon2, shablon3, shablon4, shablon5, shablon6, shablon7, shablon8]


wabl1 = ('хуй сосешь',
'наяривай членяру деган',
'хуем тебе жопу рвал',
'ебало закрой свое',
'сынуля шлюшки ты',
'коленные чашечки те выломаю',
'хуем раздроблю те ебальник',
'членом тя лавлю',
'хуем тя пиздил',
'ебало втули',
'сынишка шмары ты',
'наяривай залупу',
'на костре тя режу',
'хуем тя раздавил',
'порвал те ебальник поросенку',
'сосешь ты',
'пиздец соси',
'хуем тя унижал',
'фаршмак ты ебаный',
'хуем твою мать тушил',
'ебало те бил',
'хуем тя пиздил',
'хуй сосешь ты',
'член хватай',
'реще хуину бери',
'пиздили тя',
'ебало закрой',
'слабак ты',
'соплежуй ты',
'хуй хватай ты',
'сосешь мне',
'сосешь клану моему',
'член сакай',
'хуй бери',
'смокчи членяру',
'хуем тя тушил',
'ебашу тя залупой',
'хуй возьми уже',
'на член',
'трахнем твою семью',
'режу те матуху',
'терпила ты',
'хуй берешь',
'член сосешь',
'ебало те рву',
'режу те тело',
'слабак ты',
'хе-хе соси',
'ебать ты отсосник',
'хуй возьми и соси',
'глотай хуй ты',
'членом тя бью',
'хуем тя убил',
'я стебал твою матуху',
)
wabl2 = " отсоси"
wabl3 = 'che sosi'
wabl4 = " усоси"
wabl5 = "уу"
wabl6 = " сс"
wabl7 = " ввв"
wabl8 = " член берешь"
wabl_all = [wabl1, wabl2, wabl3, wabl4, wabl5, wabl6, wabl7, wabl8]


wablon1 = ('хуй',
'соси',
'на',
'член',
'бери',
'мою',
'хуину',
'и',
'соси',
'на',
'членяру',
'бери',
'мой',
'хуй',
'член',
'хватай',
'режу',
'тя',
'сосешь',
'ты',
'ебу',
'тя',
'нy',
'уже',
'соси',
'терпильный',
'терпилизированный',
'хуем',
'тя',
'потыкаю',
'ну',
'же',
'хуй',
'соси',
'реще',
'мне',
'соси',
'отсасывай',
'терпила',
'ты',
'хуесос',
'ты',
'слабак',
'ты',
'ебаный',
'ну',
'же',
'член',
'бери',
'и',
'смокчи',
'идиот',
'ебаный',
'ну',
'же',
'ебу',
'тя',
'хуесос',
'слабак',
'пидор',
'далбаеб',
'немощ',
'улитка',
'реще',
'соси',
'мой',
'хуй',
'давай',
'там',
)
wablon2 = " отсоси"
wablon3 = 'che sosi'
wablon4 = " усоси"
wablon5 = "уу"
wablon6 = " сс"
wablon7 = " ввв"
wablon8 = " член берешь"
wablon_all = [wablon1, wablon2, wablon3, wablon4, wablon5, wablon6, wablon7, wablon8]


class Revmatolog(loader.Module):
    """†Life Changer⛧"""
    strings = {'name': 'Private by Revmatolog'}
    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def revmacmd(self, message):
        """For revma spam🌴 - .revma + задержка + айди конференции + шапка ⛧"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        file = reply if reply and reply.file else None
        if not args:
            return await utils.answer(message, '<b>⛧Ты ввёл код неправильно⛧</b>')
        args = args.split(' ', maxsplit=2)
        try:
            time = float(args[0])
        except:
            return await utils.answer(message, '<b>⛧Напиши условия правильно</b>⛧')
        if args[1].isdigit():
            args[1] = int(args[1])
        try:
            args[2] = args[2]
        except:
            args.append('')
        status = self.db.set("revma", "status", True)
        await message.delete()
        while status:
            try:
                await message.client.send_message(args[1], args[2] + " " + random.choice(
                    shablon_all[self.db.get('revma', 'shablon', 1) - 1]), file=file)
                await sleep(time)
            except Exception as e:
                return await message.respond(f"Ошибка:\n" + str(e))
            if not self.db.get("revma", "status"): return


    async def stopcmd(self, message):
        """For stop bot - .stop Остановка бота⛧ """
        self.db.set('revma', 'status', False)
        await utils.answer(message, '<b>Остановлено⛧</b>')

    async def idcmd(self, message):
        """For id konferention🌴 - .id айди конференции отправлено в избранные⛧"""
        reply = await message.get_reply_message()
        me = await message.client.get_me()
        if not reply:
            i = str(message.chat_id)
        else:
            i = str(reply.sender_id)
        if i.startswith('-100'):
            i = i[4:]
        await message.client.send_message(message.chat.id, f'<b>🌓CHAT ID:</b> <code>{message.chat.id}</code>')
        await message.delete()


    async def phcmd(self, message):
        """For photobot🌴 - Для запуска реплай на фото и .ph⛧"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        file = reply if reply and reply.file else None
        if not args:
            return await utils.answer(message, '<b>⛧Неправильно задана задача⛧</b>')
        args = args.split(' ', maxsplit=2)
        try:
            time = float(args[0])
        except:
            return await utils.answer(message, '<b>⛧Неправильно указано время задержки⛧</b>')
        if args[1].isdigit():
            args[1] = int(args[1])
        try:
            args[2] = args[2]
        except:
            args.append('')
        status = self.db.set("revma", "status", True)
        await message.delete()
        while status:
            try:
                for i in shablon_all[self.db.get('revma', 'shablon', 1) - 1]:
                    await message.client.send_message(args[1], args[2] + " " + i, file=file)
                    await sleep(time)
                    if not self.db.get("revma", "status"): return
            except Exception as e:
                return await message.respond(f"⛧Ошибка:\n {str(e)}")
            
            
    async def SatanWablons(self, client, db) -> None:
        self.db = db
        self.client = client

    async def wabloncmd(self, message):
        """For save wablon🌴 - command .wablon + replay⛧"""
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if reply:
            await message.edit('⛧Downloading...⛧')
            if reply.text:
                text = reply.text
                fname = f'{name or message.id + reply.id}.txt'
                file = open(fname, 'w')
                file.write(text)
                file.close()
                await message.edit(
                    f'⛧Wablon saved how: <code>{fname}</code> ⛧')
            else:
                ext = reply.file.ext
                fname = f'{name or message.id + reply.id}{ext}'
                await message.client.download_media(reply, fname)
                await message.edit(
                    f'⛧Wablon saved how: <code>{fname} ⛧')
        else:
            return await message.edit('⛧Replay the file⛧')

    async def satanrvcmd(self, message):
        """For satanrv spam🌴 - time + wablon.txt + obrawenie⛧"""
        shapka = utils.get_args_raw(message)
        if not shapka:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>⛧SatanSpam is stopped⛧</b>")
            return
        await utils.answer(
            message,
            "<b>⛧SatanSpam by Revma started his work\n\n"
            "⛧for stopping bot write .SatanSpam <code>.satanrv</code></b> ⛧",
        )
        text = shapka.split(' ')
        time = int(text[0])
        sh = ''.join(text[1])
        shp = ' '.join(text[2:])
        self.db.set(self.strings["name"], "state", True)
        with open(f'{sh}', 'r', encoding='utf-8') as f:
            s = f.read()
            w = s.split('\n')
            while self.db.get(self.strings["name"], "state"):
                await message.respond((shp + random.choice(w)))
                await sleep(time)


    async def nonstopcmd(self, message):
        """For nonstop🌴 - .nonstop + задержка + айди конференции + шапка ⛧"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        file = reply if reply and reply.file else None
        if not args:
            return await utils.answer(message, '<b>⛧Ты ввёл код неправильно⛧</b>')
        args = args.split(' ', maxsplit=2)
        try:
            time = float(args[0])
        except:
            return await utils.answer(message, '<b>⛧Напиши условия правильно</b>⛧')
        if args[1].isdigit():
            args[1] = int(args[1])
        try:
            args[2] = args[2]
        except:
            args.append('')
        status = self.db.set("revma", "status", True)
        await message.delete()
        while status:
            try:
                await message.client.send_message(args[1], args[2] + " " + random.choice(
                    wabl_all[self.db.get('revma', 'wabl', 1) - 1]), file=file)
                await sleep(time)
            except Exception as e:
                return await message.respond(f"Ошибка:\n" + str(e))
            if not self.db.get("revma", "status"): return


    async def lesenkacmd(self, message):
        """For lesenka🌴 - .lesenka + задержка + айди конференции + шапка ⛧"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        file = reply if reply and reply.file else None
        if not args:
            return await utils.answer(message, '<b>⛧Ты ввёл код неправильно⛧</b>')
        args = args.split(' ', maxsplit=2)
        try:
            time = float(args[0])
        except:
            return await utils.answer(message, '<b>⛧Напиши условия правильно</b>⛧')
        if args[1].isdigit():
            args[1] = int(args[1])
        try:
            args[2] = args[2]
        except:
            args.append('')
        status = self.db.set("revma", "status", True)
        await message.delete()
        while status:
            try:
                await message.client.send_message(args[1], args[2] + " " + random.choice(
                    wablon_all[self.db.get('revma', 'wablon1', 1) - 1]), file=file)
                await sleep(time)
            except Exception as e:
                return await message.respond(f"Ошибка:\n" + str(e))
            if not self.db.get("revma", "status"): return
