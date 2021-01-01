from selenium import webdriver

# 用于打印Cookie
# options = webdriver.ChromeOptions()
# options.debugger_address = "localhost:9222"
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.implicitly_wait(5)
chrome.maximize_window()

# 打开企业微信首页
chrome.get("https://work.weixin.qq.com/wework_admin/frame#index")
# 打印Cookie
print(chrome.get_cookies())

cookies = [{'domain': '.qq.com', 'expiry': 1609488061, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ARXo9Nal4bzFjGZHInPrvErM7VSKcfDBwb61BRfXKAAIKysIdHTwApufsYj5oCKQXVBswKe1Zm1B_Ygv1rOb-fZu4quvO6dsJJHFcsosVMRkGBuw8ZN7SblC_OyiCYgHx2VNYDcCYlh0eLx_4-PPNKLTusyLk3nA7HovFuUp-T9uITss6l2xhoKA6XtHk7mHbAxW4lXRqcp3DJUFLNjJMg5VUw0HgTlMnq_LhWNqGIK_pP9cL3AJQ3TMjSzbdOePsZ3ZAINHh2k_G28iNXgePA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850343003911'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325001134045'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'jBDbsKbGJZ65q3xp7l-6_S0uz-NbQuRgK5Eckulw1Md_c8Si31RAyVTwdNnlQN2B'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5324796'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8091648147'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640614147, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1609077119'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '39938794793409858'}, {'domain': '.qq.com', 'expiry': 1609574223, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1826795027.1609486789'}, {'domain': 'work.weixin.qq.com', 'expiry': 1609518324, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8el714v'}, {'domain': '.work.weixin.qq.com', 'expiry': 1612080039, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850343003911'}, {'domain': '.qq.com', 'expiry': 1910994845, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1910994845, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_c2511982a71e8'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640613112, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1672559823, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.187272271.1590374299'}]
for cookie in cookies:
    chrome.add_cookie(cookie)


# 打开企业微信首页
chrome.get("https://work.weixin.qq.com/wework_admin/frame#index")
print(chrome.get_cookies())

# 点击"通讯录"
chrome.find_element_by_id("menu_contacts").click()

# 点击批量导入/导出
chrome.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()

# 上传文件
chrome.find_element(By.ID, "js_upload_file_input").send_keys("d:\\Contacts.xlsx")

# 确认导入
chrome.find_element_by_id("submit_csv").click()

# 重新查看
chrome.find_element_by_id("reloadContact").click()

# 验证结果
rows = chrome.find_elements_by_css_selector(".member_colRight_memberTable_tr.member_colRight_memberTable_tr_Inactive.ui-sortable-handle")
row = rows[-1]
print(row.text)
assert "张三" in row.text

