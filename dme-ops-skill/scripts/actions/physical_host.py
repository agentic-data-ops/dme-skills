"""
物理主机管理 (Physical Host) 相关操作

物理主机用于管理连接到存储设备的服务器主机，包括接入、配置启动器、主机组管理等。
"""

import sys
import os
import json

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


def list_hosts(client: DMEAPIClient, limit: int = None, start: int = None,
               sort_key: str = None, sort_dir: str = None, name: str = None,
               host_group_name: str = None, ip: str = None,
               display_status: str = None, managed_status: list = None,
               os_type: str = None, access_mode: str = None,
               az_id: str = None, az_ids: list = None,
               project_id: str = None) -> dict:
    """
    批量查询物理主机

    批量查询物理主机列表，支持多种过滤条件和分页。

    Args:
        client: DME API 客户端
        limit: 分页查询的个数（可选，1~1000，默认无限制）
        start: 分页查询的起始位置（可选，0~10000000）
        sort_key: 排序关键字（可选，initiator_count/ip/name）
        sort_dir: 排序方式（可选，desc/asc）
        name: 物理主机名称（可选，支持模糊匹配）
        host_group_name: 物理主机组名称（可选，支持模糊匹配）
        ip: 物理主机 IP（可选，支持模糊匹配）
        display_status: 展示状态（可选，OFFLINE/NOT_RESPONDING/GRAY/NORMAL/RED/YELLOW 等）
        managed_status: 物理主机纳管状态列表（可选，UNKNOWN/NORMAL/TAKE_OVERING 等）
        os_type: 操作系统类型（可选，UNKNOWN/LINUX/WINDOWS/SUSE 等）
        access_mode: 接入方式（可选，ACCOUNT/NONE/VCENTER/FUSIONSPHERE 等）
        az_id: 可用分区 ID（可选）
        az_ids: 可用分区 ID 列表（可选，最多 40 个）
        project_id: 业务群组 ID（可选）

    Returns:
        响应数据，包含物理主机列表和总数
    """
    url = "/rest/hostmgmt/v1/hosts/summary"

    payload = {}

    if limit is not None:
        payload['limit'] = limit
    if start is not None:
        payload['start'] = start
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if name is not None:
        payload['name'] = name
    if host_group_name is not None:
        payload['host_group_name'] = host_group_name
    if ip is not None:
        payload['ip'] = ip
    if display_status is not None:
        payload['display_status'] = display_status
    if managed_status is not None:
        payload['managed_status'] = managed_status
    if os_type is not None:
        payload['os_type'] = os_type
    if access_mode is not None:
        payload['access_mode'] = access_mode
    if az_id is not None:
        payload['az_id'] = az_id
    if az_ids is not None:
        payload['az_ids'] = az_ids
    if project_id is not None:
        payload['project_id'] = project_id

    response = client.post(url, json=payload)
    return response


