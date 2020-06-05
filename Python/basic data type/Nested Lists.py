if __name__ == '__main__':
    ms=[]
    sl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ms.append([name,score])
        sl.append(score)


slm = sorted(list(dict.fromkeys(sl)))[1]

for name,marks in sorted(ms):
    if marks == slm:
        print(name)

