def find_smallest_number(nums1, nums2, n):
    output = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i += 1
        else:
            output.append(nums2[j])
            j += 1
    output.extend(nums1[i:])
    output.extend(nums2[j:])
    return output[n - 1]

nums1 = [4, 9, 11]
nums2 = [3, 5, 7]
n = 5

result = find_smallest_number(nums1, nums2, n)
print(result)