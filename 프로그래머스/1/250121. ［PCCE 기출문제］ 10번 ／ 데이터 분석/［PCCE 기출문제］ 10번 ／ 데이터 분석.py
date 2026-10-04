def solution(data, ext, val_ext, sort_by):
    idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    result = [row for row in data if row[idx[ext]] < val_ext]

    result.sort(key=lambda x: x[idx[sort_by]])

    return result