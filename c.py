def f():
    N = int(input())
    turl = []
    for i in range(N):
        tem = list(map(int,input().split()))
        num = tem[0]
        tu = []
        for j in range(num):
            tu.append(tem[j*2+1:j*2+3])
        turl.append(tu)
    for i in range(N):
        num = len(turl[i])
        for j in range(num-1):
            if j==0:
                s = (turl[i][j+1][0]-turl[i][j][0])*turl[i][j][1]
                turl[i][j].append(s)
            else:
                s = turl[i][j-1][2]+(turl[i][j+1][0]-turl[i][j][0])*turl[i][j][1]
                turl[i][j].append(s)
        turl[i][num-1].append(-1)
    q = int(input())
    for qi in range(q):
        time = int(input())
        maxs=0
        maxi = -1
        for i in range(N):
            num = len(turl[i])
            ss=-1
            if num==1:
                ss=time*turl[i][0][1]
                if ss>maxs:
                    maxs=ss
                    maxi=i+1
                continue
            for j in range(1,num):
                if time <=turl[i][j][0]:
                    if j==1:
                        ss=(time-turl[i][j-1][0])*turl[i][j-1][1]
                    else:
                        ss=turl[i][j-2][2]+(time-turl[i][j-1][0])*turl[i][j-1][1]
            if ss==-1:
                ss = (time-turl[i][num-1][0])*turl[i][num-1][1]+turl[i][num-2][2]
            if ss>maxs:
                maxs=ss
                maxi=i+1
        print(maxi)
    

f()