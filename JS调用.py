import urllib

import execjs  # 导入PyExecJS 库


def get_js():  # 导入js文件
    f = open("Encrypt.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


jsstr = get_js()
ctx = execjs.compile(jsstr)


def creative_book():  # 创建密文密码字典
    f = open("top100PWD.txt")
    h = open('adobe_top100_pass_creative.txt', 'w')
    h1 = open('adobe_top100_pass_creative_random.txt', 'w')
    for line in f:
        r = line.strip('\n')
        utf = ctx.call('loginHandle', r)
        h.write(utf[0] + "\n")
        h1.write(urllib.parse.quote(utf[1]) + "\n")
        print(utf[0], urllib.parse.quote(utf[1]))
    f.close()
    h.close()
    h1.close()

creative_book()