def show_host(client: DMEAPIClient, host_id: str) -> dict:
    """
    查询指定物理主机

    查询指定物理主机的详细信息。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）

    Returns:
        物理主机详细信息
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}/summary"

    response = client.get(url)
    return response


def create_host(client: DMEAPIClient, access_mode: str, type: str,
                host_name: str = None, ip: str = None, port: int = None,
                host_username: str = None, host_password: str = None,
                description: str = None, initiator: list = None,
                azs: list = None, project_id: str = None,
                sync_to_storage: bool = False, multipath_type: str = None,
                path_type: str = None, failover_mode: str = None,
                special_mode_type: str = None, save_public_key: bool = False) -> dict:
    """
    接入物理主机

    接入物理主机或添加逻辑主机。

    Args:
        client: DME API 客户端
        access_mode: 接入方式（必选，ACCOUNT/NONE）
        type: 主机类型（必选，UNKNOWN/LINUX/WINDOWS/SUSE/EULER 等）
        host_name: 物理主机名称（NONE 模式必选，1~255 字符）
        ip: 物理主机 IP（ACCOUNT 模式必选，支持 IPv4 和 IPv6）
        port: SSH 端口（ACCOUNT 模式必选，1~65535）
        host_username: 接入用户名（ACCOUNT 模式必选，1~255 字符）
        host_password: 接入密码（ACCOUNT 模式必选，1~1024 字符）
        description: 描述信息（可选，0~63 字符）
        initiator: 启动器列表（NONE 模式必选）
        azs: 可用分区 ID 列表（可选，最多 40 个）
        project_id: 业务群组 ID（可选）
        sync_to_storage: 自动同步到存储（可选，默认 false）
        multipath_type: 多路径类型（可选，default/third_party）
        path_type: 启动器路径类型（可选，optimal_path/non_optimal_path）
        failover_mode: 启动器切换模式（可选，early_version_alua/common_alua 等）
        special_mode_type: 特殊模式类型（可选，mode_zero/mode_one 等）
        save_public_key: 自动保存公钥（可选，默认 false）

    Returns:
        创建的物理主机信息
    """
    url = "/rest/hostmgmt/v1/hosts"

    payload = {
        'access_mode': access_mode,
        'type': type
    }

    if host_name is not None:
        payload['host_name'] = host_name
    if ip is not None:
        payload['ip'] = ip
    if port is not None:
        payload['port'] = port
    # 将 host_username 和 host_password 转换为 API 参数名
    if host_username is not None:
        payload['username'] = host_username
    if host_password is not None:
        payload['password'] = host_password
    if description is not None:
        payload['description'] = description
    if initiator is not None:
        payload['initiator'] = initiator
    if azs is not None:
        payload['azs'] = azs
    if project_id is not None:
        payload['project_id'] = project_id
    if sync_to_storage is not None:
        payload['sync_to_storage'] = sync_to_storage
    if multipath_type is not None:
        payload['multipath_type'] = multipath_type
    if path_type is not None:
        payload['path_type'] = path_type
    if failover_mode is not None:
        payload['failover_mode'] = failover_mode
    if special_mode_type is not None:
        payload['special_mode_type'] = special_mode_type
    if save_public_key is not None:
        payload['save_public_key'] = save_public_key

    response = client.post(url, json=payload)
    return response


def modify_host(client: DMEAPIClient, host_id: str,
                ip: str = None, host_name: str = None,
                os_type: str = None, azs: list = None,
                project_id: str = None) -> dict:
    """
    修改物理主机基本信息

    修改物理主机基本信息（仅支持接入模式为 NONE 的主机）。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）
        ip: IP 地址（可选，IPv4 或 IPv6）
        host_name: 主机名称（可选，1~255 字符）
        os_type: 操作系统类型（可选）
        azs: 可用分区 ID 列表（可选，最多 40 个）
        project_id: 业务群组 ID（可选）

    Returns:
        修改结果
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}/general"

    payload = {}

    if ip is not None:
        payload['ip'] = ip
    if host_name is not None:
        payload['host_name'] = host_name
    if os_type is not None:
        payload['os_type'] = os_type
    if azs is not None:
        payload['azs'] = azs
    if project_id is not None:
        payload['project_id'] = project_id

    response = client.put(url, json=payload)
    return response


def delete_host(client: DMEAPIClient, host_id: str,
                sync_to_storage: bool = False) -> dict:
    """
    移除物理主机

    移除指定的物理主机。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）
        sync_to_storage: 是否同步从存储删除（可选，默认 false）

    Returns:
        删除结果
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}?sync_to_storage={str(sync_to_storage).lower()}"

    response = client.delete(url)
    return response


def initiator_add(client: DMEAPIClient, host_id: str,
                  initiators: list) -> dict:
    """
    为物理主机添加启动器

    为物理主机添加启动器（仅支持接入方式为 NONE 的主机）。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）
        initiators: 启动器列表（必选，最多 100 个）

    Returns:
        添加结果
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}/initiators/add"

    payload = {
        'initiators': initiators
    }

    response = client.put(url, json=payload)
    return response


