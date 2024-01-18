times = ('Palmeiras',
        'Gremio',
        'Atletico-MG',
        'Flamengo',
        'Botafogo',
        'Bragantino',
        'Fluminense',
        'Athletico-PR',
        'Internacional',
        'Fortaleza',
        'São Paulo',
        'Cuiaba',
        'Corinthians',
        'Cruzeiro',
        'Vasco',
        'Bahia',
        'Santos',
        'Goias',
        'Coritiba',
        'América-MG')
#5 PRIMEIROS COLOCADOS
print(f'Os 5 primeiros colocados são {times[:5]}')
#OS 4 ÚLTIMOS
print(f'Os 4 últimos colocados são {times[-4:]}')
#ORDEM ALFABÉTICA
print(f'Os times em otdem alfabética são {sorted(times)}')
#posição GALÃO DA MASSA
print(f'A posição do Maior de Minas é {times.index("Atletico-MG") + 1}º colocado')