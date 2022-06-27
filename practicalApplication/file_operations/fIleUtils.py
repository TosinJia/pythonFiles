import xlsxwriter as xw

# PS E:\iEnviroment\development\projects\pythonProjects\pythonFiles\practicalApplication\file_operations> pip install xlsxwriter
# Collecting xlsxwriter
#   Downloading XlsxWriter-3.0.3-py3-none-any.whl (149 kB)
#      |████████████████████████████████| 149 kB 297 kB/s
# Installing collected packages: xlsxwriter
# Successfully installed xlsxwriter-3.0.3
# WARNING: You are using pip version 21.2.3; however, version 22.1.2 is available.
# You should consider upgrading via the 'E:\iEnviroment\development\python\Python310\python.exe -m pip install --upgrade pip' command.

# python读取txt文件（多种方法） https://blog.csdn.net/kobeyu652453/article/details/106876829
class File():
    def read1(self, file):
        f = open(file, encoding='utf-8')
        data = []
        for line in f:
            data.append(line.strip())
        return data

    def read3(self, file):
        f = open(file, encoding='utf-8')
        data = f.readlines()
        f.close()
        return data

    def xw_toExcel(self, data, fileName):  # xlsxwriter库储存数据到excel
        workbook = xw.Workbook(fileName)  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        title = ['序号', '酒店', '价格']  # 设置表头
        worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
        i = 2  # 从第二行开始写入数据
        for j in range(len(data)):
            insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
            row = 'A' + str(i)
            worksheet1.write_row(row, insertData)
            i += 1
        workbook.close()  # 关闭表

file = File();
# data=file.read1('E:\\iEnviroment\\英语学习\\OriginalEnglish.txt')
data=file.read3('E:\\iEnviroment\\英语学习\\OriginalEnglish.txt')
for line in data:
    print(line.strip())

# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]
fileName = '测试-20220626.xlsx'
file.xw_toExcel(testData, fileName)