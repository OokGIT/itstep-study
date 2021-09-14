class CacheService(object):

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, item):
        self.data[key] = [item, 0]

    def __getitem__(self, key):
        value = self.data[key]
        value[1] += 1
        return value[0]

    def getcount(self, key):
        return self.data[key][1]


cs = CacheService()

# cs[n] = result
n = 1
while n != 0:
    n = int(input("Enter the Value for n:"))
    if n in cs.data:
        print("value is in cache:", n, cs[n])
    result = 1
    for i in range(n, 1, -1):
        result = result * i
        cs[i] = result
    print("factorial of", n, "is", result)
