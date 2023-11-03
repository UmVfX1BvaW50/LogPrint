# LogPrint
## 起源
- 最近在研究一些工具的实现源码，但是函数太多，分析调用关系比较慢，就想插桩把调用顺序打印出来。所以就写了一个一键插桩脚本

## 介绍
- 一键在源码的所有python函数中插入print语句，打印自定义的信息【调用等等】
- 可以用来追踪调用路径，分析执行逻辑
## 使用
### 依赖
- python3
- pip安装依赖库
  - argparse【命令行参数处理】
  - ast【文件解析】
  - pandas【表格录入】
### 命令行参数
> python LogPrint.py [file]
- 注意文件目录开头不要加`/`
- 示例：
python LogPrint.py test

## 运行结果
- insertion_table.csv（插入代码的信息）
- error.txt（错误信息，插入未成功）
- 然后打开显示的对应路径，就可以看到被插入的代码
