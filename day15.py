
pokemons = ['피카츄', '라이츄', '파이리', '꼬부기', '이상해']


def insert_data(idx, pokemon):

    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons)-1, idx, -1):
        pokemons[i] = pokemons[i -1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon

print(pokemons)
insert_data(3, '어니부기')
print(pokemons)
insert_data(2, '거북왕')

katok = ['다현', '정연', '쯔위', '사나', '지효']
