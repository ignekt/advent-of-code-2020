f = open('input.txt')

nums = {int(k): v+1  for v,k in enumerate(f.readline().split(','))}

last_number_spoken = nums.keys()[-1]
turn = len(nums) + 1
speaks = None
del nums[last_number_spoken]

while True:
    if turn == 2021: break
    if last_number_spoken not in nums:
        nums[last_number_spoken] = turn - 1
        speaks = 0
    else:
        speaks = turn - 1 - nums[last_number_spoken] 
        nums[last_number_spoken] = turn - 1
    last_number_spoken = speaks
    turn += 1

print(speaks)
