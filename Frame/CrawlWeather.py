1.
URLlist1 = response.css('div.box.pcity ul li')#所有城市

URLlist1[0].css('a::attr(href)').extract_first()
URLlist1[0].css('a::text').extract_first()

URLData = response.css('div.box.p ul li')#所以历史记录的URL
URLData[0].css('a::attr(href)').extract_first()
# '/aqi/beijing-201806.html'


2.爬取数据
table = response.css("table.b")
trs = table.css('tr')#里面【1，n 】是数据
trs[1].css('td::text').extract()


