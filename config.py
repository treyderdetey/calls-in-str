import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

import os

import g4f
from g4f.cookies import set_cookies

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command


import handlers
from handlers import router


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="Your Token")
# Диспетчер
dp = Dispatcher()

# async def preobraz(name_id):
#     await

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    await message.answer("/versia - узнать режим работы \n /swap - сменить режим работы")

@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("/versia - узнать режим работы \n /swap - сменить режим работы \n /zapusk - запуск ")

@dp.message(Command("versia"))
async def cmd_start(message: types.Message):
    ss = message.chat.id
    if prow(ss) == 1:
        await message.answer("Кидай 1 с без промта")
    else:
        await message.answer("Кидай много")


@dp.message(Command("zapusk"))
async def cmd_start(message: types.Message):
    name_id = message.chat.id
    gg = "Ну она есть"
    gg = proebali(gg, name_id)
    await message.answer(f"{gg}")



@dp.message(Command("swap"))
async def cmd_start(message: types.Message):
    name_id = message.chat.id
    if os.path.isfile(fr"file\{name_id}.txt"):
        file = open(fr"file\{name_id}.txt", "w", encoding="UTF-8")
        file.close()
        os.remove(fr"file\{name_id}.txt")
        file = open(fr"file\{name_id}_.txt","w")
        file.close()

    else:
        file = open(fr"file\{name_id}_.txt", "w", encoding="UTF-8")
        file.close()
        os.renames(fr"file\{name_id}_.txt", f"file/{name_id}.txt")

    await message.answer("Есть свап")





def prow(name_id):
    if os.path.isfile(f"file/{name_id}.txt") == True:
        return 1
    elif os.path.isfile(f"file/{name_id}_.txt") == True:
        return 2
    elif os.path.isfile(f"file/{name_id}.txt") == True and os.path.isfile(f"file/{name_id}_.txt") == True:
        return 1


@dp.message()
async def down(message: types.file):
    if prow(str(message.chat.id)) == 1:
        if message.document != None and message.caption == None:
            try:

                set_cookies(".bing.com", {
                    "_U": "cookie value"
                })
                set_cookies(".google.com", {
                    "__Secure-1PSID": "cookie value"
                })



                print("downloading document")
                print(message)
                ss = str(message.document.file_name)
                file_id = message.document.file_id
                name_id = message.chat.id
                file = await bot.get_file(file_id)
                file_path = file.file_path
                destination = fr"file\{name_id}.txt"
                await bot.download_file(file_path, destination)
                gg = ans(name_id)
                await message.answer(f"{ss}"+ "\n" + f"{gg}")
                print("success")
            except BaseException:
                print("Добился чего хотел, без тебя все хорошо работало если что!!!")
        elif message.document != None and message.caption != None:
            try:

                set_cookies(".bing.com", {
                    "_U": "cookie value"
                })
                set_cookies(".google.com", {
                    "__Secure-1PSID": "cookie value"
                })



                print("downloading document")
                print(message)
                ss = str(message.document.file_name)
                file_id = message.document.file_id
                name_id = message.chat.id
                file = await bot.get_file(file_id)
                file_path = file.file_path
                destination = fr"file\{name_id}.txt"
                await bot.download_file(file_path, destination)
                gg = ans(name_id,message.caption)
                await message.answer(f"{ss}"+ "\n" + f"{gg}")
                print("success")
            except BaseException:
                print()
        else:
            await message.answer("Мне Очень нужен фаел пожалуйста")
    elif prow(str(message.chat.id)) == 2:
        print("downloading document")
        print(message)
        ss = str(message.document.file_name)
        file_id = message.document.file_id
        name_id = message.chat.id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        destination = fr"file\{name_id}.txt"
        await bot.download_file(file_path, destination)
        antians(name_id,ss)
    elif prow(str(message.chat.id)) == 3:
        if message.document != None and message.caption == None:
            try:

                set_cookies(".bing.com", {
                    "_U": "cookie value"
                })
                set_cookies(".google.com", {
                    "__Secure-1PSID": "cookie value"
                })



                print("downloading document")
                print(message)
                ss = str(message.document.file_name)
                file_id = message.document.file_id
                name_id = message.chat.id
                file = await bot.get_file(file_id)
                file_path = file.file_path
                destination = fr"file\{name_id}.txt"
                await bot.download_file(file_path, destination)
                gg = ans(name_id)
                await message.answer(f"{ss}"+ "\n" + f"{gg}")
                print("success")
            except BaseException:
                print("Добился чего хотел, без тебя все хорошо работало если что!!!1111111")
        elif message.document != None and message.caption != None:
            try:

                set_cookies(".bing.com", {
                    "_U": "cookie value"
                })
                set_cookies(".google.com", {
                    "__Secure-1PSID": "cookie value"
                })



                print("downloading document")
                print(message)
                ss = str(message.document.file_name)
                file_id = message.document.file_id
                name_id = message.chat.id
                file = await bot.get_file(file_id)
                file_path = file.file_path
                destination = fr"file\{name_id}.txt"
                await bot.download_file(file_path, destination)
                gg = ans(name_id,message.caption)
                await message.answer(f"{ss}"+ "\n" + f"{gg}")
                print("success")
            except BaseException:
                print()
        else:
            await message.answer("Мне Очень нужен фаел пожалуйста")





def ans(name_id,box = '1'):
    if box == '1':
        file = open(f"file\{name_id}.txt", "r", encoding="UTF-8")
        content = file.read()
        file.close()
        promt ="Ответь на 5 вопросов по поводу телефонного разговора. \n Очень важно:каждый ответ пиши с новой строки.C-сотрудник, К-клиент. Был ли вежлив менеджер в разговоре с клиентом? смогли менеджер решить вопрос клиента? какую оценку от 1 до 5 можно поставить за этот звонок?  как можно описать summary звонка? \n Пример идеального ответа: 1)текст вопроса\n ответ на вопрос.\n Не придумывай свои вопросы и не вставляй слова из диалога в ответ. На вопросы где тебя просят дать оценку по шкале отвечай только числом."+ content
        responce = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": promt}],
        )
        return responce
    if box != '1':
        file = open(f"file\{name_id}.txt", "r", encoding="UTF-8")
        content = file.read()
        file.close()
        promt = str(box) + content
        responce = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": promt}],
        )
        print(11111)
        return responce

def antians(name_id,file_id):
    try:
        file = open(f"file\{name_id}.txt", "r", encoding="UTF-8")
        content = u" \n Диалога \n" + f" {str(file_id)}" + file.read() +  u"\n"
        file.close()
        file = open(f"file\{name_id}_.txt", "a", encoding="UTF-8")
        file.write(f"{content}")
        file.close()


    except BaseException:
        print()


def proebali(gg,name_id):

    file = open(f"file\{name_id}_.txt", "r", encoding="UTF-8")
    content = file.read()
    file.close()
    promt = "Кратко написать проблему в каждом диалог сотрудника с клиентом, диалоги разделены и пронумерованны. Очень важно писать ответ с новой строчки, нумерацией и кратким описанием диалогов" + content
    responce = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
    )

    return responce















async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    dp.include_router(handlers.router)
