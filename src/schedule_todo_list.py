import schedule
import time
import DataProcessingClass as dpc
import img_plot
import datetime


# 每天晚上11点后更新今天的学习任务
def schedule_night(current_date, current_time):
    # 创建 DataProcessingClass 实例
    dpc_instance = dpc.DataProcessingClass(current_date=current_date)

    def job():
        # 执行input_today_study函数
        dpc_instance.input_today_study(current_date=current_date)
        return

    # 如果传入的 current_time 是晚上11点或以后
    if current_time >= datetime.time(23, 0):
        # 设置立即执行 job 函数
        job()
        return  # 结束函数

    while True:
        schedule.run_pending()
        time.sleep(1)


"""
以后可以定期发送邮件，提醒自己
def schedule_morning():
    def job():
        os.system("python3 send_email.py")

    schedule.every().day.at("7:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
"""


# 判断是否是周一，如果是周一，就画一次柱状图
def schedule_week(date_today):
    if date_today.weekday() == 0:  # 如果今天是周一
        img_plot.img_plot_bar_chart(date_today)
    else:
        pass
