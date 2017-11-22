N = int(input())
par=[]
impar=[]
for i in range(N):
	v = int(input())
	if v % 2 == 0:
		par.append(v)
	else:
		impar.append(v)
par.sort()
impar.sort()
par.extend(impar[::-1])
for i in par:
   print(i)
		
