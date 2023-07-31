# fibonaci n
n = 100
f = [0] * n #create a list with n elements equal 0

f[0] = 0
f[1] = 1

for i in range(2, n):
    f[i] = f[i-1] + f[i-2]

print(f[10])