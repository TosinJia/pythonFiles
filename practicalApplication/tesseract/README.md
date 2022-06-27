
## Tesseract

- [如何利用Python识别图片中的文字](https://www.jb51.net/article/187678.htm)
### Tesseract的安装及配置
- https://digi.bib.uni-mannheim.de/tesseract/
	- https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20201127.exe

- 配置环境变量 path D:\Program Files\Tesseract-OCR
### 下载语言包
- https://tesseract-ocr.github.io/tessdoc/Data-Files
	- https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/chi_sim.traineddata
	- https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/chi_tra.traineddata

- 放置路径 D:\Program Files\Tesseract-OCR\tessdata

### 其它模块下载
```
C:\Users\Lenovo>pip install pillow
Collecting pillow
  Downloading Pillow-8.1.0-cp39-cp39-win_amd64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 60 kB/s
Installing collected packages: pillow
Successfully installed pillow-8.1.0
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'd:\program files\python\python39\python.exe -m pip install --upgrade pip' command.

C:\Users\Lenovo>pip install pytesseract
Collecting pytesseract
  Downloading pytesseract-0.3.7.tar.gz (13 kB)
Requirement already satisfied: Pillow in d:\program files\python\python39\lib\site-packages (from pytesseract) (8.1.0)
Using legacy 'setup.py install' for pytesseract, since package 'wheel' is not installed.
Installing collected packages: pytesseract
    Running setup.py install for pytesseract ... done
Successfully installed pytesseract-0.3.7
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'd:\program files\python\python39\python.exe -m pip install --upgrade pip' command.
```
