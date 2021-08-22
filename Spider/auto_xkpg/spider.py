from pandas.io import excel
from conf import *
from selenium import webdriver
from selenium.webdriver.support.select import Select

import pandas as pd
import os
import json
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(
    "chromedriver.exe", options=chrome_options)

driver.get('https://xkpg.cdgdc.edu.cn/index')
# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()
with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)
    print(cookies_list)
    for cookie in cookies_list:
        print(cookie)
        driver.add_cookie(cookie)


def save_to_excel(html, writer, sheet_name):
    dfs = pd.read_html(html)

    if len(dfs) == 2:
        head = dfs[0]
        data = dfs[1]
        data.columns = head.columns.to_list()
    else:
        data = dfs[0]

    data.to_excel(writer, sheet_name=sheet_name)
    pass


driver.get('https://xkpg.cdgdc.edu.cn/subject/publicNotice')
driver.refresh()

time.sleep(2)  # 这个时间表示服务器响应时间


print(driver.title)
print(major)
driver.execute_script(
    f'document.querySelector("#subjectItem > div > div > div > input").value = "{major}" ')
driver.execute_script(f'$("#xkSelect").val("{major[:4]}");')

for school in school_Score_maps:
    driver.execute_script(
        f'document.querySelector("#publicNoticeForm > div.layui-inline.searchSelect.searchSelect1 > div > div > div > input").value = "{school}"')
    driver.execute_script(f'$("#dwSelect").val("{school[:5]}");')

    # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[4]/div/div/div/input").send_keys("0835 - 软件工程")
    driver.find_element_by_class_name("searchSelect3").click()

    subtitles = ["出版教材质量", "国家级一流课程", "教学成果奖",
                 "在校生代表性成果", "专任教师总数", "支撑平台", "科研获奖情况"]
    excel_filename = f'学科评估//{school_Score_maps[school]}：{school[8:]}.xlsx'
    dir_name = "学科评估"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    writer = pd.ExcelWriter(
        excel_filename)
    for i in range(1, 8):
        print(school, i)

        driver.find_element_by_xpath(
            f'//*[@id="checkMenuList"]/li[{i}]').click()

        time.sleep(0.5)
        Select(driver.find_element_by_xpath(
            '//span[@class="layui-laypage-limits"]/select')).select_by_value("50")
        time.sleep(0.5)

        html = driver.page_source
        save_to_excel(html, writer=writer,
                      sheet_name=f"{str(i)}{subtitles[i-1]}")

    writer.save()

driver.quit()
