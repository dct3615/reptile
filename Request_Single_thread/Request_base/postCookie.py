# -*- coding: utf-8 -*-
"""
Created on 2020/5/3 9:27

@author: dct
"""
import requests
"""获取 post 请求"""
data = {
    'first' : "true",
    'pn' : 1,
    'kd' : 'python'
}
headers = {
    'Refer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

"""获取 post 请求"""
data = {
    'first' : "true",
    'pn' : 1,
    'kd' : 'python'
}

headers = {
    'Refer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'cookie': 'user_trace_token=20200102111739-544c3893-cfb3-460b-a384-3afe3b7e6f93; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f6442580715f-08a1664a16a94c-67e1b3f-1049088-16f64425808821%22%2C%22%24device_id%22%3A%2216f6442580715f-08a1664a16a94c-67e1b3f-1049088-16f64425808821%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2277.0.3865.90%22%7D%7D; _ga=GA1.2.1773883637.1588469447; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588469447; LGSID=20200503093045-5b03ccc9-6c1c-4e7e-8f7a-210a4a21b89a; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0s0000ax5T3eQzubEzwZyexrxcAHMnPFY%5Fy4knuPKB2rmMVp5do0Ux0HsLT1oFYPdjpUAslvvVi4-8WnFD9QG%5FGIJB-iMt9LhVx8K1TBapiZ5Qz6Alk3g06uYqFZb23Vc5r8lzkHu-12yL2LffUCAsEZYvMiH7Zd3PyVGm28vNO0obLjbcCblUf%5FfsUdv7tSR1gBb3uNBvvAhHCBzL35ODDMjNai.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRkP1f1PjDdP0KVINqGujYknH6sPHckr0KVgv-b5HDsPWDkP1fz0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KWThnqPHRvn10%26ck%3D4773.2.92.183.158.321.163.308%26dt%3D1588469442%26wd%3D%26tpl%3Dtpl%5F11534%5F21264%5F17382%26l%3D1517434154%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; LGUID=20200503093045-79adcab5-46b7-4f59-ac1f-6067cc15e281; _gid=GA1.2.919133323.1588469631; gate_login_token=0664e172ad4d1fccde86bd8a71ea6814ce41dcd0dbbaed4faf8ac933ccc6c0f5; LG_LOGIN_USER_ID=e07e7d6cb23bd838f523493ed590214ad6865ab7d184ed9febe48b20064f1877; LG_HAS_LOGIN=1; _putrc=287B5A691ECD8BB2123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABIID808B7FDC20B5D2D9148A8AED331A4E5; login=true; unick=%E8%91%A3%E4%BC%A0%E4%BA%AD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=40; privacyPolicyPopup=false; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20200503093428-171d82b994c98-06c95176062ab3-c373667-1049088-171d82b994dae3; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=57681dcf4c50f6f99969648851ed36b9403648929b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588469701; LGRID=20200503093459-c946a356-733f-4e8a-ae2a-5b5bf718743d; SEARCH_ID=2b8deb0dacbd434c82dc7c95e2752b38'
}
# response = requests.post("https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false",data = data, headers = headers)
# # print(response.text)
#
# print(type(response.json()))
# print(response.json()) # 字典形式