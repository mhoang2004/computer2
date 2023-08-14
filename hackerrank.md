# The number of square integers within [a, b]
    - return floor(sqrt(b)) - ceil(sqrt(a)) + 1

# Find the second max value in python
    def second_max(a):
        return sorted(set(a))[-2]
    - not change the array a

# None-divisible subset
    - give a list s, find a subset that any two elements in subset not divisible by k

    ```python
    def noneDivisibleSubset(s, k):
        remain = [0] * k

        for value in range (len(s)):
            remain[value % k] += 1

        count = min(1, remain[0])

        if k % 2 == 0:
            count += min(1, remain[k//2])
        
        for i in range(1, k // 2 + 1):
            if 2*i != k:
                count += max(remain[i], remain[k - i])
        
        return count
    ```

# How to use bin(), int() buit-in function in Python
    - give a list: topic = ['11101', '10101', '11001', '10111', '10000', '01110'], choose 2 elements, 
    determine the maximum XOR of them, and how many maximum pair?

    ```python
    def binaryHandle(topic):
        maxXOR = 0
        maxPair = 0

        for i in range(len(topic) - 1):
            for j in range(i + 1, len(topic)):
                res = bin(int(topic[i], 2), int(topic[j], 2)).count('1')

                if res > maxXOR:
                    maxXOR = res
                    maxPair = 1
                elif res == maxXOR:
                    maxPair += 1
        return maxXOR, maxPair
    ```


