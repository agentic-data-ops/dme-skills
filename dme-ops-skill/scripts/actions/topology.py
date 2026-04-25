"""
拓扑管理 (Topology) 相关操作
"""

import sys
import os
import json

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def query_luns(client: DMEAPIClient, entry_objects: list, storage_pool_id: str,
               lun_name: str = None, san_type: str = None, page_size: int = 20, page_no: int = 1) -> dict:
    r"""
    查询拓扑图 Lun 列表

    根据指定入口对象查询拓扑图中的 LUN 列表。

    Args:
        client: DME API 客户端
        entry_objects: 入口对象列表（必选），支持类型：
            - host: 主机
            - storage: 存储设备
            - host_group: 主机组
            - lun: LUN
            - vm: 虚拟机
            - datastore: 数据存储
            - application: 应用
            - switch_port: 交换机端口
            - storage_pool: 存储池
        storage_pool_id: 存储池 ID（必选）
        lun_name: LUN 名称，支持模糊匹配
        san_type: SAN 类型，可选值：ip_san, fc_san
        page_size: 分页查询的个数，1~20，默认 20
        page_no: 分页查询的起始位置，默认 1

    Returns:
        响应数据，包含 LUN 拓扑列表
    """
    url = "/rest/topomgmt/v1/topo-data/luns/query"

    payload = {
        "entry_objects": entry_objects,
        "storage_pool_id": storage_pool_id
    }

    if lun_name is not None:
        payload["lun_name"] = lun_name

    if san_type is not None:
        payload["san_type"] = san_type

    if page_size is not None:
        payload["page_size"] = page_size

    if page_no is not None:
        payload["page_no"] = page_no

    print(f"请求 URL: {url}")
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def query_san_path(client: DMEAPIClient, entry_objects: list, san_type: str = None) -> dict:
    r"""
    查询 SAN 路径拓扑结构

    根据指定入口对象查询 SAN 网络中从主机到存储池之间的拓扑结构。
    支持 IP_SAN 和 FC_SAN 两种类型。

    Args:
        client: DME API 客户端
        entry_objects: 入口对象列表（必选），支持类型：
            - host: 主机
            - storage: 存储设备
            - lun: LUN
            - host_group: 主机组
            - vm: 虚拟机
            - datastore: 数据存储（仅 FC_SAN）
            - application: 应用（仅 FC_SAN）
            - switch_port: 交换机端口（仅 FC_SAN）
            - storage_pool: 存储池
        san_type: SAN 类型（可选），可选值：ip_san, fc_san
                  - 不指定时，同时调用 IP_SAN 和 FC_SAN 两个 API，组合返回数据
                  - 指定为 ip_san 时，仅调用 IP_SAN API
                  - 指定为 fc_san 时，仅调用 FC_SAN API

    Returns:
        响应数据，包含主机到存储池的拓扑结构：
        - ip_san 数据：
          - switches: 交换机列表
          - hosts: 主机列表
          - storages: 存储列表
          - switch_links: 交换机连接关系列表
          - port_links: 端口连接关系列表
        - fc_san 数据：
          - fabrics: fabric 列表
          - hosts: 主机列表
          - storages: 存储列表
    """
    result = {}

    # 如果未指定 san_type，同时调用两个 API
    if san_type is None:
        # 调用 IP_SAN API
        ip_san_url = "/rest/topomgmt/v1/topo-data/ipsan/host-storage/query"
        ip_san_payload = {"entry_objects": entry_objects}
        print(f"请求 URL: {ip_san_url}")
        print(f"请求负载：{json.dumps(ip_san_payload, ensure_ascii=False, indent=2)}")
        ip_san_response = client.post(ip_san_url, json=ip_san_payload)
        result['ip_san'] = ip_san_response

        # 调用 FC_SAN API
        fc_san_url = "/rest/topomgmt/v1/topo-data/host-storage/query"
        fc_san_payload = {"entry_objects": entry_objects}
        print(f"请求 URL: {fc_san_url}")
        print(f"请求负载：{json.dumps(fc_san_payload, ensure_ascii=False, indent=2)}")
        fc_san_response = client.post(fc_san_url, json=fc_san_payload)
        result['fc_san'] = fc_san_response

        return result

    # 如果指定了 san_type，只调用对应的 API
    elif san_type == 'ip_san':
        url = "/rest/topomgmt/v1/topo-data/ipsan/host-storage/query"
        payload = {"entry_objects": entry_objects}
        print(f"请求 URL: {url}")
        print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = client.post(url, json=payload)
        return response

    elif san_type == 'fc_san':
        url = "/rest/topomgmt/v1/topo-data/host-storage/query"
        payload = {"entry_objects": entry_objects}
        print(f"请求 URL: {url}")
        print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = client.post(url, json=payload)
        return response

    else:
        raise ValueError(f"无效的 san_type 参数：{san_type}，仅支持：ip_san, fc_san")


