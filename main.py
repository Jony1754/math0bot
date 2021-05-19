from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(
    token='1822223787:AAEl8_-tM3vxxTsTPSHqXQy4Ha0DW4tMdIc', use_context=True)
dispatcher = updater.dispatcher


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="🤖 Hola, este bot fue creado por los mejores estudiantes de Ingeniería de sistemas de la Universidad Del Norte 👨🏻‍🎓👨🏻‍🎓👨🏿‍🎓. A continuación verás los comandos disponibles. \n1. 📉 /grafo V E K: Recibe como datos de entrada la cantidad de vértices de un grafo, la cantidad de aristas y el número máximo de aristas por vértice.\n 2. \n")


def graph(update, context):
    print(context.args)
    if len(context.args) < 3:
        update.message.reply_text("🤖 Debes ingresar tres valores G(V, E, K)")
        return
    elif len(context.args == 0):
        update.message.reply_text(
            "/grafo V E K: Recibe como datos de entrada la cantidad de vértices (V) de un grafo, la cantidad de aristas (E) y el número máximo de aristas por vértice (K).")
    for item in context.args:
        if not item.isnumeric():
            update.message.reply_text(
                "Ops, parece que uno de ts argumentos no es un número, intenta nuevamente.")
            break
    arguments = context.args
    text_reply = f"Genial, tus valores son \n Vertices(V): {arguments[0]} \nAristas(E): {arguments[1]} \nMax por vertice(K): {arguments[2]}"
    update.message.reply_text(text_reply)


dispatcher.add_handler(CommandHandler('ayuda', help))
dispatcher.add_handler(CommandHandler('grafo', graph))

updater.start_polling()
updater.idle()
