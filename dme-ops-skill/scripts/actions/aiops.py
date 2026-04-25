"""
AIOps 智能运维相关操作
"""

import sys
import os
import json
from datetime import datetime, timedelta

# 添加父目录到路径,以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def _build_current_alarm_params(alarm_id: str = None, severity: list = None,
                                 mo_dn: str = None, alarm_group_id: str = None,
                                 dc_id: str = None, product_name: str = None,
                                 alarm_name: str = None, occur_utc_start: str = None,
                                 occur_utc_end: str = None, fields: list = None,
                                 page_size: int = 100) -> dict:
    """构建当前告警查询参数"""
    body_params = {'size': page_size}

    if alarm_id is not None or severity is not None or mo_dn is not None or \
       alarm_group_id is not None or dc_id is not None or product_name is not None or \
       alarm_name is not None or occur_utc_start is not None or occur_utc_end is not None:

        query_filters = []

        if alarm_id is not None:
            query_filters.append({
                'name': 'ALARMID',
                'field': 'alarm_id',
                'operator': 'like',
                'values': [alarm_id]
            })

        if severity is not None:
            query_filters.append({
                'name': 'SEVERITY',
                'field': 'severity',
                'operator': 'in',
                'values': severity
            })

        if mo_dn is not None:
            query_filters.append({
                'name': 'MO_DN',
                'field': 'mo_dn',
                'operator': 'inc',
                'values': [mo_dn]
            })

        if alarm_group_id is not None:
            query_filters.append({
                'name': 'ALARM_GROUP_ID',
                'field': 'alarm_group_id',
                'operator': '=',
                'values': [alarm_group_id]
            })

        if dc_id is not None:
            query_filters.append({
                'name': 'DC_ID',
                'field': 'dc_id',
                'operator': '=',
                'values': [dc_id]
            })

        if product_name is not None:
            query_filters.append({
                'name': 'PRODUCT_NAME',
                'field': 'product_name',
                'operator': 'like',
                'values': [product_name]
            })

        if alarm_name is not None:
            query_filters.append({
                'name': 'ALARM_NAME',
                'field': 'alarm_name',
                'operator': 'like',
                'values': [alarm_name]
            })

        if occur_utc_start is not None or occur_utc_end is not None:
            values = []
            if occur_utc_start is not None:
                values.append(occur_utc_start)
            if occur_utc_end is not None:
                values.append(occur_utc_end)
            if len(values) == 2:
                query_filters.append({
                    'name': 'OCCURUTC',
                    'field': 'occur_utc',
                    'operator': 'between',
                    'values': values
                })

        body_params['query'] = {'filters': query_filters}

    if fields is not None:
        body_params['fields'] = fields

    return body_params


def _build_history_alarm_params(alarm_id: str = None, severity: list = None,
                                 mo_dn: str = None, cleared: bool = None,
                                 occur_utc_start: str = None, occur_utc_end: str = None,
                                 fields: list = None, size: int = 100,
                                 iterator: str = None) -> dict:
    """构建历史告警查询参数"""
    body_params = {'size': size}

    query_filters = []

    if alarm_id is not None:
        query_filters.append({
            'name': 'ALARMID',
            'field': 'alarm_id',
            'operator': 'like',
            'values': [alarm_id]
        })

    if severity is not None:
        query_filters.append({
            'name': 'SEVERITY',
            'field': 'severity',
            'operator': 'in',
            'values': severity
        })

    if mo_dn is not None:
        query_filters.append({
            'name': 'MO_DN',
            'field': 'mo_dn',
            'operator': 'inc',
            'values': [mo_dn]
        })

    if cleared is not None:
        query_filters.append({
            'name': 'CLEARED',
            'field': 'cleared',
            'operator': '=',
            'values': ['true' if cleared else 'false']
        })

    if occur_utc_start is not None or occur_utc_end is not None:
        values = []
        if occur_utc_start is not None:
            values.append(occur_utc_start)
        if occur_utc_end is not None:
            values.append(occur_utc_end)
        if len(values) == 2:
            query_filters.append({
                'name': 'OCCURUTC',
                'field': 'occur_utc',
                'operator': 'between',
                'values': values
            })

    if query_filters:
        body_params['query_context'] = {'filters': query_filters}

    if fields is not None:
        body_params['fields'] = fields

    if iterator is not None:
        body_params['iterator'] = iterator

    return body_params


