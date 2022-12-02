with open('src.txt', "r") as f:
    lines = f.read().splitlines()

all_elf = []
elf = []
for x in lines:
    if x.isnumeric():
        elf.append(int(x))
    else:
        all_elf.append(sum(elf))
        elf = []

print(max(all_elf))

#pt 2
all_elf.sort(reverse = True)
print(sum(all_elf[:3]))
