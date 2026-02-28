import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for s in score:
        heapq.heappush(heap, s)
        
        if len(heap) > k:
            heapq.heappop(heap)
        
        answer.append(heap[0])  # 항상 최하위 점수
    
    return answer