def ipsan_query(client: DMEAPIClient, entry_objects: list) -> dict:
    r"""
    查询 IP_SAN 网络从主机到存储池间的拓扑结构

    根据指定入口对象查询 IP_SAN 网络中从主机到存储池之间的拓扑结构。

    Args:
        client: DME API 客户端
        entry_objects: 入口对象列表（必选），支持类型：
            - host: 主机
            - storage: 存储设备
            - lun: LUN
            - host_group: 主机组
            - vm: 虚拟机
            - storage_pool: 存储池

    Returns:
        响应数据，包含主机到存储池的拓扑结构，包括：
        - switches: 交换机列表
        - hosts: 主机列表
        - storages: 存储列表
        - switch_links: 交换机连接关系列表
        - port_links: 端口连接关系列表
    """
    url = "/rest/topomgmt/v1/topo-data/ipsan/host-storage/query"

    payload = {
        "entry_objects": entry_objects
    }

    print(f"请求 URL: {url}")
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def fcsan_query(client: DMEAPIClient, entry_objects: list) -> dict:
    r"""
    查询 FC_SAN 网络从主机到存储池间的拓扑结构

    根据指定入口对象查询 FC_SAN 网络中从主机到存储池之间的拓扑结构。

    Args:
        client: DME API 客户端
        entry_objects: 入口对象列表（必选），支持类型：
            - host: 主机
            - storage: 存储设备
            - lun: LUN
            - host_group: 主机组
            - vm: 虚拟机
            - datastore: 数据存储
            - application: 应用
            - switch_port: 交换机端口
            - storage_pool: 存储池

    Returns:
        响应数据，包含主机到存储池的拓扑结构，包括：
        - fabrics: fabric 列表
        - hosts: 主机列表
        - storages: 存储列表
    """
    url = "/rest/topomgmt/v1/topo-data/host-storage/query"

    payload = {
        "entry_objects": entry_objects
    }

    print(f"请求 URL: {url}")
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def query_vms(client: DMEAPIClient, entry_objects: list, host_id: str,
              vm_name: str = None, page_size: int = 20, page_no: int = 1) -> dict:
    r"""
    查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表

    根据指定入口对象查询虚拟化资源，包括虚拟机和虚拟磁盘列表，
    或者查询 BMS（裸金属服务器）下的物理磁盘列表。

    Args:
        client: DME API 客户端
        entry_objects: 入口对象列表（必选），支持类型：
            - vm: 虚拟机
            - host_group: 主机组
            - host: 主机
            - storage: 存储设备
            - lun: LUN
            - datastore: 数据存储
            - switch_port: 交换机端口
            - storage_pool: 存储池
        host_id: 主机 ID（必选）
        vm_name: 虚拟机名称搜索参数，支持模糊匹配
        page_size: 分页查询的个数，1~20，默认 20
        page_no: 分页查询的起始位置，默认 1

    Returns:
        响应数据，包含：
        - total: 查询结果总数
        - vms: 虚拟机列表
        - disks: 物理主机关联的物理磁盘列表
    """
    url = "/rest/topomgmt/v1/topo-data/vms/query"

    payload = {
        "entry_objects": entry_objects,
        "host_id": host_id
    }

    if vm_name is not None:
        payload["vm_name"] = vm_name

    if page_size is not None:
        payload["page_size"] = page_size

    if page_no is not None:
        payload["page_no"] = page_no

    print(f"请求 URL: {url}")
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


