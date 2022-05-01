from pipe import where, select

arr = [1, 2, 3, 4, 5, 6, 7]

resArr = list(arr | where(lambda x: x % 2 == 0))

print(resArr)

resArr2 = list(arr | select(lambda x: x * 2))

print(resArr2)
