nums = input('Введите элементы списка через запятую >>> ').split(',')
IsH = True
IsL = True
for n in range(len(nums) - 1):
            if int(nums[n]) > int(nums[n + 1]):
                        IsH = False                        
            if int(nums[n]) < int(nums[n + 1]):            
                        IsL = False 
print(IsH or IsL)
