times = 'Internacional','Sao Paulo','Atletico mineiro','Vasco','Flamengo','Botafogo','Gremio','Atletico'
print(f'Os 5 primeiros sao {times[:5]}')
print(f'Os 4 ultimos sao {times[-4:]}')
print(f'Em ordem alfabatica{sorted(times[:])}')
print('O Atletico esta na {} posiçao'.format(times.index('Atletico')+1))