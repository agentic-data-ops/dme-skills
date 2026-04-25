"""
性能 (Performance) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


# ============ 性能数据 (data) 子主题函数 ============


def history_data_query(client: DMEAPIClient, obj_type_id: int, indicator_ids: list,
                       obj_ids: list, obj_type: str = None, indicators: list = None,
                       ext_dimensions: list = None, interval: str = None,
                       range: str = None, begin_time: int = None,
                       end_time: int = None) -> dict:
    """
    查询历史性能数据

    根据传入参数中的"range"字段所取的枚举值或从开始到结束时间范围内的查询数据。
    有汇聚数据情况下，返回结果序列是平均值序列，并包含最大值、最小值以及对应时间戳。

    使用说明:
    - 对象类型和指标定义：从性能指标模型文档获取 (reference/dme_performance_model/index.md)
    - 对象 ID (CMDB 实例 ID) 获取步骤:
      1. 运行 `cmdb instance list --help` 查看帮助，了解类定义和查询方式
      2. 根据帮助信息，从 CMDB 资源模型中确定要查询的资源类型 (Class 名称)
      3. 使用 `cmdb instance list --class_name <Class 名称>` 查询实例列表
      4. 从返回结果中获取对应资源的 instance_id (即 obj_ids 参数)

    Args:
        client: DME API 客户端
        obj_type_id: 监控对象类型标识（必填），对应监控对象类型 ID
                     从性能指标模型文档获取：reference/dme_performance_model/index.md
        indicator_ids: 监控指标标识列表（必填，最多 100 个），对应指标 ID
                       从性能指标模型文档获取：reference/dme_performance_model/index.md
        obj_ids: 监控对象标识列表（必填，最多 512 个），对应 CMDB 实例 ID
                 获取方式:
                 1. 运行 `cmdb instance list --help` 查看帮助，了解类定义
                 2. 根据帮助确定要查询的资源类型 (Class 名称)
                 3. 运行 `cmdb instance list --class_name <Class 名称>` 查询实例
                 4. 从返回结果中获取 instance_id
        obj_type: 监控对象类型（可选，1~512 个字符）
        indicators: 监控指标列表（可选，最多 100 个）
        ext_dimensions: 扩展维度信息列表（可选，最多 100 个）
        interval: 间隔粒度（可选）
                  取值范围：ONE_MINUTE(1 分钟), MINUTE(5 分钟), HALF_HOUR(30 分钟),
                  HOUR(1 小时), DAY(1 天), WEEK(1 周), MONTH(1 个月)
        range: 时间范围（可选，默认 LAST_1_HOUR）
               取值范围：LAST_5_MINUTE(最近 5 分钟), LAST_1_HOUR(最近 1 小时),
               LAST_1_DAY(最近 1 天), LAST_1_WEEK(最近 1 周), LAST_1_MONTH(最近 1 个月),
               LAST_1_QUARTER(最近 3 个月), HALF_1_YEAR(最近半年), LAST_1_YEAR(最近 1 年),
               BEGIN_END_TIME(自行设置开始和结束时间), INVALID(无效值)
        begin_time: 查询开始时刻（可选），仅 range 为 BEGIN_END_TIME 时生效，必须比 end_time 小
        end_time: 查询结束时刻（可选），仅 range 为 BEGIN_END_TIME 时生效，必须比 begin_time 大

    Returns:
        历史性能数据，包含 status_code, error_code, error_msg, data
    """
    url = "/rest/metrics/v1/data-svc/history-data/action/query"

    payload = {
        'obj_type_id': obj_type_id,
        'indicator_ids': indicator_ids,
        'obj_ids': obj_ids
    }

    if obj_type is not None:
        payload['obj_type'] = obj_type
    if indicators is not None:
        payload['indicators'] = indicators
    if ext_dimensions is not None:
        payload['ext_dimensions'] = ext_dimensions
    if interval is not None:
        payload['interval'] = interval
    if range is not None:
        payload['range'] = range
    if begin_time is not None:
        payload['begin_time'] = begin_time
    if end_time is not None:
        payload['end_time'] = end_time

    response = client.post(url, json=payload)
    return response


def second_history_data_query(client: DMEAPIClient, obj_type_id: int,
                              indicator_ids: list, resource_key: str,
                              resource_values: list, begin_time: int,
                              end_time: int, storage_id: str = None,
                              storage_sn: str = None) -> dict:
    """
    查询秒级历史性能数据

    使用说明:
    - 对象类型和指标定义：从性能指标模型文档获取 (reference/dme_performance_model/index.md)
    - 对象 ID: 通过 resource_values 传入 CMDB 实例 ID，resource_key 指定字段 (nguid 或 wwn)

    Args:
        client: DME API 客户端
        obj_type_id: 监控对象类型标识（必填，0~100000000000000000）
                     从性能指标模型文档获取：reference/dme_performance_model/index.md
        indicator_ids: 监控指标标识列表（必填，1~5 个），对应指标 ID
                       从性能指标模型文档获取：reference/dme_performance_model/index.md
        resource_key: 监控对象字段名称（必填），取值范围：nguid(命名空间 GUID), wwn
        resource_values: CMDB 实例 ID 列表（必填，1~10 个）
        begin_time: 查询开始时间（必填），毫秒时间戳
        end_time: 查询结束时间（必填），毫秒时间戳，必须比 begin_time 大
        storage_id: 存储设备 ID（可选），storage_id 和 storage_sn 不能同时为空
        storage_sn: 存储设备序列号（可选），storage_id 为空时有效

    Returns:
        秒级历史性能数据
    """
    url = "/rest/metrics/v1/data-svc/second-data/action/query"

    payload = {
        'obj_type_id': obj_type_id,
        'indicator_ids': indicator_ids,
        'resource_key': resource_key,
        'resource_values': resource_values,
        'begin_time': begin_time,
        'end_time': end_time
    }

    if storage_id is not None:
        payload['storage_id'] = storage_id
    if storage_sn is not None:
        payload['storage_sn'] = storage_sn

    response = client.post(url, json=payload)
    return response


# ============ 监控指标 (indicator) 子主题函数 ============


def obj_type_indicators(client: DMEAPIClient, obj_type_id: int) -> dict:
    """
    获取监控对象类型支持的监控指标

    Args:
        client: DME API 客户端
        obj_type_id: 监控对象类型标识（必填）

    Returns:
        监控指标信息，包含 indicator_ids 列表
    """
    url = f"/rest/metrics/v1/mgr-svc/obj-types/{obj_type_id}/indicators"

    response = client.get(url)
    return response


def indicators(client: DMEAPIClient, indicators: list) -> dict:
    """
    获取监控指标

    Args:
        client: DME API 客户端
        indicators: 监控对象指标标识列表（必填，最多 1000 个字符）
                   可以是整数列表或字符串列表，如 [123, 456] 或 ["123", "456"]

    Returns:
        监控指标信息，包含 kpi, data_type, data_unit, en_us, zh_cn 等字段
    """
    url = "/rest/metrics/v1/mgr-svc/indicators"

    # 确保 indicators 是整数列表
    if indicators:
        indicators = [int(i) for i in indicators]

    # API 要求直接传递数组，而不是对象
    response = client.post(url, json=indicators)
    return response


# ============ 监控对象类型 (object_type) 子主题函数 ============


def object_type_list(client: DMEAPIClient, filter: str = None) -> dict:
    """
    获取所有监控对象类型

    Args:
        client: DME API 客户端
        filter: 过滤关键字（可选），用于模糊匹配 zh_cn 和 en_us 字段
                如果提供，仅返回匹配的对象类型

    Returns:
        监控对象类型列表，包含 obj_type_id, parent_obj_type_id, resource_category,
        resource_provider, en_us, zh_cn, group_en_us, group_zh_cn 等字段
    """
    url = "/rest/metrics/v1/mgr-svc/obj-types"

    response = client.get(url)

    # 如果提供了 filter 参数，过滤结果
    if filter is not None and response and 'data' in response:
        filter_lower = filter.lower()
        filtered_data = []
        for item in response.get('data', []):
            zh_cn = item.get('zh_cn', '')
            en_us = item.get('en_us', '')
            if filter_lower in zh_cn.lower() or filter_lower in en_us.lower():
                filtered_data.append(item)
        response['data'] = filtered_data

    return response


# ============ 性能文件收集任务 (collect_task) 子主题函数 ============


def collect_task_create(client: DMEAPIClient, begin_time: int, end_time: int,
                        object_type_id: str, object_ids: list,
                        indicator_ids: list) -> dict:
    """
    创建性能文件收集任务

    收集范围为：开始日期到结束日期的性能文件，只支持收集 7 天内的数据，
    每次传入的对象乘以指标数不超过 2000。

    Args:
        client: DME API 客户端
        begin_time: 开始时间（必填，Unix 时间戳毫秒）
        end_time: 结束时间（必填，Unix 时间戳毫秒）
        object_type_id: 对象类型 ID（必填，1~32 个字符）
        object_ids: 对象 ID 列表（必填，最多 2000 个，ID 长度 1~32 位）
        indicator_ids: 指标 ID 列表（必填，最多 20 个，ID 长度 1~16 位）

    Returns:
        任务 ID
    """
    url = "/rest/pmmgmt/v1/performance-data/collection-task"

    payload = {
        'begin_time': begin_time,
        'end_time': end_time,
        'object_type_id': object_type_id,
        'object_ids': object_ids,
        'indicator_ids': indicator_ids
    }

    response = client.post(url, json=payload)
    return response


def collect_task_download(client: DMEAPIClient, task_id: str) -> dict:
    """
    下载性能文件

    Args:
        client: DME API 客户端
        task_id: 任务 ID（必填）

    Returns:
        性能文件下载链接或文件内容
    """
    url = f"/rest/pmmgmt/v1/performance-data/download/{task_id}"

    response = client.get(url)
    return response


# 动作列表，用于 CLI 帮助
# 格式：action_key: {func, description, params, subtopic}
# subtopic 表示该动作属于哪个子主题，None 表示直接动作

ACTIONS = {
    # data 子主题动作
    'data_query': {
        'func': history_data_query,
        'description': '查询历史性能数据',
        'params': ['obj_type_id', 'indicator_ids', 'obj_ids', 'obj_type', 'indicators', 'ext_dimensions', 'interval', 'range', 'begin_time', 'end_time'],
        'subtopic': 'data'
    },
    # indicator 子主题动作
    'indicator_list': {
        'func': obj_type_indicators,
        'description': '获取监控对象类型支持的监控指标',
        'params': ['obj_type_id'],
        'subtopic': 'indicator'
    },
    'indicator_detail': {
        'func': indicators,
        'description': '获取监控指标',
        'params': ['indicators'],
        'subtopic': 'indicator'
    },
    # object_type 子主题动作
    'object_type_list': {
        'func': object_type_list,
        'description': '获取所有监控对象类型',
        'params': ['filter'],
        'subtopic': 'object_type'
    },
    # collect_task 子主题动作
    'collect_task_create': {
        'func': collect_task_create,
        'description': '创建性能文件收集任务',
        'params': ['begin_time', 'end_time', 'object_type_id', 'object_ids', 'indicator_ids'],
        'subtopic': 'collect_task'
    },
    'collect_task_download': {
        'func': collect_task_download,
        'description': '下载性能文件',
        'params': ['task_id'],
        'subtopic': 'collect_task'
    },
}