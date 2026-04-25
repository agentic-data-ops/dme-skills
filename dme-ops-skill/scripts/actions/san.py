"""
LUN (Volume) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def list(client: DMEAPIClient, limit: int = 1000, offset: int = 0,
                 sort_dir: str = None, sort_key: str = None, name: str = None,
                 vstore_raw_id: str = None, vstore_name: str = None,
                 status: str = None, health_status: str = None,
                 tier_id: str = None, volume_wwn: str = None,
                 storage_id: str = None, pool_raw_id: str = None,
                 host_id: str = None) -> dict:
    """
    批量查询 LUN
    
    批量查询 LUN 信息，支持分页和多种过滤条件。
    
    Args:
        client: DME API 客户端
        limit: 分页查询的个数，默认 1000，范围：0~1000
        offset: 分页查询的起始位置，默认 0，最小值：0
        sort_dir: 排序方向，asc（升序）或 desc（降序）
        sort_key: 排序字段，可选值：name, size, alloc_capacity, capacity_usage, protection_capacity
        name: LUN 名称，支持模糊查询（1~256 个字符）
        vstore_raw_id: 存储设备上分配的租户 ID（1~64 个字符）
        vstore_name: 租户名称，支持模糊查询（1~256 个字符）
        status: 状态（已废弃，建议使用 health_status）
               可选值：creating, normal, mapping, unmapping, deleting, error, expanding, faulty, write_protected
        health_status: 健康状态，可选值：normal（正常）, faulty（故障）, write_protected（写保护）
        tier_id: 服务等级 ID（1~64 个字符）
        volume_wwn: LUN WWN（1~128 个字符）
        storage_id: 存储设备 ID（1~36 个字符，UUID 格式或 32 位十六进制）
        pool_raw_id: 存储池在存储设备上的 ID（1~64 个字符），需要同时指定 storage_id
        host_id: 主机 ID（1~64 个字符，UUID 格式或 32 位十六进制）
    
    Returns:
        LUN 列表，包含：
        - total: 总数
        - volumes: LUN 列表，包含 id, name, size, status, health_status 等
    """
    url = "/rest/blockservice/v1/volumes"
    
    query_params = {
        'limit': limit,
        'offset': offset
    }
    
    if sort_dir is not None:
        query_params['sort_dir'] = sort_dir
    if sort_key is not None:
        query_params['sort_key'] = sort_key
    if name is not None:
        query_params['name'] = name
    if vstore_raw_id is not None:
        query_params['vstore_raw_id'] = vstore_raw_id
    if vstore_name is not None:
        query_params['vstore_name'] = vstore_name
    if status is not None:
        query_params['status'] = status
    if health_status is not None:
        query_params['health_status'] = health_status
    if tier_id is not None:
        query_params['service_level_id'] = tier_id
    if volume_wwn is not None:
        query_params['volume_wwn'] = volume_wwn
    if storage_id is not None:
        query_params['storage_id'] = storage_id
    if pool_raw_id is not None:
        query_params['pool_raw_id'] = pool_raw_id
    if host_id is not None:
        query_params['host_id'] = host_id
    
    response = client.get(url, query_params=query_params)
    return response


def show(client: DMEAPIClient, volume_id: str) -> dict:
    """
    查询指定 LUN

    Args:
        client: DME API 客户端
        volume_id: LUN ID

    Returns:
        LUN 详细信息
    """
    url = f"/rest/blockservice/v1/volumes/{volume_id}"

    response = client.get(url)
    return response


def create(client: DMEAPIClient, storage_id: str, lun_specs: list = None,
                  lun_specs_pass_through: list = None, pool_id: str = None,
                  vstore_id: str = None, owner_controller: str = None,
                  initial_distribute_policy: str = None, prefetch_policy: str = None,
                  prefetch_value: int = None, tuning: dict = None,
                  mapping: dict = None, task_remarks: str = None) -> dict:
    """
    自定义创建 LUN

    自定义创建 LUN，支持常规模式和直通模式。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必填，1~64 个字符）
        lun_specs: 常规模式待创建 LUN 基本参数（必填，当存储设备模式不为直通模式时），单次最多创建 10 组
                        每项包含：name（LUN 名称，1~255 字符）, capacity（容量，单位 GB，1~65535）, count（个数，1~10）
                        可选：description、tier_id（服务等级 ID）、pool_raw_id（存储池 ID）、vstore_id（租户 ID）
        lun_specs_pass_through: 直通模式存储设备待创建 LUN 基本参数（必填，当存储设备模式为直通模式时），单次最多创建 24 组
        pool_id: 存储池 ID（当存储设备模式不为直通模式时必传）
        vstore_id: 租户 ID（可选，0~64 个字符）
        owner_controller: 归属控制器 ID（可选，1~64 个字符）
        initial_distribute_policy: 容量初始分配策略（可选，仅支持华为 V3/V5 设备）
                                  可选值：automatic（自动），highest_performance（高性能层），performance（性能层），capacity（容量层）
        prefetch_policy: 预取策略（可选）
                        可选值：no_prefetch（不预取），constant_prefetch（固定预取），variable_prefetch（可变预取），intelligent_prefetch（智能预取）
        prefetch_value: 预取策略值（可选，0~1024），固定预取单位为 KB，可变预取为倍数
        tuning: 调优属性（可选），包含 smart_tier、deduplication_enabled、compression_enabled、alloction_type、smart_qos、workload_type_raw_id
        mapping: 映射信息（可选），存在即表示为主机或主机组创建 LUN
        task_remarks: 异步任务备注信息（可选，最多 1024 个字符）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/customize"

    payload = {
        'storage_id': storage_id
    }

    if lun_specs is not None:
        payload['lun_specs'] = lun_specs
    if lun_specs_pass_through is not None:
        payload['lun_specs_pass_through'] = lun_specs_pass_through
    if pool_id is not None:
        payload['pool_id'] = pool_id
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if owner_controller is not None:
        payload['owner_controller'] = owner_controller
    if initial_distribute_policy is not None:
        payload['initial_distribute_policy'] = initial_distribute_policy
    if prefetch_policy is not None:
        payload['prefetch_policy'] = prefetch_policy
    if prefetch_value is not None:
        payload['prefetch_value'] = prefetch_value
    if tuning is not None:
        payload['tuning'] = tuning
    if mapping is not None:
        payload['mapping'] = mapping
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def delete(client: DMEAPIClient, volume_ids: list, task_remarks: str = None) -> dict:
    """
    批量删除 LUN

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表（最多 1000 个）
        task_remarks: 异步任务备注信息（可选，最多 1024 个字符）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/delete"

    payload = {
        'volume_ids': volume_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def modify(client: DMEAPIClient, volume_id: str, name: str = None,
                  description: str = None, owner_controller: str = None,
                  prefetch_policy: str = None, prefetch_value: int = None,
                  tuning: dict = None, task_remarks: str = None) -> dict:
    """
    修改指定 LUN

    Args:
        client: DME API 客户端
        volume_id: LUN ID
        name: 新名称（可选，1~255 个字符）
        description: 修改 LUN 描述信息（可选，0~255 个字符）
        owner_controller: 归属控制器（可选，仅非服务化 LUN 支持修改）
        prefetch_policy: 预取策略（可选，仅非服务化 LUN 支持修改）
                        可选值：0（不预取），1（固定预取），2（可变预取），3（智能预取）
        prefetch_value: 预取策略值（可选，仅非服务化 LUN 支持修改）
        tuning: LUN 调优属性（可选，仅非服务化 LUN 支持修改）
        task_remarks: 异步任务备注信息（可选，最多 1024 个字符）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = f"/rest/blockservice/v1/volumes/{volume_id}"

    volume = {}
    if name is not None:
        volume['name'] = name
    if description is not None:
        volume['description'] = description
    if owner_controller is not None:
        volume['owner_controller'] = owner_controller
    if prefetch_policy is not None:
        volume['prefetch_policy'] = prefetch_policy
    if prefetch_value is not None:
        volume['prefetch_value'] = prefetch_value
    if tuning is not None:
        volume['tuning'] = tuning

    payload = {
        'volume': volume
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def batch_modify_names(client: DMEAPIClient, volumes: list) -> dict:
    """
    批量修改 LUN 名称

    Args:
        client: DME API 客户端
        volumes: 待修改的 LUN 信息列表，每项包含 volume_id 和 name（最多 100 个）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes"

    payload = {
        'volumes': volumes
    }

    response = client.put(url, json=payload)
    return response


def expand(client: DMEAPIClient, volumes: list, task_remarks: str = None) -> dict:
    """
    批量扩容 LUN

    Args:
        client: DME API 客户端
        volumes: 需要扩容的 LUN 信息列表，每项包含 volume_id 和 added_capacity（最多 1000 个）
        task_remarks: 异步任务备注信息（可选，最多 1024 个字符）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/expand"

    payload = {
        'volumes': volumes
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response



def get_connection_info(client: DMEAPIClient, volume_ids: list) -> dict:
    """
    查询指定 LUN ID 的连接信息

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表（最多 1000 个）

    Returns:
        连接信息，包含 lun_id、lun_wwn、iscsi_targets、fc_targets 等
    """
    url = "/rest/blockservice/v1/volumes/connection-infos-query"

    payload = {
        'lun_ids': volume_ids
    }

    response = client.post(url, json=payload)
    return response


def list_host_luns(
    client: DMEAPIClient,
    storage_host_id: str = None,
    storage_host_group_id: str = None,
    name: str = None,
    page_size: int = 20,
    page_no: int = 1,
    sort_key: str = None,
    sort_dir: str = None
) -> dict:
    """
    指定存储主机或存储主机组查询映射 LUN 信息列表

    查询指定存储主机或存储主机组映射的 LUN 信息，包含 LUN 信息和主机 LUN ID 信息。

    Args:
        client: DME API 客户端
        storage_host_id: 存储主机 ID，与 storage_host_group_id 互斥且必须有一个下发
        storage_host_group_id: 存储主机组 ID，与 storage_host_id 互斥且必须有一个下发
        name: LUN 名称，支持模糊搜索
        page_size: 分页查询的个数，1~1000，默认 20
        page_no: 分页查询的起始位置，1~10000000，默认 1
        sort_key: 排序字段（host_lun_id、mapping_view_raw_id、lun_raw_id）
        sort_dir: 排序方向（asc 升序，desc 降序），默认 desc

    Returns:
        响应数据，包含 LUN 映射列表
    """
    url = "/rest/blockservice/v1/lun-mapping/query"

    body_params = {}

    if storage_host_id is not None:
        body_params['storage_host_id'] = storage_host_id

    if storage_host_group_id is not None:
        body_params['storage_host_group_id'] = storage_host_group_id

    if name is not None:
        body_params['name'] = name

    body_params['page_size'] = page_size
    body_params['page_no'] = page_no

    if sort_key is not None:
        body_params['sort_key'] = sort_key

    if sort_dir is not None:
        body_params['sort_dir'] = sort_dir

    response = client.post(url, json=body_params)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # 子主题动作（san lun xxx）
    'lun_list': {
        'func': list,
        'description': '批量查询 LUN',
        'params': ['limit', 'offset', 'sort_dir', 'sort_key', 'name', 'vstore_raw_id', 'vstore_name', 'status', 'health_status', 'tier_id', 'volume_wwn', 'storage_id', 'pool_raw_id', 'host_id'],
        'subtopic': 'lun'
    },
    'lun_show': {
        'func': show,
        'description': '查询指定 LUN',
        'params': ['volume_id'],
        'subtopic': 'lun'
    },
    'lun_create': {
        'func': create,
        'description': '自定义创建 LUN',
        'params': ['storage_id', 'lun_specs', 'lun_specs_pass_through', 'pool_id', 'vstore_id', 'owner_controller', 'initial_distribute_policy', 'prefetch_policy', 'prefetch_value', 'tuning', 'mapping', 'task_remarks'],
        'subtopic': 'lun'
    },
    'lun_delete': {
        'func': delete,
        'description': '批量删除 LUN',
        'params': ['volume_ids', 'task_remarks'],
        'subtopic': 'lun'
    },
    'lun_modify': {
        'func': modify,
        'description': '修改指定 LUN',
        'params': ['volume_id', 'name', 'description', 'owner_controller', 'prefetch_policy', 'prefetch_value', 'tuning', 'task_remarks'],
        'subtopic': 'lun'
    },
    'lun_modify_name': {
        'func': batch_modify_names,
        'description': '批量修改 LUN 名称',
        'params': ['volumes'],
        'subtopic': 'lun'
    },
    'lun_expand': {
        'func': expand,
        'description': '批量扩容 LUN',
        'params': ['volumes', 'task_remarks'],
        'subtopic': 'lun'
    },
    # 子主题动作（san lun xxx）
    'lun_connection': {
        'func': get_connection_info,
        'description': '查询指定 LUN ID 的连接信息',
        'params': ['volume_ids'],
        'subtopic': 'lun'
    },
    # 子主题动作（san lun xxx）
    'lun_mapping': {
        'func': list_host_luns,
        'description': '指定存储主机或存储主机组查询映射 LUN 信息列表',
        'params': ['storage_host_id', 'storage_host_group_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'lun'
    },
}
