import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
import g4f
from g4f.cookies import set_cookies


set_cookies(".bing.com", {
  "_U": "cookie value"
})
set_cookies(".google.com", {
  "__Secure-1PSID": "cookie value"
})

#чтоб файл читать
putb="0003.txt"

file = open(putb, "r",  encoding="UTF-8")
content = file.read()
file.close()

def ask_gpt(promt:str)->str:
    set_cookies(".bing.com", {
        "_U": "cookie value"
    })

    set_cookies(".google.com", {
        "__Secure-1PSID": "cookie value"
    })

    # чтоб файл читать
    putb = "file/0003.txt"

    file = open(putb, "r", encoding="UTF-8")
    content = file.read()
    file.close()

    responce = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":promt}],

    )
    return responce

print(ask_gpt("Ответь на 5 вопросов по поводу телефонного разговора. Очень важно:каждый ответ пиши с новой строки.C-сотрудник, К-клиент." + content + "Был ли вежлив менеджер в разговоре с клиентом? смогли менеджер решить вопрос клиента? какую оценку от 1 до 5 можно поставить за этот звонок? как можно описать summary звонка?"))




