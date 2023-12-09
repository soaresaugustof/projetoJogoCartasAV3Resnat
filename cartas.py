import random

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']

def montarBaralho():
    baralho = [{'Numero': carta, 'Naipe': naipe} for naipe in naipes for carta in numeros]
    random.shuffle(baralho)
    return baralho