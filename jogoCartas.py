from cartas import montarBaralho, numeros

def distribuir():
    baralho = montarBaralho()
    maos = [baralho[i:i+3] for i in range(0, len(baralho), 3)]
    cartasMesa = baralho[-2:]
    return maos, cartasMesa

def calcularPontuacao(cartas, numeros):
    pontuacao = 0

    #ponto para carta do mesmo naipe
    naipes = set(carta['Naipe'] for carta in cartas)
    for naipe in naipes:
        qtdCartasDoNaipe = sum(1 for carta in cartas if carta['Naipe'] == naipe)
        pontuacao += qtdCartasDoNaipe

    #pontos para carta em sequência
    cartasOrdenadas = sorted([carta['Numero'] for carta in cartas], key = lambda x: numeros.index(x))
    for i in range(len(cartasOrdenadas) - 1):
        if numeros.index(cartasOrdenadas[i + 1]) - numeros.index(cartasOrdenadas[i]) == 1:
            pontuacao += 2

    return pontuacao

def melhorTrio(maos, cartasMesa):
    triosDeMelhorPontuacao = []

    for mao in maos:
        cartasTotais = mao + cartasMesa
        trios = [cartasTotais[i:i+3] for i in range(0, len(cartasTotais) - 2)]
        pontuacaoTrios = [calcularPontuacao(trio, numeros) for trio in trios]
        indexMelhorTrio = pontuacaoTrios.index(max(pontuacaoTrios))
        triosDeMelhorPontuacao.append((trios[indexMelhorTrio], max(pontuacaoTrios)))

    return triosDeMelhorPontuacao

