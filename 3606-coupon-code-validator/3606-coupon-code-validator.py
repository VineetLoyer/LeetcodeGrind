class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        rank = {cat: i for i, cat in enumerate(categories)}
        ok_code = re.compile(r'^[A-Za-z0-9_]+$').fullmatch

        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if a and b in rank and c and ok_code(c):
                valid.append((rank[b], c))

        valid.sort(key=lambda x: (x[0], x[1]))  # by category rank, then code
        return [c for _, c in valid]