#!/usr/bin/env python3
"""
迁移脚本：将lun_group、mapping_view、storage中的host/host_group/port_group迁移到san.py
"""

import os
import re

# 读取源文件
def read_file_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# 写入文件
def write_file_content(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 主函数
def main():
    base_dir = '/workspace/projects/dme-skills/dme-ops-skill/scripts/actions'

    # 读取源文件
    san_content = read_file_content(os.path.join(base_dir, 'san.py'))
    lun_group_content = read_file_content(os.path.join(base_dir, 'lun_group.py'))
    mapping_view_content = read_file_content(os.path.join(base_dir, 'mapping_view.py'))
    storage_content = read_file_content(os.path.join(base_dir, 'storage.py'))

    # 提取san.py中的ACTIONS字典之前的内容（保留原有的lun子主题函数）
    san_match = re.search(r'(.*?)(ACTIONS = \{)', san_content, re.DOTALL)
    if not san_match:
        print("无法找到san.py中的ACTIONS字典")
        return

    san_functions = san_match.group(1)
    san_actions_start = san_match.group(2)
    san_actions_end = san_content[san_match.end():]

    # 提取lun_group.py中的函数（不包括ACTIONS）
    lun_group_match = re.search(r'""".*?"""(.+?)(ACTIONS = \{)', lun_group_content, re.DOTALL)
    if not lun_group_match:
        print("无法找到lun_group.py中的函数")
        return
    lun_group_functions = lun_group_match.group(1)

    # 提取lun_group.py中的ACTIONS字典
    lun_group_actions_match = re.search(r'(ACTIONS = \{.*?})', lun_group_content, re.DOTALL)
    if not lun_group_actions_match:
        print("无法找到lun_group.py中的ACTIONS字典")
        return
    lun_group_actions_dict = lun_group_actions_match.group(1)

    # 提取mapping_view.py中的函数（不包括ACTIONS）
    mapping_view_match = re.search(r'""".*?"""(.+?)(ACTIONS = \{)', mapping_view_content, re.DOTALL)
    if not mapping_view_match:
        print("无法找到mapping_view.py中的函数")
        return
    mapping_view_functions = mapping_view_match.group(1)

    # 提取mapping_view.py中的ACTIONS字典
    mapping_view_actions_match = re.search(r'(ACTIONS = \{.*?})', mapping_view_content, re.DOTALL)
    if not mapping_view_actions_match:
        print("无法找到mapping_view.py中的ACTIONS字典")
        return
    mapping_view_actions_dict = mapping_view_actions_match.group(1)

    # 从storage.py中提取host相关函数
    host_match = re.search(r'# ============ 存储主机 \(host\) 子主题函数 ============\n+(.+?)\n+# ============', storage_content, re.DOTALL)
    if not host_match:
        print("无法找到storage.py中的host函数")
        return
    host_functions = host_match.group(1)

    # 从storage.py中提取host_group相关函数
    host_group_match = re.search(r'# ============ 存储主机组 \(host_group\) 子主题函数 ============\n+(.+?)\n+# ============', storage_content, re.DOTALL)
    if not host_group_match:
        print("无法找到storage.py中的host_group函数")
        return
    host_group_functions = host_group_match.group(1)

    # 从storage.py中提取port_group相关函数
    port_group_match = re.search(r'(def port_group_list\(.+?)(# ============ 存储 VLAN)', storage_content, re.DOTALL)
    if not port_group_match:
        print("无法找到storage.py中的port_group函数")
        return
    port_group_functions = port_group_match.group(1)

    # 构建新的san.py文件
    new_san_content = f'''"""
SAN (Storage Area Network) 相关操作
包含LUN、LUN组、映射视图、存储主机、存储主机组、端口组等子主题
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient

# ============================================================================
# LUN 子主题函数
# ============================================================================

{san_functions}
# ============================================================================
# LUN 组 (lun_group) 子主题函数
# ============================================================================

{lun_group_functions}
# ============================================================================
# 映射视图 (mapping_view) 子主题函数
# ============================================================================

{mapping_view_functions}
# ============================================================================
# 存储主机 (storage_host) 子主题函数
# ============================================================================

{host_functions}
# ============================================================================
# 存储主机组 (storage_host_group) 子主题函数
# ============================================================================

{host_group_functions}
# ============================================================================
# 端口组 (port_group) 子主题函数
# ============================================================================

{port_group_functions}

# ============================================================================
# 动作列表，用于 CLI 帮助
# ============================================================================

ACTIONS = {{
    # LUN 子主题动作（san lun xxx）
    'lun_list': {{
        'func': list,
        'description': '批量查询 LUN',
        'params': ['limit', 'offset', 'sort_dir', 'sort_key', 'name', 'vstore_raw_id', 'vstore_name', 'status', 'health_status', 'tier_id', 'volume_wwn', 'storage_id', 'pool_raw_id', 'host_id'],
        'subtopic': 'lun'
    }},
    'lun_show': {{
        'func': show,
        'description': '查询指定 LUN',
        'params': ['volume_id'],
        'subtopic': 'lun'
    }},
    'lun_create': {{
        'func': create,
        'description': '自定义创建 LUN',
        'params': ['storage_id', 'lun_specs', 'lun_specs_pass_through', 'pool_id', 'vstore_id', 'owner_controller', 'initial_distribute_policy', 'prefetch_policy', 'prefetch_value', 'tuning', 'mapping', 'task_remarks'],
        'subtopic': 'lun'
    }},
    'lun_delete': {{
        'func': delete,
        'description': '批量删除 LUN',
        'params': ['volume_ids', 'task_remarks'],
        'subtopic': 'lun'
    }},
    'lun_modify': {{
        'func': modify,
        'description': '修改指定 LUN',
        'params': ['volume_id', 'name', 'description', 'owner_controller', 'prefetch_policy', 'prefetch_value', 'tuning', 'task_remarks'],
        'subtopic': 'lun'
    }},
    'lun_modify_name': {{
        'func': batch_modify_names,
        'description': '批量修改 LUN 名称',
        'params': ['volumes'],
        'subtopic': 'lun'
    }},
    'lun_expand': {{
        'func': expand,
        'description': '批量扩容 LUN',
        'params': ['volumes', 'task_remarks'],
        'subtopic': 'lun'
    }},
    'lun_connection': {{
        'func': get_connection_info,
        'description': '查询指定 LUN ID 的连接信息',
        'params': ['volume_ids'],
        'subtopic': 'lun'
    }},
    'lun_mapping': {{
        'func': list_host_luns,
        'description': '指定存储主机或存储主机组查询映射 LUN 信息列表',
        'params': ['storage_host_id', 'storage_host_group_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'lun'
    }},
    # LUN 组子主题动作（san lun_group xxx）
    'lun_group_list': {{
        'func': list_lun_groups,
        'description': '批量查询 LUN 组',
        'params': ['storage_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'lun_group'
    }},
    'lun_group_show': {{
        'func': show_lun_group,
        'description': '查询指定 LUN 组详情',
        'params': ['group_id', 'storage_id'],
        'subtopic': 'lun_group'
    }},
    'lun_group_create': {{
        'func': create_lun_group,
        'description': '创建 LUN 组',
        'params': ['storage_id', 'name', 'description'],
        'subtopic': 'lun_group'
    }},
    'lun_group_delete': {{
        'func': delete_lun_group,
        'description': '删除 LUN 组',
        'params': ['storage_id', 'group_id'],
        'subtopic': 'lun_group'
    }},
    'lun_group_add_luns': {{
        'func': add_luns_to_group,
        'description': '向 LUN 组添加 LUN',
        'params': ['storage_id', 'group_id', 'lun_ids'],
        'subtopic': 'lun_group'
    }},
    'lun_group_remove_luns': {{
        'func': remove_luns_from_group,
        'description': '从 LUN 组移除 LUN',
        'params': ['group_id', 'lun_ids', 'storage_id'],
        'subtopic': 'lun_group'
    }},
    'lun_group_show_luns': {{
        'func': list_lun_group_luns,
        'description': '查询 LUN 组中的 LUN',
        'params': ['group_id', 'storage_id'],
        'subtopic': 'lun_group'
    }},
    # 映射视图子主题动作（san mapping_view xxx）
    'mapping_view_create': {{
        'func': create_mapping_view,
        'description': '创建映射视图',
        'params': ['storage_id', 'port_group_id', 'name', 'start_host_lun_id',
                   'host_id', 'host_name', 'host_group_id', 'host_group_name',
                   'lun_group_id', 'lun_ids', 'lungroup_name', 'vbs_id'],
        'subtopic': 'mapping_view'
    }},
    'mapping_view_delete': {{
        'func': batch_delete_mapping_views,
        'description': '批量删除映射视图',
        'params': ['mapping_view_ids'],
        'subtopic': 'mapping_view'
    }},
    'mapping_view_list': {{
        'func': query_mapping_views,
        'description': '批量查询映射视图列表',
        'params': ['page_size', 'page_no', 'name', 'raw_id', 'storage_id',
                   'lun_id', 'lun_name', 'lun_group_id', 'lun_group_raw_id',
                   'lun_group_name', 'storage_host_id', 'storage_host_name',
                   'storage_host_group_id', 'storage_host_group_name',
                   'storage_host_group_raw_id', 'port_group_id', 'port_group_raw_id',
                   'port_group_name', 'sort_key', 'sort_dir'],
        'subtopic': 'mapping_view'
    }},
    'mapping_view_query': {{
        'func': query_mapping_views_by_host,
        'description': '查询物理主机（组）关联的映射关系',
        'params': ['type', 'request_id', 'storage_id'],
        'subtopic': 'mapping_view'
    }},
    # 存储主机子主题动作（san storage_host xxx）
    'storage_host_create': {{
        'func': host_create,
        'description': '创建存储主机',
        'params': ['storage_id', 'name', 'os_type', 'ip', 'description', 'initiators', 'multipath', 'task_remarks', 'vstore_id'],
        'subtopic': 'storage_host'
    }},
    'storage_host_batch_query': {{
        'func': host_batch_query,
        'description': '根据存储主机 ID 列表批量查询存储主机',
        'params': ['ids'],
        'subtopic': 'storage_host'
    }},
    'storage_host_list': {{
        'func': host_list,
        'description': '批量查询存储主机',
        'params': ['page_size', 'page_no', 'sort_key', 'sort_dir', 'name', 'raw_id', 'host_group_id',
                   'avaliable_add_to_host_group_id', 'host_group_name', 'ip', 'health_status', 'os_type',
                   'storage_id', 'avaiable_mapping_for_lun_group_id', 'avaiable_mapping_for_lun_id',
                   'support_provisioning', 'manufacturer', 'vstore_raw_id', 'vstore_name'],
        'subtopic': 'storage_host'
    }},
    'storage_host_modify': {{
        'func': host_modify,
        'description': '修改存储主机',
        'params': ['storage_host_id', 'storage_host_name', 'storage_host_description', 'storage_host_ip',
                   'storage_host_os_type', 'add_initiators', 'remove_initiators', 'multipath', 'access_mode',
                   'hyper_metro_path_optimized', 'task_remarks'],
        'subtopic': 'storage_host'
    }},
    'storage_host_delete': {{
        'func': host_delete,
        'description': '批量删除存储主机',
        'params': ['host_ids'],
        'subtopic': 'storage_host'
    }},
    'storage_host_show_paths': {{
        'func': host_show_paths,
        'description': '批量查询存储主机的路径信息',
        'params': ['page_no', 'page_size', 'storage_id', 'storage_host_ids', 'storage_host_raw_ids',
                   'health_status', 'running_status', 'initiator_type'],
        'subtopic': 'storage_host'
    }},
    'storage_host_show_luns': {{
        'func': host_show_luns,
        'description': '查询存储主机映射的 LUN 信息列表',
        'params': ['storage_host_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'storage_host'
    }},
    # 存储主机组子主题动作（san storage_host_group xxx）
    'storage_host_group_create': {{
        'func': host_group_create,
        'description': '创建存储主机组',
        'params': ['storage_id', 'name', 'description', 'exist_host_ids', 'create_storage_host_params', 'task_remarks', 'vstore_id'],
        'subtopic': 'storage_host_group'
    }},
    'storage_host_group_list': {{
        'func': host_group_list,
        'description': '批量查询存储主机组',
        'params': ['storage_id', 'name', 'raw_id', 'vstore_id', 'vstore_name', 'page_no', 'page_size',
                   'sort_key', 'sort_dir', 'avaiable_mapping_for_lun_group_id', 'avaiable_mapping_for_lun_id',
                   'support_provisioning'],
        'subtopic': 'storage_host_group'
    }},
    'storage_host_group_add_hosts': {{
        'func': host_group_add_hosts,
        'description': '添加存储主机到存储主机组',
        'params': ['storage_host_group_id', 'storage_host_id_ids', 'create_storage_host_params', 'task_remarks'],
        'subtopic': 'storage_host_group'
    }},
    'storage_host_group_remove_hosts': {{
        'func': host_group_remove_hosts,
        'description': '从存储主机组中移除主机',
        'params': ['storage_host_group_id', 'storage_host_ids', 'task_remarks'],
        'subtopic': 'storage_host_group'
    }},
    'storage_host_group_delete': {{
        'func': host_group_delete,
        'description': '批量删除存储主机组',
        'params': ['host_group_ids', 'task_remarks'],
        'subtopic': 'storage_host_group'
    }},
    'storage_host_group_show_luns': {{
        'func': host_group_show_luns,
        'description': '查询存储主机组映射的 LUN 信息列表',
        'params': ['storage_host_group_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'storage_host_group'
    }},
    # 端口组子主题动作（san port_group xxx）
    'port_group_list': {{
        'func': port_group_list,
        'description': '批量查询端口组',
        'params': ['storage_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'port_group'
    }},
    'port_group_create': {{
        'func': port_group_create,
        'description': '创建端口组',
        'params': ['storage_id', 'name', 'description'],
        'subtopic': 'port_group'
    }},
    'port_group_show_ports': {{
        'func': port_group_show_ports,
        'description': '批量查询指定端口组的端口',
        'params': ['storage_id', 'port_group_id'],
        'subtopic': 'port_group'
    }},
    'port_group_show_relations': {{
        'func': port_group_show_relations,
        'description': '批量查询端口组与端口关联关系',
        'params': ['storage_id', 'port_group_id'],
        'subtopic': 'port_group'
    }},
}}
'''

    # 写入新的san.py文件
    write_file_content(os.path.join(base_dir, 'san.py'), new_san_content)
    print("✓ 已生成新的san.py文件")

    # 删除lun_group.py和mapping_view.py文件
    os.remove(os.path.join(base_dir, 'lun_group.py'))
    print("✓ 已删除lun_group.py文件")

    os.remove(os.path.join(base_dir, 'mapping_view.py'))
    print("✓ 已删除mapping_view.py文件")

    # 从storage.py中删除host、host_group、port_group相关函数
    storage_new_content = re.sub(
        r'# ============ 存储主机 \(host\) 子主题函数 ============.*?# ============',
        '# ============',
        storage_content,
        flags=re.DOTALL
    )

    storage_new_content = re.sub(
        r'# ============ 存储主机组 \(host_group\) 子主题函数 ============.*?# ============',
        '# ============',
        storage_new_content,
        flags=re.DOTALL
    )

    # 删除port_group函数（保留到下一个主题开始之前）
    storage_new_content = re.sub(
        r'(def port_group_list\(.+?)(# ============ 存储 VLAN)',
        r'\2',
        storage_new_content,
        flags=re.DOTALL
    )

    # 删除host_show_luns和host_group_show_luns函数（这两个函数在host和host_group之后）
    storage_new_content = re.sub(
        r'\n\ndef host_show_luns\(.+?\n\ndef host_group_show_luns\(.+?\n\n(# ============)',
        r'\n\1',
        storage_new_content,
        flags=re.DOTALL
    )

    write_file_content(os.path.join(base_dir, 'storage.py'), storage_new_content)
    print("✓ 已从storage.py中删除host、host_group、port_group相关函数")

    print("\n迁移完成！")

if __name__ == '__main__':
    main()
