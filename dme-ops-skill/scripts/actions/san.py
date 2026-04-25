"""
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

# ============================================================================
# LUN 组 (lun_group) 子主题函数
# ============================================================================



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

# ============================================================================
# 映射视图 (mapping_view) 子主题函数
# ============================================================================



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



# ============================================================================
# 存储主机 (storage_host) 子主题函数
# ============================================================================

def host_create(client: DMEAPIClient, storage_id: str, name: str, os_type: str,
                ip: str = None, description: str = None, initiators: list = None,
                multipath: dict = None, task_remarks: str = None,
                vstore_id: str = None) -> dict:
    """
    创建存储主机

    在指定存储设备上创建存储主机。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必选，1~64 字符）
        name: 主机名称（必选，1~255 字符，只能包含字母、数字、_、-、.和中文字符）
        os_type: 操作系统类型（必选，LINUX/WINDOWS/SUSE 等）
        ip: 主机 IP（可选，最多 127 字符）
        description: 主机描述（可选，最多 63 字符）
        initiators: 启动器列表（可选，最多 1000 个）
                    每个启动器包含：protocol(fc/iscsi/nvme_over_roce), raw_id, alias
        multipath: 多路径配置（可选）
                   包含：multipath_type(default/third_party), path_type, failover_mode, special_mode_type
        task_remarks: 任务备注（可选，最多 1024 字符）
        vstore_id: 租户 ID（可选，1~64 字符）

    Returns:
        任务 ID
    """
    url = "/rest/hostmgmt/v1/storage-hosts"

    payload = {
        'storage_id': storage_id,
        'host_info': {
            'name': name,
            'os_type': os_type
        }
    }

    if ip is not None:
        payload['host_info']['ip'] = ip
    if description is not None:
        payload['host_info']['description'] = description
    if initiators is not None:
        payload['host_info']['initiators'] = initiators
    if multipath is not None:
        payload['host_info']['multipath'] = multipath
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id

    response = client.post(url, json=payload)
    return response


def host_batch_query(client: DMEAPIClient, ids: list) -> dict:
    """
    根据存储主机 ID 列表批量查询存储主机

    根据存储主机 ID 列表批量查询存储主机。

    Args:
        client: DME API 客户端
        ids: ID 列表（必选，1~1000 个）

    Returns:
        存储主机信息列表
    """
    url = "/rest/hostmgmt/v1/storage-hosts/query-by-ids"

    payload = {
        'ids': ids
    }

    response = client.post(url, json=payload)
    return response


def host_list(client: DMEAPIClient, page_size: int = None, page_no: int = None,
              sort_key: str = None, sort_dir: str = None, name: str = None,
              raw_id: str = None, host_group_id: str = None,
              avaliable_add_to_host_group_id: str = None, host_group_name: str = None,
              ip: str = None, health_status: str = None, os_type: str = None,
              storage_id: str = None, avaiable_mapping_for_lun_group_id: str = None,
              avaiable_mapping_for_lun_id: str = None, support_provisioning: bool = None,
              manufacturer: str = None, vstore_raw_id: str = None,
              vstore_name: str = None) -> dict:
    """
    批量查询存储主机

    批量查询存储主机列表，支持多种过滤条件和分页。

    Args:
        client: DME API 客户端
        page_size: 分页查询的个数（可选，1~1000，默认 20）
        page_no: 分页查询的页码（可选，默认 1）
        sort_key: 排序关键字（可选，ip/name/initiator_count/lun_count 等）
        sort_dir: 排序方式（可选，desc/asc）
        name: 主机名称（可选，支持模糊匹配）
        raw_id: 主机在设备侧的 ID（可选）
        host_group_id: 归属主机组 ID（可选）
        avaliable_add_to_host_group_id: 待添加主机组 id（可选）
        host_group_name: 归属主机组名称（可选）
        ip: 主机 IP（可选）
        health_status: 健康状态（可选，normal/no_redundant_link/offline 等）
        os_type: 操作系统类型（可选）
        storage_id: 存储设备 ID（可选）
        avaiable_mapping_for_lun_group_id: 可映射的 LUN 组 ID（可选）
        avaiable_mapping_for_lun_id: 可映射的 LUN ID（可选）
        support_provisioning: 是否支持发放（可选）
        manufacturer: 存储设备厂商（可选）
        vstore_raw_id: 租户 ID（可选）
        vstore_name: 租户名称（可选）

    Returns:
        响应数据，包含存储主机列表和总数
    """
    url = "/rest/hostmgmt/v1/storage-hosts/query"

    payload = {}

    if page_size is not None:
        payload['page_size'] = page_size
    if page_no is not None:
        payload['page_no'] = page_no
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if name is not None:
        payload['name'] = name
    if raw_id is not None:
        payload['raw_id'] = raw_id
    if host_group_id is not None:
        payload['host_group_id'] = host_group_id
    if avaliable_add_to_host_group_id is not None:
        payload['avaliable_add_to_host_group_id'] = avaliable_add_to_host_group_id
    if host_group_name is not None:
        payload['host_group_name'] = host_group_name
    if ip is not None:
        payload['ip'] = ip
    if health_status is not None:
        payload['health_status'] = health_status
    if os_type is not None:
        payload['os_type'] = os_type
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if avaiable_mapping_for_lun_group_id is not None:
        payload['avaiable_mapping_for_lun_group_id'] = avaiable_mapping_for_lun_group_id
    if avaiable_mapping_for_lun_id is not None:
        payload['avaiable_mapping_for_lun_id'] = avaiable_mapping_for_lun_id
    if support_provisioning is not None:
        payload['support_provisioning'] = support_provisioning
    if manufacturer is not None:
        payload['manufacturer'] = manufacturer
    if vstore_raw_id is not None:
        payload['vstore_raw_id'] = vstore_raw_id
    if vstore_name is not None:
        payload['vstore_name'] = vstore_name

    response = client.post(url, json=payload)
    return response


def host_modify(client: DMEAPIClient, storage_host_id: str,
                storage_host_name: str = None, storage_host_description: str = None,
                storage_host_ip: str = None, storage_host_os_type: str = None,
                add_initiators: list = None, remove_initiators: list = None,
                multipath: dict = None, access_mode: str = None,
                hyper_metro_path_optimized: bool = None, task_remarks: str = None) -> dict:
    """
    修改存储主机

    修改存储主机信息，包括主机名、主机 IP、主机操作系统、启动器等。

    Args:
        client: DME API 客户端
        storage_host_id: 存储主机 ID（必选，1~64 字符）
        storage_host_name: 主机名称（可选，1~255 字符，只能包含字母、数字、_、-、.和中文字符）
        storage_host_description: 主机描述（可选，0~63 字符）
        storage_host_ip: 主机 IP（可选，最多 127 字符）
        storage_host_os_type: 操作系统类型（可选，UNKNOWN/LINUX/WINDOWS/SUSE 等）
        add_initiators: 添加的启动器列表（可选，最多 1000 个）
                        每个启动器包含：protocol(fc/iscsi/nvme_over_roce), raw_id, alias
        remove_initiators: 移除的启动器 ID 列表（可选，最多 1000 个）
        multipath: 多路径配置（可选）
                   包含：multipath_type(default/third_party), path_type, failover_mode, special_mode_type
        access_mode: 访问模式（可选，balanced/asymmetric，仅支持 Dorado V6 及以后产品）
        hyper_metro_path_optimized: 双活优选路径（可选，仅支持 Dorado V6 及以后产品）
        task_remarks: 任务备注（可选，最多 1024 字符）

    Returns:
        修改结果
    """
    url = f"/rest/hostmgmt/v1/storage-hosts/{storage_host_id}"

    payload = {}

    if storage_host_name is not None:
        payload['storage_host_name'] = storage_host_name
    if storage_host_description is not None:
        payload['storage_host_description'] = storage_host_description
    if storage_host_ip is not None:
        payload['storage_host_ip'] = storage_host_ip
    if storage_host_os_type is not None:
        payload['storage_host_os_type'] = storage_host_os_type
    if add_initiators is not None:
        payload['add_initiators'] = add_initiators
    if remove_initiators is not None:
        payload['remove_initiators'] = remove_initiators
    if multipath is not None:
        payload['multipath'] = multipath
    if access_mode is not None:
        payload['access_mode'] = access_mode
    if hyper_metro_path_optimized is not None:
        payload['hyper_metro_path_optimized'] = hyper_metro_path_optimized
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def host_delete(client: DMEAPIClient, host_ids: list) -> dict:
    """
    批量删除存储主机

    批量删除指定的存储主机。

    Args:
        client: DME API 客户端
        host_ids: 存储主机 ID 列表（必选，最多 1000 个）

    Returns:
        删除结果
    """
    url = "/rest/hostmgmt/v1/storage-hosts/delete"

    payload = {
        'host_ids': host_ids
    }

    response = client.post(url, json=payload)
    return response


def host_show_paths(client: DMEAPIClient, page_no: int = None, page_size: int = None,
                    storage_id: str = None, storage_host_ids: list = None,
                    storage_host_raw_ids: list = None, health_status: str = None,
                    running_status: str = None, initiator_type: str = None) -> dict:
    """
    批量查询存储主机的路径信息

    批量查询存储主机的路径信息（host-links）。

    Args:
        client: DME API 客户端
        page_no: 分页查询的页码（可选，1~2147483647，默认 1）
        page_size: 分页查询的每页大小（可选，1~1000，默认 20）
        storage_id: 所属存储设备 ID（可选，1~64 字符）
        storage_host_ids: 所属存储主机的 ID 列表（可选，最多 20 个，1~64 字符）
        storage_host_raw_ids: 所属存储主机在设备上的 ID 列表（可选，最多 20 个，1~64 字符）
                              与 storage_host_ids 二者只能设置其中一个
        health_status: 健康状态（可选，normal/fault/no_redundant_link/offline）
        running_status: 链路状态（可选，link_up/link_down/online/disabled/connecting）
        initiator_type: 启动器类型（可选，iSCSI/FC/NVMe_over_RoCE/IB/vHBA）

    Returns:
        路径信息列表
    """
    url = "/rest/hostmgmt/v1/host-links/query"

    payload = {}

    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if storage_host_ids is not None:
        payload['storage_host_ids'] = storage_host_ids
    if storage_host_raw_ids is not None:
        payload['storage_host_raw_ids'] = storage_host_raw_ids
    if health_status is not None:
        payload['health_status'] = health_status
    if running_status is not None:
        payload['running_status'] = running_status
    if initiator_type is not None:
        payload['initiator_type'] = initiator_type

    response = client.post(url, json=payload)
    return response
# ============================================================================
# 存储主机组 (storage_host_group) 子主题函数
# ============================================================================

def host_group_create(client: DMEAPIClient, storage_id: str, name: str,
                      description: str = None, exist_host_ids: list = None,
                      create_storage_host_params: dict = None,
                      task_remarks: str = None, vstore_id: str = None) -> dict:
    """
    创建存储主机组

    创建存储主机组，可以包含现有主机或创建新主机。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必选，1~64 字符）
        name: 主机组名称（必选，1~255 字符）
        description: 主机组描述（可选，0~63 字符）
        exist_host_ids: 现有主机 ID 列表（可选，最多 1000 个）
        create_storage_host_params: 创建主机参数（可选）
                                    用于在主机组创建时同时创建主机
        task_remarks: 任务备注（可选，最多 1024 字符）
        vstore_id: 租户 ID（可选，1~64 字符）

    Returns:
        任务 ID
    """
    url = "/rest/hostmgmt/v1/storage-hostgroups"

    payload = {
        'storage_id': storage_id,
        'name': name
    }

    if description is not None:
        payload['description'] = description
    if exist_host_ids is not None:
        payload['exist_host_ids'] = exist_host_ids
    if create_storage_host_params is not None:
        payload['create_storage_host_params'] = create_storage_host_params
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id

    response = client.post(url, json=payload)
    return response


def host_group_list(client: DMEAPIClient, storage_id: str = None, name: str = None,
                    raw_id: str = None, vstore_id: str = None,
                    vstore_name: str = None, page_no: int = None,
                    page_size: int = None, sort_key: str = None,
                    sort_dir: str = None, avaiable_mapping_for_lun_group_id: str = None,
                    avaiable_mapping_for_lun_id: str = None,
                    support_provisioning: bool = None) -> dict:
    """
    批量查询存储主机组

    批量查询存储主机组列表，支持多种过滤条件和分页。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（可选，1~64 字符）
        name: 主机组名称（可选，支持模糊匹配）
        raw_id: 主机组在设备侧的 ID（可选）
        vstore_id: 租户 ID（可选）
        vstore_name: 租户名称（可选）
        page_no: 分页查询的页码（可选，默认 1）
        page_size: 分页查询的每页大小（可选，1~1000，默认 20）
        sort_key: 排序关键字（可选）
        sort_dir: 排序方式（可选，desc/asc）
        avaiable_mapping_for_lun_group_id: 可映射的 LUN 组 ID（可选）
        avaiable_mapping_for_lun_id: 可映射的 LUN ID（可选）
        support_provisioning: 是否支持发放（可选）

    Returns:
        响应数据，包含存储主机组列表和总数
    """
    url = "/rest/hostmgmt/v1/storage-hostgroups/query"

    payload = {}

    if storage_id is not None:
        payload['storage_id'] = storage_id
    if name is not None:
        payload['name'] = name
    if raw_id is not None:
        payload['raw_id'] = raw_id
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if vstore_name is not None:
        payload['vstore_name'] = vstore_name
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if avaiable_mapping_for_lun_group_id is not None:
        payload['avaiable_mapping_for_lun_group_id'] = avaiable_mapping_for_lun_group_id
    if avaiable_mapping_for_lun_id is not None:
        payload['avaiable_mapping_for_lun_id'] = avaiable_mapping_for_lun_id
    if support_provisioning is not None:
        payload['support_provisioning'] = support_provisioning

    response = client.post(url, json=payload)
    return response


def host_group_add_hosts(client: DMEAPIClient, storage_host_group_id: str,
                         storage_host_id_ids: list = None,
                         create_storage_host_params: dict = None,
                         task_remarks: str = None) -> dict:
    """
    添加存储主机到存储主机组

    将现有主机添加到存储主机组，或在主机组中创建新主机。

    Args:
        client: DME API 客户端
        storage_host_group_id: 存储主机组 ID（必选，1~64 字符）
        storage_host_id_ids: 要添加的主机 ID 列表（可选，最多 1000 个）
        create_storage_host_params: 创建主机参数（可选）
                                    用于在主机组创建新主机
        task_remarks: 任务备注（可选，最多 1024 字符）

    Returns:
        任务 ID
    """
    url = f"/rest/hostmgmt/v1/storage-hostgroups/{storage_host_group_id}/hosts/add"

    payload = {}

    if storage_host_id_ids is not None:
        payload['storage_host_id_ids'] = storage_host_id_ids
    if create_storage_host_params is not None:
        payload['create_storage_host_params'] = create_storage_host_params
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def host_group_remove_hosts(client: DMEAPIClient, storage_host_group_id: str,
                            storage_host_ids: list,
                            task_remarks: str = None) -> dict:
    """
    从存储主机组中移除主机

    从指定的存储主机组中移除一个或多个主机。

    Args:
        client: DME API 客户端
        storage_host_group_id: 存储主机组 ID（必选，1~64 字符）
        storage_host_ids: 要移除的主机 ID 列表（必选，最多 1000 个）
        task_remarks: 任务备注（可选，最多 1024 字符）

    Returns:
        任务 ID
    """
    url = f"/rest/hostmgmt/v1/storage-hostgroups/{storage_host_group_id}/hosts/remove"

    payload = {
        'storage_host_ids': storage_host_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def host_group_delete(client: DMEAPIClient, host_group_ids: list,
                      task_remarks: str = None) -> dict:
    """
    批量删除存储主机组

    批量删除指定的存储主机组。

    Args:
        client: DME API 客户端
        host_group_ids: 存储主机组 ID 列表（必选，1~100 个）
        task_remarks: 任务备注（可选，最多 1024 字符）

    Returns:
        删除结果
    """
    url = "/rest/hostmgmt/v1/storage-hostgroups/delete"

    payload = {
        'host_group_ids': host_group_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def host_show_luns(client: DMEAPIClient, storage_host_id: str,
                   name: str = None, page_size: int = 20,
                   page_no: int = 1, sort_key: str = None,
                   sort_dir: str = None) -> dict:
    """
    查询存储主机映射的 LUN 信息列表

    指定存储主机查询映射 LUN 信息列表，包含 LUN 信息和主机 LUN ID 信息。

    Args:
        client: DME API 客户端
        storage_host_id: 存储主机 ID（必选，1~64 字符）
        name: LUN 名称（可选，1~256 字符，支持模糊搜索）
        page_size: 分页查询的个数（可选，1~1000，默认 20）
        page_no: 分页查询的起始位置（可选，1~10000000，默认 1）
        sort_key: 排序字段（可选，host_lun_id/mapping_view_raw_id/lun_raw_id）
        sort_dir: 排序方向（可选，asc/desc，默认 desc）

    Returns:
        响应数据，包含 total 和 lun_mapping_list
    """
    url = "/rest/blockservice/v1/lun-mapping/query"

    payload = {
        'storage_host_id': storage_host_id,
        'page_size': page_size,
        'page_no': page_no
    }

    if name is not None:
        payload['name'] = name
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir

    response = client.post(url, json=payload)
    return response


def host_group_show_luns(client: DMEAPIClient, storage_host_group_id: str,
                         name: str = None, page_size: int = 20,
                         page_no: int = 1, sort_key: str = None,
                         sort_dir: str = None) -> dict:
    """
    查询存储主机组映射的 LUN 信息列表

    指定存储主机组查询映射 LUN 信息列表，包含 LUN 信息和主机 LUN ID 信息。

    Args:
        client: DME API 客户端
        storage_host_group_id: 存储主机组 ID（必选，1~64 字符）
        name: LUN 名称（可选，1~256 字符，支持模糊搜索）
        page_size: 分页查询的个数（可选，1~1000，默认 20）
        page_no: 分页查询的起始位置（可选，1~10000000，默认 1）
        sort_key: 排序字段（可选，host_lun_id/mapping_view_raw_id/lun_raw_id）
        sort_dir: 排序方向（可选，asc/desc，默认 desc）

    Returns:
        响应数据，包含 total 和 lun_mapping_list
    """
    url = "/rest/blockservice/v1/lun-mapping/query"

    payload = {
        'storage_host_group_id': storage_host_group_id,
        'page_size': page_size,
        'page_no': page_no
    }

    if name is not None:
        payload['name'] = name
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir

    response = client.post(url, json=payload)
    return response
# ============================================================================
# 端口组 (port_group) 子主题函数
# ============================================================================

def port_group_list(client: DMEAPIClient, storage_id: str, name: str = None,
                    page_no: int = 1, page_size: int = 100) -> dict:
    """
    批量查询端口组

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必选）
        name: 端口组名称（支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 100

    Returns:
        响应数据，包含端口组列表
    """
    url = "/rest/storagemgmt/v1/port-groups/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if storage_id is not None:
        payload['storage_id'] = storage_id
    if name is not None:
        payload['name'] = name

    response = client.post(url, json=payload)
    return response


def port_group_create(client: DMEAPIClient, storage_id: str, name: str,
                      description: str = None) -> dict:
    """
    创建端口组

    注意：仅支持 OceanStor 1800 系列存储。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必选）
        name: 端口组名称（必选）
        description: 端口组描述（可选）

    Returns:
        响应数据，包含新创建的端口组 ID
    """
    url = "/rest/storagemgmt/v1/port-groups"

    body_params = {
        'storage_id': storage_id,
        'name': name
    }

    if description is not None:
        body_params['description'] = description

    response = client.post(url, json=body_params)
    return response


def port_group_show_ports(client: DMEAPIClient, storage_id: str, port_group_id: str) -> dict:
    """
    批量查询指定端口组的端口

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        port_group_id: 端口组 ID

    Returns:
        响应数据，包含端口列表
    """
    url = f"/rest/storagemgmt/v1/port-groups/{port_group_id}/ports/query"

    payload = {
        'storage_id': storage_id
    }

    response = client.post(url, json=payload)
    return response


def port_group_show_relations(client: DMEAPIClient, storage_id: str,
                             port_group_id: str = None) -> dict:
    """
    批量查询端口组与端口关联关系

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        port_group_id: 端口组 ID（可选，不传则查询所有）

    Returns:
        响应数据，包含关联关系列表
    """
    url = "/rest/storagemgmt/v1/port-groups/ports/relations/query"

    payload = {
        'storage_id': storage_id
    }

    if port_group_id is not None:
        payload['port_group_id'] = port_group_id

    response = client.post(url, json=payload)
    return response




# ============================================================================
# 动作列表，用于 CLI 帮助
# ============================================================================

ACTIONS = {
    # LUN 子主题动作（san lun xxx）
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
    'lun_connection': {
        'func': get_connection_info,
        'description': '查询指定 LUN ID 的连接信息',
        'params': ['volume_ids'],
        'subtopic': 'lun'
    },
    'lun_mapping': {
        'func': list_host_luns,
        'description': '指定存储主机或存储主机组查询映射 LUN 信息列表',
        'params': ['storage_host_id', 'storage_host_group_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'lun'
    },
    # LUN 组子主题动作（san lun_group xxx）
    'lun_group_list': {
        'func': list_lun_groups,
        'description': '批量查询 LUN 组',
        'params': ['storage_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'lun_group'
    },
    'lun_group_show': {
        'func': show_lun_group,
        'description': '查询指定 LUN 组详情',
        'params': ['group_id', 'storage_id'],
        'subtopic': 'lun_group'
    },
    'lun_group_create': {
        'func': create_lun_group,
        'description': '创建 LUN 组',
        'params': ['storage_id', 'name', 'description'],
        'subtopic': 'lun_group'
    },
    'lun_group_delete': {
        'func': delete_lun_group,
        'description': '删除 LUN 组',
        'params': ['storage_id', 'group_id'],
        'subtopic': 'lun_group'
    },
    'lun_group_add_luns': {
        'func': add_luns_to_group,
        'description': '向 LUN 组添加 LUN',
        'params': ['storage_id', 'group_id', 'lun_ids'],
        'subtopic': 'lun_group'
    },
    'lun_group_remove_luns': {
        'func': remove_luns_from_group,
        'description': '从 LUN 组移除 LUN',
        'params': ['group_id', 'lun_ids', 'storage_id'],
        'subtopic': 'lun_group'
    },
    'lun_group_show_luns': {
        'func': list_lun_group_luns,
        'description': '查询 LUN 组中的 LUN',
        'params': ['group_id', 'storage_id'],
        'subtopic': 'lun_group'
    },
    # 映射视图子主题动作（san mapping_view xxx）
    'mapping_view_create': {
        'func': create_mapping_view,
        'description': '创建映射视图',
        'params': ['storage_id', 'port_group_id', 'name', 'start_host_lun_id',
                   'host_id', 'host_name', 'host_group_id', 'host_group_name',
                   'lun_group_id', 'lun_ids', 'lungroup_name', 'vbs_id'],
        'subtopic': 'mapping_view'
    },
    'mapping_view_delete': {
        'func': batch_delete_mapping_views,
        'description': '批量删除映射视图',
        'params': ['mapping_view_ids'],
        'subtopic': 'mapping_view'
    },
    'mapping_view_list': {
        'func': query_mapping_views,
        'description': '批量查询映射视图列表',
        'params': ['page_size', 'page_no', 'name', 'raw_id', 'storage_id',
                   'lun_id', 'lun_name', 'lun_group_id', 'lun_group_raw_id',
                   'lun_group_name', 'storage_host_id', 'storage_host_name',
                   'storage_host_group_id', 'storage_host_group_name',
                   'storage_host_group_raw_id', 'port_group_id', 'port_group_raw_id',
                   'port_group_name', 'sort_key', 'sort_dir'],
        'subtopic': 'mapping_view'
    },
    'mapping_view_query': {
        'func': query_mapping_views_by_host,
        'description': '查询物理主机（组）关联的映射关系',
        'params': ['type', 'request_id', 'storage_id'],
        'subtopic': 'mapping_view'
    },
    # 存储主机子主题动作（san storage_host xxx）
    'storage_host_create': {
        'func': host_create,
        'description': '创建存储主机',
        'params': ['storage_id', 'name', 'os_type', 'ip', 'description', 'initiators', 'multipath', 'task_remarks', 'vstore_id'],
        'subtopic': 'storage_host'
    },
    'storage_host_batch_query': {
        'func': host_batch_query,
        'description': '根据存储主机 ID 列表批量查询存储主机',
        'params': ['ids'],
        'subtopic': 'storage_host'
    },
    'storage_host_list': {
        'func': host_list,
        'description': '批量查询存储主机',
        'params': ['page_size', 'page_no', 'sort_key', 'sort_dir', 'name', 'raw_id', 'host_group_id',
                   'avaliable_add_to_host_group_id', 'host_group_name', 'ip', 'health_status', 'os_type',
                   'storage_id', 'avaiable_mapping_for_lun_group_id', 'avaiable_mapping_for_lun_id',
                   'support_provisioning', 'manufacturer', 'vstore_raw_id', 'vstore_name'],
        'subtopic': 'storage_host'
    },
    'storage_host_modify': {
        'func': host_modify,
        'description': '修改存储主机',
        'params': ['storage_host_id', 'storage_host_name', 'storage_host_description', 'storage_host_ip',
                   'storage_host_os_type', 'add_initiators', 'remove_initiators', 'multipath', 'access_mode',
                   'hyper_metro_path_optimized', 'task_remarks'],
        'subtopic': 'storage_host'
    },
    'storage_host_delete': {
        'func': host_delete,
        'description': '批量删除存储主机',
        'params': ['host_ids'],
        'subtopic': 'storage_host'
    },
    'storage_host_show_paths': {
        'func': host_show_paths,
        'description': '批量查询存储主机的路径信息',
        'params': ['page_no', 'page_size', 'storage_id', 'storage_host_ids', 'storage_host_raw_ids',
                   'health_status', 'running_status', 'initiator_type'],
        'subtopic': 'storage_host'
    },
    'storage_host_show_luns': {
        'func': host_show_luns,
        'description': '查询存储主机映射的 LUN 信息列表',
        'params': ['storage_host_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'storage_host'
    },
    # 存储主机组子主题动作（san storage_host_group xxx）
    'storage_host_group_create': {
        'func': host_group_create,
        'description': '创建存储主机组',
        'params': ['storage_id', 'name', 'description', 'exist_host_ids', 'create_storage_host_params', 'task_remarks', 'vstore_id'],
        'subtopic': 'storage_host_group'
    },
    'storage_host_group_list': {
        'func': host_group_list,
        'description': '批量查询存储主机组',
        'params': ['storage_id', 'name', 'raw_id', 'vstore_id', 'vstore_name', 'page_no', 'page_size',
                   'sort_key', 'sort_dir', 'avaiable_mapping_for_lun_group_id', 'avaiable_mapping_for_lun_id',
                   'support_provisioning'],
        'subtopic': 'storage_host_group'
    },
    'storage_host_group_add_hosts': {
        'func': host_group_add_hosts,
        'description': '添加存储主机到存储主机组',
        'params': ['storage_host_group_id', 'storage_host_id_ids', 'create_storage_host_params', 'task_remarks'],
        'subtopic': 'storage_host_group'
    },
    'storage_host_group_remove_hosts': {
        'func': host_group_remove_hosts,
        'description': '从存储主机组中移除主机',
        'params': ['storage_host_group_id', 'storage_host_ids', 'task_remarks'],
        'subtopic': 'storage_host_group'
    },
    'storage_host_group_delete': {
        'func': host_group_delete,
        'description': '批量删除存储主机组',
        'params': ['host_group_ids', 'task_remarks'],
        'subtopic': 'storage_host_group'
    },
    'storage_host_group_show_luns': {
        'func': host_group_show_luns,
        'description': '查询存储主机组映射的 LUN 信息列表',
        'params': ['storage_host_group_id', 'name', 'page_size', 'page_no', 'sort_key', 'sort_dir'],
        'subtopic': 'storage_host_group'
    },
    # 端口组子主题动作（san port_group xxx）
    'port_group_list': {
        'func': port_group_list,
        'description': '批量查询端口组',
        'params': ['storage_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'port_group'
    },
    'port_group_create': {
        'func': port_group_create,
        'description': '创建端口组',
        'params': ['storage_id', 'name', 'description'],
        'subtopic': 'port_group'
    },
    'port_group_show_ports': {
        'func': port_group_show_ports,
        'description': '批量查询指定端口组的端口',
        'params': ['storage_id', 'port_group_id'],
        'subtopic': 'port_group'
    },
    'port_group_show_relations': {
        'func': port_group_show_relations,
        'description': '批量查询端口组与端口关联关系',
        'params': ['storage_id', 'port_group_id'],
        'subtopic': 'port_group'
    },
}
