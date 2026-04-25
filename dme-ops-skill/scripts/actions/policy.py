"""
策略管理 (Policy) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def list_policies(client: DMEAPIClient, name: str = None, policy_type: str = None,
                  page_no: int = 1, page_size: int = 100) -> dict:
    """
    批量查询策略
    
    查询策略列表。
    
    Args:
        client: DME API 客户端
        name: 策略名称（支持模糊查询）
        policy_type: 策略类型
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 100
    
    Returns:
        响应数据，包含策略列表
    """
    url = "/rest/policymgmt/v1/policies/query"
    
    body_params = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if name is not None:
        body_params['name'] = name
    if policy_type is not None:
        body_params['policy_type'] = policy_type
    
    response = client.post(url, data=body_params)
    return response


def show_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    查询指定策略详情
    
    查询策略的详细信息。
    
    Args:
        client: DME API 客户端
        policy_id: 策略 ID
    
    Returns:
        策略详细信息
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}"
    
    response = client.get(url)
    return response


def create_policy(client: DMEAPIClient, name: str, policy_type: str,
                  config: dict, description: str = None) -> dict:
    """
    创建策略
    
    创建新的策略。
    
    Args:
        client: DME API 客户端
        name: 策略名称（必选）
        policy_type: 策略类型（必选）
        config: 策略配置（必选）
        description: 策略描述（可选）
    
    Returns:
        响应数据，包含新创建的策略 ID
    """
    url = "/rest/policymgmt/v1/policies"
    
    body_params = {
        'name': name,
        'policy_type': policy_type,
        'config': config
    }
    
    if description is not None:
        body_params['description'] = description
    
    response = client.post(url, data=body_params)
    return response


def delete_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    删除策略
    
    删除指定的策略。
    
    Args:
        client: DME API 客户端
        policy_id: 策略 ID
    
    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}"
    
    response = client.delete(url)
    return response


def modify_policy(client: DMEAPIClient, policy_id: str, name: str = None,
                  config: dict = None, description: str = None) -> dict:
    """
    修改策略
    
    修改策略的配置信息。
    
    Args:
        client: DME API 客户端
        policy_id: 策略 ID
        name: 策略名称（可选）
        config: 策略配置（可选）
        description: 策略描述（可选）
    
    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}"
    
    body_params = {}
    if name is not None:
        body_params['name'] = name
    if config is not None:
        body_params['config'] = config
    if description is not None:
        body_params['description'] = description
    
    response = client.put(url, data=body_params)
    return response


def bind_policy_resource(client: DMEAPIClient, policy_id: str, resource_type: str,
                         resource_id: str) -> dict:
    """
    策略关联资源
    
    将策略绑定到指定资源。
    
    Args:
        client: DME API 客户端
        policy_id: 策略 ID
        resource_type: 资源类型
        resource_id: 资源 ID
    
    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}/resources"
    
    body_params = {
        'resource_type': resource_type,
        'resource_id': resource_id
    }
    
    response = client.post(url, data=body_params)
    return response


def unbind_policy_resource(client: DMEAPIClient, policy_id: str, resource_type: str,
                           resource_id: str) -> dict:
    """
    策略解关联资源

    将策略从指定资源上解绑。

    Args:
        client: DME API 客户端
        policy_id: 策略 ID
        resource_type: 资源类型
        resource_id: 资源 ID

    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}/resources"

    body_params = {
        'resource_type': resource_type,
        'resource_id': resource_id
    }

    response = client.delete(url, data=body_params)
    return response


