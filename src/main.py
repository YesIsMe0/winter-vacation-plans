import DataProcessingClass as dpc
import schedule_todo_list
import datetime

# 获取当前的时间
current_time = datetime.datetime.now().time()
# 获取当前的日期
current_date = datetime.date.today()
# 如果没有到第二天的凌晨3点，日期修改为昨天
if current_time < datetime.time(3, 0):
    current_date = current_date - datetime.timedelta(days=1)
    
# 如果没有到第二天的凌晨3点，时间修改为昨天的23点30分
current_time = current_time.replace(hour=23, minute=30, second=0, microsecond=0)


if current_time < datetime.time(22, 0):
    print(f"{current_date}的学习任务")
    # 创建 DataProcessingClass 实例
    dpc_instance = dpc.DataProcessingClass(current_date=current_date)
    # 如果当前时间是晚上10点前
    dpc_instance.new_today_csv(current_date)
    # dpc_instance.course
    schedule_todo_list = schedule_todo_list.schedule_week(date_today=current_date)
else:
    print("schedule_night:将在23:00输入今天的学习情况")
    # 如果当前时间是晚上10点或以后
    schedule_todo_list.schedule_night(
        current_date=current_date, current_time=current_time
    )

"""放服务器运行，每天晚上11点更新今天的学习任务"""
# dpc.input_today_study()
# schedule_night = schedule_todo_list.schedule_night()
