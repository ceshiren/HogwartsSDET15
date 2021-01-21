def test_awk():
    # awk默认词典不用初始化
    time = {}
    count = {}
    # awk把每行拆分为一个个的记录，其实就是包含每条记录的列表
    # awk通过$1 $2把每个记录又拆分成了小列表
    data = [
        ["a", 1],
        ["a", 2],
        ["a", 3],
        ["b", 4],
        ["b", 5],
        ["b", 6]
    ]

    for record in data:
        # 对应$1
        k1 = record[0]
        # 对应$2
        k2 = record[1]
        # awk默认不用做初始化
        if k1 not in time:
            time[k1] = 0

        # 等价于 d[$1] += $2
        time[k1] += k2

        if k1 not in count:
            count[k1] = 0
        count[k1] += 1

    # 对应 for(k in d) print k,d[k]  写法基本一致
    for k in time:
        print(f"k={k}, avg={time[k] / count[k]}")


def test_awk_mini():
    time, count = {}, {}
    data = [
        ["a", 1],
        ["a", 2],
        ["a", 3],
        ["b", 4],
        ["b", 5],
        ["b", 6]
    ]
    for record in data:
        time.setdefault(record[0], 0)  # todo: 类型判断 string默认为"" int默认为0
        time[record[0]] += record[1]
        count.setdefault(record[0], 0)
        count[record[0]] += 1

    # 对应 for(k in d) print k,d[k]  写法基本一致
    for k in time:
        print(f"k={k}, avg={time[k] / count[k]}")
#     echo '
# a 1
# a 2
# a 3
# b 4
# b 5
# b 6
# ' | awk '{d[$1]+=$2}END{for(k in d) print k,d[k]}'
