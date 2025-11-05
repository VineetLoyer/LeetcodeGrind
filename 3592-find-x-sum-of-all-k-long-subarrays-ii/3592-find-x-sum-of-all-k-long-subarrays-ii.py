from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n: 
            return []

        cnt = defaultdict(int)
        in_top = set()
        small = []   # TOP:    (freq, value)  -> weakest at root
        large = []   # REST:  (-freq,-value) -> strongest at root
        sum_top = 0
        distinct = 0
        ans = []

        def push_small(v):
            f = cnt.get(v, 0)
            if f > 0:
                heapq.heappush(small, (f, v))

        def push_large(v):
            f = cnt.get(v, 0)
            if f > 0:
                heapq.heappush(large, (-f, -v))

        def clean_small_peek():
            # weakest in TOP
            while small:
                f, v = small[0]
                if v not in in_top or cnt.get(v, 0) != f or f == 0:
                    heapq.heappop(small)
                    continue
                return f, v
            return None

        def clean_large_peek():
            # strongest in REST
            while large:
                nf, nv = large[0]
                f, v = -nf, -nv
                if v in in_top or cnt.get(v, 0) != f or f == 0:
                    heapq.heappop(large)
                    continue
                return f, v
            return None

        def promote():
            nonlocal sum_top
            peek = clean_large_peek()
            if peek is None:
                return False
            f, v = peek
            heapq.heappop(large)
            in_top.add(v)
            sum_top += v * cnt[v]
            push_small(v)
            return True

        def demote():
            nonlocal sum_top
            peek = clean_small_peek()
            if peek is None:
                return False
            f, v = peek
            heapq.heappop(small)
            in_top.remove(v)
            sum_top -= v * cnt.get(v, 0)
            push_large(v)
            return True

        def rebalance():
            nonlocal sum_top
            target = min(x, distinct)

            # fill / shrink TOP to target size
            while len(in_top) < target and promote():
                pass
            while len(in_top) > target and demote():
                pass

            # boundary optimality swaps
            while True:
                s = clean_small_peek()
                l = clean_large_peek()
                if s is None or l is None:
                    break
                (fs, vs), (fl, vl) = s, l
                if (fl, vl) > (fs, vs):  # better outside -> swap
                    # demote vs
                    heapq.heappop(small)
                    in_top.remove(vs)
                    sum_top -= vs * cnt.get(vs, 0)
                    push_large(vs)
                    # promote vl
                    heapq.heappop(large)
                    in_top.add(vl)
                    sum_top += vl * cnt[vl]
                    push_small(vl)
                else:
                    break

        # --- build first window ---
        for j in range(k):
            v = nums[j]
            if cnt[v] == 0:
                distinct += 1
            was_in = (v in in_top)
            if was_in:
                sum_top += v
            cnt[v] += 1
            if was_in:
                push_small(v)
            else:
                push_large(v)
            rebalance()

        ans.append(sum_top)

        # --- slide the window ---
        for i in range(k, n):
            add_v = nums[i]
            rem_v = nums[i - k]

            # remove rem_v
            if rem_v in in_top:
                sum_top -= rem_v
            cnt[rem_v] -= 1
            if cnt[rem_v] == 0:
                distinct -= 1
                if rem_v in in_top:
                    in_top.remove(rem_v)  # purge ghost
                # do not push zero-count items
            else:
                if rem_v in in_top:
                    push_small(rem_v)
                else:
                    push_large(rem_v)

            # add add_v
            if cnt[add_v] == 0:
                distinct += 1
            was_in = (add_v in in_top)
            if was_in:
                sum_top += add_v
            cnt[add_v] += 1
            if was_in:
                push_small(add_v)
            else:
                push_large(add_v)

            rebalance()
            ans.append(sum_top)

        return ans
