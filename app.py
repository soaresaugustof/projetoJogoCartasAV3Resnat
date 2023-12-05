from jogoCartas import distribuir, calcularPontuacao, melhorTrio
from cartas import numeros

maos, cartasMesa = distribuir()

for i, mao in enumerate(maos):
    print(f"Jogador {i + 1}: {mao}")

print(f"Cartas na mesa: {cartasMesa}")

pontuacoes = [calcularPontuacao(mao, numeros) for mao in maos]

melhores_trios = melhorTrio(maos, cartasMesa)
for i, (melhor_trio, pontuacao) in enumerate(melhores_trios):
    print(f"Jogador {i + 1} - Melhor Trio: {melhor_trio}, Pontuação: {pontuacao}")

indice_vencedor = pontuacoes.index(max(pontuacoes))
print(f"O jogador {indice_vencedor + 1} venceu!")