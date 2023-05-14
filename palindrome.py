k= input("ENTER THE NO. : ")
f= k
h= len(k)
p= ''
for i in range (h-1, -1, -1):
    print(k[i] , end="")
    p= p + k[i]
    
if f==p:
    print(" --> {it is palindrome}")
    
else :
    print(" --> {it is not palindrome}")
    