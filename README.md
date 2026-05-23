# 🐉 中文编程示例项目

> 用中文写代码，让编程更亲切！

## 📖 项目简介

本项目收集了多种**中文编程**的示例代码，涵盖：
- Python 中文变量 / 函数 / 类
- 中文数据结构操作
- 中文异常处理
- 实际应用小项目

## 🚀 快速开始

### 环境要求

- Python 3.6+
- 支持 UTF-8 编码的编辑器 / 终端

### 安装与运行

```bash
# 克隆项目
git clone https://github.com/flygpro/chinese-programming.git
cd chinese-programming

# 运行示例
python3 examples/hello_world.py
```

## 📂 项目结构

```
chinese-programming/
├── examples/
│   ├── hello_world.py          # 基础问候
│   ├── 函数和类.py             # 中文函数与类定义
│   ├── 数据结构.py             # 列表、字典、集合
│   ├── 异常处理.py             # 中文 try-except
│   ├── 模块导入.py             # 中文别名导入
│   └── 实战示例/
│       ├── 中文计算器.py       # 中文命令行计算器
│       └── 猜数字.py           # 猜数字小游戏
├── README.md
└── LICENSE
```

## 🎯 示例预览

### 你好世界

```python
# -*- coding: utf-8 -*-
名字 = "世界"
print(f"你好，{名字}！")
```

### 中文函数

```python
def 计算面积(半径):
    圆周率 = 3.14159
    return 圆周率 * 半径 ** 2

print(f"面积：{计算面积(5):.2f}")
```

### 中文类

```python
class 动物:
    def __init__(self, 名称, 声音):
        self.名称 = 名称
        self.声音 = 声音

    def 叫(self):
        return f"{self.名称}：{self.声音}！"

猫 = 动物("猫", "喵")
print(猫.叫())  # 猫：喵！
```

## 📚 学习资源

- [Python 官方中文文档](https://docs.python.org/zh-cn/3/)
- [易语言官方](https://www.eyuyan.com/)
- [Python 中文编码规范 (PEP 8)](https://peps.python.org/pep-0008/)

## 🤝 贡献指南

欢迎提交 PR！请确保：
1. 文件首行包含 `# -*- coding: utf-8 -*-`
2. 使用有意义的中文变量名
3. 添加适当的中文注释

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 👨‍💻 作者

- **Flygpro** - [GitHub](https://github.com/flygpro)

---

> 💡 **小贴士**：中文编程适合学习和教学，生产环境建议使用英文命名以保持一致性。
