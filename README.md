#BJUT新版正方教务系统加权/GPA计算脚本
##项目说明
该项目为解决新版教务系统出现后原有查分脚本等失效的情况编写.
##依赖安装
cd BJUT_grade_new\
pip install -r requirements.txt
##使用介绍
在main.py中的user_info填写教务系统的账户密码并运行即可.若想查看全部课程成绩情况,可以自行将变量show_all_grades设置为True.
##说明
GPA算法遵循[bjuthelper(野生工大助手)](https://github.com/wangyufeng0615/bjuthelper) 的底层算法,但出国时打印成绩单似乎使用的算法与之不一致,请以实际情况为准(也可自行修改代码).
##致谢
本项目提取使用了[@NeroAsmarr](https://github.com/NeroAsmarr) 编写并开源的新版正方系统API,针对BJUT的"教务特色"作了简单的修改,原API主页如下.
> [正方教务管理系统API](https://neroasmar.top/zfnew/)
##LICENSE
MIT License

Copyright (c) 2020 wzp21142