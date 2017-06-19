# coding=utf-8
import urllib.request
import re


class dude:
    def __init__(self, target):
        self.target = target
        self.readedList = []
        self.readingList = []
        self.resultList = []
        self.src_pre = None
        self.content_pre = None

    def src(self, callback):
        self.src_pre = callback
        return self

    def content(self, callback):
        self.content_pre = callback
        return self

    def write(self):
        fp = urllib.request.urlopen(self.target)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        print(mystr)
        if self.src_pre!=None:
            self.readingList.extend(self.src_pre(mystr))
        if self.content_pre!=None:
            self.resultList.extend(self.content_pre(mystr))


d = dude('https://www.baidu.com')

def src_pre(str):
    result = re.match(r'.*',str)
    if result!=None:
        return result
    else:
        return [];

d.src(src_pre).write()
