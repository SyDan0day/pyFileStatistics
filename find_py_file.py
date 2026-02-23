"""
****************************************************
** 出指定路径下py文件的函数、类、空白行、代码行数量 V1.0 **
****************************************************
"""
from pathlib import Path

def get_py_path(dir_path) -> list:
    """
    获取python文件的路径。
    参数:目标目录的路径(str)
    返回:目标目录下所有的python文件绝对路径(str)
    """
    p = Path(dir_path)
    return list(p.rglob('*.py'))

def file_count(file_path) -> list:
# 统计python文件的类、函数、空白行、代码行的数量。
    with open(file_path, mode = 'r', encoding='utf-8') as f:
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
    print(get_py_path(dir_path))