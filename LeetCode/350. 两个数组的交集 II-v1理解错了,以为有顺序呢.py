class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1 
        
        res_l = []
        max_len = 0
        for i in range(len(nums2), 0, -1):
            for j in range(0, i):
                sub_nums2 = nums2[j:i]

                if check(nums1, sub_nums2):
                    if max_len < i-j:
                        max_len = i-j
                        res_l = sub_nums2.copy()
        
        return res_l
    
def check(nums1, sub_nums2):
    res = False
    for i in range(len(nums1) - len(sub_nums2) + 1):
        flag = True
        for j in range(len(sub_nums2)):
            if nums1[i+j] != sub_nums2[j]:
                flag = False
                break

        if flag == True:
            res = True
            break
    return res