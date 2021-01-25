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
    for line in f:
        r = line.strip('\n')
        utf = ctx.call('loginHandle', r)
        h = open('adobe_top100_pass_creative.txt', 'a')
        h1 = open('adobe_top100_pass_creative_random.txt', 'a')
        h.write("\n" + utf[0])
        h1.write("\n" + urllib.parse.quote(utf[1]))
        print(utf[0], urllib.parse.quote(utf[1]))
        h.close()
        h1.close()
    f.close()


creative_book()
