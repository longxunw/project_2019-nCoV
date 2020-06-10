from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
import pandas as pd

from show_img import *
import getData
from dataProcessing import dataProcess


class basedesk():
    def __init__(self, master):
        self.root = master
        # 给定标题
        self.root.title('2019-nCoV新冠病毒数据可视化')

        initface(self.root)  # 用来初始化页面的类


class initface():
    def __init__(self, master):
        self.master = master
        # 主页面根帧
        self.initface = Frame(self.master, )
        self.initface.pack()
        # 4个按钮
        cnButton = Button(self.initface, text='国内疫情', command=self.cnPlay, width=85, height=3)
        ncnButton = Button(self.initface, text='国外疫情', command=self.ncnPlay, width=85, height=3)
        worldButton = Button(self.initface, text='世界总疫情', command=self.worldPlay, width=85, height=3)
        dataRefreshButton = Button(self.initface, text='更新最新数据', command=self.dataRefresh, width=85, height=3)
        # 显示疫情最新情况
        with open('cache.txt') as f:
            last = f.readlines()[0]
        df = pd.read_csv('data/total.csv')
        earlyData = df.iloc[len(df) - 2, :]  # 前一天数据
        lastData = df.iloc[len(df) - 1, :]  # 最新数据

        self.lastDateLabel = Label(self.initface, text=f'最新数据更新日期：{last}', width=85, height=1)
        # 最新数据帧
        froLastData = Frame(self.initface)
        # 数据增长帧
        froIncrease = Frame(self.initface)
        lastRemain = lastData[1] - lastData[2] - lastData[3] + lastData[4] - lastData[5] - lastData[6]
        earlyRemain = earlyData[1] - earlyData[2] - earlyData[3] + earlyData[4] - earlyData[5] - earlyData[6]
        # 几个显示最新数据的label
        self.lastRemainLabel = Label(froLastData, text=f'现存确诊：{lastRemain}', width=25)
        self.lastConfirmLabel = Label(froLastData, text=f'确诊：{lastData[1] + lastData[4]}', width=20, height=1)
        self.lastCuredLabel = Label(froLastData, text=f'治愈：{lastData[2] + lastData[5]}', width=20, height=1)
        self.lastDeadLabel = Label(froLastData, text=f'死亡：{lastData[3] + lastData[6]}', width=20, height=1)
        # 几个显示增长数据的label
        self.remainIncrease = Label(froIncrease, width=25)
        if lastRemain - earlyRemain > 0:
            self.remainIncrease.config(text=f'现存确诊较昨日增加：{lastRemain - earlyRemain}')
        else:
            self.remainIncrease.config(text=f'现存确诊较昨日减少：{earlyRemain - lastRemain}')
        self.ConfirmIncrease = Label(froIncrease,
                                     text=f'确诊较昨日增加：{lastData[1] + lastData[4] - earlyData[1] - earlyData[4]}',
                                     width=20)
        self.CuredIncrease = Label(froIncrease,
                                   text=f'治愈较昨日增加：{lastData[2] + lastData[5] - earlyData[2] - earlyData[5]}',
                                   width=20)
        self.DeadIncrease = Label(froIncrease,
                                  text=f'死亡较昨日增加：{lastData[3] + lastData[6] - earlyData[3] - earlyData[6]}',
                                  width=20)
        # 将上述button和label放入界面
        cnButton.pack(side=TOP, fill='x')
        ncnButton.pack(side=TOP, fill='x')
        worldButton.pack(side=TOP, fill='x')
        dataRefreshButton.pack(side=TOP, fill='x')

        self.lastDateLabel.pack(side=TOP, fill='x')

        froLastData.pack(side=TOP, fill='x')
        self.lastRemainLabel.pack(side=LEFT, anchor=W)
        self.lastConfirmLabel.pack(side=LEFT, anchor=W)
        self.lastCuredLabel.pack(side=LEFT, anchor=W)
        self.lastDeadLabel.pack(side=LEFT, anchor=W)

        froIncrease.pack(side=TOP, fill='x')
        self.remainIncrease.pack(side=LEFT, anchor=W)
        self.ConfirmIncrease.pack(side=LEFT, anchor=W)
        self.CuredIncrease.pack(side=LEFT, anchor=W)
        self.DeadIncrease.pack(side=LEFT, anchor=W)

    def cnPlay(self):
        """国内疫情情况按钮事件，销毁主页面帧，初始化子页面帧，同时初始化默认图片"""
        self.initface.destroy()
        show_cn()
        cn(self.master)

    def ncnPlay(self):
        """国外疫情情况按钮事件，销毁主页面帧，初始化子页面帧，同时初始化默认图片"""
        self.initface.destroy()
        show_ncn()
        ncn(self.master)

    def worldPlay(self):
        """全球疫情情况按钮事件，销毁主页面帧，初始化子页面帧，同时初始化默认图片"""
        self.initface.destroy()
        show_total()
        world(self.master)

    def dataRefresh(self):
        """数据更新按钮事件，重新获取数据并处理，并更新页面显示数据"""
        getData.init()
        getData.get_data()
        dataProcess()
        # 取得最新更新日期
        with open('cache.txt') as f:
            last = f.readlines()[0]
        df = pd.read_csv('data/total.csv')

        earlyData = df.iloc[len(df) - 2, :]  # 前一天数据
        lastData = df.iloc[len(df) - 1, :]  # 最新数据

        # 最新现存确诊
        lastRemain = lastData[1] - lastData[2] - lastData[3] + lastData[4] - lastData[5] - lastData[6]
        # 前一天现存确诊
        earlyRemain = earlyData[1] - earlyData[2] - earlyData[3] + earlyData[4] - earlyData[5] - earlyData[6]

        # 更新显示数据
        self.lastRemainLabel.config(text=f'现存确诊：{lastRemain}')
        self.lastDateLabel.config(text=f'最新数据更新日期：{last}')
        self.lastConfirmLabel.config(text=f'确诊：{lastData[1] + lastData[4]}')
        self.lastCuredLabel.config(text=f'治愈：{lastData[2] + lastData[5]}')
        self.lastDeadLabel.config(text=f'死亡：{lastData[3] + lastData[6]}')

        if lastRemain - earlyRemain > 0:
            self.remainIncrease.config(text=f'现存确诊较昨日增加：{lastRemain - earlyRemain}')
        else:
            self.remainIncrease.config(text=f'现存确诊较昨日减少：{earlyRemain - lastRemain}')
        self.ConfirmIncrease.config(text=f'确诊较昨日增加：{lastData[1] + lastData[4] - earlyData[1] - earlyData[4]}')
        self.CuredIncrease.config(text=f'治愈较昨日增加：{lastData[2] + lastData[5] - earlyData[2] - earlyData[5]}')
        self.DeadIncrease.config(text=f'死亡较昨日增加：{lastData[3] + lastData[6] - earlyData[3] - earlyData[6]}')


