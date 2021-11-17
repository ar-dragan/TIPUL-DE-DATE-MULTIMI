import itertools
mult={1,2,3,4}
for i in range(len(mult)):
    submult=itertools.combinations(mult, i+1)
    print(set(submult))