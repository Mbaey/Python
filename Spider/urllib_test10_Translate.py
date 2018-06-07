import urllib.request
import urllib.response
import json
#参考 其实这是一个get请求，只需要字符串拼接就好了
# 'http://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&dt=t&q=google'
# 'https://www.zhihu.com/question/47239748/answer/111171862'

if __name__ == "__main__":
    Request_URL = 'https://translate.google.cn/translate_a/single'

    translate_word = 'Here come a bus. hello world!'
    Form_Data = {'client':'at',
    'sl':'en',
    'tl':'zh-CN',
    # 'hl':'zh-CN',
    # 'dt':'at',
    # 'dt':'bd',
    # 'dt':'ex',
    # 'dt':'ld',
    # 'dt':'md',
    # 'dt':'qca',
    # 'dt':'rw',
    # 'dt':'rm',
    # 'dt':'ss',
    'dt':'t',
    # 'ie':'UTF-8',
    # 'oe':'UTF-8',
    # 'otf':'2',
    # 'ssel':'0',
    # 'tsel':'0',
    # 'kc':'1',
                 # tk: 676080.800447
                 # q: hello world
    # 'tk':'676080.800447',
    'q':translate_word}
    #创建Form_Data字典，存储上图的Form Data
    headers={'referer':'https://translate.google.cn/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    #使用urlencode方法转换标准格式
    data = urllib.parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    request = urllib.request.Request(Request_URL, headers=headers, data=data)
    response = urllib.request.urlopen(request)
    #读取信息并解码
    html = response.read().decode('utf-8')
    print(html)
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results[0][0][0]
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)
