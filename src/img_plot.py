import matplotlib.pyplot as plt
import shutil
import pandas as pd
from datetime import timedelta
import os

# 每周一画一次柱状图，描述每科的学习情况
def img_plot_bar_chart(date_today):
    # 字体
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    # 从周一开始，往前推7天
    today = date_today
    start_day = today - timedelta(days=6)
    days = [start_day + timedelta(days=i) for i in range(7)]
    dataframes = []

    for day in days:
        filename = f"time/{day}.csv"
        if os.path.exists(filename):  # 检查文件是否存在
            df_day = pd.read_csv(filename)
            dataframes.append(df_day)
    # 合并这一周的数据
    df = pd.concat(dataframes)

    # 统计每个科目的学习次数
    counts = df["学科"].value_counts()
    # 指定图片的大小
    plt.figure(figsize=(30, 10))

    # 画柱状图，设置颜色和边框颜色
    plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black', width=0.5)

    # 设置标题和轴标签的字体大小
    plt.title(f"{start_day}到{today}每科的学习情况", fontsize=20)
    plt.xlabel("学科", fontsize=15)
    plt.ylabel("学习次数", fontsize=15)

    # 添加网格
    plt.grid(True)
    
    plt.xlabel("学科")
    plt.ylabel("学习次数")
    plt.title(f"{start_day}到{today}每科的学习情况", fontsize=16)
    # 保存文件到img文件夹下
    # 同时将文件目录和文件名写入到要保存的文件名中
    plt.savefig(f"{__file__[:-3]}.png")
    """移动文件到img文件夹下，同时保存文件根目录"""

    # 获取图片名
    file_name = f"{start_day}到{today}每科的学习情况"
    # 创建文件夹
    if not os.path.exists("img/"):
        os.makedirs("img/", exist_ok=True)

    # 原始文件名
    # 原始文件名
    original_file = f"{__file__[:-3]}.png"

    # 目标文件夹
    target_dir = "img/"

    """可用于移动文件并且不重复"""
    # 检查文件是否存在
    if os.path.exists(original_file):
        # 文件名（不包括扩展名）
        base_name = file_name
        # 扩展名
        extension = ".png"
        # 目标文件名
        target_file = f"{target_dir}/{base_name}{extension}"

        # 如果目标文件名已经存在，就增加一个数字
        i = 1
        while os.path.exists(target_file):
            target_file = f"{target_dir}/{base_name}{i}{extension}"
            i += 1

        # 移动文件
        shutil.move(original_file, target_file)
    # plt.show()


