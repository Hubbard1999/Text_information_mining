import requests
import re
import json


# 这个函数将工资全部转换为 工资/月
def calculate_salary(str):
    # 1.5万以下/年
    str = str.replace('以上', '')
    str = str.replace('以下', '')
    # 1.5万/年
    # unit = 月
    unit = str[-1]

    # wage1 = 0.8-1万
    wage1 = str[:-2]

    # line = 万
    line = wage1[-1]

    # wage2 = 0.8-1
    wage2 = wage1[:-1]

    # 若工资是一个范围
    if '-' in wage2:
        # print("工资是一个范围，取中位数")
        a, b = wage2.split('-', 1)
        # print(a, b)

        if unit == '月':
            if line == '万':
                wage2 = int(((float(b)+float(a)) / 2) * 10000)
            if line == '千':
                wage2 = int(((float(b) + float(a)) / 2) * 1000)
        if unit == '年':
            if line == '万':
                wage2 = int(((float(b)+float(a)) / 24) * 10000)
            if line == '千':
                wage2 = int(((float(b) + float(a)) / 24) * 1000)
        if unit == '天':
            wage2 = int(((float(b) + float(a)) / 2) * 30)
    # 若工资是一个确定数
    else:
        if unit == '月':
            if line == '万':
                wage2 = int(float(wage2) * 10000)
            if line == '千':
                wage2 = int(float(wage2) * 1000)
        if unit == '年':
            if line == '万':
                wage2 = int((float(wage2) / 12) * 10000)
            if line == '千':
                wage2 = int((float(wage2) / 12) * 1000)
        if unit == '天':
            wage2 = int(float(wage2) * 30)
        if unit == '小时':
            wage2 = int(float(wage2) * 240)
        if '元' in wage2:
            wage2 = float(wage2[:-1]) * 240
    return wage2

# 爬虫配置信息
params = {
    'lang': 'c',
    'postchannel': '0000',
    'workyear': '99',
    'cotype': '99',
    'degreefrom': '99',
    'jobterm': '99',
    'companysize': '99',
    'ord_field': '0',
    'dibiaoid': '0',
    'line': '',
    'welfare': '',
}
cookies = {

}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Host': 'search.51job.com',
    'Referer': 'https://search.51job.com/list/190200,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}
datelist = []

# 搜索6个关键词
nameList = ["审计","会计","CPA","ACCA","税务管理","管理会计"]
pageList = [131, 389, 13, 3, 9, 6]

# 开始爬虫
for i in range(0,len(nameList)):
    tempName = nameList[i]
    print(tempName+"---------------------------")
    for page in range(0, pageList[i]+1):
        try:
            print(page)
            url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,{},2,{}.html'.format(tempName,page)

            response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
            response.encoding = response.apparent_encoding
            r = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text, re.S)
            string = ''.join(r)

            info_dict = json.loads(string)
            dit_py = info_dict['engine_search_result']
            dit = {}
            for i in dit_py:
                attribute_text = ' '.join(i['attribute_text'][1:])

                dit['job_name'] = i['job_name']
                dit['company_name'] = i['company_name']
                # 判断 如果工资为空 则不爬取这条数据
                if(i['providesalary_text']==''):
                    continue
                # 操作 统一工资为 工资/月
                wage = calculate_salary(i['providesalary_text'])
                dit['money'] = wage
                dit['workarea'] = i['workarea_text']
                dit['updatedate'] = i['updatedate']
                dit['companytype'] = i['companytype_text']
                dit['jobwelf'] = i['jobwelf']
                dit['attribute'] = attribute_text
                dit['companysize'] = i['companysize_text']
                # 将这条数据写入本地表格 6个关键词生成6个表格
                with open('./huizong/{}.csv'.format(tempName), mode='a', encoding='utf-8') as f:
                    f.write('{},{},{},{},{},{},{},{}\n'.format(dit['job_name'], dit['company_name'], dit['money'], dit['workarea'], dit['companytype'], dit['jobwelf'], dit['attribute'], dit['companysize']))

        except:
            print("当前第页面有异常符号，跳过到下一页！")
            continue

