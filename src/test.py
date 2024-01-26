import DataProcessingClass as dp_module
import datetime as datetime
import schedule_todo_list
import os
for i in range(1, 80):
    current_date = datetime.date.today() + datetime.timedelta(days=i)
    dp = dp_module.DataProcessingClass(current_date)
    dp.new_today_csv()
    dp.get_course()
    print(dp.today_course)
    print(dp.today)
    print(dp.course)
    print("---------------------------------")
    dp.input_today_study()
    # 画图
    # 移动temp文件夹中的文件到time文件夹中
    os.system("mv temp/* time/")
    schedule_todo_list.schedule_week(current_date)


    