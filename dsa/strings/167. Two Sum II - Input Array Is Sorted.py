numbers = [2,7,11,15]
target = 9
left = 0
right = len(numbers) - 1
while left < right:
    sums = numbers[left] + numbers[right] 
    if(sums == target):
        print(left+1)
        print(right+1)
        break
    elif sums < target:
        left += 1
    else:
        right -=1