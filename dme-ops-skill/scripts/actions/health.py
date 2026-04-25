"""
健康度 (Health) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def object_health(client: DMEAPIClient, object_type: str, object_name: str = None,
                  object_ids: list = None, page_no: int = None, page_size: int = None,
                  sort_key: str = None, sort_dir: str = None) -> dict:
    """
    查询对象健康度
    
    查询指定类型对象的健康度信息。
    
    Args:
        client: DME API 客户端
        object_type: 对象类型（必选）
                    可选值：storage（存储设备）, storage_pool（存储池）, storage_host（存储主机）,
                           storage_disk（硬盘）, storage_port（存储端口）, fcswitch_port（光纤交换机端口）,
                           storage_file_system（文件系统）, controller（控制器）, replication_cg（远程复制一致性组）,
                           volume（LUN）, tier（服务等级）, datastore（数据存储）, virtual_machine（虚拟机）,
                           storage_name_space（命名空间）, storage_node（存储节点）, dpc（并行客户端）
        object_name: 对象名称，支持模糊查询（可选，最多 256 个字符）
        object_ids: 对象 resId 列表，用于批量精确查找（可选，最多支持 100 个 ID）
        page_no: 分页查询的起始位置（可选，最小值：1）
        page_size: 每页显示的数量（可选，1~100，默认 20）
        sort_key: 排序字段（可选），按分数进行排序，可选值：health_score
        sort_dir: 排序方式（可选），可选值：asc, desc
    
    Returns:
        响应数据，包含：
        - total: 对象总数
        - objects: 对象列表，包含 object_id, object_type, object_name, is_distributed,
                  health_score, dimension_scores 等
    """
    url = "/rest/healthmgmt/v1/health-result/query"
    
    payload = {
        'object_type': object_type
    }
    
    if object_name is not None:
        payload['object_name'] = object_name
    if object_ids is not None:
        payload['object_ids'] = object_ids
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    
    response = client.post(url, json=payload)
    return response


def dimension_score(client: DMEAPIClient, object_id: str, object_type: str,
                    health_dimension: str) -> dict:
    """
    查询健康维度的扣分详情
    
    查询指定对象在指定健康维度下的扣分详情。
    
    Args:
        client: DME API 客户端
        object_id: 对象 Id（必选，1~128 个字符）
        object_type: 对象类型（必选）
                    可选值：storage, storage_pool, storage_host, storage_disk, storage_port,
                           fcswitch_port, storage_file_system, controller, replication_cg, volume,
                           tier, datastore, virtual_machine, storage_name_space, storage_node,
                           dpc, gfs, dpc_client, vbs_client
        health_dimension: 健康维度（必选）
                        可选值：alarm（告警）, performance_anomaly（性能异常）,
                              performance_prediction（性能预警）, capacity_prediction（容量预警）
    
    Returns:
        响应数据，包含：
        - indicators: 指标扣分列表，包含 indicator（指标名）, deduct_score（扣分数）,
                     last_check_time（最近一次检查时间）
    """
    url = "/rest/healthmgmt/v1/health-result/dimension-score/query"
    
    payload = {
        'object_id': object_id,
        'object_type': object_type,
        'health_dimension': health_dimension
    }
    
    response = client.post(url, json=payload)
    return response


def performance_anomaly(client: DMEAPIClient, object_id: str, object_type: str,
                        indicator: str, begin_time: int, end_time: int) -> dict:
    """
    查询性能异常检查数据
    
    查询性能异常数据，返回的异常检测数据包括推理上下限数据以及当前指标的实际值。
    
    Args:
        client: DME API 客户端
        object_id: 对象 id（必选，1~128 个字符）
        object_type: 对象类型（必选）
                    可选值：storage_host, controller, storage_file_system, replication_cg,
                           fcswitch_port, storage_node, storage_name_space, volume,
                           storage_disk, storage_pool, storage_port, storage
        indicator: 指标名（必选，1~64 个字符）
        begin_time: 开始时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
        end_time: 结束时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
    
    Returns:
        响应数据，包含：
        - data: 性能异常数据列表，包含 timestamp, warning_upper, warning_lower,
               critical_upper, critical_lower, actual
    """
    url = "/rest/metrics/v1/performance/anomaly-data/query"
    
    payload = {
        'object_id': object_id,
        'object_type': object_type,
        'indicator': indicator,
        'begin_time': begin_time,
        'end_time': end_time
    }
    
    response = client.post(url, json=payload)
    return response


def performance_predict(client: DMEAPIClient, object_id: str, begin_time: int,
                        end_time: int, object_type: str, indicator: str) -> dict:
    """
    获取性能预测数据
    
    获取最近一次预测结果的指定时间段内的历史趋势数据和预测数据。
    
    Args:
        client: DME API 客户端
        object_id: 资源 ID（必选，1~256 个字符）
        begin_time: 开始时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
        end_time: 结束时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
        object_type: 对象类型（必选）
                    可选值：storage, storage_pool, storage_host, storage_disk, storage_port,
                           fcswitch_port, storage_file_system, controller, replication_cg,
                           storage_node, storage_name_space, dpc, gfs, dpc_client, vbs_client
        indicator: 资源类型所对应的指标（必选，1~64 个字符）
                  storage: cpuUsage, throughput, bandwidth
                  storage_pool: throughput, bandwidth
                  storage_host: throughput, bandwidth, responseTime, readResponseTime, writeResponseTime
                  storage_disk: utility, throughput, bandwidth, responseTime
                  storage_port: utility, throughput, bandwidth, responseTime, readResponseTime, writeResponseTime, serviceTime
                  fcswitch_port: utility, utilityRx, utilityTx, bandwidth, bandwidthRx, bandwidthTx
                  storage_file_system: serviceTime, throughput, bandwidth, readResponseTime, writeResponseTime
                  controller: writeCacheUsage, blockBandwidth, fileBandwidth, throughput, cpuUsage
                  replication_cg: syncDuration
                  storage_node, storage_name_space, dpc, gfs, dpc_client, vbs_client: 根据具体类型确定
    
    Returns:
        响应数据，包含：
        - data: 查询结果，包含 history（历史数据）和 forecast（预测数据）
               每个数据项包含 timestamp 和 value
    """
    url = "/rest/pmmgmt/v1/prediction/query-performance-predict"
    
    payload = {
        'object_id': object_id,
        'begin_time': begin_time,
        'end_time': end_time,
        'object_type': object_type,
        'indicator': indicator
    }
    
    response = client.post(url, json=payload)
    return response


def data_query(client: DMEAPIClient, type: str, object_id: str, begin_time: int,
               end_time: int, object_type: str, indicator: str = None) -> dict:
    """
    查询健康度相关数据

    查询容量预测、性能预测、性能异常等健康度相关数据。

    Args:
        client: DME API 客户端
        type: 数据类型（必选），可选值：capacity_prediction（容量预测）, performance_prediction（性能预测）, performance_anomaly（性能异常）
        object_id: 资源 ID（必选，1~256 个字符）
        begin_time: 开始时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
        end_time: 结束时间（必选），自 1970 年 1 月 1 日（00:00:00GMT）至当前时间的毫秒数
        object_type: 资源类型（必选）
        indicator: 资源类型所对应的指标（capacity_prediction 和 performance_prediction 必选）

    Returns:
        响应数据，包含查询结果
    """
    if type == 'capacity_prediction':
        url = "/rest/pmmgmt/v1/prediction/query-capacity-predict"
    elif type == 'performance_prediction' or type == 'performance_predict':
        url = "/rest/pmmgmt/v1/prediction/query-performance-predict"
    elif type == 'performance_anomaly':
        url = "/rest/metrics/v1/performance/anomaly-data/query"
    else:
        raise ValueError(f"不支持的 type 参数：{type}")

    payload = {
        'object_id': object_id,
        'begin_time': begin_time,
        'end_time': end_time,
        'object_type': object_type
    }

    if indicator is not None:
        payload['indicator'] = indicator

    response = client.post(url, json=payload)
    return response


def score_list(client: DMEAPIClient, object_type: str, object_name: str = None,
               object_ids: list = None, page_no: int = None, page_size: int = None,
               sort_key: str = None, sort_dir: str = None) -> dict:
    """
    查询对象健康度

    查询指定类型对象的健康度信息。

    Args:
        client: DME API 客户端
        object_type: 对象类型（必选）
                    可选值：storage（存储设备）, storage_pool（存储池）, storage_host（存储主机）,
                           storage_disk（硬盘）, storage_port（存储端口）, fcswitch_port（光纤交换机端口）,
                           storage_file_system（文件系统）, controller（控制器）, replication_cg（远程复制一致性组）,
                           volume（LUN）, tier（服务等级）, datastore（数据存储）, virtual_machine（虚拟机）,
                           storage_name_space（命名空间）, storage_node（存储节点）, dpc（并行客户端）
        object_name: 对象名称，支持模糊查询（可选，最多 256 个字符）
        object_ids: 对象 resId 列表，用于批量精确查找（可选，最多 100 个 ID）
        page_no: 分页查询的起始位置（可选，最小值：1）
        page_size: 每页显示的数量（可选，1~100，默认 20）
        sort_key: 排序字段（可选），按分数进行排序，可选值：health_score
        sort_dir: 排序方式（可选），可选值：asc, desc

    Returns:
        响应数据，包含对象健康度列表
    """
    url = "/rest/healthmgmt/v1/health-result/query"

    payload = {
        'object_type': object_type
    }

    if object_name is not None:
        payload['object_name'] = object_name
    if object_ids is not None:
        payload['object_ids'] = object_ids
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir

    response = client.post(url, json=payload)
    return response


def score_detail(client: DMEAPIClient, object_id: str, object_type: str,
                 health_dimension: str) -> dict:
    """
    查询健康维度的扣分详情

    查询指定对象在指定健康维度下的扣分详情。

    Args:
        client: DME API 客户端
        object_id: 对象 Id（必选，1~128 个字符）
        object_type: 对象类型（必选）
                    可选值：storage, storage_pool, storage_host, storage_disk, storage_port,
                           fcswitch_port, storage_file_system, controller, replication_cg, volume,
                           tier, datastore, virtual_machine, storage_name_space, storage_node,
                           dpc, gfs, dpc_client, vbs_client
        health_dimension: 健康维度（必选）
                        可选值：alarm（告警）, performance_anomaly（性能异常）,
                              performance_prediction（性能预警）, capacity_prediction（容量预警）

    Returns:
        响应数据，包含指标扣分列表
    """
    url = "/rest/healthmgmt/v1/health-result/dimension-score/query"

    payload = {
        'object_id': object_id,
        'object_type': object_type,
        'health_dimension': health_dimension
    }

    response = client.post(url, json=payload)
    return response


# 动作注册信息
ACTIONS = {
    # data 子主题动作
    'data_query': {
        'func': data_query,
        'description': '查询健康度相关数据（容量预测/性能预测/性能异常）',
        'params': ['type', 'object_id', 'begin_time', 'end_time', 'object_type', 'indicator'],
        'subtopic': 'data'
    },
    # score 子主题动作
    'score_list': {
        'func': score_list,
        'description': '查询对象健康度',
        'params': ['object_type', 'object_name', 'object_ids', 'page_no', 'page_size', 'sort_key', 'sort_dir'],
        'subtopic': 'score'
    },
    'score_detail': {
        'func': score_detail,
        'description': '查询健康维度的扣分详情',
        'params': ['object_id', 'object_type', 'health_dimension'],
        'subtopic': 'score'
    }
}