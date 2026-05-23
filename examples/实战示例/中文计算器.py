# -*- coding: utf-8 -*-
"""中文命令行计算器 —— 支持四则运算"""


def 计算(表达式):
    """安全地计算数学表达式"""
    # 只允许数字和基本运算符
    允许的字符 = set("0123456789+-*/.() ")
    if not all(c in 允许的字符 for c in 表达式):
        return "❌ 表达式包含非法字符"

    try:
        结果 = eval(表达式)
        return 结果
    except ZeroDivisionError:
        return "❌ 错误：不能除以零"
    except Exception:
        return "❌ 错误：表达式格式不正确"


def 显示帮助():
    """显示帮助信息"""
    print("""
╔══════════════════════════════╗
║     🧮 中文计算器 v1.0       ║
╠══════════════════════════════╣
║  支持：+  -  *  /  ()        ║
║  输入表达式即可计算           ║
║  输入 '帮助' 显示此信息       ║
║  输入 '退出' 结束程序         ║
╚══════════════════════════════╝
""")


# ============ 主程序 ============

if __name__ == "__main__":
    显示帮助()

    计算次数 = 0

    while True:
        try:
            用户输入 = input("🧮 请输入表达式 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 再见！")
            break

        if not 用户输入:
            continue
        if 用户输入 in ("退出", "quit", "exit", "q"):
            print(f"👋 再见！本次共计算 {计算次数} 次。")
            break
        if 用户输入 in ("帮助", "help", "h"):
            显示帮助()
            continue

        结果 = 计算(用户输入)
        print(f"   = {结果}")
        计算次数 += 1
