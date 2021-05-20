from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram
from my_graph import graph_img
from secuencia import get_subsequence
updater = Updater(
    token='1822223787:AAEl8_-tM3vxxTsTPSHqXQy4Ha0DW4tMdIc', use_context=True)
dispatcher = updater.dispatcher


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="🤖 Hola, este bot fue creado por los mejores estudiantes de <b>Ingeniería de sistemas</b> de la Universidad Del Norte 👨🏻‍🎓👨🏻‍🎓👨🏿‍🎓. A continuación verás los comandos disponibles. \n1. 📉 /grafo V E K: Recibe como datos de entrada la cantidad de vértices de un grafo, la cantidad de aristas y el número máximo de aristas por vértice.\n 2. ♻ /recurrencia a b c d: Recibe los coeficientes de un polinomio caracteristico para una relacion de recurrencia \n3. 📏 /serie a b c d: Recibe una secuencia ORDENADA y determina una subsecuencia de la sucesion de <b>fibonacci</b>", parse_mode=telegram.ParseMode.HTML)


def secuencia(update, context):
    # CONVERTIR LOS ELEMENTOS DE LOS ARGUMENTOS A NUMEROS, VALIDAR PRIMERO
    for item in context.args:
        if not item.isnumeric():
            update.message.reply_text(
                "❌Ops, parece que uno de tus argumentos no es un número, intenta nuevamente.❌")
            break

    # AGREGAR CADA ELEMENTO CADENA EN UNA LISTA NUMERICA
    arguments = [int(element) for element in context.args]
    if is_ascendente(arguments):
        resultado = get_subsequence(arguments, 0)
        if len(resultado) > 0:
            update.message.reply_text(
                f"🤖Hey!, he encontrado esta secuencia: <b>{resultado}</b> \nNota que cada numero es el resultado de la suma de los dos inmediatamente anteriores y que todos ellos se encuentran en la secuencia que me diste. Genial, ¿No?", parse_mode=telegram.ParseMode.HTML)
        else:
            update.message.reply_text(
                f"😢 No he podido encontrar una secuencia que tenga el flow de fibonacci, lo siento. ", parse_mode=telegram.ParseMode.HTML)
            pass
    else:
        update.message.reply_text(
            "❌Lo siento, la secuencia debe ser <b>ascendente</b>📉", parse_mode=telegram.ParseMode.HTML)


def is_ascendente(sequence):
    swp = True
    for element in range(0, len(sequence) - 1, 1):
        if sequence[element] < sequence[element + 1]:
            swp = True
        elif sequence[element] > sequence[element + 1]:
            swp = False
            break
    return swp


def graph(update, context):
    if len(context.args) < 3:
        update.message.reply_text("🤖 Debes ingresar tres valores G(V, E, K)")
        return
    # else:
    #     update.message.reply_text(
    #         "/grafo V E K: Recibe como datos de entrada la cantidad de vértices (V) de un grafo, la cantidad de aristas (E) y el número máximo de aristas por vértice (K).")
    for item in context.args:
        if not item.isnumeric():
            update.message.reply_text(
                "❌Ops, parece que uno de tus argumentos no es un número, intenta nuevamente.❌")
            break
    arguments = context.args
    graph_img(int(arguments[0]), int(arguments[2]), int(arguments[1]))
    text_reply = f"✅Genial, tus valores son \nVertices(V): {arguments[0]} \nAristas(E): {arguments[1]} \nMax por vertice(K): {arguments[2]}"
    update.message.reply_text(text_reply)
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
                          photo=open("graph.png", "rb"))


dispatcher.add_handler(CommandHandler('ayuda', help))
dispatcher.add_handler(CommandHandler('grafo', graph))
dispatcher.add_handler(CommandHandler('secuencia', secuencia))

updater.start_polling()
updater.idle()
