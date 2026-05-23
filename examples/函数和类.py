# -*- coding: utf-8 -*-
"""中文函数与类的定义示例"""


# ============ 中文函数 ============

def 计算面积(半径):
    """计算圆的面积"""
    圆周率 = 3.14159
    return 圆周率 * 半径 ** 2


def 打招呼(名字, 语气="你好"):
    """带参数的问候函数"""
    return f"{语气}，{名字}！"


def 最大值(数字列表):
    """找出列表中的最大值"""
    if not 数字列表:
        return None
    当前最大 = 数字列表[0]
    for 数字 in 数字列表:
        if 数字 > 当前最大:
            当前最大 = 数字
    return 当前最大


# ============ 中文类 ============

class 动物:
    """动物基类"""

    def __init__(self, 名称, 声音):
        self.名称 = 名称
        self.声音 = 声音

    def 叫(self):
        return f"{self.名称}：{self.声音}！"

    def __str__(self):
        return f"这是一只{self.名称}"


class 猫(动物):
    """猫，继承自动物"""

    def __init__(self, 名称="猫", 颜色="橘色"):
        super().__init__(名称, "喵")
        self.颜色 = 颜色

    def 抓老鼠(self):
        return f"{self.颜色}的{self.名称}正在抓老鼠！"


class 狗(动物):
    """狗，继承自动物"""

    def __init__(self, 名称="狗"):
        super().__init__(名称, "汪")

    def 看门(self):
        return f"{self.名称}在看门！"


# ============ 运行演示 ============

if __name__ == "__main__":
    print("【函数演示】")
    print(f"圆的面积：{计算面积(5):.2f}")
    print(打招呼("小明"))
    print(打招呼("小红", "早上好"))
    print(f"最大值：{最大值([3, 7, 2, 9, 1])}")

    print("\n【类演示】")
    猫咪 = 猫("小橘", "橘色")
    狗狗 = 狗("旺财")

    print(猫咪)
    print(猫咪.叫())
    print(猫咪.抓老鼠())
    print()
    print(狗狗)
    print(狗狗.叫())
    print(狗狗.看门())
