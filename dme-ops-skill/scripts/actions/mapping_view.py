"""
映射视图管理 (Mapping View) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def create_mapping_view(
    client: DMEAPIClient,
    storage_id: str,
    port_group_id: str = None,
    name: str = None,
    start_host_lun_id: int = None,
    host_id: str = None,
    host_name: str = None,
    host_group_id: str = None,
    host_group_name: str = None,
    lun_group_id: str = None,
    lun_ids: list = None,
    lungroup_name: str = None,
    vbs_id: str = None
) -> dict:
    """
    创建映射视图

    创建映射视图，将 LUN 映射给主机、主机组或 VBS。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        port_group_id: 端口组 ID（可选）
        name: 映射视图名称（可选，设备类型为 OceanStor V3/V5时有效）
        start_host_lun_id: 主机 LUN ID（可选）
        host_id: 主机 ID（可选，与 host_name 二选一）
        host_name: 待创建主机名称（可选，与 host_id 二选一）
        host_group_id: 主机组 ID（可选，与 host_group_name 二选一）
        host_group_name: 待创建主机组名称（可选，与 host_group_id 二选一）
        lun_group_id: LUN 组 ID（可选）
        lun_ids: LUN ID 列表（可选，与 lun_group_id 互斥）
        lungroup_name: LUN 组名称（可选，lun 映射时需创建指定名称 lun 组时下发）
        vbs_id: VBS ID（可选，仅 OceanStor Pacific 和 OceanStor FusionStorage 系列存储支持）

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/mapping-views"

    body_params = {
        'storage_id': storage_id
    }

    if name is not None:
        body_params['name'] = name

    if port_group_id is not None:
        body_params['port_group_id'] = port_group_id

    if start_host_lun_id is not None:
        body_params['start_host_lun_id'] = start_host_lun_id

    # 主机映射（与 vbs、host_group 互斥）
    if host_id is not None or host_name is not None:
        host_info = {}
        if host_id is not None:
            host_info['id'] = host_id
        if host_name is not None:
            host_info['todo_host_name'] = host_name
        body_params['host'] = host_info

    # 主机组映射（与 host、vbs 互斥）
    if host_group_id is not None or host_group_name is not None:
        host_group_info = {}
        if host_group_id is not None:
            host_group_info['id'] = host_group_id
        if host_group_name is not None:
            host_group_info['todo_host_group_name'] = host_group_name
        body_params['host_group'] = host_group_info

    # VBS 映射（与 host、host_group 互斥，仅 Pacific/FusionStorage 支持）
    if vbs_id is not None:
        body_params['vbs'] = {'id': vbs_id}

    # LUN 组映射（与 luns 互斥）
    if lun_group_id is not None:
        body_params['lun_group'] = {'id': lun_group_id}

    # LUN 列表映射（与 lun_group 互斥）
    if lun_ids is not None:
        luns_info = {'ids': lun_ids}
        if lungroup_name is not None:
            luns_info['lungroup_name'] = lungroup_name
        body_params['luns'] = luns_info

    response = client.post(url, json=body_params)
    return response


