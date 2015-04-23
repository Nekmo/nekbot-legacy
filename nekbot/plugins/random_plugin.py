# coding=utf-8
import requests
from nekbot.core.commands import command

__author__ = 'nekmo'

@command
def veryrandom(msg, min=1, max=6, base=10, num=1):
    """Los datos generados por veryrandom provienen de random.org, lo cual
    es una garantía adicional de la aleatoriedad de los resultados. Se
    obtendrá un número aleatorio entre los 2 definidos, ambos inclusive.
    """
    url = 'http://www.random.org/integers/'
    try:
        data = requests.get(url, params={
            'min': min, 'max': max, 'base': base, 'num': num,
            'col': 1, 'format': 'plain', 'rdn': 'new',
        }).text
    except Exception as e:
        data = str(e)
    msg.reply(data.replace('\n', ' '))
