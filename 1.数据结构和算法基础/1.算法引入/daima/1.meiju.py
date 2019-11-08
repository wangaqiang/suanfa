#a+b+c=1000,并且a^2+b^2=c^2,求a,b,c组合

# for a in range(1001):
    # for b in range(1001):
        # for c in range(1001):
            # if a+b+c==1000 and a**2+b**2==c**2:
                # print(a,b,c)

# c = 1000- a-b
for a in range(1001):
    for b in range(1001):
        c=1000-a-b
        if a**2 + b**2 ==c**2:
            print(a,b,c)