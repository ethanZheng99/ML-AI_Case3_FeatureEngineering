import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
system = os.name


def logToTXT(file: str, filename: str, content: list):
    if file is None:
        filepath = os.path.join(dir_path, '..', 'log')
    else:
        filepath = os.path.join(dir_path, '..', 'log', file)

    if system == 'nt':
        url = filepath + "//" + filename
    else:
        url = filepath + "/" + filename

    with open(url, 'w') as file:
        for line in content:
            file.write(str(line) + "\n")
        print("已成功写入: 文件：" + filename)
        file.close()


def logToCSV(file: str, filename: str, data: tuple or list):
    if file is None:
        filepath = os.path.join(dir_path, '..', 'log')
    else:
        filepath = os.path.join(dir_path, '..', 'log', file)

    if system == 'nt':
        url = filepath + "//" + filename
    else:
        url = filepath + "/" + filename
    # 打开文件，设置为写入模式
    with open(url, 'w', newline='') as file:
        writer = csv.writer(file)
        # 写入所有行
        for row in data:
            writer.writerow(row)
        print("已成功写入: 文件：" + filename)

def dataToCSV(file: str, filename: str, data: tuple or list):
    if file is None:
        filepath = os.path.join(dir_path, '..', 'data')
    else:
        filepath = os.path.join(dir_path, '..', 'data', file)

    if system == 'nt':
        url = filepath + "//" + filename
    else:
        url = filepath + "/" + filename
    # 打开文件，设置为写入模式
    with open(url, 'w', newline='') as file:
        writer = csv.writer(file)
        # 写入所有行
        for row in data:
            writer.writerow(row)
        print("已成功写入: 文件：" + filename)


"""
                测试用例
                data1 = [
                    ["姓名", "年龄", "城市"],
                    ["Alice", 30, "New York"],
                    ["Bob", 25, "Los Angeles"],
                    ["Charlie", 35, "Chicago"]
                ]
                logToCSV("Person_log","test.csv", data1)
                logToTXT("Person_log","test.txt", data1)
"""

