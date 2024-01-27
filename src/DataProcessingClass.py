# data processing class
import pandas as pd
import os
from datetime import timedelta
import shutil

Max_study_course = 7  # 最多学习科目数

class DataProcessingClass:
    def __init__(self, current_date):

        self.today = current_date  # 初始日期
        self.course = self.new_today_csv(current_date)
        self.today_course = self.get_course(current_date)

    # 获取今天的学习任务
    def get_course(self,current_date):
        today = current_date
        self.course = pd.read_csv(f"data/{today}.csv", usecols=["学科", "完成情况"])
        self.today_course = self.course[self.course["完成情况"].isnull()][
            "学科"
        ].tolist()
        print(f"今天的学习科目{self.today_course}")

        # 将列表转换为DataFrame
        df_today_course = pd.DataFrame(self.today_course, columns=["学科"])
        # 将DataFrame保存为CSV文件
        df_today_course.to_csv(f"temp/{today}.csv", index=False)
        return self.course

    # 新建今天的csv文件
    def new_today_csv(self,current_date):
        # 获取今天的日期
        today = current_date
        yesterday = today - timedelta(days=1)
        # 如果没有昨天的csv文件，就新建一个，有的话就读取昨天的csv文件
        if not os.path.exists(f"data/{yesterday}.csv"):
            self.new_today_csv_from_plan(today)
        else:
            # 处理昨天的csv文件
            self.yesterday_data_process(today)

    # 从plan.csv文件新建今天的csv文件
    def new_today_csv_from_plan(self, current_date):
        today = current_date  # 初始日期
        data = pd.read_csv("data/plan.csv", usecols=["学科", "权值"])
        # 将每一行转换为一个对象
        data_dict = data.to_dict("records")
        # 对权值进行降序排序
        data = data.sort_values("权值", ascending=False).reset_index(drop=True)
        # 从高到低依次添加完成情况，初始化为""，第七个开始为0
        data["完成情况"] = ""
        data.loc[data.index >= 6, "完成情况"] = 0
        # 添加学习时间列
        data["学习时间"] = ""
        data.loc[data.index >= 6, "学习时间"] = 0

        data.to_csv(f"data/{today}.csv", index=False)
        return data_dict

    # 处理昨天的csv文件
    def yesterday_data_process(self, current_date):
        today = current_date  # 初始日期
        yesterday = today - timedelta(days=1)
        # 读取昨天的数据
        data_yesterday = pd.read_csv(f"data/{yesterday}.csv")
        # 对每一行进行处理
        for index, row in data_yesterday.iterrows():
            # 如果昨天未完成，调高权重
            if row["完成情况"] == 1:
                data_yesterday.at[index, "权值"] = self.yesterday_unfinished_weight(
                    row["权值"]
                )  # +0.7
            # 如果昨天学习时间最长，调高权重
            elif row["学习时间"] == data_yesterday["学习时间"].max():
                data_yesterday.at[index, "权值"] = self.yesterday_longest_time_weight(
                    row["权值"]
                )  # +0.5
            # 如果昨天没有学习，调高权重
            elif row["学习时间"] == 0:
                data_yesterday.at[index, "权值"] = self.yesterday_no_study_weight(
                    row["权值"]
                )  # +1
            # 大幅超额
            elif row["完成情况"] == 4:
                data_yesterday.at[index, "权值"] = self.Greatly_overachieved(
                    row["权值"]
                )  # -0.5
            # 小幅超额
            elif row["完成情况"] == 3:
                data_yesterday.at[index, "权值"] = self.Slightly_overachieved(
                    row["权值"]
                )  # -0.3
            # 如果昨天学过，初始化权重
            elif row["完成情况"] != 0:
                data_yesterday.at[index, "权值"] = self.plan_init_weight(
                    row["权值"]
                )  # init
            else:
                pass

        # 清理完成情况和学习时间
        data = data_yesterday
        # 删除特定列
        data = data.drop("完成情况", axis=1)
        data = data.drop("学习时间", axis=1)
        # 对权值进行降序排序
        data = data.sort_values("权值", ascending=False).reset_index(drop=True)

        # 从高到低依次添加完成情况，初始化为""，第七个开始为0
        data["完成情况"] = ""
        data.loc[data.index >= Max_study_course, "完成情况"] = 0
        # 添加学习时间列
        data["学习时间"] = ""
        data.loc[data.index >= Max_study_course, "学习时间"] = 0
        # 所有数据保留一位小数
        data = data.round(1)
        # 保存处理后的数据
        data.to_csv(f"data/{today}.csv", index=False)

    # 初始化权重，从plan.csv文件中读取
    def plan_init_weight(self, plan_date):
        data = pd.read_csv("data/plan.csv", usecols=["学科", "权值"])
        weight = plan_date
        for index, row in data.iterrows():
            if row["学科"] == plan_date:
                weight = row["权值"]

        return weight

    def yesterday_unfinished_weight(self, yesterday_date):
        return yesterday_date + 0.5

    def yesterday_longest_time_weight(self, yesterday_date):
        return yesterday_date + 0.2

    def yesterday_no_study_weight(self, yesterday_date):
        return yesterday_date + 0.7

    # Slightly overachieved
    def Slightly_overachieved(self, yesterday_date):
        return yesterday_date - 0.3

    # Greatly overachieved
    def Greatly_overachieved(self, yesterday_date):
        return yesterday_date - 0.5

    # 输入今天的学习时间和学习情况
    def input_today_study(self, current_date):
        # 如果 time/{today}.csv 文件不存在，就新建一个,有就退出
        today = current_date
        if not os.path.exists(f"time/{today}.csv"):
            data = pd.read_csv(f"data/{today}.csv")
            today_course_temp = pd.read_csv(f"temp/{today}.csv", usecols=["学科"])
            today_course_list = today_course_temp["学科"].tolist()  # 将 "学科" 列转换为列表
            # os.system("cls")
            for index, row in data.iterrows():
                if row["学科"] in today_course_list:
                    study_time = input(f"请输入{row['学科']}的学习时间（默认为1.5）：")
                    data.at[index, "学习时间"] = study_time if study_time else "1.5"
            print("=============================================")
            for index, row in data.iterrows():
                if row["学科"] in today_course_list:
                    completion_status = input(f"请输入{row['学科']}的完成情况（默认为2）：")
                    data.at[index, "完成情况"] = (
                        completion_status if completion_status else "2"
                    )
            data.to_csv(f"data/{today}.csv", index=False)
            # 完成输入，将temp文件夹中的文件移动到time文件夹中
            if not os.path.exists("time"):
                os.mkdir("time")
            
            shutil.move(f"temp/{today}.csv", f"time/{today}.csv")
           
            print("将今天的学习情况保存到time文件夹中")
            return
        else:
            print("今天的学习情况已经输入过了")
            return
