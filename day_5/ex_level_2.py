ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

# ages.append(ages[0])
# ages.append(ages[-2])
# print(ages)

a = len(ages)//2
print(a)

print(ages[a])

def Average(age):
    return sum(ages) / len(ages)

average = Average(ages)
print("Average of the ages =", round(average, 2))

