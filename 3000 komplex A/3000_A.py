def find_different_lines(path1, path2):
    file1 = open(path1, encoding="utf-8").readlines()
    file2 = open(path2, encoding="utf-8").readlines()
    list = []
    i = 0
    while i < len(file1):
        if file1[i] != file2[i]:
            list.append(i+1)
        i+=1
    return list

def write_list_to_file(lists, path):
    file = open(f"./{path}", "x")
    for item in lists:
        if type(item) == bool:
            if item:
                file.write("igen\n")
            else:
                file.write("nem\n")
        elif type(item) == list:
            sor = ""
            for i in item:
                sor += f"{i} "
            sor = sor.removesuffix(" ")
            file.write(f"{sor}\n")
        elif type(item) == set:
            sor = ""
            for i in item:
                sor += f"{i} "
            sor = sor.removesuffix(" ")
            file.write(f"{sor}\n")
        else:
            file.write(f"{item}\n")
    file.close()

szamok = [open("./input1.txt", encoding="utf-8").readlines(), open("./input2.txt", encoding="utf-8").readlines(), open("./input3.txt", encoding="utf-8").readlines()]

for r in range(1, 3):
    szamok[r] = [int(x[:-1]) for x in szamok[r]]
    eredmeny_lista = []
    
    eredmeny1 = [x for x in szamok[r] if x % 2 == 0]
    print(len(eredmeny1))
    eredmeny_lista.append(len(eredmeny1))
 
    eredmeny2 = 0
    for n in szamok[r]:
        if n > 0:
            eredmeny2+=n
    print(eredmeny2)
    eredmeny_lista.append(eredmeny2)

    lst = [x for x in szamok[r] if x % 2 == 1]
    eredmeny3 = max(lst)
    print(eredmeny3)
    eredmeny_lista.append(eredmeny3)

    lst = [x for x in szamok[r] if x % 2 == 1 and x < 0]
    lst2 = [x for x in szamok[r] if x % 2 == 1]
    eredmeny4 = len(lst) == len(lst2)
    print(eredmeny4)
    eredmeny_lista.append(eredmeny4)

    eredmeny5 = -1
    i = 0
    while i < len(szamok[r]) and (szamok[r][i] > 0 or szamok[r][i] % 2 == 1):
        i+=1
    if i != len(szamok[r]):
        eredmeny5 = i
    print(eredmeny5)
    eredmeny_lista.append(eredmeny5)

    eredmeny6 = []
    for n in szamok[r]:
        if n % 7 == 0:
            eredmeny6.append(n*5)
    print(eredmeny6)
    eredmeny_lista.append(eredmeny6)

    i = len(szamok[r])-1
    while i > 0 and szamok[r][i] > 0:
        i-=1
    print(szamok[r][i])
    eredmeny_lista.append(szamok[r][i])

    i = len(szamok[r])-1
    done = False
    while i > 1 and not done:
        if szamok[r][i] > 0 and szamok[r][i-1] < 0 and szamok[r][i-1] % 2 ==0:
            done = True
        i-=1
    if i == 1:
        print(-1, "nincs")
        eredmeny_lista.append([-1, "nincs"])
    else:
        print(i, szamok[r][i])
        eredmeny_lista.append([i, szamok[r][i]])
 
    eredmeny9 = -10000
    i = 0
    eri = 0
    for n in szamok[r]:
        if n < 0 and szamok[r][i] > eredmeny9:
            eredmeny9 = n
            eri = i
        i +=1
    if eredmeny9 == -10000:
        print("nincs ilyen")
    else:
        print(eri, eredmeny9)
        eredmeny_lista.append([eri, eredmeny9])

    i = 1
    while i < len(szamok[r])-1 and (szamok[r][i-1] + szamok[r][i+1]) / 2 != szamok[r][i]:
        i+=1
    eredmeny10 = i != len(szamok[r])-1
    print(eredmeny10)
    eredmeny_lista.append(eredmeny10)

    eredmeny11 = [-1000,-1000,-1000,-1000]
    i = len(szamok[r]) - 1 
    while i > 3:
        if eredmeny11[0]+eredmeny11[1]+eredmeny11[2]+eredmeny11[3] < szamok[r][i] + szamok[r][i-1] + szamok[r][i-2] + szamok[r][i-3]:
            eredmeny11 = [szamok[r][i], szamok[r][i-1], szamok[r][i-2], szamok[r][i-3]]
        i-=1
    eredmeny11.reverse()
    print(eredmeny11)
    eredmeny_lista.append(eredmeny11)

    eredmeny12 = [x for x in szamok[r] if x > 0 and x % 7 == 0]
    eredmeny12.sort()
    print(eredmeny12)
    eredmeny_lista.append(eredmeny12)

    elen = len(szamok[r]) // 2

    i = 0
    halmaz1 = []
    while i < elen:
        halmaz1.append(szamok[r][i])
        i+=1
    halmaz1 = set(halmaz1)

    halmaz2 = []
    while i < len(szamok[r]):
        halmaz2.append(szamok[r][i])
        i+=1
    halmaz2 = set(halmaz2)
    print(halmaz1.intersection(halmaz2))
    eredmeny_lista.append(halmaz1.intersection(halmaz2))

    eredmeny14 = []
    i = 0
    while i < 7:
        eredmeny14.append(round(len([x for x in szamok[r] if x % 7 == i]), 2))
        i+= 1
    print(eredmeny14)
    eredmeny_lista.append(eredmeny14)

    eredmeny15 = []
    i=0
    while i < 8:
        eredmeny15.append(max([x for x in szamok[r] if x % 8 == i]))
        i+= 1
    print(eredmeny15)
    eredmeny_lista.append(eredmeny15)

    eredmeny16 = []
    i=0
    while i < 9:
        lst = [x for x in szamok[r] if x % 9 == i]
        eredmeny16.append(round(sum(lst) / len(lst), 2))
        i+= 1
    print(eredmeny16)
    eredmeny_lista.append(eredmeny16)
    print("\n\n")
    write_list_to_file(eredmeny_lista, f"./output{r+1}.txt")
    print(find_different_lines(f"./mo_output{r+1}.txt", f"./output{r+1}.txt"))