def graph_query(client: DMEAPIClient, entry_res_type: str, entry_res_id: str,
                type: str = None, filter: list = None) -> dict:
    r"""
    查询拓扑图库信息

    根据指定入口资源查询拓扑图库信息，支持 NAS、K8s、DB 等业务类型。

    Args:
        client: DME API 客户端
        entry_res_type: 入口资源类型（必选），支持类型：
            - storage_device: 存储设备
            - disk: 磁盘
            - storage_pool: 存储池
            - hyper_scale_pool: 超大规模池
            - file_system: 文件系统
            - controller: 控制器
            - eth_port: 以太网端口
            - ib_port: InfiniBand 端口
            - logic_port: 逻辑端口
            - ip_client: IP 客户端
            - dtree: Dtree
            - lun: LUN
            - k8s_application: K8s 应用
            - k8s_workload: K8s 工作负载
            - k8s_pod: K8s Pod
            - k8s_pvc: K8s PVC
            - k8s_pv: K8s PV
            - k8s_cluster: K8s 集群
            - k8s_node: K8s 节点
            - k8s_vc_job: K8s VC 任务
            - dturbo_client: DataTurbo 客户端
            - enclosures: 机柜
            - eth_switch: 以太网交换机
            - storage_zone: 存储区域
            - service_network: 服务网络
            - db_instance: 数据库实例
            - db_node: 数据库节点
        entry_res_id: 入口资源 ID（必选）
        type: 业务类型，可选值：nas, k8s, db
        filter: 过滤条件列表，最多 10 个

    Returns:
        响应数据，包含：
        - nodes: 节点列表，每个节点包含 id, type, label, sub_type
        - edges: 边列表，每条边包含 source, target, edge_type
    """
    url = "/rest/dmegraphanalysis/v1/topo-data/query"

    payload = {
        "entry_res_type": entry_res_type,
        "entry_res_id": entry_res_id
    }

    if type is not None:
        payload["type"] = type

    if filter is not None:
        payload["filter"] = filter

    print(f"请求 URL: {url}")
    print(f"请求负载：{json.dumps(payload, ensure_ascii=False, indent=2)}")

    response = client.post(url, json=payload)
    return response


ACTIONS = {
    'query_san_path': {
        'func': query_san_path,
        'description': '查询 SAN 路径拓扑结构（支持 IP_SAN 和 FC_SAN）',
        'params': ['entry_objects', 'san_type'],
        'subtopic': None
    },
    'query_luns': {
        'func': query_luns,
        'description': '查询拓扑图 LUN 列表',
        'params': ['entry_objects', 'storage_pool_id', 'lun_name', 'san_type', 'page_size', 'page_no'],
        'subtopic': None
    },
    'query_vms': {
        'func': query_vms,
        'description': '查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表',
        'params': ['entry_objects', 'host_id', 'vm_name', 'page_size', 'page_no'],
        'subtopic': None
    },
    'query_graph_path': {
        'func': graph_query,
        'description': '查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）',
        'params': ['entry_res_type', 'entry_res_id', 'type', 'filter'],
        'subtopic': None
    },
    'lun_list': {
        'func': query_luns,
        'description': '查询拓扑图 LUN 列表',
        'params': ['entry_objects', 'storage_pool_id', 'lun_name', 'san_type', 'page_size', 'page_no'],
        'subtopic': 'lun'
    },
    'ipsan_query': {
        'func': ipsan_query,
        'description': '查询 IP_SAN 网络从主机到存储池间的拓扑结构',
        'params': ['entry_objects'],
        'subtopic': 'ipsan'
    },
    'fcsan_query': {
        'func': fcsan_query,
        'description': '查询 FC_SAN 网络从主机到存储池间的拓扑结构',
        'params': ['entry_objects'],
        'subtopic': 'fcsan'
    },
    'vm_list': {
        'func': query_vms,
        'description': '查询拓扑图虚拟机和虚拟磁盘列表，或查询 BMS 下物理磁盘列表',
        'params': ['entry_objects', 'host_id', 'vm_name', 'page_size', 'page_no'],
        'subtopic': 'vm'
    },
    'graph_query': {
        'func': graph_query,
        'description': '查询拓扑图库信息（支持 NAS、K8s、DB 等业务类型）',
        'params': ['entry_res_type', 'entry_res_id', 'type', 'filter'],
        'subtopic': 'graph'
    }
}