def list_check_policies(client: DMEAPIClient, policy_name: str = None, exact_query: bool = None,
                        status: str = None, policy_type: str = None, policy_source: str = None,
                        alarm_type: str = None, object_type: str = None, page_no: int = 1,
                        page_size: int = 20, sort_key: str = None, sort_dir: str = None,
                        administrative_status: str = None, policy_category: str = None,
                        object_category: str = None) -> dict:
    """
    查询检查策略列表

    查询检查策略列表，支持多种过滤条件和分页查询。

    Args:
        client: DME API 客户端
        policy_name: 策略名称（支持模糊查询，1~256 个字符）
        exact_query: 名称是否精确查询（true-精确查询，false-模糊查询），默认 false
        status: 策略状态（normal-正常，checking-检查中，failed-检查失败，queuing-排队中）
        policy_type: 策略类型（performance-性能阈值，capacity-容量阈值，availability-可用性，
                    configuration-配置，recyclable-可回收资源，lowload-低负载资源，
                    performance_anomaly-性能异常，performance_prediction-性能预警，
                    capacity_prediction-容量预警，history_performance-历史性能，
                    load_imbalance-负载失衡，highload-高负载资源）
        policy_source: 来源（pre-define-预置，user-define-自定义）
        alarm_type: 告警类型（violation-异常，alarm-告警，event-事件）
        object_type: 对象类型（storage-存储，lun-逻辑单元，host-主机等）
        page_no: 分页查询的页码，1~1000，默认 1
        page_size: 分页查询的个数，1~100，默认 20
        sort_key: 排序字段（last_check_time-最后检查时间，failed_count-检查不通过的对象个数）
        sort_dir: 排序方式（asc-正序，desc-降序）
        administrative_status: 管理状态（enable-启用，disable-禁用）
        policy_category: 检查分类（configuration-配置，performance-性能，capacity-容量，faults-故障，optimization-优化）
        object_category: 对象分类（Storage-存储设备，IPSwitch-以太网交换机，FCSwitch-光纤交换机，
                       Virtualization-虚拟化，Server-服务器，HCI-超融合，Client-客户端）

    Returns:
        响应数据，包含 total（总数）和 policies（策略列表）
    """
    url = "/rest/policymgmt/v2/policies/query"

    body_params = {
        'page_no': page_no,
        'page_size': page_size
    }

    if policy_name is not None:
        body_params['policy_name'] = policy_name
    if exact_query is not None:
        body_params['exact_query'] = exact_query
    if status is not None:
        body_params['status'] = status
    if policy_type is not None:
        body_params['policy_type'] = policy_type
    if policy_source is not None:
        body_params['policy_source'] = policy_source
    if alarm_type is not None:
        body_params['alarm_type'] = alarm_type
    if object_type is not None:
        body_params['object_type'] = object_type
    if sort_key is not None:
        body_params['sort_key'] = sort_key
    if sort_dir is not None:
        body_params['sort_dir'] = sort_dir
    if administrative_status is not None:
        body_params['administrative_status'] = administrative_status
    if policy_category is not None:
        body_params['policy_category'] = policy_category
    if object_category is not None:
        body_params['object_category'] = object_category

    response = client.post(url, json=body_params)
    return response


def execute_check_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    执行检查策略

    执行指定的检查策略。

    Args:
        client: DME API 客户端
        policy_id: 策略 ID（1~64 个字符）

    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}/execute"

    response = client.post(url)
    return response


def enable_check_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    启用检查策略

    启用指定的检查策略。

    Args:
        client: DME API 客户端
        policy_id: 策略 ID（1~64 个字符）

    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}/enable"

    response = client.post(url)
    return response


def disable_check_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    禁用检查策略

    禁用指定的检查策略。

    Args:
        client: DME API 客户端
        policy_id: 策略 ID（1~64 个字符）

    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}/disable"

    response = client.post(url)
    return response


def delete_check_policy(client: DMEAPIClient, policy_id: str) -> dict:
    """
    删除检查策略

    删除指定的检查策略。

    Args:
        client: DME API 客户端
        policy_id: 策略 ID（1~64 个字符）

    Returns:
        响应数据
    """
    url = f"/rest/policymgmt/v1/policies/{policy_id}"

    response = client.delete(url)
    return response


