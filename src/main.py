
import DataProcessingClass as dpc
import schedule_todo_list
import datetime
# 今天的日期
current_date = datetime.date.today()
dpc = dpc.DataProcessingClass(current_date=current_date)
dpc.new_today_csv()
dpc.course

"""放服务器运行，每天晚上11点更新今天的学习任务"""
# DataProcessing.input_today_study()
# schedule_night = schedule_night.schedule_night()

schedule_todo_list = schedule_todo_list.schedule_week(date_today=current_date)

