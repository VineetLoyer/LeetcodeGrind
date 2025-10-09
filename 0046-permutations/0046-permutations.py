class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #use backtracking
        # - fix one element at start
        # - recursively permute the rest
        # - track which eleement are in current permutation(using set or boolean array)
        # - build the permutation until it contains all elements, then add to the output.
        result = []
        def backtrack(path,used):
            #base case: if path is a complete permutation
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue #skip already used eleemnts
                used[i]=True
                path.append(nums[i])

                #continue building this permutation
                backtrack(path,used)
                path.pop()

                used[i]=False
        used = [False]*len(nums)
        backtrack([],used)
        return result