def batch_delete_mapping_views(client: DMEAPIClient, mapping_view_ids: list) -> dict:
    """
    批量删除映射视图

    批量删除指定的映射视图。

    Args:
        client: DME API 客户端
        mapping_view_ids: 映射视图 ID 列表

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/mapping-views/batch-delete"

    body_params = {}

    if mapping_view_ids is not None:
        body_params['mapping_view_ids'] = mapping_view_ids

    response = client.post(url, json=body_params)
    return response


def query_mapping_views(
    client: DMEAPIClient,
    page_size: int = 100,
    page_no: int = 1,
    name: str = None,
    raw_id: str = None,
    storage_id: str = None,
    lun_id: str = None,
    lun_name: str = None,
    lun_group_id: str = None,
    lun_group_raw_id: str = None,
    lun_group_name: str = None,
    storage_host_id: str = None,
    storage_host_name: str = None,
    storage_host_group_id: str = None,
    storage_host_group_name: str = None,
    storage_host_group_raw_id: str = None,
    port_group_id: str = None,
    port_group_raw_id: str = None,
    port_group_name: str = None,
    sort_key: str = None,
    sort_dir: str = None
) -> dict:
    """
    批量查询映射视图列表

    批量查询存储设备上的映射视图信息，支持多种过滤条件。

    Args:
        client: DME API 客户端
        page_size: 分页查询的个数，0~1000，默认 100
        page_no: 分页查询的起始位置，1~10000000，默认 1
        name: 映射视图名称，支持模糊搜索
        raw_id: 映射视图在存储设备上的 ID
        storage_id: 存储设备的唯一标识
        lun_id: LUN 的唯一标识，和 lun_name 参数不支持同时下发
        lun_name: LUN 名称，支持模糊搜索，和 lun_id 参数不支持同时下发
        lun_group_id: LUN 组的唯一标识，和 lun_group_raw_id、lun_group_name 参数不支持同时下发
        lun_group_raw_id: 设备侧分配的 LUN 组 ID，和 lun_group_id、lun_group_name 参数不支持同时下发
        lun_group_name: LUN 组名称，支持模糊查询，和 lun_group_id、lun_group_raw_id 参数不支持同时下发
        storage_host_id: 存储主机的唯一标识，和 storage_host_name 参数不支持同时下发
        storage_host_name: 存储主机名称，支持模糊搜索，仅 OceanStor Dorado v6 和 OceanProtect X 系列设备支持
        storage_host_group_id: 存储主机组的唯一标识，和 storage_host_group_name、storage_host_group_raw_id 参数不支持同时下发
        storage_host_group_name: 存储主机组名称，支持模糊搜索，和 storage_host_group_id、storage_host_group_raw_id 参数不支持同时下发
        storage_host_group_raw_id: 设备侧分配的存储主机组 ID，和 storage_host_group_id、storage_host_group_name 参数不支持同时下发
        port_group_id: 端口组的唯一标识，和 port_group_raw_id、port_group_name 参数不支持同时下发
        port_group_raw_id: 设备侧分配的端口组 ID，和 port_group_id、port_group_name 参数不支持同时下发
        port_group_name: 端口组名称，支持模糊搜索，和 port_group_id、port_group_raw_id 参数不支持同时下发
        sort_key: 排序字段（raw_id、storage_host_group_raw_id、lun_group_raw_id、port_group_raw_id）
        sort_dir: 排序方向（asc 升序，desc 降序）

    Returns:
        响应数据，包含映射视图列表
    """
    url = "/rest/blockservice/v1/mapping-views/query"

    body_params = {
        'page_size': page_size,
        'page_no': page_no
    }

    if name is not None:
        body_params['name'] = name

    if raw_id is not None:
        body_params['raw_id'] = raw_id

    if storage_id is not None:
        body_params['storage_id'] = storage_id

    if lun_id is not None:
        body_params['lun_id'] = lun_id

    if lun_name is not None:
        body_params['lun_name'] = lun_name

    if lun_group_id is not None:
        body_params['lun_group_id'] = lun_group_id

    if lun_group_raw_id is not None:
        body_params['lun_group_raw_id'] = lun_group_raw_id

    if lun_group_name is not None:
        body_params['lun_group_name'] = lun_group_name

    if storage_host_id is not None:
        body_params['storage_host_id'] = storage_host_id

    if storage_host_name is not None:
        body_params['storage_host_name'] = storage_host_name

    if storage_host_group_id is not None:
        body_params['storage_host_group_id'] = storage_host_group_id

    if storage_host_group_name is not None:
        body_params['storage_host_group_name'] = storage_host_group_name

    if storage_host_group_raw_id is not None:
        body_params['storage_host_group_raw_id'] = storage_host_group_raw_id

    if port_group_id is not None:
        body_params['port_group_id'] = port_group_id

    if port_group_raw_id is not None:
        body_params['port_group_raw_id'] = port_group_raw_id

    if port_group_name is not None:
        body_params['port_group_name'] = port_group_name

    if sort_key is not None:
        body_params['sort_key'] = sort_key

    if sort_dir is not None:
        body_params['sort_dir'] = sort_dir

    response = client.post(url, json=body_params)
    return response


def query_host_lun_mapping(
    client: DMEAPIClient,
    storage_host_id: str = None,
    storage_host_name: str = None,
    lun_id: str = None,
    lun_name: str = None,
    storage_id: str = None
) -> dict:
    """
    查询存储主机和 LUN 映射关系

    根据存储主机/存储主机名称或 LUN 过滤查询映射关系。

    Args:
        client: DME API 客户端
        storage_host_id: 存储主机 ID，和 storage_host_name 参数不支持同时下发
        storage_host_name: 存储主机名称，支持模糊搜索，和 storage_host_id 参数不支持同时下发
        lun_id: LUN ID，和 lun_name 参数不支持同时下发
        lun_name: LUN 名称，支持模糊搜索，和 lun_id 参数不支持同时下发
        storage_id: 存储设备 ID

    Returns:
        响应数据，包含映射关系列表
    """
    url = "/rest/blockservice/v1/storage-host-lun-mappings/query"

    body_params = {}

    if storage_id is not None:
        body_params['storage_id'] = storage_id

    if storage_host_id is not None:
        body_params['storage_host_id'] = storage_host_id

    if storage_host_name is not None:
        body_params['storage_host_name'] = storage_host_name

    if lun_id is not None:
        body_params['lun_id'] = lun_id

    if lun_name is not None:
        body_params['lun_name'] = lun_name

    response = client.post(url, json=body_params)
    return response


def query_mapping_views_by_host(
    client: DMEAPIClient,
    type: str,
    request_id: str,
    storage_id: str
) -> dict:
    """
    查询物理主机（组）关联的映射关系

    根据物理主机/主机组 ID 过滤查询指定存储设备上的映射视图。

    Args:
        client: DME API 客户端
        type: 查询类别（host-物理主机，host_group-主机组）
        request_id: 物理主机/主机组 ID
        storage_id: 存储设备 ID

    Returns:
        响应数据，包含映射视图列表
    """
    url = "/rest/blockservice/v1/volumes/mapping-view/query"

    body_params = {
        'type': type,
        'request_id': request_id,
        'storage_id': storage_id
    }

    response = client.post(url, json=body_params)
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


def unmapping_host(
    client: DMEAPIClient,
    volume_ids: list,
    host_id: str,
    host_type: str = "host",
    task_remarks: str = None
) -> dict:
    """
    解除主机映射

    LUN 解除主机映射。

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表
        host_id: 主机 ID
        host_type: 映射类型（storage_host-存储主机，host-主机），默认 host
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/volumes/host-unmapping"

    body_params = {
        'volume_ids': volume_ids,
        'host_id': host_id,
        'host_type': host_type
    }

    if task_remarks is not None:
        body_params['task_remarks'] = task_remarks

    response = client.post(url, json=body_params)
    return response


