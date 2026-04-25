#!/usr/bin/env python3
"""
迁移脚本：将policy和topology迁移到aiops.py
"""

import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    base_dir = '/workspace/projects/dme-skills/dme-ops-skill/scripts/actions'

    # 读取源文件
    aiops_content = read_file(os.path.join(base_dir, 'aiops.py'))
    policy_content = read_file(os.path.join(base_dir, 'policy.py'))
    topology_content = read_file(os.path.join(base_dir, 'topology.py'))

    # 提取aiops.py中ACTIONS之前的内容
    aiops_actions_idx = aiops_content.find('ACTIONS = {')
    aiops_before = aiops_content[:aiops_actions_idx]

    # 提取aiops.py中ACTIONS字典
    brace_count = 0
    actions_start = aiops_actions_idx
    for i in range(actions_start, len(aiops_content)):
        if aiops_content[i] == '{':
            brace_count += 1
        elif aiops_content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                actions_end = i + 1
                break

    aiops_actions_dict = aiops_content[actions_start:actions_end]

    # 提取policy.py中的check_policy相关函数（从def list_check_policies到def list_abnormal_results之前）
    policy_lines = policy_content.split('\n')
    policy_check_start = None
    policy_check_end = None
    for i, line in enumerate(policy_lines):
        if 'def list_check_policies' in line:
            policy_check_start = i
        if 'def list_abnormal_results' in line and policy_check_start is not None:
            policy_check_end = i
            break

    if policy_check_start and policy_check_end:
        policy_check_funcs = '\n'.join(policy_lines[policy_check_start:policy_check_end])
    else:
        policy_check_funcs = ""

    # 提取policy.py中的check_result相关函数（从def list_abnormal_results到ACTIONS之前）
    policy_result_start = None
    policy_result_end = None
    for i, line in enumerate(policy_lines):
        if 'def list_abnormal_results' in line:
            policy_result_start = i
        if 'ACTIONS' in line and policy_result_start is not None:
            policy_result_end = i
            break

    if policy_result_start and policy_result_end:
        policy_result_funcs = '\n'.join(policy_lines[policy_result_start:policy_result_end])
    else:
        policy_result_funcs = ""

    # 提取topology.py中的所有函数（从第一个def到ACTIONS之前）
    topology_lines = topology_content.split('\n')
    topology_start = None
    topology_end = None
    for i, line in enumerate(topology_lines):
        if line.startswith('def ') and topology_start is None:
            topology_start = i
        if 'ACTIONS' in line and topology_start is not None:
            topology_end = i
            break

    if topology_start and topology_end:
        topology_funcs = '\n'.join(topology_lines[topology_start:topology_end])
    else:
        topology_funcs = ""

    # 构建新的aiops.py内容
    new_aiops = aiops_before

    # 添加check_policy子主题函数
    new_aiops += '# ============================================================================\n'
    new_aiops += '# 检查策略 (check_policy) 子主题函数\n'
    new_aiops += '# ============================================================================\n\n'
    new_aiops += policy_check_funcs
    new_aiops += '\n'

    # 添加check_result子主题函数
    new_aiops += '# ============================================================================\n'
    new_aiops += '# 检查结果 (check_result) 子主题函数\n'
    new_aiops += '# ============================================================================\n\n'
    new_aiops += policy_result_funcs
    new_aiops += '\n'

    # 添加topology子主题函数
    new_aiops += '# ============================================================================\n'
    new_aiops += '# 拓扑管理 (topology) 子主题函数\n'
    new_aiops += '# ============================================================================\n\n'
    new_aiops += topology_funcs
    new_aiops += '\n'

    # 添加ACTIONS字典
    new_aiops += '# ============================================================================\n'
    new_aiops += '# 动作列表，用于 CLI 帮助\n'
    new_aiops += '# ============================================================================\n\n'

    # 保留原有的ACTIONS，但移除最后的闭合括号
    new_aiops += aiops_actions_dict[:-1].rstrip() + '\n'

    # 添加check_result子主题的ACTIONS
    new_aiops += '    # check_result 子主题动作\n'
    new_aiops += "    'check_result_list': {\n"
    new_aiops += "        'func': list_abnormal_results,\n"
    new_aiops += "        'description': '查询检查策略异常检查结果列表',\n"
    new_aiops += "        'params': ['object_name', 'level', 'object_ids', 'object_native_id', 'object_type', 'policy_id', 'policy_name', 'policy_types', 'cause', 'alarm_type', 'first_occur_time', 'last_occur_time', 'page_no', 'page_size', 'sort_key', 'sort_dir'],\n"
    new_aiops += "        'subtopic': 'check_result'\n"
    new_aiops += "    },\n"
    new_aiops += "    'check_result_show': {\n"
    new_aiops += "        'func': show_abnormal_result,\n"
    new_aiops += "        'description': '查询检查策略异常检查结果详情',\n"
    new_aiops += "        'params': ['check_result_id'],\n"
    new_aiops += "        'subtopic': 'check_result'\n"
    new_aiops += "    },\n"

    # 添加check_policy子主题的ACTIONS
    new_aiops += '    # check_policy 子主题动作\n'
    new_aiops += "    'check_policy_list': {\n"
    new_aiops += "        'func': list_check_policies,\n"
    new_aiops += "        'description': '查询检查策略列表',\n"
    new_aiops += "        'params': ['policy_name', 'exact_query', 'status', 'policy_type', 'policy_source', 'alarm_type', 'object_type', 'page_no', 'page_size', 'sort_key', 'sort_dir', 'administrative_status', 'policy_category', 'object_category'],\n"
    new_aiops += "        'subtopic': 'check_policy'\n"
    new_aiops += "    },\n"
    new_aiops += "    'check_policy_execute': {\n"
    new_aiops += "        'func': execute_check_policy,\n"
    new_aiops += "        'description': '执行检查策略',\n"
    new_aiops += "        'params': ['policy_id'],\n"
    new_aiops += "        'subtopic': 'check_policy'\n"
    new_aiops += "    },\n"
    new_aiops += "    'check_policy_enable': {\n"
    new_aiops += "        'func': enable_check_policy,\n"
    new_aiops += "        'description': '启用检查策略',\n"
    new_aiops += "        'params': ['policy_id'],\n"
    new_aiops += "        'subtopic': 'check_policy'\n"
    new_aiops += "    },\n"
    new_aiops += "    'check_policy_disable': {\n"
    new_aiops += "        'func': disable_check_policy,\n"
    new_aiops += "        'description': '禁用检查策略',\n"
    new_aiops += "        'params': ['policy_id'],\n"
    new_aiops += "        'subtopic': 'check_policy'\n"
    new_aiops += "    },\n"
    new_aiops += "    'check_policy_delete': {\n"
    new_aiops += "        'func': delete_check_policy,\n"
    new_aiops += "        'description': '删除检查策略',\n"
    new_aiops += "        'params': ['policy_id'],\n"
    new_aiops += "        'subtopic': 'check_policy'\n"
    new_aiops += "    },\n"

    # 添加topology子主题的ACTIONS
    new_aiops += '    # topology 子主题动作\n'
    new_aiops += "    'topology_query_san_path': {\n"
    new_aiops += "        'func': query_san_path,\n"
    new_aiops += "        'description': '查询 SAN 路径拓扑结构（支持 IP_SAN 和 FC_SAN）',\n"
    new_aiops += "        'params': ['entry_objects', 'san_type'],\n"
    new_aiops += "        'subtopic': 'topology'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_query_luns': {\n"
    new_aiops += "        'func': query_luns,\n"
    new_aiops += "        'description': '查询拓扑图 LUN 列表',\n"
    new_aiops += "        'params': ['entry_objects', 'storage_pool_id', 'lun_name', 'san_type', 'page_size', 'page_no'],\n"
    new_aiops += "        'subtopic': 'topology'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_query_vms': {\n"
    new_aiops += "        'func': query_vms,\n"
    new_aiops += "        'description': '查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表',\n"
    new_aiops += "        'params': ['entry_objects', 'host_id', 'vm_name', 'page_size', 'page_no'],\n"
    new_aiops += "        'subtopic': 'topology'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_query_graph_path': {\n"
    new_aiops += "        'func': graph_query,\n"
    new_aiops += "        'description': '查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）',\n"
    new_aiops += "        'params': ['entry_res_type', 'entry_res_id', 'type', 'filter'],\n"
    new_aiops += "        'subtopic': 'topology'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_lun_list': {\n"
    new_aiops += "        'func': query_luns,\n"
    new_aiops += "        'description': '查询拓扑图 LUN 列表',\n"
    new_aiops += "        'params': ['entry_objects', 'storage_pool_id', 'lun_name', 'san_type', 'page_size', 'page_no'],\n"
    new_aiops += "        'subtopic': 'topology_lun'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_ipsan_query': {\n"
    new_aiops += "        'func': ipsan_query,\n"
    new_aiops += "        'description': '查询 IP_SAN 网络从主机到存储池间的拓扑结构',\n"
    new_aiops += "        'params': ['entry_objects'],\n"
    new_aiops += "        'subtopic': 'topology_ipsan'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_fcsan_query': {\n"
    new_aiops += "        'func': fcsan_query,\n"
    new_aiops += "        'description': '查询 FC_SAN 网络从主机到存储池间的拓扑结构',\n"
    new_aiops += "        'params': ['entry_objects'],\n"
    new_aiops += "        'subtopic': 'topology_fcsan'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_vm_list': {\n"
    new_aiops += "        'func': query_vms,\n"
    new_aiops += "        'description': '查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表',\n"
    new_aiops += "        'params': ['entry_objects', 'host_id', 'vm_name', 'page_size', 'page_no'],\n"
    new_aiops += "        'subtopic': 'topology_vm'\n"
    new_aiops += "    },\n"
    new_aiops += "    'topology_graph_query': {\n"
    new_aiops += "        'func': graph_query,\n"
    new_aiops += "        'description': '查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）',\n"
    new_aiops += "        'params': ['entry_res_type', 'entry_res_id', 'type', 'filter'],\n"
    new_aiops += "        'subtopic': 'topology_graph'\n"
    new_aiops += "    }\n"

    new_aiops += '}\n'

    # 写入新的aiops.py文件
    write_file(os.path.join(base_dir, 'aiops.py'), new_aiops)
    print(f"✓ 已生成新的aiops.py文件，共{new_aiops.count(chr(10))}行")

    # 删除源文件
    os.remove(os.path.join(base_dir, 'policy.py'))
    print("✓ 已删除policy.py文件")

    os.remove(os.path.join(base_dir, 'topology.py'))
    print("✓ 已删除topology.py文件")

    print("\n迁移完成！")

if __name__ == '__main__':
    main()
