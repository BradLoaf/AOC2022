with open('src.txt') as f:
    lines = f.read().splitlines()

rucksack = [(x[:len(x)//2], x[len(x)//2:]) for x in lines]

def dupe(sack):
    for x in sack[0]:
        if x in sack[1]:
            return x


letters = []
for sack in rucksack:
    letters.append(dupe(sack))

sum = 0
for letter in letters:
    if letter.isupper():
        sum += (ord(letter)-38)

    else:
        sum += (ord(letter)-96)

print(sum)

#pt 2

groups = []
group = []
for x in range(len(lines)):
    if x % 3 == 0 and x > 0:
        groups.append(group)
        group = [lines[x]]
    else:
        group.append(lines[x])

groups.append(group)

let = []
for x in groups:
    let.append([y for y in x[0] if y in [z for z in x[1] if z in x[2]]])

let = [x[0] for x in let]

sum = 0
for letter in let:
    if letter.isupper():
        sum += (ord(letter)-38)

    else:
        sum += (ord(letter)-96)

print(sum)
