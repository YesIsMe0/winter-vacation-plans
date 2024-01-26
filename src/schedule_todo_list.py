
import schedule
import time
import DataProcessingClass
import img_plot


def schedule_night():
    def job():
        DataProcessingClass.input_today_study()

    schedule.every().day.at("23:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

"""
以后可以定期发送邮件，提醒自己
def schedule_morning():
    def job():
        img_plot.img_plot_bar_chart()

    schedule.every().day.at("7:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
"""

# 判断是否是周一，如果是周一，就画一次柱状图
def schedule_week(date_today):
    if date_today.weekday()  == 0: # 如果今天是周一
        img_plot.img_plot_bar_chart(date_today)
        
    else:
        pass
