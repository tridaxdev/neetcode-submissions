class Solution:      
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        if 0 in counts and counts[0] >= 3:
            res.append([0, 0, 0])

        pos = sorted([x for x in counts if x > 0])
        neg = sorted([x for x in counts if x < 0])

        if not pos or not neg:
            return res

        if 0 in counts:
            for p in pos:
                if -p in counts:
                    res.append([-p, 0, p])

        for p in pos:
            for n in neg:
                diff = -p - n
                if diff > n:
                    continue
                if diff < neg[0]:
                    break
                if diff == n:
                    if counts[n] >= 2:
                        res.append([n, n, p])
                elif diff in counts:
                    res.append([diff, n, p])

        for n in neg:
            for p in pos:
                diff = -n - p
                if diff > p:
                    continue
                if diff < pos[0]:
                    break
                if diff == p:
                    if counts[p] >= 2:
                        res.append([n, p, p])
                elif diff in counts:
                    res.append([n, diff, p])

        return res
