# coding=utf-8
import os
import argparse
import datetime
import jd_assistant

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--area', type=str, help='area')
parser.add_argument('-s', '--sku_ids', type=str, help='sku_ids')
parser.add_argument('-b', '--buy_time', type=str, help='buy_time')
parser.add_argument('-m', '--mode', type=str, help='mode')
parser.add_argument('-i', '--index', type=str, help='index')
args = parser.parse_args()


def get_account_list(index):
    account_list = []
    if os.environ.get('JD_COOKIE'):
        if '&' in os.environ['JD_COOKIE']:
            account_list = os.environ['JD_COOKIE'].split('&')
        elif '\n' in os.environ['JD_COOKIE']:
            account_list = os.environ['JD_COOKIE'].split('\n')
        else:
            account_list = [os.environ['JD_COOKIE']]
    if index:
        index_list = [int(i) for i in index.split(',')]
        account_list = [account_list[i] for i in index_list]
    return account_list


if __name__ == '__main__':
    if args.sku_ids and args.buy_time and args.mode:
        account_list = get_account_list(args.index)
        buy_time = '{} {}'.format(datetime.datetime.now().strftime('%Y-%m-%d'), args.buy_time)
        jd_assistant.main(args.area, args.sku_ids, buy_time, args.mode, account_list)
