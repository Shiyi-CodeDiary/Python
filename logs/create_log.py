# 创建文件：create_log.py
import datetime
import os

def create_daily_log():
    """生成当天的学习日志模板"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"log_{today}.md"

    # 日志直接写入本脚本所在目录（logs 文件夹），不再嵌套创建子目录
    log_dir = os.path.dirname(os.path.abspath(__file__))

    # 日志模板内容
    template = f"""# 学习日志 - {today}

## 📅 日期
{today}

## 📚 今天学了什么
- 

## ✍️ 今天写了什么代码/笔记
- 

## ❌ 遇到的错误与解决方案
### 错误 1：
- **错误信息**：
- **原因**：
- **解决方案**：


## 🔄 明天需要复习的内容
- [] 
- [] 


## 💡 今日总结与感悟


---
*学习时间： 小时*
"""

    # 写入文件
    filepath = os.path.join(log_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"✅ 日志模板已创建：{filepath}")


if __name__ == "__main__":
    print("🚀 开始创建日志...")
    create_daily_log()
    print("🏁 完成！")