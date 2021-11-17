A={'A','B','C','D'}
B=[[]]
for i in A:
    B+=[k+[i] for k in B]
print(sorted(B))