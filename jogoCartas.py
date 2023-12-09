from cartas import montarBaralho, numeros

def distribuir():
    baralho = montarBaralho()
    if len(baralho) < 12:
        raise ValueError("Número insuficiente de cartas no baralho para distribuir para 4 jogadores.")
    
    maos_jogadores = [baralho[i:i+3] for i in range(0, 12, 3)]  # Cada jogador recebe exatamente 3 cartas
    cartas_mesa = baralho[-2:]
    
    return maos_jogadores, cartas_mesa

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