class cn():
    def __init__(self, master):
        self.master = master  # 获取根页面
        # 初始化子页面根帧
        self.cnroot = Frame(self.master, width=1000, height=500)
        # 用来显示图片的帧
        forImage = Frame(self.cnroot)
        # 用来显示按钮的帧
        forButton = Frame(self.cnroot)

        # 几个用来获取参数的复选框，都初始化为True
        self.confirmVar = BooleanVar()
        self.confirmVar.set(True)
        confirmButton = Checkbutton(forButton, text='确诊', variable=self.confirmVar,
                                    onvalue=True, offvalue=False)
        self.remainVar = BooleanVar()
        self.remainVar.set(True)
        remainButton = Checkbutton(forButton, text='现存', variable=self.remainVar,
                                   onvalue=True, offvalue=False)
        self.curedVar = BooleanVar()
        self.curedVar.set(True)
        curedButton = Checkbutton(forButton, text='治愈', variable=self.curedVar,
                                  onvalue=True, offvalue=False)
        self.deadVar = BooleanVar()
        self.deadVar.set(True)
        deadButton = Checkbutton(forButton, text='死亡', variable=self.deadVar,
                                 onvalue=True, offvalue=False)
        self.provinceVar = StringVar()
        self.provinceVar.set('全国')
        provinceCmb = ttk.Combobox(forButton, width=20, textvariable=self.provinceVar)
        # 设置省份选项values
        provinceCmb['values'] = ['全国', '北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省',
                                 '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
                                 '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省',
                                 '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省',
                                 '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区',
                                 '新疆维吾尔自治区', '台湾省', '香港特别行政区', '澳门特别行政区']
        # 设置默认值为'全国'
        provinceCmb.current(0)

        # 几个按钮
        # 提交选择，获取所需图片
        changeButton = Button(forButton, text='确认', command=self.change_img, width=20, height=1)
        # 保存图片到本地
        saveButton = Button(forButton, text='保存图片', command=self.save_img, width=20, height=1)
        # 获取所选择的最新详细疫情数字
        conclusionButton = Button(forButton, text='最新详细数据', command=self.conclusion, width=20, height=1)
        # 返回主页
        backButton = Button(self.cnroot, text='返回主页', command=self.back, width=20, height=2)

        # 获取图片，并resize图片到相应大小
        self.img = Image.open('img/cn/全国.png').resize((800, 500))
        # 由于tkinter不支持png图片，所以使用PIL库进行处理
        the_image = ImageTk.PhotoImage(self.img)
        # 图片label
        self.imglabel = Label(forImage, width=800, height=500)
        # 设置图片
        self.imglabel['image'] = the_image
        self.imglabel.image = the_image

        # 将上述元素放入页面中
        self.cnroot.pack()
        forImage.pack(side=LEFT, fill='y')
        self.imglabel.pack(side=TOP, fill='both')

        backButton.pack(side=TOP, fill='x')
        forButton.pack(side=RIGHT, anchor=CENTER)
        confirmButton.pack(side=TOP, fill='x')
        remainButton.pack(side=TOP, fill='x')
        curedButton.pack(side=TOP, fill='x')
        deadButton.pack(side=TOP, fill='x')

        provinceCmb.pack(side=TOP, anchor=CENTER)

        changeButton.pack(side=TOP, fill='x')
        conclusionButton.pack(side=TOP, fill='x')
        saveButton.pack(side=TOP, fill='x')

    def back(self):
        """返回主页"""
        # 销毁当前页面根帧
        self.cnroot.destroy()
        # 初始化主页面帧
        initface(self.master)

    def change_img(self):
        """提交所选参数，更新图片"""
        # 向图片生成模块提交参数，生成图片
        show_cn(self.confirmVar.get(), self.remainVar.get(), self.curedVar.get(), self.deadVar.get(),
                self.provinceVar.get())
        # 获取图片并使用PIL库进行处理
        self.img = Image.open(f'img/cn/{self.provinceVar.get()}.png').resize((800, 500))
        the_image = ImageTk.PhotoImage(self.img)
        # 设置图片
        self.imglabel['image'] = the_image
        self.imglabel.image = the_image

    def save_img(self):
        """保存图片"""
        # 获取保存路径
        fname = asksaveasfilename(title='保存图片', filetypes=[('PNG', '.png')])
        # 若保存路径非空，保存图片
        if fname:
            self.img.save(str(fname) + '.png', 'PNG')
            messagebox.showinfo('提示', f'保存成功：{fname}')

    def conclusion(self):
        """显示所选参数对应的详细信息，并更新图片"""
        # 更新图片
        self.change_img()
        # 获得最新数据更新日期
        with open('cache.txt') as f:
            last = f.readlines()[0]
        # 读取最新一天的数据
        df = pd.read_csv(f'data/cn/{last}.csv')
        # 获取省份参数
        province = self.provinceVar.get()
        # 得到具体数据
        confirm, cured, dead = 0, 0, 0
        if province == '全国':
            confirm = df.iloc[0, 8]
            cured = df.iloc[0, 10]
            dead = df.iloc[0, 11]
        else:
            provinces = list(df['province'])
            idx = provinces.index(province)
            confirm = df.iloc[idx, 8]
            cured = df.iloc[idx, 10]
            dead = df.iloc[idx, 11]
        # 弹出消息框显示最新信息
        messagebox.showinfo(f'{province}疫情最新信息：',
                            f'确诊：{confirm}，现存确诊：{confirm - cured - dead}，\n治愈：{cured}，死亡：{dead}')


