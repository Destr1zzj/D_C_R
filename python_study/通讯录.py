import easygui as g
import sys


msg = "请填写以下内容"
title = "账号中心"
fieldNames = ["*使用网站","*账号","*密码","邮箱","手机","其他"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('【%s】为必填项\n\n' % fieldNames[i])
    if errmsg ==  "":
        break
    fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
msg = '用户资料如下：\n %s ' % str(fieldValues)
title = '确认'
if g.ccbox(msg, title):
    with open('账号.txt', 'a') as f:
        f.write(str(fieldValues))
    pass
else:
    sys.exit(0)
