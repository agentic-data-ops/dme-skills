#!/usr/bin/env python3
"""
生成正确的test/todo.md测试用例文档
按照 test/spec.txt 的规则生成
"""
import subprocess
import re

def get_all_commands():
    """获取所有命令及其描述"""
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
        elif '│       ├─── ' in line or '│   ├─── ' in line:
            # 解析动作和描述
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
        # 匹配直接动作（│     ├──）
        elif '│     ├── ' in line:
            parts = line.split('├── ')
            if len(parts) > 1:
                action_part = parts[1].strip()
                last_dash = action_part.rfind(' - ')
                if last_dash > 0:
                    action = action_part[:last_dash].strip()
                    action_desc = action_part[last_dash + 3:].strip()
                    
                    # 对于virtualization主题，动作格式是 "<subtopic> <action>"
                    # 例如：cluster list, host adapter_list
                    subtopic = None
                    if current_topic == 'virtualization':
                        action_parts = action.split(' ')
                        if len(action_parts) >= 2:
                            subtopic = action_parts[0]
                            action = ' '.join(action_parts[1:])
                    
                    commands.append({
                        'topic': current_topic,
                        'topic_desc': current_topic_desc,
                        'subtopic': subtopic,
                        'action': action,
                        'action_desc': action_desc
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
                    else:
                        # 检查参数后面几行
                        for i in range(lines.index(line) + 1, min(lines.index(line) + 5, len(lines))):
                            if '必选' in lines[i]:
                                params.append(param)
                                break
                            elif lines[i].strip().startswith('--'):
                                break

        return params
    except:
        return []

def generate_md():
    """生成Markdown文档"""
    commands = get_all_commands()

    # 按主题和子主题分组
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
    md = """# DME CLI 测试执行清单

## 测试环境准备

- [ ] 配置环境变量
  - 配置DME API端点：`export DME_API_ENDPOINT=<your-dme-api-url>`
  - 配置用户名：`export DME_API_USERNAME=<username>`
  - 配置密码：`export DME_API_PASSWORD=<password>`

"""

    # 遍历所有主题
    for topic_name, topic_data in topics.items():
        md += f"## {topic_name} {topic_data['desc']}\n\n"

        # 子主题
        for subtopic_name, actions in topic_data['subtopics'].items():
            md += f"### {subtopic_name}\n\n"
            for action in actions:
                # 获取必选参数
                params = get_action_params(topic_name, subtopic_name, action['action'])

                # 构建命令
                cmd = f"python scripts/dme_cli.py {topic_name} {subtopic_name} {action['action']}"
                if params:
                    param_str = ' '.join([f'--{p} <{p}>' for p in params])
                    cmd += f' {param_str}'

                # 使用 --list-topics 中的动作描述
                action_desc = action.get('action_desc') or action['action']

                md += f"- [ ] **{topic_name} {subtopic_name} {action['action']}**\n"
                md += f"  - 描述：{action_desc}\n"
                md += f"  - 命令：{cmd}\n\n"

        # 直接动作
        if topic_data['direct_actions']:
            md += f"### 直接动作\n\n"
            for action in topic_data['direct_actions']:
                # 获取必选参数
                params = get_action_params(topic_name, None, action['action'])

                # 构建命令
                cmd = f"python scripts/dme_cli.py {topic_name} {action['action']}"
                if params:
                    param_str = ' '.join([f'--{p} <{p}>' for p in params])
                    cmd += f' {param_str}'

                # 使用 --list-topics 中的动作描述
                action_desc = action.get('action_desc') or action['action']

                md += f"- [ ] **{topic_name} {action['action']}**\n"
                md += f"  - 描述：{action_desc}\n"
                md += f"  - 命令：{cmd}\n\n"

        md += "---\n\n"

    # 添加统计
    total_topics = len(topics)
    total_actions = len(commands)
    total_with_params = sum(1 for cmd in commands if get_action_params(cmd['topic'], cmd['subtopic'], cmd['action']))

    md += f"""## 测试统计

- 总主题数：{total_topics}
- 总动作数：{total_actions}
- 带必选参数的动作数：{total_with_params}
"""

    return md

if __name__ == '__main__':
    md = generate_md()
    with open('test/todo.md', 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"✅ 已生成 test/todo.md")
