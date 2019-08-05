import sys
N=[]
L=[]
lines = sys.stdin.readlines()
print("len(lines)=",len(lines))
print("lines=",lines)
for i in range(len(lines)):
  if i%2==0:
    print("i=",i)
    print("lines[i].strip()=",lines[i].strip())
    N.append(int(lines[i].strip()))
  else:
    Tem1=[Tem.strip() for Tem in lines[i].split()] 
    print("Tem1=",Tem1)
    L.append(list(map(int,Tem1)))
print("N=",N)
print("L=",L)

if len(N)!= len(L):
  print("Invalid Input") 

R0=[]
for i in range(len(N)):
  R1=[]
  R1.append(1)
  for j in range(1,N[i]):
    best =1
    for k in range(j):
      if L[i][k]<L[i][j]:
        best=max(best,R1[k]+1)
    R1.append(best)
  R0.append(R1[N[i]-1])
print("R0=",R0)
