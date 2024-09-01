def find_max_min(a):
    if not a:
        return None, None  # 如果数组为空，返回None

    maxe = mine = a[0]  # 初始化最大值和最小值为数组的第一个元素

    for num in a[1:]:  # 从数组的第二个元素开始遍历
        if num > maxe:
            maxe = num  # 更新最大值
        elif num < mine:
            mine = num  # 更新最小值

    return maxe, mine  # 返回最大值和最小值