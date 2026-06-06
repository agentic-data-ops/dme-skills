"""
租户自助服务 (Self Service) 相关操作

租户自助服务用于管理服务等级和业务群组。
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient

# ============ lun 子主题函数 ============


def lun_create(client: DMEAPIClient, volumes: list,
               service_level_id: str, task_remarks: str = None,
               project_id: str = None, availability_zone: str = None,
               scheduler_hints: dict = None, mapping: dict = None) -> dict:
    """
    服务化批量创建 LUN

    Args:
        client: DME API 客户端
        volumes: 待创建 LUN 基本参数列表 (List<ServiceVolumeBasicParams>, 数组最大成员个数: 1000)。参数格式如下：[{
                name: LUN名称 (1~255个字符, 支持字母数字._-和中文字符),
                capacity: 容量GB (1~262144),
                count: 创建数量 (1~500),
                description: 描述 (0~255个字符),
                start_suffix: 起始后缀编号 (0~9999),
                suffix_length: 后缀长度规则 (1~4, 名称长度+后缀长度<=255)
             }, ...]
        service_level_id: 服务等级 ID（必填，0~64 个字符）
        task_remarks: 异步任务备注信息（可选，最多 1024 个字符）
        project_id: 业务群组 ID（可选，0~64 个字符）
        availability_zone: 可用分区 ID（可选，0~64 个字符）
        scheduler_hints: 调度策略 (可选, SchedulerHints 对象)。参数格式如下：{
                affinity: 是否开启亲和性。可选值：true (开启), false (不开启)。默认不开启,
                affinity_volume: 待亲和的 LUN ID (可选, 0~64个字符)
             }
        mapping: 映射信息 (可选, ServiceVolumeMapping 对象, 存在即表示为主机或主机组创建 LUN)。参数格式如下：{
                host_id: 主机ID (可选, 0~64个字符, 与hostgroup_id二选其一),
                hostgroup_id: 主机组ID (可选, 0~64个字符, 与host_id二选其一)
             }

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes"

    payload = {
        'volumes': volumes,
        'service_level_id': service_level_id
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    if project_id is not None:
        payload['project_id'] = project_id
    if availability_zone is not None:
        payload['availability_zone'] = availability_zone
    if scheduler_hints is not None:
        payload['scheduler_hints'] = scheduler_hints
    if mapping is not None:
        payload['mapping'] = mapping

    response = client.post(url, json=payload)
    return response


def update_volume_service_level(client: DMEAPIClient, volume_ids: list,
                                tier_id: str, attributes_auto_change: bool = None) -> dict:
    """
    批量更新 LUN 的服务等级

    Args:
        client: DME API 客户端
        volume_ids: LUN ID 列表
        tier_id: 服务等级 ID
        attributes_auto_change: 是否根据服务等级参数刷新 LUN 属性（可选，true/false）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/update-service-level"

    payload = {
        'volume_ids': volume_ids,
        'service_level_id': tier_id
    }

    if attributes_auto_change is not None:
        payload['attributes_auto_change'] = attributes_auto_change

    response = client.post(url, json=payload)
    return response


def bind_service_level(client: DMEAPIClient, volume_id: str,
                       tier_id: str, attributes_auto_change: bool = None) -> dict:
    """
    LUN 关联服务等级

    Args:
        client: DME API 客户端
        volume_id: LUN ID
        tier_id: 服务等级 ID
        attributes_auto_change: 是否根据服务等级参数刷新 LUN 属性（可选，true/false）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/add-to-service-level"

    payload = {
        'volume_ids': [volume_id],
        'service_level_id': tier_id
    }

    if attributes_auto_change is not None:
        payload['attributes_auto_change'] = attributes_auto_change

    response = client.post(url, json=payload)
    return response


def unbind_service_level(client: DMEAPIClient, volume_id: str) -> dict:
    """
    解除 LUN 与服务等级关联

    Args:
        client: DME API 客户端
        volume_id: LUN ID

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/blockservice/v1/volumes/remove-service-level"

    payload = {
        'volume_ids': [volume_id]
    }

    response = client.post(url, json=payload)
    return response


def bind_business_group(client: DMEAPIClient, volume_id: str,
                        business_group_id: str) -> dict:
    """
    LUN 关联业务群组

    Args:
        client: DME API 客户端
        volume_id: LUN ID
        business_group_id: 业务群组 ID

    Returns:
        响应数据
    """
    url = f"/rest/blockservice/v1/projects/{business_group_id}/volumes/bound"

    payload = {
        'volume_ids': [volume_id]
    }

    response = client.put(url, json=payload)
    return response


def unbind_business_group(client: DMEAPIClient, volume_id: str,
                          business_group_id: str) -> dict:
    """
    解除 LUN 与业务群组间关联

    Args:
        client: DME API 客户端
        volume_id: LUN ID
        business_group_id: 业务群组 ID

    Returns:
        响应数据
    """
    url = f"/rest/blockservice/v1/projects/{business_group_id}/volumes/unbound"

    payload = {
        'volume_ids': [volume_id]
    }

    response = client.put(url, json=payload)
    return response


# ============ tier 子主题函数 ============


def list_service_levels(client: DMEAPIClient, name: str = None,
                        project_id: str = None, available_zone_id: str = None,
                        storage_array_id: str = None, start: int = 0,
                        limit: int = 200, sort_key: str = 'name',
                        sort_dir: str = 'asc', type: str = None) -> dict:
    """
    批量查询服务等级

    查询服务等级列表，支持按名称、项目 ID、可用区、存储 ID 等过滤和分页。

    Args:
        client: DME API 客户端
        name: 服务等级名称（可选，支持模糊查询）
        project_id: 业务群组 ID（可选）
        available_zone_id: 可用区 ID（可选）
        storage_array_id: 存储设备 ID（可选）
        start: 查询的起始位置，默认 0
        limit: 每页数量，10~1000，默认 200
        sort_key: 排序字段，name/total_capacity/created_at，默认 name
        sort_dir: 排序方向，asc/desc，默认 asc
        type: 存储类型，FILE/BLOCK/VIRTUAL_DATASTORE（可选）

    Returns:
        响应数据，包含服务等级列表
    """
    url = "/rest/service-policy/v1/service-levels"

    query_params = {
        'start': start,
        'limit': limit
    }

    if name is not None:
        query_params['name'] = name

    if project_id is not None:
        query_params['project_id'] = project_id

    if available_zone_id is not None:
        query_params['available_zone_id'] = available_zone_id

    if storage_array_id is not None:
        query_params['storage_array_id'] = storage_array_id

    query_params['sort_key'] = sort_key
    query_params['sort_dir'] = sort_dir

    if type is not None:
        query_params['type'] = type

    response = client.get(url, query_params=query_params)
    return response


def list_project_slo_relations_by_service_level(client: DMEAPIClient, tier_id: str = None,
                                page_no: int = 1, page_size: int = 200) -> dict:
    """
    批量查询业务群组与服务等级关联关系

    查询业务群组与服务等级的关联关系列表，支持按服务等级 ID 过滤。

    Args:
        client: DME API 客户端
        tier_id: 服务等级 ID（可选）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，10~1000，默认 200

    Returns:
        响应数据，包含关联关系列表
    """
    url = "/rest/service-policy/v1/service-levels/projects/relations"

    query_params = {
        'pageNo': page_no,
        'pageSize': page_size
    }

    if tier_id is not None:
        query_params['serviceLevelId'] = tier_id

    response = client.get(url, query_params=query_params)
    return response


# ============ project 子主题函数 ============


def list_projects(client: DMEAPIClient, name: str = None,
                  start: int = 1, limit: int = 20) -> dict:
    """
    批量查询业务群组

    查询业务群组列表，支持按名称过滤和分页。

    Args:
        client: DME API 客户端
        name: 业务群组名称（可选，支持模糊查询）
        start: 分页的页号，从 1 开始，默认 1
        limit: 分页的大小，1~512，默认 20

    Returns:
        响应数据，包含业务群组列表
    """
    url = "/rest/projectmgmt/v1/projects"

    query_params = {
        'start': start,
        'limit': limit
    }

    if name is not None:
        query_params['name'] = name

    response = client.get(url, query_params=query_params)
    return response


def list_project_slo_relations_by_project(client: DMEAPIClient, project_id: str = None,
                                page_no: int = 1, page_size: int = 200) -> dict:
    """
    批量查询业务群组与服务等级关联关系

    查询指定业务群组的关联服务等级列表。

    Args:
        client: DME API 客户端
        project_id: 业务群组 ID（可选）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，10~1000，默认 200

    Returns:
        响应数据，包含关联关系列表
    """
    url = "/rest/service-policy/v1/service-levels/projects/relations"

    query_params = {
        'pageNo': page_no,
        'pageSize': page_size
    }

    if project_id is not None:
        query_params['projectId'] = project_id

    response = client.get(url, query_params=query_params)
    return response


# 动作列表，用于 CLI 帮助
# 本主题无直接动作，所有动作均在子主题下
ACTIONS = {
    # tier 子主题
    'tier_list': {
        'func': list_service_levels,
        'description': '批量查询服务等级',
        'params': ['name', 'project_id', 'available_zone_id', 'storage_array_id', 'start', 'limit', 'sort_key', 'sort_dir', 'type'],
        'subtopic': 'tier'
    },
    'tier_show_projects': {
        'func': list_project_slo_relations_by_service_level,
        'description': '批量查询业务群组与服务等级关联关系',
        'params': ['tier_id', 'page_no', 'page_size'],
        'subtopic': 'tier'
    },
    # project 子主题
    'project_list': {
        'func': list_projects,
        'description': '批量查询业务群组',
        'params': ['name', 'start', 'limit'],
        'subtopic': 'project'
    },
    'project_show_tiers': {
        'func': list_project_slo_relations_by_project,
        'description': '批量查询业务群组与服务等级关联关系',
        'params': ['project_id', 'page_no', 'page_size'],
        'subtopic': 'project'
    },
    # lun 子主题
    'lun_create': {
        'func': lun_create,
        'description': '服务化批量创建 LUN',
        'params': ['volumes', 'service_level_id', 'task_remarks', 'project_id', 'availability_zone', 'scheduler_hints', 'mapping'],
        'subtopic': 'lun'
    },
    'lun_change_tier': {
        'func': update_volume_service_level,
        'description': '批量更新 LUN 的服务等级',
        'params': ['volume_ids', 'tier_id'],
        'subtopic': 'lun'
    },
    'lun_bind_tier': {
        'func': bind_service_level,
        'description': 'LUN 关联服务等级',
        'params': ['volume_id', 'tier_id'],
        'subtopic': 'lun'
    },
    'lun_unbind_tier': {
        'func': unbind_service_level,
        'description': '解除 LUN 与服务等级关联',
        'params': ['volume_id'],
        'subtopic': 'lun'
    },
    'lun_bind_project': {
        'func': bind_business_group,
        'description': 'LUN 关联业务群组',
        'params': ['volume_id', 'business_group_id'],
        'subtopic': 'lun'
    },
    'lun_unbind_project': {
        'func': unbind_business_group,
        'description': '解除 LUN 与业务群组间关联',
        'params': ['volume_id', 'business_group_id'],
        'subtopic': 'lun'
    },
}
