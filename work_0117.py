
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
