import os
import time


def main():
    content = '轻舟科技欢迎你，为你开天辟地。。。'
    while True:
        # 清理屏幕上的输出
        os.system("cls")
        print(content)
        # 休眠200ms
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
