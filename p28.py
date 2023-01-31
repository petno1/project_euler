import numpy as np
n = 1001
arr = np.zeros((n,n))
x, y = n//2, n//2

arr[x,y] = 1
y += 1
arr[x, y] = 2
count = 2

#down
for i in range(10000):
    
    x += 1
        
    while 0 <= x-1<= 1000 and 0 <= y-1 <= 1000 and arr[x-1,y-1] != 0:
        count += 1
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            arr[x,y] = count
        
        x += 1
        #left
    y -= 1
    x -= 1
    while 0 <= x-1<= 1000 and 0 <= y+1 <= 1000 and arr[x - 1, y + 1] != 0:
        count += 1
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            arr[x,y] = count
        y -= 1
        
    y += 1
    x -= 1
        
        #up
        
    while 0 <= x+1<= 1000 and 0 <= y+1 <= 1000 and  arr[x+1, y+1] != 0 :
        count += 1
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            arr[x,y] = count
        x -= 1    
            
    x += 1
    y += 1
        
    while 0 <= x+1<= 1000 and 0 <= y-1 <= 1000 and arr[x+1, y-1] != 0:
        count += 1
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            arr[x,y] = count
        y += 1   
        
    y -= 1
       
diag_1 = np.arange(n)
diag_2 = np.arange(n-1, -1, -1)
diag_sum = np.sum(arr[diag_1, diag_1]) + np.sum(arr[diag_2, diag_1])
print(int(diag_sum - 1))
