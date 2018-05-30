# pdf-translate

[![Build Status](https://travis-ci.com/yuantailing/pdf-translate.svg?branch=master)](https://travis-ci.com/yuantailing/pdf-translate)

Source of [pdf.tsing.net](http://pdf.tsing.net), a PDF viewer with translation.

用户指定哪个词就翻译哪个词，以免整句翻译后词不达意。

避免生僻词“见一次搜一次”，自动记录的词典正好能辅助记单词。

如果要整篇翻译，没必要用这个网页，请移步 https://onlinedoctranslator.com/ 等翻译服务。

## 网页使用说明

1. 打开 PDF 文件：右上角打开按钮，或拖拽到浏览器

1. 划词翻译：鼠标划词，按回车键，或者点左上角的加号。词典会保存在本地，刷新页面不会丢失

1. 自行编辑词和翻译：直接修改左上角的列表

1. 重新自动翻译：列表右侧的刷新按钮

1. 显示原文：鼠标移到翻译的词上，就会显示原文

## 本地构建

见 [.travis.yml](.travis.yml) 。

## 待解决的问题

- [ ] 展开侧栏时，界面的位置应相应变化
- [ ] 界面样式优化
- [ ] 文字居中
- [ ] 翻译句子。目前 yandex 翻译句子效果差，有道证书有问题
- [ ] 选取句子时，前一个 div 的最后一个词、后一个 div 的第一个词会连在一起
- [ ] 跨 div 的词无法选中，也无法翻译
- [ ] 选择范围超过一页时出错
- [ ] 更准地定位字母位置。pdf.js 提供的 textStream 接口是按行定位的，字体宽度与 PDF 里的字体宽度不一致时会偏差较大
- [ ] 在某些情况下，Ctrl + 鼠标滚轮会调用浏览器的页面缩放，而不是 PDF 阅读器的缩放
