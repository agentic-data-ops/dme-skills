#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
按照test/spec.txt规则生成测试用例
"""
import subprocess
import re
import os
import sys

def get_all_commands():
    """从CLI获取所有命令及其描述"""
    result = subprocess.run(['python', 'scripts/dme_cli.py', '--list-topics'],
                          capture_output=True, text=True, encoding='utf-8')
    output = result.stdout

    commands = []
    lines = output.split('\n')
    current_topic = None
    current_topic_desc = None
    current_subtopic = None

    for line in lines:
        # 匹配主题
        if line.startswith('📁 '):
            match = re.search(r'📁 (.+?) - (.+)$', line)
            if match:
                current_topic = match.group(1).strip()
                current_topic_desc = match.group(2).strip()
                current_subtopic = None
        # 匹配子主题（带虚线的格式）
        elif '├── 📂 ' in line:
            match = re.search(r'📂 (.+?)$', line)
            if match:
                current_subtopic = match.group(1).strip()
        # 匹配子主题下的动作
        elif '│       ├─── ' in line or '│   ├─── ' in line:
            parts = line.split('├─── ')
            if len(parts) > 1:
                action_part = parts[1].strip()
                last_dash = action_part.rfind(' - ')
                if last_dash > 0:
                    action = action_part[:last_dash].strip()
                    action_desc = action_part[last_dash + 3:].strip()
                    commands.append({
                        'topic': current_topic,
                        'topic_desc': current_topic_desc,
                        'subtopic': current_subtopic,
                        'action': action,
                        'action_desc': action_desc
                    })
        # 匹配直接动作
        elif '│     ├── ' in line:
            parts = line.split('├── ')
            if len(parts) > 1:
                action_part = parts[1].strip()
                last_dash = action_part.rfind(' - ')
                if last_dash > 0:
                    action = action_part[:last_dash].strip()
                    action_desc = action_part[last_dash + 3:].strip()
                    commands.append({
                        'topic': current_topic,
                        'topic_desc': current_topic_desc,
                        'subtopic': None,
                        'action': action,
                        'action_desc': action_desc
                    })

    return commands

def get_action_help(topic, subtopic, action):
    """获取动作的帮助信息"""
    if subtopic:
        cmd = f'python scripts/dme_cli.py {topic} {subtopic} {action}'
    else:
        cmd = f'python scripts/dme_cli.py {topic} {action}'

    result = subprocess.run(cmd + ' --help', shell=True,
                          capture_output=True, text=True, encoding='utf-8')
    output = result.stdout

    # 提取必选参数
    params = []
    in_param_section = False
    current_param = None
    current_param_desc = []
    lines = output.split('\n')

    for i, line in enumerate(lines):
        if '参数说明' in line:
            in_param_section = True
            continue
        if in_param_section:
            param_match = re.match(r'^\s+--(\S+)', line)
            if param_match:
                if current_param and ' '.join(current_param_desc).strip():
                    full_desc = ' '.join(current_param_desc).strip()
                    if '必选' in full_desc:
                        params.append((current_param, full_desc))
                current_param = param_match.group(1)
                current_param_desc = [line.strip()]
            elif current_param:
                stripped = line.strip()
                if stripped.startswith('=='):
                    full_desc = ' '.join(current_param_desc).strip()
                    if '必选' in full_desc:
                        params.append((current_param, full_desc))
                    current_param = None
                    break
                elif not stripped:
                    pass
                elif stripped.startswith('- '):
                    current_param_desc.append(stripped)
                elif stripped:
                    current_param_desc.append(stripped)

    if current_param and ' '.join(current_param_desc).strip():
        full_desc = ' '.join(current_param_desc).strip()
        if '必选' in full_desc:
            params.append((current_param, full_desc))

    return params

def generate_test_todo():
    """生成测试用例文件"""
    commands = get_all_commands()

    if not commands:
        print("错误：未获取到任何命令")
        return

    # 组织命令按主题和子主题分组
    topics = {}
    for cmd in commands:
        topic = cmd['topic']
        if topic not in topics:
            topics[topic] = {
                'desc': cmd['topic_desc'],
                'subtopics': {},
                'direct_actions': []
            }

        if cmd['subtopic']:
            if cmd['subtopic'] not in topics[topic]['subtopics']:
                topics[topic]['subtopics'][cmd['subtopic']] = []
            topics[topic]['subtopics'][cmd['subtopic']].append(cmd)
        else:
            topics[topic]['direct_actions'].append(cmd)

    # 生成Markdown
    md = "# DME CLI 测试用例\n\n"
    md += "## 测试环境准备\n\n"
    md += "- [ ] 配置环境变量：`export DME_API_URL=<your-dme-api-url>`\n"
    md += "- [ ] 配置认证信息：`export DME_API_USERNAME=<username>`\n"
    md += "- [ ] 配置认证信息：`export DME_API_PASSWORD=<password>`\n\n"
    md += "---\n\n"

    total_count = 0
    topic_count = 0

    # 按字母顺序排列主题
    for topic_name in sorted(topics.keys()):
        topic_data = topics[topic_name]
        md += f"## {topic_name} {topic_data['desc']}\n\n"
        topic_count += 1

        # 子主题
        for subtopic_name in sorted(topic_data['subtopics'].keys()):
            actions = topic_data['subtopics'][subtopic_name]
            md += f"### {subtopic_name}\n\n"

            for action in actions:
                total_count += 1
                # 按spec.txt格式输出：- [ ] <主题> <子主题> <动作>
                md += f"- [ ] **{action['topic']} {action['subtopic']} {action['action']}**\n"
                md += f"  - 描述：{action['action_desc']}\n"

                # 获取动作帮助
                params = get_action_help(action['topic'], action['subtopic'], action['action'])
                if params:
                    # 按spec.txt格式输出：- 命令：python scripts/dme_cli.py <主题> <子主题> <动作> --<必选参数1> <必选参数1描述> --<必选参数2> <必选参数2描述> ...
                    param_strs = [f'--{p[0]} <{p[0]}>' for p in params]
                    cmd_str = f"python scripts/dme_cli.py {action['topic']} {action['subtopic']} {action['action']} {' '.join(param_strs)}"
                else:
                    cmd_str = f"python scripts/dme_cli.py {action['topic']} {action['subtopic']} {action['action']}"
                md += f"  - 命令：{cmd_str}\n\n"

        # 直接动作
        if topic_data['direct_actions']:
            md += f"### 直接动作\n\n"
            for action in topic_data['direct_actions']:
                total_count += 1
                # 按spec.txt格式输出：- [ ] <主题> <动作>
                md += f"- [ ] **{action['topic']} {action['action']}**\n"
                md += f"  - 描述：{action['action_desc']}\n"

                # 获取动作帮助
                params = get_action_help(action['topic'], None, action['action'])
                if params:
                    param_strs = [f'--{p[0]} <{p[0]}>' for p in params]
                    cmd_str = f"python scripts/dme_cli.py {action['topic']} {action['action']} {' '.join(param_strs)}"
                else:
                    cmd_str = f"python scripts/dme_cli.py {action['topic']} {action['action']}"
                md += f"  - 命令：{cmd_str}\n\n"

    # 测试执行统计
    md += "---\n\n"
    md += "## 测试执行统计\n\n"
    md += f"- **主题数**：{topic_count}\n"
    md += f"- **测试用例数**：{total_count}\n"
    md += f"- **已完成**：0\n"
    md += f"- **通过率**：0%\n\n"
    md += "## 注意事项\n\n"
    md += "1. 执行前请先配置环境变量\n"
    md += "2. 命令中的 `<...>` 需替换为实际值\n"
    md += "3. 部分命令需要管理员权限\n"
    md += "4. 测试完成后请更新checkbox状态\n"

    # 写入文件
    output_path = 'test/todo.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✅ 测试用例已生成：{output_path}")
    print(f"   - 主题数：{topic_count}")
    print(f"   - 测试用例数：{total_count}")

if __name__ == '__main__':
    generate_test_todo()
