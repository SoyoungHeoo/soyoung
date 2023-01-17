
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