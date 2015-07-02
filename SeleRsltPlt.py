#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

result=collections.OrderedDict() #順序つきdictionaryを用いる

f = open('stl.txt') #スタートリストを読み込み
stlLines = f.readlines() 
f.close()

f = open('lap.txt') #ラップを読み込み
lapLines = f.readlines()
f.close()
 
for line in stlLines:   #スタリの読み込み
    time,name = line.split()
    result[name] = 0


for line in lapLines:   #ラップの読み込み
    name, hour, minu, sec, univ = line.split()
    time = 3600*int(hour)+60*int(minu)+int(sec) #hh:mm:ssを秒に変換する
    result[name] = time

for bar in result.values(): #リダイレクションでファイルを作る
    print bar
