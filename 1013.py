import math
a, b, c = input().split(' ')
R=(int(a)+int(b)+abs(int(a)-int(b)))/2
R2=(int(R)+int(c)+abs(int(R)-int(c)))/2
print("%d eh o maior" % R2)
