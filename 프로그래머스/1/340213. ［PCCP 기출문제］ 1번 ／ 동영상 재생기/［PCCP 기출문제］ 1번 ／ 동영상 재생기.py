def solution(video_len, pos, op_start, op_end, commands):
    def to_second(time):
        minute, second = map(int, time.split(":"))
        return minute * 60 + second

    def to_time(seconds):
        minute = seconds // 60
        second = seconds % 60
        return f"{minute:02d}:{second:02d}"

    video_len = to_second(video_len)
    pos = to_second(pos)
    op_start = to_second(op_start)
    op_end = to_second(op_end)

    def skip_opening(pos):
        if op_start <= pos <= op_end:
            return op_end
        return pos

    pos = skip_opening(pos)

    for command in commands:
        if command == "next":
            pos += 10
        elif command == "prev":
            pos -= 10

        if pos < 0:
            pos = 0

        if pos > video_len:
            pos = video_len

        pos = skip_opening(pos)

    return to_time(pos)