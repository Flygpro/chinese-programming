# -*- coding: utf-8 -*-
"""中文异常处理示例"""


def 安全除法(被除数, 除数):
    """安全的除法，捕获所有可能的错误"""
    try:
        结果 = 被除数 / 除数
    except ZeroDivisionError:
        print("  ❌ 错误：除数不能为零！")
        return None
    except TypeError:
        print("  ❌ 错误：参数必须是数字！")
        return None
    else:
        print(f"  ✅ {被除数} ÷ {除数} = {结果:.4f}")
        return 结果
    finally:
        print("  ℹ️  计算完成。")


def 安全转换(文本):
    """安全地将文本转换为整数"""
    try:
        数字 = int(文本)
    except ValueError:
        print(f"  ❌ '{文本}' 不是有效的整数")
        return None
    else:
        print(f"  ✅ 转换成功：{数字}")
        return 数字


# 自定义异常
class 分数错误(Exception):
    """分数范围错误"""
    pass


def 设置分数(分数):
    """设置分数，必须在 0-100 之间"""
    if not 0 <= 分数 <= 100:
        raise 分数错误(f"分数 {分数} 超出范围 (0-100)")
    return 分数


# ============ 运行演示 ============

if __name__ == "__main__":
    print("【安全除法演示】")
    安全除法(10, 3)
    安全除法(10, 0)
    安全除法("abc", 2)

    print("\n【安全转换演示】")
    安全转换("42")
    安全转换("abc")
    安全转换("3.14")

    print("\n【自定义异常演示】")
    for 分数 in [85, 150, -10]:
        try:
            结果 = 设置分数(分数)
            print(f"  ✅ 分数 {结果} 设置成功")
        except 分数错误 as 错误:
            print(f"  ❌ {错误}")
