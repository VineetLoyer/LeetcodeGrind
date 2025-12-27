class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        # Min-heap of available room indices
        free = list(range(n))
        heapq.heapify(free)

        # Min-heap of (end_time, room_index) for busy rooms
        busy = []

        # Count of meetings per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free all rooms whose meetings have finished by 'start'
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                # Use the smallest-index free room
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                # No room free; delay this meeting
                earliest_end, room = heapq.heappop(busy)
                new_end = earliest_end + duration
                heapq.heappush(busy, (new_end, room))
                count[room] += 1

        # Room with maximum number of meetings (smallest index on ties)
        best_room = 0
        for i in range(1, n):
            if count[i] > count[best_room]:
                best_room = i

        return best_room