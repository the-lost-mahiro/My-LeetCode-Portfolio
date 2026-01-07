class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1, map2 = set(nums1), set(nums2)
        return [list(map1 - map2), list(map2 - map1)]
