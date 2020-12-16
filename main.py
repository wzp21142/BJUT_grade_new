import datetime

import GetInfo, Login

user_info = ('填你的账号', '填你的密码')
base_url = 'https://jwglxt.bjut.edu.cn'

lgn = Login(base_url=base_url)
lgn.login(user_info[0], user_info[1])
cookies = lgn.cookies  # cookies获取方法
person = GetInfo(base_url=base_url, cookies=cookies)
pinfo = person.get_pinfo()
entryear = pinfo.get('entryDate')[0:4]
totalCredits = 0
totalGrades = 0
total_gradePoints = 0
for i in range(datetime.datetime.now().year - int(entryear) + 1):
    tempYear = str(int(entryear) + i)
    grade = person.get_grade(tempYear, '0')  # 2019年、第1学期(0 or 1 or 2 此处0为全年)
    for a in grade.get('course'):
        if a.get('gradePoint') != '':
            totalCredits = totalCredits + float(a.get('credit'))
            totalGrades = totalGrades + float(a.get('credit')) * int(a.get('grade'))
            gradePoint = (4 if (int(a.get('grade')) >= 85) else 3 if (int(a.get('grade')) >= 70) else 2 if (
                    int(a.get('grade')) >= 60) else 0)
            total_gradePoints = total_gradePoints + float(a.get('credit')) * gradePoint
weighted_grade = totalGrades / totalCredits
GPA = total_gradePoints / totalCredits
print('%.2f' % weighted_grade)
print('%.2f' % GPA)
