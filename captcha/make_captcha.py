# coding=utf-8
# 生成图片验证码

from captcha.image import ImageCaptcha
import random
import sys,getopt

image = ImageCaptcha()
num = '0123456789'
littleletter = 'abcdefghijklmnopqrstuvwxyz'
bigletter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alllen = len(num)+len(littleletter)+len(bigletter)
allran = num+littleletter+bigletter
make_captchastr = ''    #存储字符串
make_captchastrlen = 6 #默认验证码长度
#print('make_captcha.py -h for help')
#sys.exit(2)   2常用于命令行错误
try:
    opts,args = getopt.getopt(sys.argv[1:],"hi:")
    for opt,arg in opts:
        if opt == '-h':
            print('usage: python3 make_captcha.py -i <numlength> default:6')
            sys.exit()  #此时会抛出异常SystemExit 如果被捕获到会继续执行代码
        elif opt == '-i':
            make_captchastrlen = int(arg)
except getopt.GetoptError:
    make_captchastrlen = 6

for i in range(make_captchastrlen):
    tmp = random.randint(0,alllen-1)
    make_captchastr+=allran[tmp]

image.write(make_captchastr,make_captchastr+'.png')
print("build successfully")