def list_abnormal_results(client: DMEAPIClient, object_name: str = None, level: str = None,
                          object_ids: list = None, object_native_id: str = None,
                          object_type: str = None, policy_id: str = None,
                          policy_name: str = None, policy_types: list = None,
                          cause: str = None, alarm_type: str = None,
                          first_occur_time: dict = None, last_occur_time: dict = None,
                          page_no: int = 1, page_size: int = 20, sort_key: str = None,
                          sort_dir: str = None) -> dict:
    """
    查询检查策略异常检查结果列表

    查询检查策略的异常检查结果，支持多种过滤条件和分页查询。

    Args:
        client: DME API 客户端
        object_name: 对象名称（支持模糊查询，1~256 个字符）
        level: 异常级别（critical-紧急，major-重要，minor-次要，info-提示）
        object_ids: 对象 ID 列表（最多 100 个）
        object_native_id: 对象 nativeId（1~384 个字符）
        object_type: 对象类型（storage-存储，lun-逻辑单元，host-主机等）
        policy_id: 策略 ID（精确查询，1~64 个字符）
        policy_name: 策略名称（支持模糊查询，1~256 个字符）
        policy_types: 策略类型列表（最多 30 个）
        cause: 异常原因（支持模糊查询，1~768 个字符）
        alarm_type: 告警类型（violation-异常，alarm-告警，event-事件）
        first_occur_time: 第一次异常时间范围（{beginTime, endTime}，UTC 时间戳，单位 ms）
        last_occur_time: 最后一次异常时间范围（{beginTime, endTime}，UTC 时间戳，单位 ms）
        page_no: 分页查询的页码，1~10000，默认 1
        page_size: 分页查询的个数，1~2000，默认 20
        sort_key: 排序字段（violation_count-异常次数）
        sort_dir: 排序方式（asc-正序，desc-降序）

    Returns:
        响应数据，包含 total（总数）和 results（异常检查结果列表）
    """
    url = "/rest/policymgmt/v1/abnormal-check-results/query"

    body_params = {
        'page_no': page_no,
        'page_size': page_size
    }

    if object_name is not None:
        body_params['object_name'] = object_name
    if level is not None:
        body_params['level'] = level
    if object_ids is not None:
        body_params['object_ids'] = object_ids
    if object_native_id is not None:
        body_params['object_native_id'] = object_native_id
    if object_type is not None:
        body_params['object_type'] = object_type
    if policy_id is not None:
        body_params['policy_id'] = policy_id
    if policy_name is not None:
        body_params['policy_name'] = policy_name
    if policy_types is not None:
        body_params['policy_types'] = policy_types
    if cause is not None:
        body_params['cause'] = cause
    if alarm_type is not None:
        body_params['alarm_type'] = alarm_type
    if first_occur_time is not None:
        body_params['first_occur_time'] = first_occur_time
    if last_occur_time is not None:
        body_params['last_occur_time'] = last_occur_time
    if sort_key is not None:
        body_params['sort_key'] = sort_key
    if sort_dir is not None:
        body_params['sort_dir'] = sort_dir

    response = client.post(url, json=body_params)
    return response


def show_abnormal_result(client: DMEAPIClient, check_result_id: str) -> dict:
    """
    查询检查策略异常检查结果详情

    查询指定检查结果的详细信息。

    Args:
        client: DME API 客户端
        check_result_id: 检查结果 ID（1~64 个字符）

    Returns:
        响应数据，包含检查结果的详细信息
    """
    url = f"/rest/policymgmt/v1/abnormal-check-results/{check_result_id}"

    response = client.get(url)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # 直接动作 - 策略管理（两级结构）
    'list': {
        'func': list_check_policies,
        'description': '查询检查策略列表',
        'params': ['policy_name', 'exact_query', 'status', 'policy_type', 'policy_source', 'alarm_type', 'object_type', 'page_no', 'page_size', 'sort_key', 'sort_dir', 'administrative_status', 'policy_category', 'object_category'],
        'subtopic': None
    },
    'delete': {
        'func': delete_policy,
        'params': ['policy_id'],
        'description': '删除检查策略',
        'subtopic': None
    },
    'execute': {
        'func': execute_check_policy,
        'description': '执行检查策略',
        'params': ['policy_id'],
        'subtopic': None
    },
    'enable': {
        'func': enable_check_policy,
        'description': '启用检查策略',
        'params': ['policy_id'],
        'subtopic': None
    },
    'disable': {
        'func': disable_check_policy,
        'description': '禁用检查策略',
        'params': ['policy_id'],
        'subtopic': None
    },
    # 子主题动作 - result（三级结构）
    'result_list': {
        'func': list_abnormal_results,
        'description': '查询检查策略异常检查结果列表',
        'params': ['object_name', 'level', 'object_ids', 'object_native_id', 'object_type', 'policy_id', 'policy_name', 'policy_types', 'cause', 'alarm_type', 'first_occur_time', 'last_occur_time', 'page_no', 'page_size', 'sort_key', 'sort_dir'],
        'subtopic': 'result'
    },
    'result_show': {
        'func': show_abnormal_result,
        'description': '查询检查策略异常检查结果详情',
        'params': ['check_result_id'],
        'subtopic': 'result'
    },
}
