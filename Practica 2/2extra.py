nums = [0,1,2,3,4,5]
suma = 0
for num in nums:
    suma+=num
print(f"La suma es: {suma}")

suma1 = sum( num for num in nums)
print(f"La suma es: {suma1}")