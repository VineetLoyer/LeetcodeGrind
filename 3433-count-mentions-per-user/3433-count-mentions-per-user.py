class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        parsed = []
        for typ, ts, payload in events:
            parsed.append((int(ts), typ, payload))
        parsed.sort(key=lambda x: x[0])

        online = [True] * numberOfUsers
        offline_end = [0] * numberOfUsers
        heap = []  # (end_time, user)

        direct = [0] * numberOfUsers      # counts from explicit "idX" mentions
        here_acc = [0] * numberOfUsers    # accumulated HERE mentions per user
        last_here = [0] * numberOfUsers   # globalHere value when user last became online

        globalHere = 0
        globalAll = 0

        i = 0
        n = len(parsed)

        while i < n:
            t = parsed[i][0]

            # 1) Apply auto-online transitions up to time t (before any events at t)
            while heap and heap[0][0] <= t:
                end_t, u = heappop(heap)
                # Only accept if this is the current scheduled end
                if offline_end[u] == end_t and not online[u]:
                    online[u] = True
                    last_here[u] = globalHere  # starts accruing HERE from now (before messages at t)

            # 2) Collect all events at timestamp t
            offs = []
            msgs = []
            while i < n and parsed[i][0] == t:
                _, typ, payload = parsed[i]
                if typ == "OFFLINE":
                    offs.append(payload)   # payload is user id as string
                else:
                    msgs.append(payload)   # payload is mentions string
                i += 1

            # 3) Process OFFLINE events first (per statement)
            for uid_str in offs:
                u = int(uid_str)
                if online[u]:
                    # cash in HERE mentions earned while online
                    here_acc[u] += globalHere - last_here[u]
                online[u] = False
                new_end = t + 60
                if new_end > offline_end[u]:
                    offline_end[u] = new_end
                heappush(heap, (offline_end[u], u))

            # 4) Process MESSAGE events
            for mentions in msgs:
                if mentions == "ALL":
                    globalAll += 1
                elif mentions == "HERE":
                    globalHere += 1
                else:
                    for tok in mentions.split():
                        if tok.startswith("id"):
                            direct[int(tok[2:])] += 1

        # 5) Finalize HERE for users still online
        for u in range(numberOfUsers):
            if online[u]:
                here_acc[u] += globalHere - last_here[u]

        # Everyone gets all ALL-mentions; HERE and direct already computed
        return [direct[u] + here_acc[u] + globalAll for u in range(numberOfUsers)]