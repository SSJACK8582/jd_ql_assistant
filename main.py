# coding=utf-8
import os
import hmac
import json
import requests
import configparser
import jd_assistant
from log import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def list_to_json(item_list):
    json = {}
    for item in item_list:
        json[item[0]] = item[1]
    return json


def get_config(file_name='config.ini'):
    file = os.path.join(os.getcwd(), file_name)
    config = configparser.RawConfigParser()
    config.read(file, encoding='utf-8-sig')
    return config.items('config')


def get_account(file_name='config.ini'):
    file = os.path.join(os.getcwd(), file_name)
    config = configparser.RawConfigParser()
    config.read(file, encoding='utf-8-sig')
    return config.items('account')


if __name__ == '__main__':
    config_list = get_config()
    account_list = get_account()
    accounts = [account for _, account in account_list]
    config_json = list_to_json(config_list)
    area = config_json.get('area', '')
    sku_ids = config_json.get('sku_ids', '')
    buy_time = config_json.get('buy_time', '')
    mode = config_json.get('mode', '')
    if sku_ids and buy_time and mode:
        jd_assistant.main(area, sku_ids, buy_time, mode, accounts)
        input('\n')
