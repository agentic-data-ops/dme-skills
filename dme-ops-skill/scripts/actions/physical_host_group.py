"""
物理主机组管理 (Host Group) 相关操作

物理主机组用于将多个物理主机分组管理，便于批量操作和权限控制。
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def list(client: DMEAPIClient, limit: int = None, start: int = None,
         name: str = None, project_id: str = None) -> dict:
    """
    批量查询物理主机组

    批量查询物理主机组列表。

    Args:
        client: DME API 客户端
        limit: 分页查询的个数（可选，1~1000）
        start: 分页查询的起始位置（可选）
        name: 物理主机组名称（可选，支持模糊匹配）
        project_id: 业务群组 ID（可选）

    Returns:
        响应数据，包含物理主机组列表和总数
    """
    url = "/rest/hostmgmt/v1/hostgroups/summary"

    payload = {}

    if limit is not None:
        payload['limit'] = limit
    if start is not None:
        payload['start'] = start
    if name is not None:
        payload['name'] = name
    if project_id is not None:
        payload['project_id'] = project_id

    response = client.post(url, json=payload)
    return response


def show(client: DMEAPIClient, hostgroup_id: str) -> dict:
    """
    查询指定物理主机组

    查询指定物理主机组的详细信息。

    Args:
        client: DME API 客户端
        hostgroup_id: 物理主机组 ID（必选）

    Returns:
        物理主机组详细信息
    """
    url = f"/rest/hostmgmt/v1/hostgroups/{hostgroup_id}/summary"

    response = client.get(url)
    return response


def create(client: DMEAPIClient, name: str, host_ids: list,
           azs: list = None, project_id: str = None,
           description: str = None) -> dict:
    """
    创建物理主机组

    指定物理主机创建物理主机组。

    Args:
        client: DME API 客户端
        name: 物理主机组名称（必选，1~255 字符）
        host_ids: 物理主机 ID 列表（必选，最多 100 个）
        azs: 可用分区 ID 列表（可选，最多 40 个）
        project_id: 业务群组 ID（可选）
        description: 描述信息（可选，0~63 字符）

    Returns:
        创建的物理主机组信息
    """
    url = "/rest/hostmgmt/v1/hostgroups"

    payload = {
        'name': name,
        'host_ids': host_ids
    }

    if azs is not None:
        payload['azs'] = azs
    if project_id is not None:
        payload['project_id'] = project_id
    if description is not None:
        payload['description'] = description

    response = client.post(url, json=payload)
    return response


def modify(client: DMEAPIClient, hostgroup_id: str,
           name: str = None, description: str = None,
           azs: list = None, project_id: str = None) -> dict:
    """
    修改物理主机组基本信息

    修改物理主机组基本信息。

    Args:
        client: DME API 客户端
        hostgroup_id: 物理主机组 ID（必选）
        name: 主机组名称（可选，1~255 字符）
        description: 描述信息（可选，0~63 字符）
        azs: 可用分区 ID 列表（可选，最多 40 个）
        project_id: 业务群组 ID（可选）

    Returns:
        修改结果
    """
    url = f"/rest/hostmgmt/v1/hostgroups/{hostgroup_id}/general"

    payload = {}

    if name is not None:
        payload['name'] = name
    if description is not None:
        payload['description'] = description
    if azs is not None:
        payload['azs'] = azs
    if project_id is not None:
        payload['project_id'] = project_id

    response = client.put(url, json=payload)
    return response


def delete(client: DMEAPIClient, hostgroup_id: str,
           sync_to_storage: bool = False) -> dict:
    """
    删除指定物理主机组

    删除指定物理主机组，自动解除与物理主机的关系。

    Args:
        client: DME API 客户端
        hostgroup_id: 物理主机组 ID（必选）
        sync_to_storage: 是否同步从存储删除（可选，默认 false）

    Returns:
        删除结果
    """
    url = f"/rest/hostmgmt/v1/hostgroups/{hostgroup_id}?sync_to_storage={str(sync_to_storage).lower()}"

    response = client.delete(url)
    return response


def host_add(client: DMEAPIClient, hostgroup_id: str,
             host_ids: list, sync_to_storage: bool = False) -> dict:
    """
    向物理主机组中增加物理主机

    向物理主机组中增加物理主机。

    Args:
        client: DME API 客户端
        hostgroup_id: 物理主机组 ID（必选）
        host_ids: 物理主机 ID 列表（必选，最多 100 个）
        sync_to_storage: 是否同步添加到存储（可选，默认 false）

    Returns:
        添加结果
    """
    url = f"/rest/hostmgmt/v1/hostgroups/{hostgroup_id}/hosts/add?sync_to_storage={str(sync_to_storage).lower()}"

    payload = {
        'host_ids': host_ids
    }

    response = client.put(url, json=payload)
    return response


def host_remove(client: DMEAPIClient, hostgroup_id: str,
                host_ids: list, sync_to_storage: bool = False) -> dict:
    """
    物理主机组移除物理主机

    从物理主机组中移除物理主机。

    Args:
        client: DME API 客户端
        hostgroup_id: 物理主机组 ID（必选）
        host_ids: 物理主机 ID 列表（必选，最多 1000 个）
        sync_to_storage: 是否同步从存储移除（可选，默认 false）

    Returns:
        移除结果
    """
    url = f"/rest/hostmgmt/v1/hostgroups/{hostgroup_id}/hosts/remove?sync_to_storage={str(sync_to_storage).lower()}"

    payload = {
        'host_ids': host_ids
    }

    response = client.put(url, json=payload)
    return response


def map_lun(client: DMEAPIClient, volume_ids: list, hostgroup_id: str,
            mapping_policy: str = None, task_remarks: str = None) -> dict:
    """
    LUN 映射给物理主机组

    将 LUN 映射给指定的物理主机组。

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表
        hostgroup_id: 主机组 ID
        mapping_policy: 映射策略（exclusive-独占，shared-共享），默认 exclusive
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/volumes/hostgroup-mapping"

    payload = {
        'volume_ids': volume_ids,
        'hostgroup_id': hostgroup_id
    }

    if mapping_policy is not None:
        payload['mapping_policy'] = mapping_policy

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def unmap_lun(client: DMEAPIClient, volume_ids: list, hostgroup_id: str,
              host_group_type: str = "host_group", task_remarks: str = None) -> dict:
    """
    解除主机组映射

    解除 LUN 与主机组的映射关系。

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表
        hostgroup_id: 主机组 ID
        host_group_type: 映射类型（storage_host_group-存储主机组，host_group-主机组），默认 host_group
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/volumes/hostgroup-unmapping"

    payload = {
        'volume_ids': volume_ids,
        'hostgroup_id': hostgroup_id,
        'host_group_type': host_group_type
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    'list': {
        'func': list,
        'description': '批量查询物理主机组',
        'params': ['limit', 'start', 'name', 'project_id'],
        'subtopic': None
    },
    'show': {
        'func': show,
        'description': '查询指定物理主机组',
        'params': ['hostgroup_id'],
        'subtopic': None
    },
    'create': {
        'func': create,
        'description': '创建物理主机组',
        'params': ['name', 'host_ids', 'azs', 'project_id', 'description'],
        'subtopic': None
    },
    'modify': {
        'func': modify,
        'description': '修改物理主机组基本信息',
        'params': ['hostgroup_id', 'name', 'description', 'azs', 'project_id'],
        'subtopic': None
    },
    'delete': {
        'func': delete,
        'description': '删除指定物理主机组',
        'params': ['hostgroup_id', 'sync_to_storage'],
        'subtopic': None
    },
    'add_hosts': {
        'func': host_add,
        'description': '向物理主机组中增加物理主机',
        'params': ['hostgroup_id', 'host_ids', 'sync_to_storage'],
        'subtopic': None
    },
    'remove_hosts': {
        'func': host_remove,
        'description': '物理主机组移除物理主机',
        'params': ['hostgroup_id', 'host_ids', 'sync_to_storage'],
        'subtopic': None
    },
    'map_luns': {
        'func': map_lun,
        'description': 'LUN映射给物理主机组',
        'params': ['volume_ids', 'hostgroup_id', 'mapping_policy', 'task_remarks'],
        'subtopic': None
    },
    'unmap_luns': {
        'func': unmap_lun,
        'description': '解除主机组映射',
        'params': ['volume_ids', 'hostgroup_id', 'host_group_type', 'task_remarks'],
        'subtopic': None
    },
    }
