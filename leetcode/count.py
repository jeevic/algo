import os
import os.path


def count_leetcode(path):
    count = 0
    children_path = os.listdir(path)

    is_dir = False
    for cp in children_path:
        # 判断是否全部是文件
        is_dir = is_dir or os.path.isdir(path + "/" + cp)

    if not is_dir:
        return 1
    for cp in children_path:
        sub_path = path + "/" + cp
        if os.path.isdir(sub_path):
            count += count_leetcode(sub_path)

    return count


if __name__ == '__main__':
    path = "."
    counter = count_leetcode(".")
    print("做题数量:{}".format(counter))