
  # 7.1
year_list = [1999+i for i in range(0,5)]
print(year_list)

  # 7.2
print(year_list[3])

  # 7.3
print(year_list[-1])

  # 7.8
surprise = ["Groucho", "Chico", "Harpo"]

  # 7.9
surprise[2] = surprise[2].lower()[::-1].title()
print(surprise)

  # 7.10
odd_nums = [i for i in range(10) if i % 2 == 0]
print(odd_nums)

  # 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
]
start2 = "Someone better"

for word1, word2 in rhymes:
    line1 = [start.title() + "!" for start in start1]
    line1.append(word1.title() + "!")
    print(' '.join(line1))
    print(start2, word2 + '.')


  # 8.1
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}

  # 8.2
print(e2f['walrus'])

  # 8.3
words = list(e2f.items())
# f2e = {}
# for k, v in words:
#     f2e[v] = k
f2e = { v:k for k, v in words}

print(f2e)

  # 8.4
key = [k for k, v in e2f.items() if v == "chien"]
print(key[0])

  # 8.5
for k in list(e2f.keys()):
    print(k)

  # 8.6
life = {
    'animals': {
    'cat': 'Henri',
    'octopi': 'Grumpy',
    'emus': 'Lucy'
    },
    'planets':{},
    'other':{}
}

  # 8.7
print(life.keys())

  # 8.8
key_1 = list(life.keys()) # [animals, planets, other]
key_2 = [list(i.keys()) for i in list(life.values()) if list(i.keys())]
for k in key_1:
    print(k)
for k in key_2[0]:
    print(k)

    # list(life.values) = [{'cat': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'}, {}, {}]
    #  ㄴ> 순회하며 key 들이 있는 경우 리스트로 묶어서 가져오기
    # 결과물 : [['cat', 'octopi', 'emus']]
    # for문 돌려서 출력

  # 8.8 - 방법2
key_list = []
items = list(life.items())
print('items : ', items)
for i in items:
    print(i)
    key_list.append(i[0])
    if type(i[1]) == dict and i[1].keys():
        for key2 in list(i[1].keys()):
            key_list.append(key2)
print(key_list)

    # 빈 리스트(key_list) 만들기
    # items 리스트 만들기
    # items 리스트 순회하며 key 저장, 해당 key가 가지는 value의 타입, 빈 리스트 여부 확인
    # 저장할 하위 키가 있을 시 추가로 append
    # key_list 출력



  # 8.9
print(life['animals']['cat'])

  # 8.10
square = {i:i**2 for i in range(10)}
print(square)

  # 8.13
dict_glass = dict(zip(('optimist', 'pessimist', 'troll'), ('The glass is half full', 'The glass is half empty', 'How did you get the glass?')))
print(dict_glass)

  # 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']

movie = dict(zip(titles, plots))
print(movie)