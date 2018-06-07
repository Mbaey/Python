[setting]
UseNet=0
NextTry=259200


http://gplt.patest.cn/api/cached/board?timestamp=1523317101133

http://gplt.patest.cn/api/cached/board?timestamp=1523316646881


http://gplt.patest.cn/api/cached/board/team/5aa0d439d795a0dcfd77a70d?timestamp=1523318505248
http://gplt.patest.cn/api/cached/board/team/5a66c88dd795a0dcfd480429?timestamp=1523318564797
5a66c88dd795a0dcfd480429  usst打铁梦之队

 _id : 队号
 _sid : 学校号
 s0 : L1题的得分
 s1 : L2题的得分
 s2 : L3题的得分
 tScore : 学校总得分
insert into PAT_schools (_sid,name,s0,s1,s2,tScore) values 
(%s, %s,%s, %s,%s, %s); 
5a2fe33c95b589002a5cf52b	 			
5a2fe33c95b589002a5cf52b
杭州电子科技大学

insert into PAT_teams (_tid,_sid,name,s0,s1,s2,tPass,tScore) values (%s, %s,%s, %s,%s, %s,%s, %s)

insert into PAT_members (_id,_tid,tname,sname,name,L1-01,L1-02,L1-03,L1-04,L1-05,L1-06,L1-07,L1-08,L2-01,L2-02,L2-03,L2-04,L3-01,L3-02,L3-03,tScore) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)




0	2205
1	2172
2	1991
3	1239
4	709
5	1750
6	1457
tScore	6368

	2205	2172	1991	6368
5a66c88dd795a0dcfd480429


insert into PAT_members (_tid,tname,sname,_id,name,L1-01,L1-02,L1-03,L1-04,L1-05,L1-06,L1-07,L1-08,L2-01,L2-02,L2-03,L2-04,L3-01,L3-02,L3-03,tScore) values ("58d0cc49e40d8ed00a5d0354", "万里一队", "浙江万里学院", "5aa537cfd795a0dcfd8ec84f", "叶奕威", 20, 15, 5, 5, 10, 15, 10, 20, 25, 25, 25, 17, 0, 0, 0, 192);



应用AK：
TXZ1vt6bC0tT6G3owXQy5F0EyvrX9lZn

sk 
AKv1ssU5dG62U8X7yv5EnMYrRbe56i7F
二：坐标转换
http://api.map.baidu.com/geocoder/v2/?address=%E5%8C%97%E4%BA%AC%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6&output=json&ak=R5O1nVWz9FiqrZEPXedQZzGRu1DjnAre


update PAT_schools set lng=%s, lat=%s where _sid=%s;
update PAT_schools set lng=1, lat=1 where _sid=571229d1f7f0c5a215de7af9;
UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;