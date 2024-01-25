# 寒假计划分配

## 写一个简单的程序

### 框架

1. 计算每天要学习的 6 项内容，平均一项内容学习 1.5h = 9h
2. 将所有要学习的内容作为 csv 的表头，每一列记录
    1. 学习的日期 **2024-01-21**
    2. 学习进度 - 布置学习内容和章节
    3. 学习权重
    4. 输入完成情况

### 学习权重分配

1. 根据学习重要程度设置初始权重
2. 昨天未完成的学习内容，可以适当调高权重 （+0.7）
3. 从 `ManicTimeData_Data.csv` 中获取学习情况，持续时间最长的内容调高学习权重（+0.5）
4. 昨天没有学习的内容提高学习权重（+1）
5. 昨天学过的内容初始化 （权重重置为初始值）
6. 其他因素

最后，基于自身学习情况，适当调整学习初始化的学习权重

### 完成情况

1. 设置每天晚上 11 点，输入程序
2. 根据完成情况输入，1，2，3，4 ，分别为大幅超额、小幅超额、刚好完成、未完成
3. 大幅超额、小幅超额的学习内容适当降低权重 (-0.5)(0.3)，未完成的内容提高其学习权重 (+0.5)

### 任务分配

选取权重前 6 的为今天的学习任务

## 项目介绍

1. 复制data/template.csv 到 data/"f{today}".csv
2. 根据 data/"f{today-1}".csv 中的数据，计算出今天的权值
3. 如果yesterday为0，则使用默认权值
4. 如果yesterday不为0，则根据 Completion(昨天的完成情况) 计算出今天的权值
5. 将新权值写入 data/"f{today}".csv 中
6. 选取权值最大的前六个任务，将 Completion 置为 1
7. 并且在晚上 11 点，将弹出弹窗，提示输入 Completion

