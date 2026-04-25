"""
CMDB (Configuration Management Database) 相关操作
"""

import sys
import os
import re
import json
import glob

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


# ============================================================================
# Class 子主题相关动作
# ============================================================================

def class_list(client: DMEAPIClient, class_filter: str = None) -> list:
    """
    查询 CMDB 类列表

    从 reference/dme_resource_model/index.md 中获取类信息，支持模糊查询。

    Args:
        client: DME API 客户端（必需，由 CLI 框架自动传递）
        class_filter: 模糊匹配关键词，可选

    Returns:
        类信息列表，每项包含 class_name 和 description
    """
    # 如果 class_filter 是 DMEAPIClient 对象（参数解析错误），设置为 None
    if hasattr(class_filter, 'endpoint'):
        class_filter = None

    # 获取 resource_model 目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resource_model_dir = os.path.join(
        os.path.dirname(os.path.dirname(script_dir)),
        'reference', 'dme_resource_model'
    )

    # 读取 index.md 文件
    index_file = os.path.join(resource_model_dir, 'index.md')
    if not os.path.exists(index_file):
        return []

    with open(index_file, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # 解析 index.md 中的子章节链接，提取类名和文件名
    # 匹配格式：-   [类名](文件名.md)
    pattern = r'-\s+\[([^\]]+)\]\(([^)]+)\.md\)'
    matches = re.findall(pattern, index_content)

    # 构建类名到文件名的映射
    class_files = {}
    for class_name, filename in matches:
        class_files[class_name] = filename

    # 如果提供了 filter，在 index.md 中进行模糊匹配（仅匹配类名和文件名）
    if class_filter:
        filter_lower = class_filter.lower()
        filtered_classes = {}
        for name, file in class_files.items():
            # 匹配类名或文件名
            if filter_lower in name.lower() or filter_lower in file.lower():
                filtered_classes[name] = file
        class_files = filtered_classes

    # 遍历匹配的文件，获取类名和描述
    result = []
    for class_name, filename in class_files.items():
        # 添加 .md 后缀（index.md 中解析出来的文件名没有后缀）
        file_path = os.path.join(resource_model_dir, f'{filename}.md')
        if not os.path.exists(file_path):
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找文件标题（作为描述）
        title_pattern = r'^#\s+([^\n<]+)'
        title_match = re.search(title_pattern, content, re.MULTILINE)
        description = title_match.group(1).strip() if title_match else filename

        # 查找 SYS_开头的类名（第一个出现的）
        class_pattern = r'SYS_[A-Za-z0-9_]+'
        class_matches = re.findall(class_pattern, content)

        # 过滤掉重复和无效的类名
        valid_classes = []
        seen = set()
        for cls in class_matches:
            if cls not in seen and len(cls) > 4:  # 跳过 SYS_ 本身
                valid_classes.append(cls)
                seen.add(cls)

        # 取第一个有效的类名
        if valid_classes:
            result.append({
                'class_name': valid_classes[0],
                'description': description
            })

    return result


# ============================================================================
# Class Show 动作
# ============================================================================

def class_show(client: DMEAPIClient, class_name: str) -> dict:
    """
    查询类属性定义

    通过类名模糊匹配模型文件，返回类的属性定义。

    Args:
        client: DME API 客户端（必需，由 CLI 框架自动传递）
        class_name: 类名（必选），支持模糊匹配（支持 SYS_类名或中文名称）

    Returns:
        类属性定义（JSON 数组格式），包含属性名、数据类型、单位、枚举值、描述
    """
    # 如果 class_name 是 DMEAPIClient 对象（参数解析错误），返回错误
    if hasattr(class_name, 'endpoint'):
        return {'error': 'class_name 参数不能为空'}

    # 获取 resource_model 目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resource_model_dir = os.path.join(
        os.path.dirname(os.path.dirname(script_dir)),
        'reference', 'dme_resource_model'
    )

    # 读取 index.md 文件
    index_file = os.path.join(resource_model_dir, 'index.md')
    if not os.path.exists(index_file):
        return {'error': 'index.md 文件不存在', 'class_name': class_name}

    with open(index_file, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # 解析 index.md 中的子章节链接，提取文件名
    pattern = r'-\s+\[([^\]]+)\]\(([^)]+)\.md\)'
    matches = re.findall(pattern, index_content)

    # 构建类名（中文）到文件名的映射
    class_files = {}
    for class_name_cn, filename in matches:
        class_files[class_name_cn] = filename

    # 模糊匹配类名（中文名称或文件名）
    target_file = None
    matched_class_cn = None
    search_term = class_name.lower()

    for class_cn, filename in class_files.items():
        # 匹配中文类名或文件名
        if search_term in class_cn.lower() or search_term in filename.lower():
            target_file = filename
            matched_class_cn = class_cn
            break

    # 如果没找到，尝试从文件内容中查找 SYS_类名
    if not target_file:
        for class_cn, filename in class_files.items():
            file_path = os.path.join(resource_model_dir, f'{filename}.md')
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 查找 SYS_类名
                class_pattern = r'SYS_[A-Za-z0-9_]+'
                all_classes = re.findall(class_pattern, content)
                for cls in all_classes:
                    if search_term in cls.lower():
                        target_file = filename
                        matched_class_cn = class_cn
                        break
            if target_file:
                break

    if not target_file:
        return {'error': f'未找到匹配的类：{class_name}', 'class_name': class_name}

    # 打开模型文件，精确判断类名字段是否匹配
    file_path = os.path.join(resource_model_dir, f'{target_file}.md')
    if not os.path.exists(file_path):
        return {'error': f'模型文件不存在：{target_file}.md', 'class_name': class_name}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找精确匹配的类名（SYS_开头的）
    class_pattern = r'SYS_[A-Za-z0-9_]+'
    all_classes = re.findall(class_pattern, content)

    # 精确匹配类名
    exact_class_name = None
    for cls in all_classes:
        if cls.lower() == class_name.lower():
            exact_class_name = cls
            break

    # 如果没有精确匹配，尝试模糊匹配
    if not exact_class_name:
        for cls in all_classes:
            if class_name.lower() in cls.lower():
                exact_class_name = cls
                break

    if not exact_class_name:
        # 如果输入的是中文，返回所有可用的类名列表
        # 如果输入的是 SYS_类名，尝试部分匹配
        if class_name.startswith('SYS_'):
            for cls in all_classes:
                if class_name.lower() in cls.lower():
                    exact_class_name = cls
                    break

    if not exact_class_name:
        return {
            'error': f'在文件 {target_file}.md 中未找到类：{class_name}',
            'class_name': class_name,
            'available_classes': list(set(all_classes))
        }

    # 解析属性表格
    # 查找 "## 属性" 章节
    attr_section_pattern = r'##\s+属性.*?(?=##\s+|\Z)'
    attr_section_match = re.search(attr_section_pattern, content, re.DOTALL)

    if not attr_section_match:
        return {
            'class_name': exact_class_name,
            'description': matched_class_cn,
            'attributes': []
        }

    attr_section = attr_section_match.group(0)

    # 解析表格中的属性
    # 表格格式：| 属性 | 数据类型 | 单位 | 枚举值 | 描述 |
    # 提取表格内容
    table_pattern = r'<table>.*?</table>'
    table_match = re.search(table_pattern, attr_section, re.DOTALL)

    attributes = []
    if table_match:
        table_content = table_match.group(0)

        # 只提取 tbody 中的行（数据行），跳过 thead（表头）
        tbody_pattern = r'<tbody[^>]*>(.*?)</tbody>'
        tbody_match = re.search(tbody_pattern, table_content, re.DOTALL)

        if tbody_match:
            tbody_content = tbody_match.group(1)

            # 提取每一行（tr 标签）
            row_pattern = r'<tr[^>]*>(.*?)</tr>'
            rows = re.findall(row_pattern, tbody_content, re.DOTALL)

            for row in rows:
                # 提取单元格内容（td 标签）
                cell_pattern = r'<td[^>]*>(.*?)</td>'
                cells_html = re.findall(cell_pattern, row, re.DOTALL)

                # 从每个 td 中提取文本内容（去除所有 HTML 标签）
                cells = []
                for cell_html in cells_html:
                    # 去除所有 HTML 标签，只保留文本
                    text = re.sub(r'<[^>]+>', '', cell_html)
                    # 去除 &nbsp; 和空白
                    text = text.replace('&nbsp;', '').strip()
                    cells.append(text)

                if len(cells) >= 5:
                    attr_name = cells[0]
                    attr_type = cells[1]
                    attr_unit = cells[2] if cells[2] else None
                    attr_enum = cells[3] if cells[3] else None
                    attr_desc = cells[4]

                    # 处理枚举值（可能有多个，用换行分隔）
                    enum_values = []
                    if attr_enum:
                        enum_values = [e.strip() for e in re.split(r'[\n\r]+', attr_enum) if e.strip()]

                    attributes.append({
                        'name': attr_name,
                        'type': attr_type,
                        'unit': attr_unit,
                        'enum_values': enum_values if enum_values else None,
                        'description': attr_desc
                    })

    # 解析关联关系表格
    # 查找 "## 关联关系" 章节
    relation_section_pattern = r'##\s+关联关系.*?(?=##\s+|\Z)'
    relation_section_match = re.search(relation_section_pattern, content, re.DOTALL)

    relations = []
    if relation_section_match:
        relation_section = relation_section_match.group(0)

        # 提取表格内容
        table_pattern = r'<table>.*?</table>'
        table_match = re.search(table_pattern, relation_section, re.DOTALL)

        if table_match:
            table_content = table_match.group(0)

            # 只提取 tbody 中的行（数据行），跳过 thead（表头）
            tbody_pattern = r'<tbody[^>]*>(.*?)</tbody>'
            tbody_match = re.search(tbody_pattern, table_content, re.DOTALL)

            if tbody_match:
                tbody_content = tbody_match.group(1)

                # 提取每一行（tr 标签）
                row_pattern = r'<tr[^>]*>(.*?)</tr>'
                rows = re.findall(row_pattern, tbody_content, re.DOTALL)

                for row in rows:
                    # 提取单元格内容（td 标签）
                    cell_pattern = r'<td[^>]*>(.*?)</td>'
                    cells_html = re.findall(cell_pattern, row, re.DOTALL)

                    # 从每个 td 中提取文本内容（去除所有 HTML 标签）
                    cells = []
                    for cell_html in cells_html:
                        # 去除所有 HTML 标签，只保留文本
                        text = re.sub(r'<[^>]+>', '', cell_html)
                        # 去除 &nbsp; 和空白
                        text = text.replace('&nbsp;', '').strip()
                        cells.append(text)

                    if len(cells) >= 5:
                        relation_name = cells[0]
                        source_instance = cells[1]
                        target_instance = cells[2]
                        cardinality = cells[3]
                        relation_record = cells[4]

                        relations.append({
                            'relation_name': relation_name,
                            'source_instance': source_instance,
                            'target_instance': target_instance,
                            'cardinality': cardinality,
                            'relation_record': relation_record
                        })

    return {
        'class_name': exact_class_name,
        'description': matched_class_cn,
        'attributes': attributes,
        'relations': relations
    }


# ============================================================================
# Instance 子主题相关动作
# ============================================================================

def instance_list(client: DMEAPIClient, class_name: str, page_no: int = 1,
                  page_size: int = 20, condition: str = None,
                  order_by: str = None, content_selector: str = None,
                  group_name: str = None) -> dict:
    """
    查询指定资源类型的所有实例

    条件查询某类型资源的所有实例。

    Args:
        client: DME API 客户端
        class_name: 资源类型名称（可通过 `cmdb class show --class_filter <类名描述>` 获取类列表）
        page_no: 页码，默认 1，最小值 1
        page_size: 页大小，默认 20，范围 1~1000
        condition: 查询条件，受 Http Header 最大 81920 字符限制
            格式：{"constraint":[{"logOp":"and","simple":{"name":"<field1>","operator":"<operator>","caseSensitive":true,"value":<field1_value>}},{"logOp":"and","simple":{"name":"<field2>","operator":"<operator>","value":<field2_value>}},...]}
            其中：
            - logOp: 多个条件的关系，可选，默认为 or，可选值：and, or
            - name: CMDB 类的属性名称（可通过 `cmdb class show --class_name <类名>` 获取属性列表），必选
            - value: 字段的过滤值，必选
            - caseSensitive: 是否区分大小写，可选项
            - operator: 属性比较操作符，可选，默认值 equal
            操作符取值范围：equal, not equal, contain, not contain, in, not in, begin with, not begin with, end with, not end with, is null, not null, less than, not less than, greater than, not greater than
        order_by: 排序方式，格式：[{"field":"attr1","asc":true}]
        content_selector: 要返回的字段，默认返回所有字段，格式：["attr1","attr2"]
        group_name: 要返回的属性所属属性组名称，默认不返回属性组属性

    Returns:
        资源实例列表
    """
    url = f"/rest/resourcedb/v1/instances/{class_name}"

    query_params = {
        'pageNo': page_no,
        'pageSize': page_size
    }

    if condition is not None:
        query_params['condition'] = condition
    if order_by is not None:
        query_params['orderBy'] = order_by
    if content_selector is not None:
        query_params['contentSelector'] = content_selector
    if group_name is not None:
        query_params['groupName'] = group_name

    response = client.get(url, query_params=query_params)
    return response


def instance_show(client: DMEAPIClient, class_name: str, instance_id: str,
                  group_name: str = None, content_selector: str = None) -> dict:
    """
    查询单个资源实例

    Args:
        client: DME API 客户端
        class_name: 资源类型名称
        instance_id: 资源实例 ID，32~36 个字符
        group_name: 要返回的属性所属属性组名称，默认不返回属性组属性
        content_selector: 要返回的字段，默认返回所有字段，格式：["attr1","attr2"]

    Returns:
        资源实例详细信息
    """
    url = f"/rest/resourcedb/v1/instances/{class_name}/{instance_id}"

    query_params = {}
    if group_name is not None:
        query_params['groupName'] = group_name
    if content_selector is not None:
        query_params['contentSelector'] = content_selector

    response = client.get(url, query_params=query_params if query_params else None)
    return response


# ============================================================================
# Relation 子主题相关动作
# ============================================================================

def relation_list(client: DMEAPIClient, relation_name: str, page_no: int = 1,
                  page_size: int = 20, condition: str = None,
                  order_by: str = None) -> dict:
    """
    条件查询某类型关系的所有实例

    Args:
        client: DME API 客户端
        relation_name: 资源关系名称（可通过 `cmdb class show --class_name <类名>` 获取关联关系列表）
        page_no: 页码，默认 1，最小值 1
        page_size: 页大小，默认 20，范围 1~1000
        condition: 查询条件，受 Http Header 最大 81920 字符限制
            格式：{"constraint":[{"logOp":"and","simple":{"name":"<field1>","operator":"<operator>","caseSensitive":true,"value":<field1_value>}},{"logOp":"and","simple":{"name":"<field2>","operator":"<operator>","value":<field2_value>}},...]}
            其中：
            - logOp: 多个条件的关系，可选，默认为 or，可选值：and, or
            - name: 关系的属性名称，必选，包括 source_Instance_Id, target_Instance_Id, last_Modified
            - value: 属性的过滤值，必选
            - caseSensitive: 是否区分大小写，可选项
            - operator: 属性比较操作符，可选，默认值 equal
            操作符取值范围：equal, not equal, contain, not contain, in, not in, begin with, not begin with, end with, not end with, is null, not null, less than, not less than, greater than, not greater than
        order_by: 排序方式，格式：[{"field":"attr1","asc":true}]

    Returns:
        资源关系实例列表
    """
    url = f"/rest/resourcedb/v1/relations/{relation_name}/instances"

    query_params = {}

    if condition is not None:
        query_params['condition'] = condition
    if order_by is not None:
        query_params['orderBy'] = order_by

    response = client.get(url, query_params=query_params if query_params else None)
    return response


def relation_show(client: DMEAPIClient, relation_name: str, instance_id: str,
                  content_selector: str = None) -> dict:
    """
    查询单个资源关系的实例

    Args:
        client: DME API 客户端
        relation_name: 资源关系名称
        instance_id: 资源关系实例 ID
        content_selector: 要返回的字段，默认返回所有字段，格式：["attr1","attr2"]

    Returns:
        资源关系实例详细信息
    """
    url = f"/rest/resourcedb/v1/relations/{relation_name}/instances/{instance_id}"

    query_params = {}
    if content_selector is not None:
        query_params['contentSelector'] = content_selector

    response = client.get(url, query_params=query_params if query_params else None)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # Class 子主题动作
    'class_list': {
        'func': class_list,
        'description': '查询 CMDB 类列表',
        'params': ['class_filter'],
        'subtopic': 'class'
    },
    'class_show': {
        'func': class_show,
        'description': '查询类属性定义',
        'params': ['class_name'],
        'subtopic': 'class'
    },
    # Instance 子主题动作
    'instance_list': {
        'func': instance_list,
        'description': '查询指定资源类型的所有实例',
        'params': ['class_name', 'page_no', 'page_size', 'condition', 'order_by', 'content_selector', 'group_name'],
        'subtopic': 'instance'
    },
    'instance_show': {
        'func': instance_show,
        'description': '查询单个资源实例',
        'params': ['class_name', 'instance_id', 'group_name', 'content_selector'],
        'subtopic': 'instance'
    },
    # Relation 子主题动作
    'relation_list': {
        'func': relation_list,
        'description': '条件查询某类型关系的所有实例',
        'params': ['relation_name', 'page_no', 'page_size', 'condition', 'order_by', 'content_selector', 'count'],
        'subtopic': 'relation'
    },
    'relation_show': {
        'func': relation_show,
        'description': '查询单个资源关系的实例',
        'params': ['relation_name', 'instance_id', 'content_selector'],
        'subtopic': 'relation'
    },
}
