N = int(input())
original=[]
ordenado = []
cont = 0
for i in range(N):
	X = int(input())
	k = list(map(int,input().split()))
	for y in range(X):
		original.insert(y,int(k[y]))		
	ordenado = sorted(original, reverse=True)
	for x in range(len(original)):	
		if ordenado[x] == original [x]:	cont+=1
	print(cont)		
		
