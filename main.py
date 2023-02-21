from time import sleep
import pandas as pd
import request
import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot("6263357775:AAEL9rqOeHw5brkKGZ9u5V3KhvOKl2Z0EV0")
meu_serial = 1203678033
df = pd.read_csv('tabela dados.csv', sep=";")


# retornar nome e sobrenome
def nome_pessoa():
    resposta = bot.getUpdates()
    return resposta[-1]["message"]["from"]["first_name"] + " " + resposta[0]["message"]["from"]["last_name"]


# retornar messagem
def texto_mensagem_recebida():
    texto_recebido = bot.getUpdates()
    return texto_recebido[-1]["message"]["text"]


def id_de_mensageiro():
    id_enviador = bot.getUpdates()
    return id_enviador[-1]["message"]["from"]["id"]


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("Recebi uma mensagem do tipo:", msg)

    #mandar_mensagem(1203678033, f'{msg["from"]["first_name"]} {msg["from"]["last_name"]} solicitou informações sobre o '
                                #f'incidente {msg["text"]} e obteve como resposta == {resposta(msg, df)}')

    mandar_mensagem(chat_id, resposta(msg, df))


def mandar_mensagem(id_dest, texto):
    bot.sendMessage(id_dest, texto)


def resposta(mensagem, df):
    incidente = df["incidente"].tolist()
    texto = mensagem["text"]
    if texto in incidente:
        posicao = incidente.index(texto)
        print(posicao)
        ##elementos
        os_original = df["OS"].tolist()[posicao]
        incidentex = df["incidente"].tolist()[posicao]
        m2 = df["m2"].tolist()[posicao]
        obs = df["obs"].tolist()[posicao]

        return f"{m2} m² para o incidente: {incidentex}, OS: {os_original}, obs: {obs}"

    else:
        return "não encontrei sua OS por favor verifique se o número esta correto, dê prioridade a execução do serviço"


MessageLoop(bot, handle).run_as_thread()

while True:
    sleep(1)
    pass