class ncn():
    def __init__(self, master):
        self.master = master  # 获取根页面
        # 初始化子页面根帧
        self.ncnroot = Frame(self.master, width=1000, height=500)
        # 用来显示图片的帧
        forImage = Frame(self.ncnroot)
        # 用来显示按钮的帧
        forButton = Frame(self.ncnroot)

        # 几个用来获取参数的复选框，都初始化为True
        self.confirmVar = BooleanVar()
        self.confirmVar.set(True)
        confirmButton = Checkbutton(forButton, text='确诊', variable=self.confirmVar,
                                    onvalue=True, offvalue=False)
        self.remainVar = BooleanVar()
        self.remainVar.set(True)
        remainButton = Checkbutton(forButton, text='现存', variable=self.remainVar,
                                   onvalue=True, offvalue=False)
        self.curedVar = BooleanVar()
        self.curedVar.set(True)
        curedButton = Checkbutton(forButton, text='治愈', variable=self.curedVar,
                                  onvalue=True, offvalue=False)
        self.deadVar = BooleanVar()
        self.deadVar.set(True)
        deadButton = Checkbutton(forButton, text='死亡', variable=self.deadVar,
                                 onvalue=True, offvalue=False)
        # 获取国家的下拉框
        self.countryVar = StringVar()
        self.countryVar.set('国外汇总')
        countryCmb = ttk.Combobox(forButton, width=20, textvariable=self.countryVar)
        # 由于国家数目可能会出现增加，所以获取最新国家列表
        with open('cache.txt') as f:
            text = f.readlines()[0]
        # 读取最新国外数据
        df = pd.read_csv(f'data/ncn/{text}.csv')
        values = list(df['country'])
        # 加入'国外汇总'这一默认值
        values.insert(0, '国外汇总')
        # 设置下拉框values
        countryCmb['values'] = values
        # 设置默认值
        countryCmb.current(0)

        # 几个按钮
        changeButton = Button(forButton, text='确认', command=self.change_img, width=20, height=1)
        saveButton = Button(forButton, text='保存图片', command=self.save_img, width=20, height=1)
        conclusionButton = Button(forButton, text='详细数据', command=self.conclusion, width=20, height=1)
        backButton = Button(self.ncnroot, text='返回主页', command=self.back, width=20, height=2)
        # 获取图片并更改图片大小和格式
        self.img = Image.open('img/ncn/国外汇总.png').resize((800, 500))
        the_image = ImageTk.PhotoImage(self.img)
        # 图片label
        self.imglabel = Label(forImage, width=800, height=500)
        # 设置图片
        self.imglabel['image'] = the_image
        self.imglabel.image = the_image

        # 将上述元素放入页面中
        self.ncnroot.pack()
        forImage.pack(side=LEFT, fill='y')
        self.imglabel.pack(side=TOP, fill='both')

        backButton.pack(side=TOP, fill='x')
        forButton.pack(side=RIGHT, anchor=CENTER)
        confirmButton.pack(side=TOP, fill='x')
        remainButton.pack(side=TOP, fill='x')
        curedButton.pack(side=TOP, fill='x')
        deadButton.pack(side=TOP, fill='x')

        countryCmb.pack(side=TOP, anchor=CENTER)

        changeButton.pack(side=TOP, fill='x')
        conclusionButton.pack(side=TOP, fill='x')
        saveButton.pack(side=TOP, fill='x')

    def back(self):
        """返回主页"""
        self.ncnroot.destroy()
        initface(self.master)

    def change_img(self):
        """提交所选参数，更新图片"""
        show_ncn(self.confirmVar.get(), self.remainVar.get(), self.curedVar.get(), self.deadVar.get(),
                 self.countryVar.get())
        # 获取对应图片
        self.img = Image.open(f'img/ncn/{self.countryVar.get()}.png').resize((800, 500))
        the_img = ImageTk.PhotoImage(self.img)
        # 设置图片
        self.imglabel['image'] = the_img
        self.imglabel.image = the_img

    def save_img(self):
        """保存图片"""
        fname = asksaveasfilename(title='保存图片', filetypes=[('PNG', '.png')])
        if fname:
            self.img.save(str(fname) + '.png', 'PNG')
            messagebox.showinfo('提示', f'保存成功：{fname}')

    def conclusion(self):
        """显示所选参数对应的详细信息，并更新图片"""
        # 更新图片
        self.change_img()
        # 获取最新数据
        with open('cache.txt') as f:
            last = f.readlines()[0]
        df = pd.read_csv(f'data/ncn/{last}.csv')
        # 获取国家参数
        country = self.countryVar.get()
        # 获取具体数据
        confirm, cured, dead = 0, 0, 0
        if country == '国外汇总':
            confirm = df.iloc[0, 8]
            cured = df.iloc[0, 10]
            dead = df.iloc[0, 11]
        else:
            countries = list(df['country'])
            idx = countries.index(country)
            confirm = df.iloc[idx, 8]
            cured = df.iloc[idx, 10]
            dead = df.iloc[idx, 11]
        # 弹出消息框显示最新信息
        messagebox.showinfo(f'{country}疫情最新信息：', f'确诊：{confirm}，现存确诊：{confirm - cured - dead}，\n治愈：{cured}，死亡：{dead}')


