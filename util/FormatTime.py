# coding:utf-8
import time


def date_time_chinese():
    strf_time = time.strftime('%Y年%m月%日 %H点%M分%S', time.localtime(time.time()))
    return strf_time


def time_chinese():
    strf_time = time.strftime('%H点%M分%S', time.localtime(time.time()))
    return strf_time


def date_time_english():
    strf_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return strf_time


def time_english():
    strf_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
    return strf_time
