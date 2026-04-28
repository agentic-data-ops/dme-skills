#!/usr/bin/env python
"""删除输入内容中英文之间的空格"""
import re
import sys


def remove_spaces(text: str) -> str:
    """移除中英文、数字之间的多余空格"""
    # 中文与英文之间的空格
    text = re.sub(r'([\u4e00-\u9fa5])\s+([a-zA-Z])', r'\1\2', text)
    text = re.sub(r'([a-zA-Z])\s+([\u4e00-\u9fa5])', r'\1\2', text)

    # 中文与数字之间的空格
    text = re.sub(r'([\u4e00-\u9fa5])\s+(\d)', r'\1\2', text)
    text = re.sub(r'(\d)\s+([\u4e00-\u9fa5])', r'\1\2', text)

    return text


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 从命令行参数读取
        content = ' '.join(sys.argv[1:])
        print(remove_spaces(content))
    else:
        # 从 stdin 读取
        for line in sys.stdin:
            print(remove_spaces(line), end='')