def list_alarms(client: DMEAPIClient, alarm_id: str = None, severity: list = None,
                mo_dn: str = None, alarm_group_id: str = None, dc_id: str = None,
                product_name: str = None, alarm_name: str = None,
                occur_utc_start: str = None, occur_utc_end: str = None,
                fields: list = None, page_no: int = 1, page_size: int = 100,
                cleared: bool = None, size: int = 100, iterator: str = None,
                include_history: bool = None) -> dict:
    """
    查询告警信息

    查询当前告警,可选择是否同时查询历史告警.

    Args:
        client: DME API 客户端
        alarm_id: 告警 ID,支持模糊匹配
        severity: 告警级别列表,取值:critical, major, minor, warning, indeterminate, cleared
        mo_dn: 被管理对象 DN,支持 inc 操作符匹配
        alarm_group_id: 告警组 ID
        dc_id: 数据中心 ID
        product_name: 产品名称
        alarm_name: 告警名称,支持模糊匹配
        occur_utc_start: 告警发生开始时间(毫秒时间戳)
        occur_utc_end: 告警发生结束时间(毫秒时间戳)
        fields: 指定返回的字段列表
        page_no: 分页查询的起始页码,默认 1
        page_size: 每页数量,1~1000,默认 100(当前告警查询用)
        cleared: 是否已清除,true/false(历史告警查询用)
        size: 返回的结果集最大条数,1~1000,默认 100(历史告警查询用)
        iterator: 迭代子,首次查询无需传入,后续查询使用上次返回的 iterator(历史告警查询用)
        include_history: 开关参数,指定则同时查询历史告警

    Returns:
        响应数据,包含告警列表
    """
    result = {
        'current_alarms': None,
        'history_alarms': None
    }

    # 查询当前告警(默认总是查询)
    current_url = "/rest/alarmmgmt/v1/alarms/current-alarm/query"
    current_params = _build_current_alarm_params(
        alarm_id=alarm_id, severity=severity, mo_dn=mo_dn,
        alarm_group_id=alarm_group_id, dc_id=dc_id, product_name=product_name,
        alarm_name=alarm_name, occur_utc_start=occur_utc_start,
        occur_utc_end=occur_utc_end, fields=fields, page_size=page_size
    )

    current_response = client.post(current_url, json=current_params)
    result['current_alarms'] = current_response

    # 如果指定了 include_history,同时查询历史告警
    if include_history:
        history_url = "/rest/alarmmgmt/v1/alarms/history-alarms/query"
        history_params = _build_history_alarm_params(
            alarm_id=alarm_id, severity=severity, mo_dn=mo_dn,
            cleared=cleared, occur_utc_start=occur_utc_start,
            occur_utc_end=occur_utc_end, fields=fields, size=size,
            iterator=iterator
        )

        history_response = client.post(history_url, json=history_params)
        result['history_alarms'] = history_response

    return result


