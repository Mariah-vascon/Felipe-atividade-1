idades = [20, 25, 30, 35, 40]
nomes = ['Ana','João','Maria','Pedro','Carla']
amigos = []
for indice in range(len(nomes)):
    amigos.append((nomes[indice], idades[indice]))
for posicao_atual in range(len(amigos)):
    for proxima_posicao in range(posicao_atual + 1, len(amigos)):
        if amigos[posicao_atual][1] > amigos[proxima_posicao][1]:
            temp = amigos[posicao_atual]
            amigos[posicao_atual] = amigos[proxima_posicao]
            amigos[proxima_posicao] = temp
maiores_de_30 = []
for amigo in amigos:
    if amigo[1] > 30:
        maiores_de_30.append(amigo)
iniciais = []
for nome in nomes:
    iniciais.append(nome[0])
print('Lista de amigos:')
for amigo in amigos:
    print(amigo[0], '-', amigo[1], 'anos')