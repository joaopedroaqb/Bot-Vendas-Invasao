import telebot

CHAVE_API = "6360414397:AAE7DEeIbvLmXcRgK5Bsj2UAoJzeqqiEUrQ"

bot = telebot.TeleBot(CHAVE_API) 

@bot.message_handler(commands=["compraporunidade"])
def conversao(mensagem):
    texto = "Você escolheu a opção comprar por unidade. \n\nTemos Colete, Short Doll, Samba Canção, Camisa, Caneca e Tirante.\n\nPara comprar Colete digite ou clique em  \n/colete \n\nPara comprar Short Doll digite ou clique em /shortdoll \n\nPara comprar Camiseta digite ou clique em /camiseta \n\nPara comprar Samba Canção digite ou clique em /sambacancao \n\nPara comprar Caneca digite ou clique em \n/caneca .\n\nPara comprar Tirante digite ou clique em  \n/tirante \n\n"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["compraporkit"])
def conversao(mensagem):
    texto = "Você escolheu a opção comprar por kit. \n\nTemos três tipos de kit. Temmos o Kit Simples, Kit Médio e o Kit Mega Invasão .\n\nPara comprar o Kit Simples digite ou clique em  \n/kitsimples \n\nPara comprar o Kit Médio digite ou clique em  \n/kitmedio \n\nPara comprar o Kit Mega Invão digite ou clique em  \n/kitmega ."
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kitsimples"])
def conversao(mensagem):
    texto = "Você escolheu o Kit Simples. O Kit Simples incluí Caneca + Tirante. \n\nPara adiquirir o Kit Simples no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUAcHHG3"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kitmedio"])
def conversao(mensagem):
    texto = "Você escolheu o Kit Médio. O Kit Médio incluí Colete + Samba Canção ou Colote + Short Doll. \n\nPara adiquirir o Kit Médio no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUAdyqm2"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kitmega"])
def conversao(mensagem):
    texto = "Você escolheu o Kit Mega Invasão. O Kit Mega Invasão incluí Caneca + Tirante + Colete + Camiseta + Samba Canção ou Short Doll. \n\nPara adiquirir o Kit Mega Invasão no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUAepzb5"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["colete"])
def conversao(mensagem):
    texto = "Você escolheu colete. \n\nPara adiquirir o colete no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUwWVUnR"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["shortdoll"])
def conversao(mensagem):
    texto = "Você escolheu Short Doll. \n\nPara adiquirir o Short Doll no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUwZCU-n"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["sambacancao"])
def conversao(mensagem):
    texto = "Você escolheu Samba Canção. \n\nPara adiquirir a Samba Canção no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUwZft2J"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["caneca"])
def conversao(mensagem):
    texto = "Você escolheu caneca. \n\nPara adiquirir a Caneca no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUAgg12L"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["camista"])
def conversao(mensagem):
    texto = "Você escolheu camiseta. \n\nPara adiquirir a Camiseta no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUwX_6sR"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["tirante"])
def conversao(mensagem):
    texto = "Você escolheu Tirante. \n\nPara adiquirir o Tirante no cartão (crédito ou débito) basta clicar em https://pag.ae/7ZUAhArnQ"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["help"])
def conversao(mensagem):
      print(mensagem)
      bot.send_message(mensagem.chat.id,"Você solicitou ajuda.\n\nO nosso bot é um bot de vendas de produtos da Atletica Invasão do IFTM.\n\nQualquer dúvida entrar em contato em (34)99689-0845 \n\nPara compras digite ou clique em /compra")


def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = "Olá! \n\nAqui é o Bot de vendas da Atletica Invasão do IFTM. \n\nEscolha alguma opção para continuar (Clique no item desejado). \n\nPara fazer uma compra de produtos unitários, digite ou clique em  \n/compraporunidade .\n\n Para fazer uma compra de kit de produtos, digite ou clique em /compraporkit .\n\nPara qualquer duvida, digite ou clique /help ."
    bot.reply_to(mensagem,texto)

bot.polling()