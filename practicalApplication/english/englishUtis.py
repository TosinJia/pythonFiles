from urllib import request
import re
import xlsxwriter as xw
import datetime

class Dictionary():
    url = 'https://www.dictionary.com/browse/{}'
    word_pattern = '<h1 data-first-headword="true" class="css-1sprl0b e1wg9v5m5">([a-z,A-Z]*?)<\/h1>'
    # pronIpa_pattern = '<span class="pron-ipa-content css-7iphl0 evh0tcl1">([^"]*?)<\/span>'
    pronIpa_pattern = '<span class="pron-ipa-content css-7iphl0 evh0tcl1">([\s\S]*?)<\/span><button'
    audio_pattern = 'src="([^<]+)" type="audio\/mpeg"'

    def __fetch_content(self, word):

        try:
            r = request.urlopen(Dictionary.url.format(word))
            content = r.read()
            # html = content.decode('utf-8')
            return str(content, encoding='utf-8')
        except:
            pass
        return ''

    def __analysis(self, html):
        ipa_list = re.findall(Dictionary.pronIpa_pattern, html)
        word_list = re.findall(Dictionary.word_pattern, html)
        audio_list = re.findall(Dictionary.audio_pattern, html)

        ipa_original = ipa_list[0] if len(ipa_list) > 0 else ''
        element_pattern='<span class="[a-z- ]+?">|<\/span>'
        ipa = re.sub(element_pattern, "", ipa_original)
        return {"word":word_list[0] if len(word_list)>0 else '',
                "ipa":ipa,
                "audio":audio_list[0] if len(audio_list)>0 else ''}

    def query(self, word):
        html = self.__fetch_content(word)
        # print(html)
        info = self.__analysis(html)
        info["word_original"] = word
        return info

# 记录开始时间
start_time = datetime.datetime.now()
word_total = 0

maxnumbers_perline = 10 # 每行最大单词数
file_pathname = 'E:\\iEnviroment\\英语学习\\OriginalEnglish-20220627.txt'
f = open(file_pathname, encoding='utf-8')
data = f.readlines()

word_pattern = '([a-zA-Z]+)'
word_or_noword_pattern = '([a-zA-Z]+)|([^a-zA-Z]+)'
dictionary = Dictionary()

excel_file_pathname = file_pathname.replace('.txt', '.xlsx')
workbook = xw.Workbook(excel_file_pathname)  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
# worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头

i = 1  # 从第一行开始写入数据


row_ipa = []
row_audio = []
row_word = []
row_word_original = []

column_number = [chr(i) for i in range(ord('A'),ord('Z')+1)]
def newLine(worksheet1, i):
    global row_ipa
    global row_audio
    global row_word
    global row_word_original

    if len(row_word_original) > 0:
        worksheet1.write_row('A' + str(i), row_ipa)
        # worksheet1.write_row('A' + str(i + 1), row_word)

        for j in range(len(row_word_original)):
            worksheet1.write_url(column_number[j] + str(i + 1), row_audio[j], string=row_word[j])

        worksheet1.write_row('A' + str(i + 2), row_word_original)
        i+=4
        row_ipa = []
        row_audio = []
        row_word = []
        row_word_original = []
    return i

for line in data:
    print(line.strip())
    element_list = re.findall(word_or_noword_pattern, line.strip())

    i = newLine(worksheet1, i)

    for element in element_list:
        word = element[0]
        noword = element[1]
        if len(word)>0:
            word_total+=1
            info = dictionary.query(word)
            print(info)
            row_ipa.append(info['ipa'].replace('/', '').strip())
            row_audio.append(info['audio'])
            row_word.append(info['word'])
            row_word_original.append(info['word_original'])
            if len(row_word_original) > maxnumbers_perline:
                i = newLine(worksheet1, i)
        else:
            noword = noword.strip()
            if len(noword)>0:
                row_ipa.append('')
                row_audio.append('')
                row_word.append('')
                row_word_original.append(noword)

newLine(worksheet1, i)

workbook.close()

# 记录结束时间
end_time = datetime.datetime.now()

print('耗时：', end_time-start_time, '单词总数：', word_total)