class world():
    def __init__(self, master):
        self.master = master  # 获取根页面
        # 初始化子页面根帧
        self.world = Frame(self.master, width=1000, height=500)
        # 用来显示图片的帧
        forImage = Frame(self.world)
        # 用来显示按钮的帧
        forButton = Frame(self.world)

        # 几个用来获取参数的复选框，对参数进行初始化
        self.confirmVar = BooleanVar()
        self.confirmVar.set(True)
        confirmButton = Checkbutton(forButton, text='确诊', variable=self.confirmVar,
                                    onvalue=True, offvalue=False)
        self.remainVar = BooleanVar()
        self.remainVar.set(True)
        remainButton = Checkbutton(forButton, text='现存', variable=self.remainVar,
                                   onvalue=True, offvalue=False)
        self.curedVar = BooleanVar()
        self.curedVar.set(True)
        curedButton = Checkbutton(forButton, text='治愈', variable=self.curedVar,
                                  onvalue=True, offvalue=False)
        self.deadVar = BooleanVar()
        self.deadVar.set(True)
        deadButton = Checkbutton(forButton, text='死亡', variable=self.deadVar,
                                 onvalue=True, offvalue=False)
        nullLabel = Label(forButton, text='   ')
        self.cnVar = BooleanVar()
        self.cnVar.set(False)
        cnButton = Checkbutton(forButton, text='国内', variable=self.cnVar,
                               onvalue=True, offvalue=False)
        self.ncnVar = BooleanVar()
        self.ncnVar.set(False)
        ncnButton = Checkbutton(forButton, text='国外', variable=self.ncnVar,
                                onvalue=True, offvalue=False)
        self.worldVar = BooleanVar()
        self.worldVar.set(True)
        worldButton = Checkbutton(forButton, text='全球', variable=self.worldVar,
                                  onvalue=True, offvalue=False)
        # 获取图片并更改图片大小和格式
        self.img = Image.open('img/total.png').resize((800, 500))
        the_image = ImageTk.PhotoImage(self.img)
        # 图片label
        self.imglabel = Label(forImage, width=800, height=500)
        # 设置图片
        self.imglabel['image'] = the_image
        self.imglabel.image = the_image

        # 几个按钮
        changeButton = Button(forButton, text='确认', width=20, height=1, command=self.change_img)
        saveButton = Button(forButton, text='保存图片', width=20, height=1, command=self.save_img)
        conclusionButton = Button(forButton, text='详细数据', width=20, height=1, command=self.conclusion)
        backButton = Button(self.world, text='返回主页', width=20, height=2, command=self.back)

        # 将上述元素放入页面
        self.world.pack()
        forImage.pack(side=LEFT, fill='y')
        self.imglabel.pack(side=TOP, fill='both')

        backButton.pack(side=TOP, fill='x')
        forButton.pack(side=RIGHT, anchor=CENTER)
        confirmButton.pack(side=TOP, fill='x')
        remainButton.pack(side=TOP, fill='x')
        curedButton.pack(side=TOP, fill='x')
        deadButton.pack(side=TOP, fill='x')

        nullLabel.pack(side=TOP, fill='x')

        cnButton.pack(side=TOP, fill='x')
        ncnButton.pack(side=TOP, fill='x')
        worldButton.pack(side=TOP, fill='x')

        changeButton.pack(side=TOP, fill='x')
        conclusionButton.pack(side=TOP, fill='x')
        saveButton.pack(side=TOP, fill='x')

    def back(self):
        """返回主页"""
        self.world.destroy()
        initface(self.master)

    def change_img(self):
        """提交所选参数，更新图片"""
        show_total(self.confirmVar.get(), self.remainVar.get(), self.curedVar.get(), self.deadVar.get(),
                   self.cnVar.get(), self.ncnVar.get(), self.worldVar.get())
        # 获取图片
        self.img = Image.open('img/total.png').resize((800, 500))
        the_image = ImageTk.PhotoImage(self.img)
        # 设置图片
        self.imglabel['image'] = the_image
        self.imglabel.image = the_image

    def save_img(self):
        """保存图片"""
        fname = asksaveasfilename(title='保存图片', filetypes=[('PNG', '.png')])
        if fname:
            self.img.save(str(fname) + '.png', 'PNG')
            messagebox.showinfo('提示', f'保存成功：{fname}')

    def conclusion(self):
        """显示所选参数对应的详细信息，并更新图片"""
        # 更新图片
        self.change_img()
        # 获取最新数据
        with open('cache.txt') as f:
            last = f.readlines()[0]
        df = pd.read_csv('data/total.csv')
        l = len(df)
        cn_confirm, cn_cured, cn_dead = df.iloc[l - 1, 1], df.iloc[l - 1, 2], df.iloc[l - 1, 3]
        ncn_confirm, ncn_cured, ncn_dead = df.iloc[l - 1, 4], df.iloc[l - 1, 5], df.iloc[l - 1, 6]
        world_confirm, world_cured, world_dead = cn_confirm + ncn_confirm, cn_cured + ncn_cured, cn_dead + ncn_dead
        # 计算所需显示的信息
        s = ''
        if self.cnVar.get():
            s = f'{s}\n国内最新疫情信息：\n\t确诊：{cn_confirm}，现存确诊：{cn_confirm - cn_cured - cn_dead}，\n\t治愈：{cn_cured}，死亡：{cn_dead}'
        if self.ncnVar.get():
            s = f'{s}\n国外最新疫情信息：\n\t确诊：{ncn_confirm}，现存确诊：{ncn_confirm - ncn_cured - ncn_dead}，\n\t治愈：{ncn_cured}，死亡：{ncn_dead}'
        if self.worldVar.get():
            s = f'{s}\n全球最新疫情信息：\n\t确诊：{world_confirm}，现存确诊：{world_confirm - world_cured - world_dead}，\n\t治愈：{world_cured}，死亡：{world_dead}'
        # 弹出消息框显示最新信息
        messagebox.showinfo('最新疫情信息', s)


if __name__ == '__main__':
    root = Tk()  # 即整个用户界面都在这个根界面下运行
    basedesk(root)  # 驱动根界面运转类
    root.mainloop()  # 界面主循环
