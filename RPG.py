nm = input("Qual o nome do personagem?")
hp = int(input(f'Qual vai ser a vida do personagem {nm}'))
if hp > 0:
    print('Personagem tem uma quantidade de vida aceitavel.')
    print(f'Então o personagem {nm} está vivo com {hp} de HP.')
else:
    print('A vida do personagem é invalida.')
    print(f'Pensando assim o personagem {nm} está morto com {hp} de HP.')