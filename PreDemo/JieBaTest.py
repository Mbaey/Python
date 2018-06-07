import jieba
# https://github.com/fxsjy/jieba
import collections

seg_list = jieba.lcut("上海自来水来自海上")
print(seg_list)
len(seg_list)
# it = iter(seg_list)
# while 1:
#     try:
#         print(type(next(it)))
#     except StopIteration:
#         break


seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
for i in seg_list:
    print(i)


seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

