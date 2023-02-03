def find_idx(new_p, hp):
    findPos = -1
    for i in range(len(pokemons)):
        pair = pokemons[i]
        if hp >= list(pair.values())[0] :
            findPos = i
            break

    if findPos == -1:
        findPos = len(pokemons)

    insert_data(findPos, {new_p: hp})

def insert_data(idx, new_p):
    if idx < 0 or idx > len(pokemons):
        print("데이터 삽입 범위를 벗어났습니다.")
        return

    pokemons.append(None)

    for i in range(len(pokemons)-1, idx, -1): # 리스트 맨끝번부터 값 삽입하고자 하는 idx 까지 거꾸로 순회
        pokemons[i] = pokemons[i-1] # 이전 값을 그 다음번 인덱스에 복사
        pokemons[i-1] = None # 이전 인덱스 비우기. 반복

    pokemons[idx] = new_p # None으로 비워진 idx번에 값 삽입.

pokemons = [{"파이리": 50}, {"피카츄": 40}, {"야도란": 30}, {"버터풀": 20}]

if __name__ == "__main__":
    while True:
        print(pokemons)
        name = input("새 포켓몬 이름: ")
        hp = int(input("포켓몬 체력 : "))
        find_idx(name, hp)
        print(pokemons)

##
