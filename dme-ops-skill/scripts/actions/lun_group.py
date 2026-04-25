"""
LUN 组管理 (LUN Group) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def list_lun_groups(client: DMEAPIClient, storage_id: str, name: str = None,
                    page_no: int = 1, page_size: int = 100) -> dict:
    """
    批量查询 LUN 组

    查询 LUN 组列表。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        name: LUN 组名称（支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 100

    Returns:
        响应数据，包含 LUN 组列表
    """
    url = "/rest/blockservice/v1/lun-groups/query"

    body_params = {
        'storage_id': storage_id,
        'page_no': page_no,
        'page_size': page_size
    }

    if name is not None:
        body_params['name'] = name

    response = client.post(url, json=body_params)
    return response


def show_lun_group(client: DMEAPIClient, group_id: str, storage_id: str = None) -> dict:
    """
    查询指定 LUN 组详情

    查询 LUN 组的详细信息。

    Args:
        client: DME API 客户端
        group_id: LUN 组 ID
        storage_id: 存储设备 ID（保留参数，实际不使用）

    Returns:
        LUN 组详细信息
    """
    url = f"/rest/blockservice/v1/lun-groups/{group_id}"

    response = client.get(url)
    return response


def create_lun_group(client: DMEAPIClient, storage_id: str, name: str,
                     description: str = None) -> dict:
    """
    创建 LUN 组

    创建新的 LUN 组。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        name: LUN 组名称（必选）
        description: LUN 组描述（可选）

    Returns:
        响应数据，包含新创建的 LUN 组 ID
    """
    url = "/rest/blockservice/v1/lun-groups"

    body_params = {
        'storage_id': storage_id,
        'name': name
    }

    if description is not None:
        body_params['description'] = description

    response = client.post(url, json=body_params)
    return response


def delete_lun_group(client: DMEAPIClient, storage_id: str, group_id: str) -> dict:
    """
    删除 LUN 组

    删除指定的 LUN 组。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        group_id: LUN 组 ID

    Returns:
        响应数据
    """
    url = "/rest/blockservice/v1/lun-groups/delete"

    body_params = {
        'storage_id': storage_id,
        'lun_group_ids': [group_id]
    }

    response = client.post(url, json=body_params)
    return response


def add_luns_to_group(client: DMEAPIClient, storage_id: str, group_id: str,
                      lun_ids: list) -> dict:
    """
    向 LUN 组添加 LUN

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        group_id: LUN 组 ID
        lun_ids: LUN ID 列表

    Returns:
        响应数据
    """
    url = f"/rest/blockservice/v1/lun-groups/{group_id}/add-luns"

    # 将 lun_ids 转换为 API 要求的格式：[{"lun_id": "xxx"}, ...]
    lun_id_objects = [{"lun_id": lun_id} for lun_id in lun_ids]

    body_params = {
        'existing_lun_ids': lun_id_objects
    }

    response = client.post(url, json=body_params)
    return response


def remove_luns_from_group(client: DMEAPIClient, group_id: str,
                           lun_ids: list, storage_id: str = None) -> dict:
    """
    从 LUN 组移除 LUN

    Args:
        client: DME API 客户端
        group_id: LUN 组 ID
        lun_ids: LUN ID 列表
        storage_id: 存储设备 ID（可选，实际不需要）

    Returns:
        响应数据
    """
    url = f"/rest/blockservice/v1/lun-groups/{group_id}/remove-luns"

    body_params = {
        'lun_ids': lun_ids
    }

    response = client.post(url, json=body_params)
    return response


def list_lun_group_luns(client: DMEAPIClient, group_id: str, storage_id: str = None) -> dict:
    """
    查询 LUN 组中的 LUN

    Args:
        client: DME API 客户端
        group_id: LUN 组 ID
        storage_id: 存储设备 ID（可选，实际不需要）

    Returns:
        响应数据，包含 LUN 列表
    """
    url = f"/rest/blockservice/v1/lun-groups/{group_id}/luns/query"

    response = client.post(url, json={})
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # 直接动作（两级结构）
    'list': {
        'func': list_lun_groups,
        'description': '批量查询 LUN 组',
        'params': ['storage_id', 'name', 'page_no', 'page_size'],
        'subtopic': None
    },
    'show': {
        'func': show_lun_group,
        'description': '查询指定 LUN 组详情',
        'params': ['group_id', 'storage_id'],
        'subtopic': None
    },
    'create': {
        'func': create_lun_group,
        'description': '创建 LUN 组',
        'params': ['storage_id', 'name', 'description'],
        'subtopic': None
    },
    'delete': {
        'func': delete_lun_group,
        'description': '删除 LUN 组',
        'params': ['storage_id', 'group_id'],
        'subtopic': None
    },
    # LUN 管理 - 2级动作
    'add_luns': {
        'func': add_luns_to_group,
        'description': '向 LUN 组添加 LUN',
        'params': ['storage_id', 'group_id', 'lun_ids'],
        'subtopic': None
    },
    'remove_luns': {
        'func': remove_luns_from_group,
        'description': '从 LUN 组移除 LUN',
        'params': ['group_id', 'lun_ids', 'storage_id'],
        'subtopic': None
    },
    'show_luns': {
        'func': list_lun_group_luns,
        'description': '查询 LUN 组中的 LUN',
        'params': ['group_id', 'storage_id'],
        'subtopic': None
    },
}
