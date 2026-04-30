#!/usr/bin/env python3
"""
生成正确的test/todo.md测试用例文档
按照 test/spec.txt 的规则生成
"""
import subprocess
import re

def get_all_commands():
    """获取所有命令及其参数"""
    result = subprocess.run(['python', 'scripts/dme_cli.py', '--list-topics'],
                           capture_output=True, text=True)
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
        # 匹配子主题
        elif '├── 📂 ' in line:
            match = re.search(r'📂 (.+?)$', line)
            if match:
                current_subtopic = match.group(1).strip()
        # 匹配子主题下的动作
        elif '│       ├─── ' in line:
            match = re.search(r'─ (.+?) -', line)
            if match:
                action = match.group(1).strip()
                commands.append({
                    'topic': current_topic,
                    'topic_desc': current_topic_desc,
                    'subtopic': current_subtopic,
                    'action': action
                })
        # 匹配直接动作（│     ├──）
        elif '│     ├── ' in line:
            match = re.search(r'─ (.+?) -', line)
            if match:
                action = match.group(1).strip()
                commands.append({
                    'topic': current_topic,
                    'topic_desc': current_topic_desc,
                    'subtopic': None,
                    'action': action
                })
        # 匹配直接动作（├───）
        elif line.startswith('│   ├─── '):
            match = re.search(r'─ (.+?) -', line)
            if match:
                action = match.group(1).strip()
                commands.append({
                    'topic': current_topic,
                    'topic_desc': current_topic_desc,
                    'subtopic': None,
                    'action': action
                })

    return commands

def get_action_params(topic, subtopic, action):
    """获取动作的必选参数名"""
    if subtopic:
        cmd = f'python scripts/dme_cli.py {topic} {subtopic} {action}'
    else:
        cmd = f'python scripts/dme_cli.py {topic} {action}'

    try:
        result = subprocess.run(cmd + ' --help', shell=True,
                               capture_output=True, text=True, timeout=5)
        output = result.stdout

        # 提取必选参数
        params = []
        in_param_section = False
        lines = output.split('\n')

        for line in lines:
            if '参数说明' in line:
                in_param_section = True
                continue
            if in_param_section:
                if line.strip().startswith('=='):
                    break
                param_match = re.match(r'^\s+--(\S+)', line)
                if param_match:
                    param = param_match.group(1)
                    # 检查描述行是否有必选
                    next_line = lines[lines.index(line) + 1] if lines.index(line) + 1 < len(lines) else ''
                    if '必选' in next_line:
                        params.append(param)

        return params
    except:
        return []

def generate_todo_md():
    """生成test/todo.md"""
    commands = get_all_commands()

    md = """# DME CLI 测试执行清单

## 测试环境准备

- [ ] 配置环境变量
  - 配置DME API端点：`export DME_API_ENDPOINT=<your-dme-api-url>`
  - 配置用户名：`export DME_API_USERNAME=<username>`
  - 配置密码：`export DME_API_PASSWORD=<password>`

"""

    # 按主题组织
    topic_groups = {}
    for cmd in commands:
        topic = cmd['topic']
        if topic not in topic_groups:
            topic_groups[topic] = {
                'desc': cmd['topic_desc'],
                'commands': []
            }
        topic_groups[topic]['commands'].append(cmd)

    # 生成主题内容
    for topic, topic_info in sorted(topic_groups.items()):
        md += f"## {topic} {topic_info['desc']}\n\n"

        # 按子主题分组
        subtopic_groups = {}
        direct_actions = []
        for cmd in topic_info['commands']:
            subtopic = cmd['subtopic']
            if subtopic is None:
                direct_actions.append(cmd)
            else:
                if subtopic not in subtopic_groups:
                    subtopic_groups[subtopic] = []
                subtopic_groups[subtopic].append(cmd)

        # 生成直接动作
        for cmd in direct_actions:
            action = cmd['action']
            params = get_action_params(topic, None, action)

            # 构建命令
            cmd_str = f"python scripts/dme_cli.py {topic} {action}"
            if params:
                cmd_str += ' ' + ' '.join([f'--{p} <{p}>' for p in params])

            md += f"- [ ] **{topic} {action}**\n"
            md += f"  - 描述：{action}\n"
            md += f"  - 命令：{cmd_str}\n\n"

        # 生成子主题内容
        for subtopic, subtopic_commands in sorted(subtopic_groups.items()):
            md += f"### {subtopic}\n\n"

            for cmd in subtopic_commands:
                action = cmd['action']
                params = get_action_params(topic, subtopic, action)

                # 构建命令
                cmd_str = f"python scripts/dme_cli.py {topic} {subtopic} {action}"
                if params:
                    cmd_str += ' ' + ' '.join([f'--{p} <{p}>' for p in params])

                md += f"- [ ] **{topic} {subtopic} {action}**\n"
                md += f"  - 描述：{action}\n"
                md += f"  - 命令：{cmd_str}\n\n"

    return md

if __name__ == '__main__':
    md_content = generate_todo_md()
    with open('test/todo.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("✅ 已生成 test/todo.md")
    print(f"总主题数: {len(set(cmd['topic'] for cmd in get_all_commands()))}")
    print(f"总测试用例数: {len(get_all_commands())}")
