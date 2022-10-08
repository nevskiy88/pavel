def qqq():
    a = int(input())
    list_1 = []
    for i in range(a):
        number = int(input())
        list_1.append(number)
    return list_1

def mean(list_1):
    sum = 0
    w = len(list_1)
    for i in list_1:
        sum += i
        mean_number = sum / w
    return mean_number

a = qqq()
print(min(a))
print(max(a))
a.sort()
print(a)
print(mean(a))