def ack(client: DMEAPIClient, csns: list) -> dict:
    r"""
    确认告警

    对指定告警执行确认 (ACK) 操作.

    Args:
        client: DME API 客户端
        csns: 告警流水号列表(必选),最多 30 个

    Returns:
        操作结果
    """
    url = "/rest/alarmmgmt/v1/alarms/operation"

    if not isinstance(csns, list) or len(csns) < 1 or len(csns) > 30:
        raise ValueError("csns 必须是包含 1-30 个元素的列表")

    payload = {
        "csns": csns,
        "operation_type": "ACK"
    }

    print(f"请求 URL: {url}")
    print(f"请求负载:{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def unack(client: DMEAPIClient, csns: list) -> dict:
    r"""
    取消确认告警

    对指定告警执行取消确认 (UNACK) 操作.

    Args:
        client: DME API 客户端
        csns: 告警流水号列表(必选),最多 30 个

    Returns:
        操作结果
    """
    url = "/rest/alarmmgmt/v1/alarms/operation"

    if not isinstance(csns, list) or len(csns) < 1 or len(csns) > 30:
        raise ValueError("csns 必须是包含 1-30 个元素的列表")

    payload = {
        "csns": csns,
        "operation_type": "UNACK"
    }

    print(f"请求 URL: {url}")
    print(f"请求负载:{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def clear(client: DMEAPIClient, csns: list) -> dict:
    r"""
    清除告警

    对指定告警执行清除 (CLEAR) 操作.

    Args:
        client: DME API 客户端
        csns: 告警流水号列表(必选),最多 30 个

    Returns:
        操作结果
    """
    url = "/rest/alarmmgmt/v1/alarms/operation"

    if not isinstance(csns, list) or len(csns) < 1 or len(csns) > 30:
        raise ValueError("csns 必须是包含 1-30 个元素的列表")

    payload = {
        "csns": csns,
        "operation_type": "CLEAR"
    }

    print(f"请求 URL: {url}")
    print(f"请求负载:{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def diagnose_task_create(client: DMEAPIClient, object_ids: list, object_type: str,
                         begin_time: int, end_time: int, analysis_types: list) -> dict:
    r"""
    创建智能分析任务

    创建智能分析任务,支持多种分析类型.

    Args:
        client: DME API 客户端
        object_ids: 入口分析对象 ID 列表(必选),数组大小:1~50
        object_type: 入口对象类型(必选),取值范围:
            - VM: 虚拟机
            - STORAGE_HOST: 存储主机
            - STORAGE_DEVICE: 存储设备
            - LUN: LUN
            - FILE_SYSTEM: 文件系统
            - VBS_CLIENT: VBS 客户端
            - DATATURBO: 并行客户端
            - STORAGE_POOL: 存储池
            - IP_CLIENT: IP 客户端
            - HOST_GROUP: 存储主机组
            - FC_PORT: FC 端口
            - ETH_PORT: 以太端口
            - LUN_GROUP: LUN 组
            - LOGIC_PORT: 逻辑端口
            - CONTROLLER: 控制器
            - NAMESPACE: 命名空间
        begin_time: 分析开始时间(必选),Unix 时间戳(毫秒),必须为整分钟时间点,支持最近七天内的诊断
        end_time: 分析结束时间(必选),Unix 时间戳(毫秒),必须为整分钟时间点
                  分析时间间隔范围必须大于 30 分钟,小于 24 小时
        analysis_types: 智能分析类型列表(必选),数组大小:1~4,取值范围:
            - highLatency: 高时延
            - healthAnalysis: 健康快检
            - IOInterrupt: IO 中断
            - highReadLatency: 高读时延
            - highWriteLatency: 高写时延
            - trafficAnalysis: 流量分析


    """

# ============ Performance 性能监控子主题函数 ============


def create_collect_task(client: DMEAPIClient, begin_time: int, end_time: int,
                        object_type_id: str, object_ids: list,
                        indicator_ids: list) -> dict:
    """
    创建性能文件收集任务

    收集范围为开始日期到结束日期的性能文件,只支持收集 7 天内的数据,
    每次传入的对象乘以指标数不超过 2000.

    Args:
        client: DME API 客户端
        begin_time: 开始时间(必填,Unix 时间戳毫秒)
        end_time: 结束时间(必填,Unix 时间戳毫秒)
        object_type_id: 对象类型 ID(必填,1~32 个字符)
        object_ids: 对象 ID 列表(必填,最多 2000 个,ID 长度 1~32 位)
        indicator_ids: 指标 ID 列表(必填,最多 20 个,ID 长度 1~16 位)

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


def download_collect_result(client: DMEAPIClient, task_id: str) -> dict:
    """
    下载性能文件

    Args:
        client: DME API 客户端
        task_id: 任务 ID(必填)

    Returns:
        性能文件下载链接或文件内容
    """
    url = f"/rest/pmmgmt/v1/performance-data/download/{task_id}"

    response = client.get(url)
    return response


def query(client: DMEAPIClient, obj_type_id: int, indicator_ids: list,
          obj_ids: list, obj_type: str = None, indicators: list = None,
          ext_dimensions: list = None, interval: str = None,
          range: str = None, begin_time: int = None,
          end_time: int = None) -> dict:
    """
    查询历史性能数据

    根据传入参数中的"range"字段所取的枚举值或从开始到结束时间范围内的查询数据.
    有汇聚数据情况下,返回结果序列是平均值序列,并包含最大值,最小值以及对应时间戳.

    使用说明:
    - 对象类型和指标定义:从性能指标模型文档获取 (reference/dme_performance_model/index.md)
    - 对象 ID (CMDB 实例 ID) 获取步骤:
      1. 运行 `cmdb instance list --help` 查看帮助,了解类定义和查询方式
      2. 根据帮助信息,从 CMDB 资源模型中确定要查询的资源类型 (Class 名称)
      3. 使用 `cmdb instance list --class_name <Class 名称>` 查询实例列表
      4. 从返回结果中获取对应资源的 instance_id (即 obj_ids 参数)

    Args:
        client: DME API 客户端
        obj_type_id: 监控对象类型标识(必填),对应监控对象类型 ID
                     从性能指标模型文档获取:reference/dme_performance_model/index.md
        indicator_ids: 监控指标标识列表(必填,最多 100 个),对应指标 ID
                       从性能指标模型文档获取:reference/dme_performance_model/index.md
        obj_ids: 监控对象标识列表(必填,最多 512 个),对应 CMDB 实例 ID
                 获取方式:
                 1. 运行 `cmdb instance list --help` 查看帮助,了解类定义
                 2. 根据帮助确定要查询的资源类型 (Class 名称)
                 3. 运行 `cmdb instance list --class_name <Class 名称>` 查询实例
                 4. 从返回结果中获取 instance_id
        obj_type: 监控对象类型(可选,1~512 个字符)
        indicators: 监控指标列表(可选,最多 100 个)
        ext_dimensions: 扩展维度信息列表(可选,最多 100 个)
        interval: 间隔粒度(可选)
                  取值范围:ONE_MINUTE(1 分钟), MINUTE(5 分钟), HALF_HOUR(30 分钟),
                  HOUR(1 小时), DAY(1 天), WEEK(1 周), MONTH(1 个月)
        range: 时间范围(可选,默认 LAST_1_HOUR)
               取值范围:LAST_5_MINUTE(最近 5 分钟), LAST_1_HOUR(最近 1 小时),
               LAST_1_DAY(最近 1 天), LAST_1_WEEK(最近 1 周), LAST_1_MONTH(最近 1 个月),
               LAST_1_QUARTER(最近 3 个月), HALF_1_YEAR(最近半年), LAST_1_YEAR(最近 1 年),
               BEGIN_END_TIME(自行设置开始和结束时间), INVALID(无效值)
        begin_time: 查询开始时刻(可选),仅 range 为 BEGIN_END_TIME 时生效,必须比 end_time 小
        end_time: 查询结束时刻(可选),仅 range 为 BEGIN_END_TIME 时生效,必须比 begin_time 大

    Returns:
        历史性能数据,包含 status_code, error_code, error_msg, data
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


def show_indicators(client: DMEAPIClient, obj_type_id: int) -> dict:
    """
    获取监控对象类型支持的监控指标

    Args:
        client: DME API 客户端
        obj_type_id: 监控对象类型标识(必填)

    Returns:
        监控指标信息,包含 indicator_ids 列表
    """
    url = f"/rest/metrics/v1/mgr-svc/obj-types/{obj_type_id}/indicators"

    response = client.get(url)
    return response


def list_indicators(client: DMEAPIClient, indicators: list) -> dict:
    """
    获取监控指标

    Args:
        client: DME API 客户端
        indicators: 监控对象指标标识列表(必填,最多 1000 个字符)
                   可以是整数列表或字符串列表,如 [123, 456] 或 ["123", "456"]

    Returns:
        监控指标信息,包含 kpi, data_type, data_unit, en_us, zh_cn 等字段
    """
    url = "/rest/metrics/v1/mgr-svc/indicators"

    # 确保 indicators 是整数列表
    if indicators:
        indicators = [int(i) for i in indicators]

    # API 要求直接传递数组,而不是对象
    response = client.post(url, json=indicators)
    return response


def list_object_types(client: DMEAPIClient, filter: str = None) -> dict:
    """
    获取所有监控对象类型

    Args:
        client: DME API 客户端
        filter: 过滤关键字(可选),用于模糊匹配 zh_cn 和 en_us 字段
                如果提供,仅返回匹配的对象类型

    Returns:
        监控对象类型列表,包含 obj_type_id, parent_obj_type_id, resource_category,
        resource_provider, en_us, zh_cn, group_en_us, group_zh_cn 等字段
    """
    url = "/rest/metrics/v1/mgr-svc/obj-types"

    response = client.get(url)

    # 如果提供了 filter 参数,过滤结果
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



# ============ Performance 性能监控子主题函数 ============




def diagnose_task_status(client: DMEAPIClient, task_id: str) -> dict:
    r"""
    查询性能诊断任务状态

    根据任务 ID 查询诊断任务状态.

    Args:
        client: DME API 客户端
        task_id: 任务 ID(必选),1~128 个字符

    Returns:
        响应数据,包含:
        - task_id: 任务 ID
        - task_status: 任务状态,取值范围:
            - executing: 执行中
            - failed: 失败
            - success: 成功
            - waiting: 等待
            - terminated: 已终止
        - task_result: 任务结果,取值范围:
            - un_analyzed: 未分析
            - warning: 警告
            - abnormal: 异常
            - event: 事件
        - total_step_count: 总步骤数
        - finish_step_count: 已完成步骤数
    """
    url = "/rest/dmegraphanalysis/v1/perf-tasks/query-status"

    payload = {
        "task_id": task_id
    }

    print(f"请求 URL: {url}")
    print(f"请求负载:{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


ACTIONS = {
    'alarm_list': {
        'func': list_alarms,
        'description': '查询告警信息(当前告警,可选择是否包含历史告警)',
        'params': ['alarm_id', 'severity', 'mo_dn', 'alarm_group_id', 'dc_id',
                   'product_name', 'alarm_name', 'occur_utc_start', 'occur_utc_end',
                   'fields', 'page_no', 'page_size', 'cleared', 'size', 'iterator', 'include_history'],
        'subtopic': 'alarm'
    },
    'alarm_ack': {
        'func': ack,
        'description': '确认告警',
        'params': ['csns'],
        'subtopic': 'alarm'
    },
    'alarm_unack': {
        'func': unack,
        'description': '取消确认告警',
        'params': ['csns'],
        'subtopic': 'alarm'
    },
    'alarm_clear': {
        'func': clear,
        'description': '清除告警',
        'params': ['csns'],
        'subtopic': 'alarm'
    },
    'diagnose_task_status': {
        'func': diagnose_task_status,
        'description': '查询性能诊断任务状态',
        'params': ['task_id'],
        'subtopic': 'diagnose_task'
    },
    # performance 子主题动作
    'performance_create_collect_task': {
        'func': create_collect_task,
        'description': '创建性能文件收集任务',
        'params': ['begin_time', 'end_time', 'object_type_id', 'object_ids', 'indicator_ids'],
        'subtopic': 'performance'
    },
    'performance_download_collect_result': {
        'func': download_collect_result,
        'description': '下载性能文件',
        'params': ['task_id'],
        'subtopic': 'performance'
    },
    'performance_query': {
        'func': query,
        'description': '查询历史性能数据',
        'params': ['obj_type_id', 'indicator_ids', 'obj_ids', 'obj_type', 'indicators', 'ext_dimensions', 'interval', 'range', 'begin_time', 'end_time'],
        'subtopic': 'performance'
    },
    'performance_show_indicators': {
        'func': show_indicators,
        'description': '获取监控对象类型支持的监控指标',
        'params': ['obj_type_id'],
        'subtopic': 'performance'
    },
    'performance_list_indicators': {
        'func': list_indicators,
        'description': '获取监控指标',
        'params': ['indicators'],
        'subtopic': 'performance'
    },
    'performance_list_object_types': {
        'func': list_object_types,
        'description': '获取所有监控对象类型',
        'params': ['filter'],
        'subtopic': 'performance'
    }
}
