def decimal_to_binary(n, arr):
    maps = []

    for i in range(n):
        row = []
        temp = arr[i]

        while temp != 0:
            if temp % 2 == 0:
                row.append("0")
            else:
                row.append("#")
            temp //= 2
        row.reverse()

        # 부족한 길이만큼 앞에 0 추가
        while len(row) < n:
            row.insert(0, "0")

        maps.append(row)

    return maps


def compare_2_map(n, map1, map2):
    secret_map = []

    for i in range(n):
        secret_width = ""

        for j in range(n):
            if map1[i][j] == "0" and map2[i][j] == "0":
                secret_width += " "
            else:
                secret_width += "#"

        secret_map.append(secret_width)

    return secret_map


def solution(n, arr1, arr2):
    map1 = decimal_to_binary(n, arr1)
    map2 = decimal_to_binary(n, arr2)
    answer = compare_2_map(n, map1, map2)
    return answer
