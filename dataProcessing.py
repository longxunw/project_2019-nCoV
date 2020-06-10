import pandas as pd
import os
import numpy as np


def dataProcess():
    file_list = os.listdir('data/')
    file_list = [os.path.join('data/', i) for i in file_list]

    dates = []
    cn_total = [[], [], []]
    ncn_total = [[], [], []]
    for i in file_list:
        #跳过toal.csv文件
        if i.find('-') == -1:
            continue
        df = pd.read_csv(i)
        date = df.iloc[0, 0]#获得当日日期

        #国内国外数据分离
        df1 = df[df['country'] == '中国']
        df = df[df['country'] != '中国']

        #获取国内每日汇总
        cn = [df1.iloc[0, 7], df1.iloc[0, 9], df1.iloc[0, 10]]
        #计算国外每日汇总
        ncn = [np.sum(df['confirmed']), np.sum(df['cured']), np.sum(df['dead'])]

        for j in range(3):
            cn_total[j].append(cn[j])
            ncn_total[j].append(ncn[j])
        dates.append(date)
        #将国内国外数据分开保存
        df1.to_csv(f'data/cn/{date}.csv')
        df.to_csv(f'data/ncn/{date}.csv')
    #保存汇总数据
    with open('data/total.csv', mode='w', encoding='utf-8') as f:
        f.write('date,cn_confirmed,cn_cured,cn_dead,ncn_confirmed,ncn_cured,ncn_dead\n')
        for i in range(len(dates)):
            f.write(
                f'{dates[i]},{cn_total[0][i]},{cn_total[1][i]},{cn_total[2][i]},{ncn_total[0][i]},{ncn_total[1][i]},{ncn_total[2][i]}\n')

    #得到文件列表
    file_list = os.listdir('data/cn')
    file_list = [os.path.join('data/cn', i) for i in file_list]
    #得到一个初始化DataFrame
    df_total = pd.read_csv(file_list[0])
    for file in file_list[1:]:
        #跳过total.csv文件
        if file.find('-') == -1:
            continue
        df = pd.read_csv(file)
        #连接到total文件
        df_total = pd.concat([df_total, df], axis=0)
    #更新行索引号
    df_total.index = range(len(list(df_total['date'])))
    #生成文件
    df_total.to_csv('data/cn/total.csv')

    file_list = os.listdir('data/ncn')
    file_list = [os.path.join('data/ncn', i) for i in file_list]
    df_total = pd.read_csv(file_list[0])
    for file in file_list[1:]:
        if file.find('-') == -1:
            continue
        df = pd.read_csv(file)
        df_total = pd.concat([df_total, df], axis=0)
    df_total.index = range(len(list(df_total['date'])))
    df_total.to_csv('data/ncn/total.csv')
