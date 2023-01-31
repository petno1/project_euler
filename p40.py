num = ""
for i in range(1000000):
    num += str(i)

prod = int(num[1])*int(num[10])*int(num[100])*int(num[1000])*int(num[10000])*int(num[100000])*int(num[1000000])
print(prod)