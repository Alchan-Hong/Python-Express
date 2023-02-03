def erastos():
    lst = [i for i in range(2,101)]

    for i in range(2,100):
        for j in range(i+1,100):
            if j%i==0 and (j in lst):
                lst.remove(j)

    print(lst)

erastos()
