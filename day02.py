with open('src.txt') as f:
    lines = f.read().splitlines()

you_dict = {'X':1,'Y':2,'Z':3}

def win(elf, you):
    if elf == 'A':
        if you == 'Y':
            return 6
        elif you == 'X':
            return 3
        else:
            return 0
    elif elf == 'B':
        if you == 'Z':
            return 6
        elif you == 'Y':
            return 3
        else:
            return 0
    else:
        if you == 'X':
            return 6
        elif you == 'Z':
            return 3
        else:
            return 0

score = 0
for x in lines:
    temp = x.split()
    elf = temp[0]
    you = temp[1]
    score += win(elf,you)
    score += you_dict[you]

print(score)

#pt 2

score_dict = {'X':0,'Y':3,'Z':6}
elf_dict = {'A':1, 'B':2, 'C':3}

def win2(elf,win_or_not):
    if win_or_not == 'Y':
        return elf_dict[elf]
    elif win_or_not == 'X':
        if elf == 'A':
            return elf_dict['C']
        elif elf == 'B':
            return elf_dict['A']
        else:
            return elf_dict['B']
    else:
        if elf == 'A':
            return elf_dict['B']
        elif elf == 'B':
            return elf_dict['C']
        else:
            return elf_dict['A']

score2 = 0
for x in lines:
    temp = x.split()
    play = temp[0]
    win_or_not = temp[1]
    score2 += score_dict[win_or_not]
    score2 += win2(play, win_or_not)

print(score2)
