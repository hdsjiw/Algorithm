from itertools import combinations

def split(word):
    # 문자열 길이를 기준으로 가능한 모든 분할 지점 조합 구하기
    n = len(word)
    split_indices = combinations(range(1, n), 2)  # 1부터 n-1 사이에서 두 개의 분할 지점 선택

    all_splits = []
    for i, j in split_indices:
        part1 = word[:i]
        part2 = word[i:j]
        part3 = word[j:]
        all_splits.append((part1, part2, part3))
    
    return all_splits

def reverse_and_combine(words):
    result = []
    for parts in words:
        # 각 부분 문자열을 뒤집기 (reversed 사용)
        reversed_parts = ["".join(reversed(part)) for part in parts]
        # 뒤집힌 부분 문자열을 결합
        combined = "".join(reversed_parts)
        result.append(combined)
    return result

# 사용자 입력
word = input()

# 분할 및 뒤집기 수행
splits = split(word)
result = reverse_and_combine(splits)

result.sort()
print(result[0])
