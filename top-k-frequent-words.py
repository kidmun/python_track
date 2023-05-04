class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = {}
        for i, w in enumerate(words):
            if w in count:
                count[w] = (count[w][0] + 1, i)
            else:
                count[w] = (1, i)
        my_heap = []
        heapify(my_heap)
        i = 0
        for key in count:
            if i < k:
                heappush(my_heap, (count[key][0], -1 * count[key][1], key))
            else:
                heappushpop(my_heap, (count[key][0], -1 * count[key][1], key))
            i += 1
        ans = []
        for i in range(k):
            ans.append(heappop(my_heap)[2])
        return ans[::-1]