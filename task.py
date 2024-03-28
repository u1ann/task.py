def concat_twice(nums):
    n = len(nums)
    ans = [0] * (2 * n) 
    for i in range(n):
        ans[i] = nums[i] 
        ans[i + n] = nums[i]  

    return ans

nums1 = [1, 2, 1]
result1 = concat_twice(nums1)
print(result1)  

nums2 = [1, 3, 2, 1]
result2 = concat_twice(nums2)
print(result2)  





def permute(nums):
    n = len(nums)
    ans = [0] * n  

    for i in range(n):
        ans[i] = nums[nums[i]]  

    return ans


nums3 = [0, 2, 1, 5, 3, 4]
result3 = permute(nums3)
print(result3)  
nums4 = [5, 0, 1, 2, 3, 4]
result4 = permute(nums4)
print(result4)





def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [round(kelvin, 5), round(fahrenheit, 5)]

temp1 = 36.50
result_temp1 = convert_temperature(temp1)
print(result_temp1)  

temp2 = 122.11
result_temp2 = convert_temperature(temp2)
print(result_temp2)  
