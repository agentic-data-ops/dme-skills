"""
Kubernetes 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client.dme_api_client import DMEAPIClient


def list_clusters(client: DMEAPIClient, name: str = None,
                  page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器集群列表
    
    查询容器集群列表，支持按名称过滤和分页。
    
    Args:
        client: DME API 客户端
        name: 容器集群名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含容器集群列表
    """
    url = "/rest/dmecaasmgmt/v1/clusters/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


def list_nodes(client: DMEAPIClient, cluster_id: str = None,
               name: str = None, page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器节点列表
    
    查询容器节点列表，支持按集群 ID 和名称过滤。
    
    Args:
        client: DME API 客户端
        cluster_id: 容器集群 ID（可选）
        name: 容器节点名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含容器节点列表
    """
    url = "/rest/dmecaasmgmt/v1/nodes/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if cluster_id is not None:
        payload['cluster_id'] = cluster_id
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


def list_pods(client: DMEAPIClient, cluster_id: str = None,
              namespace: str = None, name: str = None,
              page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器组列表
    
    查询容器组（Pod）列表，支持按集群 ID、命名空间和名称过滤。
    
    Args:
        client: DME API 客户端
        cluster_id: 容器集群 ID（可选）
        namespace: 容器命名空间（可选）
        name: 容器组名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含容器组列表
    """
    url = "/rest/dmecaasmgmt/v1/pods/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if cluster_id is not None:
        payload['cluster_id'] = cluster_id
    if namespace is not None:
        payload['namespace'] = namespace
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


def list_namespaces(client: DMEAPIClient, cluster_id: str = None,
                    name: str = None, page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器命名空间列表
    
    查询容器命名空间列表，支持按集群 ID 和名称过滤。
    
    Args:
        client: DME API 客户端
        cluster_id: 容器集群 ID（可选）
        name: 命名空间名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含命名空间列表
    """
    url = "/rest/dmecaasmgmt/v1/namespaces/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if cluster_id is not None:
        payload['cluster_id'] = cluster_id
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


def list_pvcs(client: DMEAPIClient, cluster_id: str = None,
              namespace: str = None, name: str = None,
              page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器持久卷声明列表
    
    查询容器持久卷声明（PVC）列表，支持按集群 ID、命名空间和名称过滤。
    
    Args:
        client: DME API 客户端
        cluster_id: 容器集群 ID（可选）
        namespace: 容器命名空间（可选）
        name: 持久卷声明名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含持久卷声明列表
    """
    url = "/rest/dmecaasmgmt/v1/pvcs/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if cluster_id is not None:
        payload['cluster_id'] = cluster_id
    if namespace is not None:
        payload['namespace'] = namespace
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


def list_pvs(client: DMEAPIClient, cluster_id: str = None,
             name: str = None, page_no: int = 1, page_size: int = 20) -> dict:
    """
    查询容器持久卷列表
    
    查询容器持久卷（PV）列表，支持按集群 ID 和名称过滤。
    
    Args:
        client: DME API 客户端
        cluster_id: 容器集群 ID（可选）
        name: 持久卷名称（可选，支持模糊查询）
        page_no: 分页查询的起始页码，默认 1
        page_size: 每页数量，1~1000，默认 20
    
    Returns:
        响应数据，包含持久卷列表
    """
    url = "/rest/dmecaasmgmt/v1/pvs/query-list"
    
    payload = {
        'page_no': page_no,
        'page_size': page_size
    }
    
    if cluster_id is not None:
        payload['cluster_id'] = cluster_id
    if name is not None:
        payload['name'] = name
    
    response = client.post(url, body=payload)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # 集群管理
    'cluster_list': {
        'func': list_clusters,
        'description': '查询容器集群列表',
        'params': ['name', 'page_no', 'page_size'],
        'subtopic': 'cluster'
    },
    # 节点管理
    'node_list': {
        'func': list_nodes,
        'description': '查询容器节点列表',
        'params': ['cluster_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'node'
    },
    # 容器组管理
    'pod_list': {
        'func': list_pods,
        'description': '查询容器组列表',
        'params': ['cluster_id', 'namespace', 'name', 'page_no', 'page_size'],
        'subtopic': 'pod'
    },
    # 命名空间管理
    'namespace_list': {
        'func': list_namespaces,
        'description': '查询容器命名空间列表',
        'params': ['cluster_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'namespace'
    },
    # 持久卷声明管理
    'pvc_list': {
        'func': list_pvcs,
        'description': '查询容器持久卷声明列表',
        'params': ['cluster_id', 'namespace', 'name', 'page_no', 'page_size'],
        'subtopic': 'pvc'
    },
    # 持久卷管理
    'pv_list': {
        'func': list_pvs,
        'description': '查询容器持久卷列表',
        'params': ['cluster_id', 'name', 'page_no', 'page_size'],
        'subtopic': 'pv'
    },
}
