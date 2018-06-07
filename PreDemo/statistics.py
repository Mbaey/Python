fr = open(r'data/xyj.txt', 'br')

characters = []
stat = {}

re = fr.read().decode('utf-8')
# i=0
for char in re:
    # i +=1
    # if(i > 20):
    #     break
    char = char.strip()
    l = len(char)
    if (l == 0 ):
        continue

    if(not char in characters):
        characters.append(char)

    if(not char in stat):
        stat[char] = 0

    stat[char] += 1


print(len(characters))
stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)

for i in range(20):
    print(stat[i][0], stat[i][1])

fr.close()
