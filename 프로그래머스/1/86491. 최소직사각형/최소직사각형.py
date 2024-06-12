def solution(sizes):
    w = []
    h = [] #가로, 세로를 저장할 리스트 생성
    
    #sizes에서 값을 꺼내서 큰 값은 w에, 작은 값은 h에 넣어준다
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    
    #w의 최대값과 h의 최대값을 곱해서 반환
    return max(w) * max(h)