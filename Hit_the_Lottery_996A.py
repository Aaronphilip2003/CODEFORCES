cash=int(input())
copy=cash
notes=0
denominations=[100,20,10,5,1]
 
 
for i in denominations :
  if i<=cash:
    fac=cash//i
    cash = cash - fac*i
    notes = notes + fac
print(notes)
