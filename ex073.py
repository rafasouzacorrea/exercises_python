"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

time = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
        'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
        'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
c = time.index('Chapecoense')
print(f'a) {time[0:5]} '
      f'\nb) {time[-4:]} '
      f'\nc) {sorted(time)} '
      f'\nd) {c + 1}')
