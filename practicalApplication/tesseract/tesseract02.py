import pytesseract
import os

# 文字图片路径
path = "test_imgs/"
# 获取图片路径列表
imgs = [path + i for i in os.listdir(path)]
# 打开文件
fileName = "text.txt"
f = open(fileName, 'w+', encoding='utf-8')
# 将各个图片的路径写入text.txt文件中
for img in imgs:
    f.write(img+"\n")
# 关闭文件
f.close()

# 文件识别
str = pytesseract.image_to_string(fileName, lang="chi_sim")
print(str)