
def get_suffix(filename,need_dot=False):
    """
    获取文件的后缀名
    :param filename:文件名
    :param need_dot: 返回的后缀名是否需要带小数点
    :return: 文件后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) -1 :
        index = pos if need_dot else pos + 1
        return filename[index:]
    else:
        return ''


def main():
    filename = input("请输入文件名：")
    need_dot = input("是否需要文件名(Y or N):")
    if need_dot == 'Y':
        need_dot = True

    print(get_suffix(filename,need_dot))


if __name__ == "__main__":
    main()