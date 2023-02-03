
pokemons = ['피카츄', '라이츄', '파이리', '꼬부기', '이상해']


def delete_data(idx):

    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    # for i in range(idx+1, len(pokemons)):
    #     pokemons[i-1] = pokemons[i]
    #     pokemons[i] = None
    #
    # del(pokemons[len(pokemons)-1])

    for i in range(idx, len(pokemons)):
        del(pokemons[-1])

    

if __name__ == "__main__":
    print(pokemons)
    delete_data(2)
    print(pokemons)

