# project_2019-nCoV
 基于python的2019新冠病毒GUI可视化项目，数据源来源：https://github.com/canghailan/Wuhan-2019-nCoV/tree/master/Data  
 
 项目功能：  
1、可以实时更新数据  
2、国内可以按省份生成可视化数据，可任选确诊，现存确诊，治愈，死亡人数  
3、国外可以按国家生成可视化数据，可任选确诊，现存确诊，治愈，死亡人数  
4、全世界可以生成总体数据，可任选确诊，现存确诊，治愈，死亡人数  
5、可以获取到当日新增确诊，现存确诊，治愈，死亡人数  
6、可以获取到当日某省份（国内），某国家（国外），世界详细数据  
项目结构：  
1、data文件夹存储数据文件，其中分别包括国内，国外和世界数据  
2、img文件夹存储图片，其中分别包括国内，国外和世界图片  
3、cache.txt文件存储数据最新更新日期  
4、getData.py为数据爬取模块  
5、dataProcessing.py为数据处理模块  
6、show_img.py为图片生成模块  
7、UI为用户界面模块  
