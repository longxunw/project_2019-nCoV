import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def show_cn(confirm=True, remain=True, cured=True, dead=True, province='全国'):
    plt.figure()
    # 即需要生成的是省份疫情图片
    if province != '全国':
        df = pd.read_csv('data/cn/total.csv')
        df = df[df['province'] == province] # 得到对应省份疫情信息
        df = df.groupby(by=['date']) # 按天分组
        x = [] # 存储日期
        confirmed_data = []
        cured_data = []
        dead_data = []
        for key, data in df:
            x.append(key)
            # 选择第一行数据，即省份总体数据
            confirmed_data.append(data.iloc[0, -4])
            cured_data.append(data.iloc[0, -2])
            dead_data.append(data.iloc[0, -1])
        x = pd.to_datetime(x)
        # 计算现存确诊
        remain_data = np.array(confirmed_data)-np.array(cured_data)-np.array(dead_data)
        # 检查是否需要加入对应数据，如需要，就将数据加入图像中
        if confirm:
            plt.plot(x, confirmed_data, linestyle='-', color='red', label=f'{province}确诊人数')
        if remain:
            plt.plot(x, remain_data, linestyle='-', color='pink', label=f'{province}现存确诊')
        if cured:
            plt.plot(x, cured_data, linestyle='-', color='green', label=f'{province}治愈人数')
        if dead:
            plt.plot(x, dead_data, linestyle='-', color='black', label=f'{province}死亡人数')
    else: # 需要生成的是全国总体数据
        df = pd.read_csv('data/total.csv')
        x = pd.to_datetime(df['date'])
        y1 = df['cn_confirmed']
        y2 = df['cn_cured']
        y3 = df['cn_dead']
        y4 = y1 - y2 - y3
        if confirm:
            plt.plot(x, y1, linestyle='-', color='red', label='全国确诊人数')
        if remain:
            plt.plot(x, y4, linestyle='-', color='pink', label='全国现存确诊')
        if cured:
            plt.plot(x, y2, linestyle='-', color='green', label='全国治愈人数')
        if dead:
            plt.plot(x, y3, linestyle='-', color='black', label='全国死亡人数')
    plt.title(f'{province}疫情') # 设置图片标题
    plt.legend() # 添加图例
    plt.grid()  # 添加坐标轴
    plt.xticks(rotation=30) # 避免坐标值过密
    plt.savefig(f'img/cn/{province}.png', dpi=600) # 保存图片


def show_ncn(confirm=True, remain=True, cured=True, dead=True, country='国外汇总'):
    plt.figure()
    # 需要生成的不是国外汇总数据图片
    if country != '国外汇总':
        df = pd.read_csv('data/ncn/total.csv')
        df = df[df['country'] == country] # 拿到对应国家的数据
        x = pd.to_datetime(df['date'])
        y1 = df['confirmed']
        y2 = df['cured']
        y3 = df['dead']
        y4 = y1 - y2 - y3
        if confirm:
            plt.plot(x, y1, linestyle='-', color='red', label=f'{country}确诊人数')
        if remain:
            plt.plot(x, y4, linestyle='-', color='pink', label=f'{country}现存确诊')
        if cured:
            plt.plot(x, y2, linestyle='-', color='green', label=f'{country}治愈人数')
        if dead:
            plt.plot(x, y3, linestyle='-', color='black', label=f'{country}死亡人数')
    else: # 需要生成的是国外总体图片
        df = pd.read_csv('data/total.csv')
        x = pd.to_datetime(df['date'])
        y1 = df['ncn_confirmed']
        y2 = df['ncn_cured']
        y3 = df['ncn_dead']
        y4 = y1 - y2 - y3
        if confirm:
            plt.plot(x, y1, linestyle='-', color='red', label='国外确诊人数')
        if remain:
            plt.plot(x, y4, linestyle='-', color='pink', label='国外现存确诊')
        if cured:
            plt.plot(x, y2, linestyle='-', color='green', label='国外治愈人数')
        if dead:
            plt.plot(x, y3, linestyle='-', color='black', label='国外死亡人数')
    plt.title(f'{country}疫情')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=30)
    plt.savefig(f'img/ncn/{country}.png', dpi=600)


def show_total(confirm=True, remain=True, cured=True, dead=True, cn=False, ncn=False, w=True):
    df = pd.read_csv('data/total.csv')
    x = pd.to_datetime(df['date'])
    plt.figure()
    # 需要在图片中显示国内疫情情况
    if cn:
        y1 = df['cn_confirmed']
        y2 = df['cn_cured']
        y3 = df['cn_dead']
        y4 = y1 - y2 - y3
        # 根据选择地区不同，使用不同线条样式
        if confirm:
            plt.plot(x, y1, linestyle=':', color='red', label='国内确诊人数')
        if remain:
            plt.plot(x, y4, linestyle=':', color='pink', label='国内现存确诊')
        if cured:
            plt.plot(x, y2, linestyle=':', color='green', label='国内治愈人数')
        if dead:
            plt.plot(x, y3, linestyle=':', color='black', label='国内死亡人数')
    # 需要在图片中显示国外疫情情况
    if ncn:
        y1 = df['ncn_confirmed']
        y2 = df['ncn_cured']
        y3 = df['ncn_dead']
        y4 = y1 - y2 - y3
        if confirm:
            plt.plot(x, y1, linestyle='--', color='red', label='国外确诊人数')
        if remain:
            plt.plot(x, y4, linestyle='--', color='pink', label='国外现存确诊')
        if cured:
            plt.plot(x, y2, linestyle='--', color='green', label='国外治愈人数')
        if dead:
            plt.plot(x, y3, linestyle='--', color='black', label='国外死亡人数')
    # 需要在图片中显示全世界疫情情况
    if w:
        # 根据国内国外数据计算总体数据
        y1 = df['cn_confirmed'] + df['ncn_confirmed']
        y2 = df['cn_cured'] + df['ncn_cured']
        y3 = df['cn_dead'] + df['ncn_dead']
        y4 = y1-y2-y3
        if confirm:
            plt.plot(x, y1, linestyle='-', color='red', label='全球确诊人数')
        if remain:
            plt.plot(x, y4, linestyle='-', color='pink', label='全球现存确诊')
        if cured:
            plt.plot(x, y2, linestyle='-', color='green', label='全球治愈人数')
        if dead:
            plt.plot(x, y3, linestyle='-', color='black', label='全球死亡人数')
    plt.legend()
    plt.grid()
    plt.savefig('img/total.png', dpi=600)
