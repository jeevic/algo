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
    parent =os.path.split(os.path.realpath(__file__))[0];
    path = os.path.join(parent, "leetcode")
    leetcode_counter = count_leetcode(path)
    path = os.path.join(parent, "datastruct")
    data_struct_counter = count_leetcode(path)

    print("leetcode做题数量:{}".format(leetcode_counter))
    print("data_struct做题数量:{}".format(data_struct_counter))
    print("总数量:{}".format(leetcode_counter + data_struct_counter))