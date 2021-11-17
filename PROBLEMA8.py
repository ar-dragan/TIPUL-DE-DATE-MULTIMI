A=set(map(int, input('Introdu elemnetele multimii A ').split()))
nr_intregi=True
for a in A:
    if type(a)!=int:
        nr_intregi=False
if nr_intregi==True:
    B=set(map(int, input('Introdu elemnetele multimii B ').split()))
    nr_intregi2=True
    for b in B:
        if type(b)!=int:
            nr_intregi2=False
    if nr_intregi2==True:
        print('a)intersectia multimilor=',A.intersection(B))
        print('b)reuniunea multimilor=',A.union(B))
        print('c)diferenta multimilor A-B=',A.difference(B))
        print('d)intersectia multimilor B-A=',B.difference(A))
    else:
        print("Doar numere intregi!")
else:
    print("Doar numere intregi!")