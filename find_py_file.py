"""
**********************************************
** 出指定路径下py文件的函数、类、空白行、代码行数量 **
**********************************************
"""
import os

def get_py_path(dir_path) -> list:
# 获取python文件的路径。
    file_path = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                file_path.append(os.path.join(root + '/' + file))
    return file_path

def file_count(file_path) -> list:
# 统计python文件的类、函数、空白行、代码行的数量。
    with open(file_path, mode = 'r') as f:
        lines = f.readlines()
        func_cnt = 0
        class_cnt = 0
        blank_cnt = 0
        code_cnt = 0
        for line in lines:
            if line.startswith('def'):
                func_cnt += 1
                code_cnt += 1 
            elif line.startswith('class'):
                class_cnt += 1
                code_cnt += 1
            elif line.startswith('\n'):
                blank_cnt += 1
            else:
                code_cnt += 1
            
    return {
        'filePath'    : file_path,
        'classes'     : class_cnt,
        'functions'   : func_cnt,
        'blank_lines' : blank_cnt,
        'code_lines'  : code_cnt,
    }


if __name__ == '__main__':
    dir_path = '/Users/bellchen/AI_Test'
    print(file_count(get_py_path(dir_path)[0]))