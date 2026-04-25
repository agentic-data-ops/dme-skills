"""
告警管理 (Alarm) 相关操作
"""

import sys
import os
import json
from datetime import datetime, timedelta

# 添加父目录到路径，以便导入 dme_api_client
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

    查询当前告警，可选择是否同时查询历史告警。

    Args:
        client: DME API 客户端
        alarm_id: 告警 ID，支持模糊匹配
        severity: 告警级别列表，取值：critical, major, minor, warning, indeterminate, cleared
        mo_dn: 被管理对象 DN，支持 inc 操作符匹配
        alarm_group_id: 告警组 ID
        dc_id: 数据中心 ID
        product_name: 产品名称
        alarm_name: 告警名称，支持模糊匹配
        occur_utc_start: 告警发生开始时间（毫秒时间戳）
        occur_utc_end: 告警发生结束时间（毫秒时间戳）
        fields: 指定返回的字段列表
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 100（当前告警查询用）
        cleared: 是否已清除，true/false（历史告警查询用）
        size: 返回的结果集最大条数，1~1000，默认 100（历史告警查询用）
        iterator: 迭代子，首次查询无需传入，后续查询使用上次返回的 iterator（历史告警查询用）
        include_history: 开关参数，指定则同时查询历史告警

    Returns:
        响应数据，包含告警列表
    """
    result = {
        'current_alarms': None,
        'history_alarms': None
    }

    # 查询当前告警（默认总是查询）
    current_url = "/rest/alarmmgmt/v1/alarms/current-alarm/query"
    current_params = _build_current_alarm_params(
        alarm_id=alarm_id, severity=severity, mo_dn=mo_dn,
        alarm_group_id=alarm_group_id, dc_id=dc_id, product_name=product_name,
        alarm_name=alarm_name, occur_utc_start=occur_utc_start,
        occur_utc_end=occur_utc_end, fields=fields, page_size=page_size
    )

    current_response = client.post(current_url, json=current_params)
    result['current_alarms'] = current_response

    # 如果指定了 include_history，同时查询历史告警
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

    对指定告警执行确认 (ACK) 操作。

    Args:
        client: DME API 客户端
        csns: 告警流水号列表（必选），最多 30 个

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
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def unack(client: DMEAPIClient, csns: list) -> dict:
    r"""
    取消确认告警

    对指定告警执行取消确认 (UNACK) 操作。

    Args:
        client: DME API 客户端
        csns: 告警流水号列表（必选），最多 30 个

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
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def clear(client: DMEAPIClient, csns: list) -> dict:
    r"""
    清除告警

    对指定告警执行清除 (CLEAR) 操作。

    Args:
        client: DME API 客户端
        csns: 告警流水号列表（必选），最多 30 个

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
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


ACTIONS = {
    'list': {
        'func': list_alarms,
        'description': '查询告警信息（当前告警，可选择是否包含历史告警）',
        'params': ['alarm_id', 'severity', 'mo_dn', 'alarm_group_id', 'dc_id',
                   'product_name', 'alarm_name', 'occur_utc_start', 'occur_utc_end',
                   'fields', 'page_no', 'page_size', 'cleared', 'size', 'iterator', 'include_history'],
        'subtopic': None
    },
    'ack': {
        'func': ack,
        'description': '确认告警',
        'params': ['csns'],
        'subtopic': None
    },
    'unack': {
        'func': unack,
        'description': '取消确认告警',
        'params': ['csns'],
        'subtopic': None
    },
    'clear': {
        'func': clear,
        'description': '清除告警',
        'params': ['csns'],
        'subtopic': None
    }
}