def unmapping_host_group(
    client: DMEAPIClient,
    volume_ids: list,
    hostgroup_id: str,
    host_group_type: str = "host_group",
    task_remarks: str = None
) -> dict:
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

    body_params = {
        'volume_ids': volume_ids,
        'hostgroup_id': hostgroup_id,
        'host_group_type': host_group_type
    }

    if task_remarks is not None:
        body_params['task_remarks'] = task_remarks

    response = client.post(url, json=body_params)
    return response


def map_host(
    client: DMEAPIClient,
    volume_ids: list,
    host_id: str,
    mapping_policy: str = None,
    task_remarks: str = None
) -> dict:
    """
    LUN 映射给物理主机

    将 LUN 映射给指定的物理主机。

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表
        host_id: 主机 ID
        mapping_policy: 映射策略（exclusive-独占，shared-共享），默认 exclusive
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/blockservice/v1/volumes/host-mapping"

    body_params = {
        'volume_ids': volume_ids,
        'host_id': host_id
    }

    if mapping_policy is not None:
        body_params['mapping_policy'] = mapping_policy

    if task_remarks is not None:
        body_params['task_remarks'] = task_remarks

    response = client.post(url, json=body_params)
    return response


def map_host_group(
    client: DMEAPIClient,
    volume_ids: list,
    hostgroup_id: str,
    mapping_policy: str = None,
    task_remarks: str = None
) -> dict:
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

    body_params = {
        'volume_ids': volume_ids,
        'hostgroup_id': hostgroup_id
    }

    if mapping_policy is not None:
        body_params['mapping_policy'] = mapping_policy

    if task_remarks is not None:
        body_params['task_remarks'] = task_remarks

    response = client.post(url, json=body_params)
    return response


ACTIONS = {
    # 映射视图管理 - 2 级动作
    'create': {
        'func': create_mapping_view,
        'description': '创建映射视图',
        'params': ['storage_id', 'port_group_id', 'name', 'start_host_lun_id',
                   'host_id', 'host_name', 'host_group_id', 'host_group_name',
                   'lun_group_id', 'lun_ids', 'lungroup_name', 'vbs_id'],
        'subtopic': None
    },
    'delete': {
        'func': batch_delete_mapping_views,
        'description': '批量删除映射视图',
        'params': ['mapping_view_ids'],
        'subtopic': None
    },
    'list': {
        'func': query_mapping_views,
        'description': '批量查询映射视图列表',
        'params': ['page_size', 'page_no', 'name', 'raw_id', 'storage_id',
                   'lun_id', 'lun_name', 'lun_group_id', 'lun_group_raw_id',
                   'lun_group_name', 'storage_host_id', 'storage_host_name',
                   'storage_host_group_id', 'storage_host_group_name',
                   'storage_host_group_raw_id', 'port_group_id', 'port_group_raw_id',
                   'port_group_name', 'sort_key', 'sort_dir'],
        'subtopic': None
    },
    'query': {
        'func': query_mapping_views_by_host,
        'description': '查询物理主机（组）关联的映射关系',
        'params': ['type', 'request_id', 'storage_id'],
        'subtopic': None
    },
}
