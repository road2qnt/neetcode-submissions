class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num #hitung nilai yang dibutuhkan
            if complement in seen: #Jika nilai tersebut sudah ada di dict
                return [seen[complement], i] #kembalikan index

            seen[num]=i #simpan nilai saat ini berdasar index
        return []
