class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        d1 = deque(sentence1.split())
        d2 = deque(sentence2.split())
        if len(d1)>len(d2):
            d1,d2=d2,d1
        
        while d1 and d2 and d1[0]==d2[0]:
            d1.popleft()
            d2.popleft()

        while d1 and d2 and d1[-1]==d2[-1]:
            d1.pop()
            d2.pop()
        
        return not d1