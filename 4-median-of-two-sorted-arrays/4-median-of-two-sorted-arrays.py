class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        while i < n1:
            arr.append(nums1[i])
            i += 1
        while j < n2:
            arr.append(nums2[j])
            j += 1

        n = len(arr)
        if n % 2 == 0:
            return (arr[n/2] + arr[n/2 - 1]) / 2.0
        return (arr[n/2])