def initiator_remove(client: DMEAPIClient, host_id: str,
                     initiators: list) -> dict:
    """
    从物理主机移除启动器

    从物理主机移除启动器（仅支持接入方式为 NONE 的主机）。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）
        initiators: 启动器 ID 列表（必选，最多 1000 个）

    Returns:
        移除结果
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}/initiators/remove"

    payload = {
        'initiators': initiators
    }

    response = client.put(url, json=payload)
    return response


def initiator_list(client: DMEAPIClient, host_id: str,
                   port_name: str = None, protocol: str = None,
                   status: str = None) -> dict:
    """
    查询指定物理主机的启动器

    查询指定物理主机的启动器列表。

    Args:
        client: DME API 客户端
        host_id: 物理主机 ID（必选）
        port_name: 启动器 WWN 或 IQN（可选）
        protocol: 启动器类型（可选，FC/ISCSI/NVME_OVER_ROCE）
        status: 启动器状态（可选，UNKNOWN/ONLINE/OFFLINE/UNBOUND）

    Returns:
        启动器列表
    """
    url = f"/rest/hostmgmt/v1/hosts/{host_id}/initiators"

    params = {}
    if port_name is not None:
        params['port_name'] = port_name
    if protocol is not None:
        params['protocol'] = protocol
    if status is not None:
        params['status'] = status

    response = client.get(url, query_params=params)
    return response


def test(client: DMEAPIClient, storage_id: str,
         host_ids: list = None, hostgroup_id: str = None,
         auto_zoning: bool = False,
         target_fcports: list = None,
         target_fcportgroups: list = None) -> dict:
    """
    检测存储设备和物理主机连通性

    检测存储设备和物理主机之间的连通性。

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必选）
        host_ids: 物理主机 ID 列表（可选，与 hostgroup_id 二选一）
        hostgroup_id: 物理主机组 ID（可选，与 host_ids 二选一）
        auto_zoning: 自动划 zone 策略（可选，默认 false）
        target_fcports: 端口 wwn 列表（可选，auto_zoning 为 true 时生效）
        target_fcportgroups: 端口组 id 列表（可选，auto_zoning 为 true 时生效）

    Returns:
        连通性检测结果
    """
    url = "/rest/hostmgmt/v1/connectivity/host-and-storage"

    payload = {
        'storage_id': storage_id
    }

    if host_ids is not None:
        payload['host_ids'] = host_ids
    if hostgroup_id is not None:
        payload['hostgroup_id'] = hostgroup_id
    if auto_zoning is not None:
        payload['auto_zoning'] = auto_zoning
    if target_fcports is not None:
        payload['target_fcports'] = target_fcports
    if target_fcportgroups is not None:
        payload['target_fcportgroups'] = target_fcportgroups

    response = client.post(url, json=payload)
    return response


def sshkey_save(client: DMEAPIClient, ip: str, key: str,
                port: int = None) -> dict:
    """
    保存指定物理主机 SSH 公钥

    保存物理主机的 SSH 公钥，用于后续通信中检测通信物理主机的身份是否合法。

    Args:
        client: DME API 客户端
        ip: 物理主机 IP 地址（必选）
        key: 物理主机 SSH 公钥（必选）
        port: SSH 端口（可选，默认 22）

    Returns:
        保存结果
    """
    url = "/rest/hostmgmt/v1/host-keys"

    payload = {
        'ip': ip,
        'key': key
    }

    if port is not None:
        payload['port'] = port

    response = client.put(url, json=payload)
    return response


def sshkey_query(client: DMEAPIClient, ip: str,
                 port: int = None) -> dict:
    """
    查询指定物理主机 SSH 公钥

    查询指定物理主机的 SSH 公钥信息。

    Args:
        client: DME API 客户端
        ip: 物理主机 IP 地址（必选）
        port: SSH 端口（可选，默认 22）

    Returns:
        SSH 公钥信息
    """
    url = "/rest/hostmgmt/v1/host-keys"

    params = {
        'ip': ip
    }

    if port is not None:
        params['port'] = port

    response = client.get(url, query_params=params)
    return response


def initiator_show_owner(client: DMEAPIClient, initiator_id: str = None,
                         raw_id: str = None, protocol: str = None) -> dict:
    """
    根据启动器查询关联的物理主机

    根据启动器 ID 或启动器 WWPN/IQN/NQN 查询关联的物理主机。

    Args:
        client: DME API 客户端
        initiator_id: 启动器 ID（可选，与 raw_id 互斥）
        raw_id: 启动器 WWPN/IQN/NQN（可选，与 initiator_id 互斥）
        protocol: 启动器类型（可选，FC/ISCSI/NVME_OVER_ROCE）

    Returns:
        关联的物理主机信息
    """
    url = "/rest/hostmgmt/v1/hosts/query-by-initiator"

    payload = {}

    if initiator_id is not None:
        payload['initiator_id'] = initiator_id
    if raw_id is not None:
        payload['raw_id'] = raw_id
    if protocol is not None:
        payload['protocol'] = protocol

    response = client.post(url, json=payload)
    return response


def map_lun(client: DMEAPIClient, volume_ids: list, host_id: str,
            mapping_policy: str = None, task_remarks: str = None) -> dict:
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

    payload = {
        'volume_ids': volume_ids,
        'host_id': host_id
    }

    if mapping_policy is not None:
        payload['mapping_policy'] = mapping_policy

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def unmap_lun(client: DMEAPIClient, volume_ids: list, host_id: str,
              host_type: str = "host", task_remarks: str = None) -> dict:
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

    payload = {
        'volume_ids': volume_ids,
        'host_id': host_id,
        'host_type': host_type
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    'list': {
        'func': list_hosts,
        'description': '批量查询物理主机',
        'params': ['limit', 'start', 'sort_key', 'sort_dir', 'name',
                   'host_group_name', 'ip', 'display_status', 'managed_status',
                   'os_type', 'access_mode', 'az_id', 'az_ids', 'project_id'],
        'subtopic': None
    },
    'show': {
        'func': show_host,
        'description': '查询指定物理主机',
        'params': ['host_id'],
        'subtopic': None
    },
    'create': {
        'func': create_host,
        'description': '接入物理主机',
        'params': ['access_mode', 'type', 'host_name', 'ip', 'port',
                   'host_username', 'host_password', 'description', 'initiator',
                   'azs', 'project_id', 'sync_to_storage', 'multipath_type',
                   'path_type', 'failover_mode', 'special_mode_type', 'save_public_key'],
        'subtopic': None
    },
    'modify': {
        'func': modify_host,
        'description': '修改物理主机基本信息',
        'params': ['host_id', 'ip', 'host_name', 'os_type', 'azs', 'project_id'],
        'subtopic': None
    },
    'delete': {
        'func': delete_host,
        'description': '移除物理主机',
        'params': ['host_id', 'sync_to_storage'],
        'subtopic': None
    },
    'add_initiators': {
        'func': initiator_add,
        'description': '为物理主机添加启动器',
        'params': ['host_id', 'initiators'],
        'subtopic': None
    },
    'remove_initiators': {
        'func': initiator_remove,
        'description': '从物理主机移除启动器',
        'params': ['host_id', 'initiators'],
        'subtopic': None
    },
    'show_initiators': {
        'func': initiator_list,
        'description': '查询指定物理主机的启动器',
        'params': ['host_id', 'port_name', 'protocol', 'status'],
        'subtopic': None
    },
    'test': {
        'func': test,
        'description': '检测存储设备和物理主机连通性',
        'params': ['storage_id', 'host_ids', 'hostgroup_id', 'auto_zoning', 'target_fcports', 'target_fcportgroups'],
        'subtopic': None
    },
    'query_sshkey': {
        'func': sshkey_query,
        'description': '查询指定物理主机SSH公钥',
        'params': ['ip', 'port'],
        'subtopic': None
    },
    'save_sshkey': {
        'func': sshkey_save,
        'description': '保存指定物理主机SSH公钥',
        'params': ['ip', 'key', 'port'],
        'subtopic': None
    },
    'query_by_initiator': {
        'func': initiator_show_owner,
        'description': '根据启动器查询关联的物理主机',
        'params': ['initiator_id', 'raw_id', 'protocol'],
        'subtopic': None
    },
    'map_luns': {
        'func': map_lun,
        'description': 'LUN映射给物理主机',
        'params': ['volume_ids', 'host_id', 'mapping_policy', 'task_remarks'],
        'subtopic': None
    },
    'unmap_luns': {
        'func': unmap_lun,
        'description': '解除主机映射',
        'params': ['volume_ids', 'host_id', 'host_type', 'task_remarks'],
        'subtopic': None
    },
    }
