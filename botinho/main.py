import telebot
import aimlBotinho
import bdBotinho
import util.stringUtil as stringUtil

CHAVE_TELEGRAM = "5156865606:AAEZWIanR3_HSoyUHyDSpHadNwFa2-cw4ek"

bot = telebot.TeleBot(CHAVE_TELEGRAM)

def verificar(mensagem):
    return True

def get_resposta(mensagem):
	resposta = aimlBotinho.get_reposta(mensagem)
	resposta = bdBotinho.get_resposta(mensagem,resposta)
	return resposta

@bot.message_handler(func=verificar)
def main(mensagem):
	textoMensagem = stringUtil.remover_caractares(mensagem.text)
	resposta = get_resposta(textoMensagem)
	bot.reply_to(mensagem,resposta)

bot.polling()