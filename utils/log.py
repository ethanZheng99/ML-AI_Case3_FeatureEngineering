import csv


def logToTXT(filename: str, content: list):
    filepath = '../log'
    url = filepath + "/" + filename
    with open(url, 'w') as file:
        for line in content:
            file.write(str(line) + "\n")
        print("已成功写入 文件：" + filename)
        file.close()


def logToCSV(filename: str, data: tuple or list):
    filepath = '../log'
    url = filepath + "/" + filename
    # 打开文件，设置为写入模式
    with open(url, 'w', newline='') as file:
        writer = csv.writer(file)
        # 写入所有行
        for row in data:
            writer.writerow(row)
        print("已成功写入 文件：" + filename)


"""
                测试用例
                data1 = [
                    ["姓名", "年龄", "城市"],
                    ["Alice", 30, "New York"],
                    ["Bob", 25, "Los Angeles"],
                    ["Charlie", 35, "Chicago"]
                ]
                logToCSV("test.csv", data1)
                logToTXT("test.txt", data1)
"""
