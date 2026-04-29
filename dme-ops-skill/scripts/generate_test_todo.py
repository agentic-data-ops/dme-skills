#!/usr/bin/env python3
"""
生成正确的test/todo.md测试用例文档
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
    current_subtopic = None

    for line in lines:
        # 匹配主题
        if line.startswith('📁 '):
            match = re.search(r'📁 (.+?) -', line)
            if match:
                current_topic = match.group(1).strip()
                current_subtopic = None
        # 匹配子主题
        elif '├── 📂 ' in line:
            match = re.search(r'📂 (.+?)$', line)
            if match:
                current_subtopic = match.group(1).strip()
        # 匹配动作
        elif '├─── ' in line:
            match = re.search(r'─ (.+?) -', line)
            if match:
                action = match.group(1).strip()
                commands.append({
                    'topic': current_topic,
                    'subtopic': current_subtopic,
                    'action': action
                })
        # 匹配直接动作
        elif '│     ├── ' in line:
            match = re.search(r'─ (.+?) -', line)
            if match:
                action = match.group(1).strip()
                commands.append({
                    'topic': current_topic,
                    'subtopic': None,
                    'action': action
                })

    return commands

def get_action_params(topic, subtopic, action):
    """获取动作的必选参数"""
    if subtopic:
        cmd = f'python scripts/dme_cli.py {topic} {subtopic} {action}'
    else:
        # 处理virtualization的直接动作（如"cluster list"）
        if ' ' in action:
            cmd = f'python scripts/dme_cli.py {topic} {action}'
        else:
            cmd = f'python scripts/dme_cli.py {topic} {action}'

    result = subprocess.run(cmd + ' --help', shell=True,
                           capture_output=True, text=True)
    output = result.stdout

    # 提取必选参数
    params = []
    in_param_section = False
    for line in output.split('\n'):
        if '参数说明' in line:
            in_param_section = True
            continue
        if in_param_section:
            match = re.match(r'^\s+--(\S+)', line)
            if match:
                param = match.group(1)
                # 检查是否是必选参数
                if '(必选)' in line or '(必填)' in line:
                    params.append(f'--{param}<{param}>')
            elif line.strip().startswith('=='):
                break

    return params

def generate_todo_md():
    """生成test/todo.md"""
    commands = get_all_commands()

    md = """# DME CLI 测试执行清单

## 环境准备

- [ ] 配置DME API环境变量
  ```bash
  export DME_API_ENDPOINT="https://<dme-server>:<port>"
  export DME_API_USERNAME="<username>"
  export DME_API_PASSWORD="<password>"
  ```

- [ ] 验证连接
  ```bash
  python scripts/dme_cli.py --list-topics
  ```

- [ ] 验证登录
  ```bash
  python scripts/dme_cli.py system login --help
  ```

"""

    # 按主题组织
    topic_groups = {}
    for cmd in commands:
        topic = cmd['topic']
        if topic not in topic_groups:
            topic_groups[topic] = []
        topic_groups[topic].append(cmd)

    # 生成主题内容
    for i, (topic, topic_commands) in enumerate(sorted(topic_groups.items()), 1):
        md += f"### {i}. {topic} 主题\n\n"

        # 按子主题分组
        subtopic_groups = {}
        for cmd in topic_commands:
            subtopic = cmd['subtopic']
            if subtopic is None:
                subtopic = '直接动作'
            if subtopic not in subtopic_groups:
                subtopic_groups[subtopic] = []
            subtopic_groups[subtopic].append(cmd)

        # 生成子主题内容
        for j, (subtopic, subtopic_commands) in enumerate(sorted(subtopic_groups.items()), 1):
            if subtopic == '直接动作':
                md += f"#### {j}.1 直接动作\n\n"
            else:
                md += f"#### {j}.{j+1} {subtopic} 子主题\n\n"

            for cmd in subtopic_commands:
                action = cmd['action']
                params = get_action_params(topic, cmd['subtopic'], action)

                if cmd['subtopic']:
                    cmd_str = f"python scripts/dme_cli.py {topic} {cmd['subtopic']} {action}"
                else:
                    if ' ' in action:
                        # virtualization的直接动作
                        cmd_str = f"python scripts/dme_cli.py {topic} {action}"
                    else:
                        cmd_str = f"python scripts/dme_cli.py {topic} {action}"

                if params:
                    cmd_str += ' ' + ' '.join(params)

                md += f"- [ ] **{topic} {action}**\n"
                md += f"  - 描述: {action}\n"
                md += f"  - 命令: `{cmd_str}`\n\n"

    # 添加统计信息
    md += "## 测试执行统计\n\n"
    md += f"- 总主题数: {len(topic_groups)}\n"
    md += f"- 总测试用例数: {len(commands)}\n"
    md += f"- 已执行用例: {0}\n"
    md += f"- 未执行用例: {len(commands)}\n"
    md += f"- 执行进度: {0}%\n"

    return md

if __name__ == '__main__':
    md_content = generate_todo_md()
    with open('test/todo.md.new', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("✅ 已生成 test/todo.md.new")
    print(f"总主题数: {len(set(cmd['topic'] for cmd in get_all_commands()))}")
    print(f"总测试用例数: {len(get_all_commands())}")
