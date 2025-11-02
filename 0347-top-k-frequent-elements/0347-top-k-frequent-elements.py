class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #brute force, making a frequency dict and then converting to array and returning top k
        # # count={}
        # # for num in nums:
        # #     count[num]=1+count.get(num,0)
        # # arr=[]
        # # for num,cnt in count.items():
        # #     arr.append([cnt,num])
        # # arr.sort()
        # # res=[]
        # # while len(res)<k:
        # #     res.append(arr.pop()[1])
        # # return res

        # # we can optimize this using bucket sort, in bucket sort we have frequencies as buckets, and each bucket has a set of numbers.
        # count={}
        # freq=[[] for _ in range(len(nums)+1)]
        # for num in nums:
        #     count[num]=1+count.get(num,0)
        # for num,cnt in count.items():
        #     freq[cnt].append(num)
        # res=[]
        # for i in range(len(freq)-1,0,-1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res)==k:
        #             return res
        freq = Counter(nums)
        # Sort unique elements based on count (descending)
        sorted_unique = sorted(freq, key=lambda x: -freq[x])
        return sorted_unique[:k]