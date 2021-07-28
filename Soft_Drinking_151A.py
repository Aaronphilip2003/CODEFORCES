n,k,l,c,d,p,nl,np=[int(x) for x in input().split()]

vol=k*l
toasts1=int(vol/nl)

toasts2=c*d
toasts3=int(p/np)

print(int(min(toasts1,toasts2,toasts3)/n))