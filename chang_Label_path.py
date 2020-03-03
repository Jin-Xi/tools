import os

def string_switch(x,y,z,s=1):

    with open(x, "r", encoding="utf-8") as f:
        #readlines以列表的形式将文件读出
        lines = f.readlines()
 
    with open(x, "w", encoding="utf-8") as f_w:
        # 定义一个数字，用来记录在读取文件时在列表中的位置
        n = 0
        # 默认选项，只替换第一次匹配到的行中的字符串
        if s == 1:
            for line in lines:
                if y in line:
                    line = line.replace(y,z)
                    f_w.write(line)
                    n += 1
                    break
                f_w.write(line)
                n += 1
            # 将剩余的文本内容继续输出
            for i in range(n,len(lines)):
                f_w.write(lines[i])
        # 全局匹配替换
        elif s == 'g':
            for line in lines:
                pass
                if y in line:
                    line = line.replace(y,z)
                f_w.write(line)


def filechanger(path):
    filenames = os.listdir(path)
    for filename in filenames:
        domain = os.path.abspath(path)
        filename = os.path.join(domain, filename)
        if os.path.isdir(filename):
            filechanger(filename)
            continue
        string_switch(filename, "/home/jinx/darknet/mask_dataset", "/home/jinx/darknet/mask_dataset")



if __name__ == "__main__":
    filechanger("/home/jinx/darknet/mask_dataset/label_mask (copy)")              