# -*- coding: utf-8 -*-

__author__ = 'Zhenyue Qin'

import os
import json

#setting
_StackOverflow_URL = "http://stackoverflow.com/"
_Login_URL = "https://stackoverflow.com/users/login"
_Cookies_File_Name = "cookies.json"

#global var
_session = None
_header = {'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://www.stackoverflow.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; '
                         'Trident/7.0; Touch; LCJB; rv:11.0)'
                         ' like Gecko',
           'Host': 'www.stackoverflow.com'}

def create_cookies():
    '''
    create the cookie file, please follow the instructions
    :return: None
    :type: None
    '''
    if os.path.isfile(_Cookies_File_Name) is False:
        email = input("Please input your email: ")
        password = input("Please input your password")

def login(email='', password='', captcha='', save_cookies=True):
    '''
    login to the StackOverflow manually

    :param str email: email address
    :param str password: password
    :param str captcha: captcha
    :param bool savecookies: whether to store cookie files
    :return: the first return value stands for "whether succeed"
             the second return value stands for "the information why failed"
    :rtype: (int, dict)
    '''
    global _session
    global _header

    data = {'email': email, 'password': password,
            'rememberme': 'y', 'captcha': captcha}
    r = _session.post(_Login_URL, data=data)
    j = r.json()
    c = int(j['r'])
    m = j['msg']
    if c == 0 and save_cookies is True:
        with open(_Cookies_File_Name, 'w') as f:
            json.dump(_session.cookies.get_dict(), f)
    return c, m


login("chin290956355@gmail.com", "940915")