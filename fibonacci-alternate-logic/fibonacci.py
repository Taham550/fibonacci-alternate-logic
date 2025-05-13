# Fibonacci Series Generator using alternate logic
# 1 1 2 3 5 8 13 21....
n = int(input("Enter the number: "))
pre1 = 1 # let pre1 = 1and pre2 = 1
pre2 = 1
 
for i in range(1,n+1): # for loop fro 1 to n 
        
        if i == 1 or i == 2: # condition if i = 1 or i = 2 then we print  1
            print(1)
            
    
        elif i>2 and i%2 !=0: # but when i%2 i!=0 then it print only pre1 
            pre1 = pre1 + pre2 # for every i%2 != 0 condition it update pre1 value 
            print(pre1)
        else: # and when i%2 == 0 then it print pre2 
            pre2 = pre2 + pre1 # same as update pre2 value when i%2 == 0
        print(pre2)