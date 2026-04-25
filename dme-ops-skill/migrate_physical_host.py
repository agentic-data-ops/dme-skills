#!/usr/bin/env python3
"""
迁移脚本：将physical_host和physical_host_group迁移到san.py
"""

import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(content)

def extract_functions(lines):
    """提取函数部分（从第一个def到ACTIONS之前）"""
    start = None
    for i, line in enumerate(lines):
        if line.startswith('def ') or line.startswith('async def '):
            start = i
            break
        elif 'ACTIONS' in line:
            return []

    if start is None:
        return []

    for i, line in enumerate(lines[start:], start):
        if 'ACTIONS' in line:
            return lines[start:i]

    return []

def extract_actions_dict(lines):
    """提取ACTIONS字典内容"""
    start = None
    for i, line in enumerate(lines):
        if 'ACTIONS' in line:
            start = i
            break

    if start is None:
        return None

    brace_count = 0
    for i, line in enumerate(lines[start:], start):
        if 'ACTIONS' in line:
            brace_count = 1
        else:
            brace_count += line.count('{')
            brace_count -= line.count('}')

        if brace_count == 0 and i > start:
            # 找到最后一个条目的逗号，移除它
            lines_to_return = lines[start:i+1]
            for j in range(len(lines_to_return)-1, 0, -1):
                if lines_to_return[j].strip().rstrip(',').rstrip('}').strip():
                    # 找到最后一个条目
                    if '},\n' in lines_to_return[j-1:j+1]:
                        lines_to_return[j-1] = lines_to_return[j-1].replace('},', '}')
                    break
            return lines_to_return

    return None

def main():
    base_dir = '/workspace/projects/dme-skills/dme-ops-skill/scripts/actions'

    # 读取文件
    san_lines = read_file(os.path.join(base_dir, 'san.py'))
    physical_host_lines = read_file(os.path.join(base_dir, 'physical_host.py'))
    physical_host_group_lines = read_file(os.path.join(base_dir, 'physical_host_group.py'))

    # 找到san.py中ACTIONS字典的位置
    actions_start = None
    actions_end = None
    brace_count = 0
    in_actions = False

    for i, line in enumerate(san_lines):
        if 'ACTIONS = {' in line:
            actions_start = i
            in_actions = True
            brace_count = 1
        elif in_actions:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count == 0:
                actions_end = i + 1
                break

    print(f"san.py的ACTIONS字典: 第{actions_start+1}行到第{actions_end}行")

    # 提取physical_host和physical_host_group的函数和ACTIONS
    physical_host_funcs = extract_functions(physical_host_lines)
    physical_host_group_funcs = extract_functions(physical_host_group_lines)
    physical_host_actions = extract_actions_dict(physical_host_lines)
    physical_host_group_actions = extract_actions_dict(physical_host_group_lines)

    print(f"physical_host函数: {len(physical_host_funcs)}行")
    print(f"physical_host_group函数: {len(physical_host_group_funcs)}行")

    # 构建新的san.py内容
    # 1. 保留san.py中ACTIONS之前的内容（包括所有现有函数）
    new_san_lines = san_lines[:actions_start]

    # 2. 添加physical_host函数
    new_san_lines.extend([
        '\n',
        '# ============================================================================\n',
        '# 物理主机 (physical_host) 子主题函数\n',
        '# ============================================================================\n',
        '\n',
    ])
    new_san_lines.extend(physical_host_funcs)

    # 3. 添加physical_host_group函数
    new_san_lines.extend([
        '\n',
        '# ============================================================================\n',
        '# 物理主机组 (physical_host_group) 子主题函数\n',
        '# ============================================================================\n',
        '\n',
    ])
    new_san_lines.extend(physical_host_group_funcs)

    # 4. 添加san.py的ACTIONS字典开头
    new_san_lines.append('\n')
    new_san_lines.extend(san_lines[actions_start:actions_end])

    # 5. 在ACTIONS字典中添加physical_host和physical_host_group的动作
    # 找到最后一个闭合括号之前
    insert_pos = -2  # 在最后一行的空行和}之前

    physical_host_actions_str = ''.join(physical_host_actions)
    physical_host_group_actions_str = ''.join(physical_host_group_actions)

    # 移除开头的"ACTIONS = {"和结尾的"}"
    physical_host_actions_str = physical_host_actions_str.replace('ACTIONS = {', '').rstrip('}\n')
    physical_host_group_actions_str = physical_host_group_actions_str.replace('ACTIONS = {', '').rstrip('}\n')

    # 添加新动作
    new_san_lines.insert(insert_pos, ',\n')
    new_san_lines.insert(insert_pos, physical_host_group_actions_str)
    new_san_lines.insert(insert_pos, '\n    ')
    new_san_lines.insert(insert_pos, ',\n')
    new_san_lines.insert(insert_pos, physical_host_actions_str)
    new_san_lines.insert(insert_pos, '\n    ')

    # 写入新的san.py文件
    write_file(os.path.join(base_dir, 'san.py'), new_san_lines)
    print(f"✓ 已生成新的san.py文件，共{len(new_san_lines)}行")

    # 删除源文件
    os.remove(os.path.join(base_dir, 'physical_host.py'))
    print("✓ 已删除physical_host.py文件")

    os.remove(os.path.join(base_dir, 'physical_host_group.py'))
    print("✓ 已删除physical_host_group.py文件")

    print("\n迁移完成！")

if __name__ == '__main__':
    main()
