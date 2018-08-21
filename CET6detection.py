import requests
import re
import tkinter
import codecs
import time
# 要提交的键值对的一个结构
keywords = {
    'stype': 'Y',
    'stuno': '2017123040',
    'LANG': '英语',
    'GD': '6'
}
# 表单要提交到的目的地址
url = "http://cet.tinyin.cc/regstep2.asp"  # 注册
r = requests.session()
r.headers.update({'referer':'http://cet.tinyin.cc/register.asp'})  # 注册

s = r.post(url, data=keywords)
html = s.text
html_doc = str(html)
res_tr = r"<font.*?color=.*?<\/font>"
m_tr = html_doc[4100:4150]
m_change = m_tr
print("开始检测：初始匹配项：",m_tr)
i = 0
while (m_change == m_tr):
    i += 1
    time.sleep(60)   # 每分钟检测一次
    r.headers.update({'referer': 'http://cet.tinyin.cc/register.asp'})
    s = r.post(url, data=keywords)
    html = s.text
    html_doc = str(html)
    res_tr = r"<font.*?color=.*?<\/font>"
    # m_change = re.findall(res_tr, html_doc, re.S | re.M | re.I)
    m_change = html_doc[4100:4150]
    print("第", i, "次检测结果：")
    print(m_change)
    print(m_tr)
print(m_change == m_tr)
def show():
    tkinter.tkMessageBox.showinfo(title='aaa', message='bbb')
def creatfram():
    root = tkinter.Tk()
    root.state("zoomed")
    root.wm_attributes('-topmost', 1)  # 最大化置顶弹窗
    b = tkinter.Button(root, text="六级有名额了！！", command=show)
    b.pack()
    root.mainloop()
creatfram()