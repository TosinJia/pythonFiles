import pytesseract
from PIL import Image

filename = "test_imgs/tesseract-english.png"
filename = "test_imgs/tesseract-chi_sim.png"
# eng.traineddata
lang = "eng"
# chi_sim.traineddata 将语言设置为简体中文或其它语言后，Tesseract还是可以识别出英文字符
lang = 'chi_sim'

# 读取图片
img = Image.open(filename)
# 识别文字
str = pytesseract.image_to_string(img, lang=lang)

print(str)
