import argparse
import os
import ast
import pandas as pd

def insert_print_statements(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        tree = ast.parse(file.read())

        class Visitor(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                # 插入代码
                try:
                    content = "print('function " + node.name + " in " + file_path + " be called!!!')"
                    print_statement = ast.parse(content)
                    node.body.insert(0, print_statement.body[0])
                    # 打印插入信息
                    print("File: ", file_path)
                    print("Line: ", node.lineno)
                    print("Insert content: ", content)
                    print()
                    # 将插入信息添加到DataFrame中
                    table_data.loc[len(table_data)] = [file_path, node.lineno, content]
                except :
                    # 打印错误信息
                    err_info = "Error inserting code in " + file_path
                    print(err_info)
                    err = open('error.txt', "a")
                    err.write(err_info+'\n')

        visitor = Visitor()
        visitor.visit(tree)

        file.seek(0)
        file.write(ast.unparse(tree))
        file.truncate()

def process_directory(directory_path):
    # 遍历寻找所有py文件
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                insert_print_statements(file_path)
    table_data.to_csv('insertion_table.csv', index=False)

if __name__ == '__main__':
    table_data = pd.DataFrame(columns=['File', 'Line', 'Insert Content'])
    parser = argparse.ArgumentParser(description='Python code instrumentation tool')
    parser.add_argument('directory', type=str, help='Directory to instrument')

    # 解析命令行参数
    args = parser.parse_args()

    # 处理目录下的所有Python文件
    process_directory(args.directory)
