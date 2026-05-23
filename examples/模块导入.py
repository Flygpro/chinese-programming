# -*- coding: utf-8 -*-
"""中文别名导入模块示例"""

import random as 随机
import datetime as 日期时间
import math as 数学


def 掷骰子(数量=1):
    """模拟掷骰子"""
    return [随机.randint(1, 6) for _ in range(数量)]


def 今天星期几():
    """返回今天是星期几"""
    星期名 = ["一", "二", "三", "四", "五", "六", "日"]
    今天 = 日期时间.date.today()
    星期序号 = 今天.weekday()
    return f"{今天} 星期{星期名[星期序号]}"


def 计算直角三角形斜边(直角边1, 直角边2):
    """用勾股定理计算斜边"""
    return 数学.sqrt(直角边1**2 + 直角边2**2)


# ============ 运行演示 ============

if __name__ == "__main__":
    print("【掷骰子】")
    结果 = 掷骰子(5)
    print(f"掷了5个骰子：{结果}，总和：{sum(结果)}")

    print(f"\n【今天】{今天星期几()}")

    print("\n【勾股定理】")
    a, b = 3, 4
    c = 计算直角三角形斜边(a, b)
    print(f"直角边 {a} 和 {b}，斜边 = {c:.2f}")
