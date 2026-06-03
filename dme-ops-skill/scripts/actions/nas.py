"""
NAS 相关操作
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


# ============================================================================
# DPC (并行客户端) 子主题函数
# ============================================================================


def dpc_list(client: DMEAPIClient, ids: list = None, hostname: str = None, ip: str = None,
             mgmt_status: list = None, status: list = None, sn: str = None,
             storage_id: str = None, dpc_om_id: str = None, dpc_type: list = None,
             client_version: str = None, page_no: int = 1, page_size: int = 20) -> dict:
    """
    批量查询并行客户端列表

    批量查询并行客户端列表，包含 OceanStor A800 的 Dataturbo 客户端和 OceanStor Pacific/A310 的 DPC 信息。

    Args:
        client: DME API 客户端
        ids: 并行客户端 ID 列表（精确查询）
        hostname: 计算节点的主机名称（模糊查询）
        ip: 并行客户端所在计算节点的管理 IP（模糊查询）
        mgmt_status: 管理状态列表，可选值：normal（正常）, abnormal（异常）, unready（未就绪）,
                    subhealth（亚健康）, pre_registered（预注册）, unknown（未知）
        status: 业务状态列表，可选值：normal（正常）, abnormal（异常）, subhealth（亚健康）, unknown（未知）
        sn: 并行客户端所在计算节点的硬件 SN（模糊查询）
        storage_id: 存储设备 ID（精确查询）
        dpc_om_id: 并行客户端 O&M ID（精确查询）
        dpc_type: DPC 类型列表，可选值：DPC, DataTurbo
        client_version: 并行客户端版本号（精确查询）
        page_no: 分页页码，默认 1
        page_size: 每页数据条数，默认 20

    Returns:
        并行客户端列表
    """
    url = "/rest/dpc-mgmt/v1/dpcs/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if ids is not None:
        payload['ids'] = ids
    if hostname is not None:
        payload['hostname'] = hostname
    if ip is not None:
        payload['ip'] = ip
    if mgmt_status is not None:
        payload['mgmt_status'] = mgmt_status
    if status is not None:
        payload['status'] = status
    if sn is not None:
        payload['sn'] = sn
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if dpc_om_id is not None:
        payload['dpc_om_id'] = dpc_om_id
    if dpc_type is not None:
        payload['dpc_type'] = dpc_type
    if client_version is not None:
        payload['client_version'] = client_version

    response = client.post(url, json=payload)
    return response


def dpc_show(client: DMEAPIClient, dpc_id: str) -> dict:
    """
    查询并行客户端详情

    查询并行客户端详情，包含 OceanStor A800 的 Dataturbo 客户端和 OceanStor Pacific/A310 的 DPC 信息。

    Args:
        client: DME API 客户端
        dpc_id: 并行客户端 ID

    Returns:
        并行客户端详细信息
    """
    url = f"/rest/dpc-mgmt/v1/dpcs/{dpc_id}"

    response = client.get(url)
    return response


def dpc_version_list(client: DMEAPIClient) -> dict:
    """
    查询并行客户端版本信息列表

    查询并行客户端版本列表。

    Args:
        client: DME API 客户端

    Returns:
        并行客户端版本列表
    """
    url = "/rest/dpc-mgmt/v1/dpcs-versions"

    response = client.get(url)
    return response


def dtree_list(client: DMEAPIClient, id_in_storage: str = None, name: str = None,
               device_name: str = None, storage_id: str = None, zone_id: str = None,
               manufacturer: str = None, tier_name: str = None, fs_name: str = None,
               fs_id: str = None, namespace_name: str = None, namespace_id: str = None,
               quota_switch: bool = None, security_mode: str = None,
               nas_locking_policy: str = None, sort_key: str = None,
               sort_dir: str = None, page_no: int = 1, page_size: int = 20,
               dc_id: str = None, dc_name: str = None) -> dict:
    """
    查询 Dtree 列表

    查询 Dtree 列表。

    Args:
        client: DME API 客户端
        id_in_storage: Dtree 在存储侧的 ID
        name: Dtree 名称，支持模糊搜索
        device_name: dtree 所属存储设备名称，支持模糊搜索
        storage_id: dtree 所属存储设备 ID，支持过滤
        zone_id: dtree 所属 zone 的 ID
        manufacturer: dtree 所属存储设备厂商，huawei third_part
        tier_name: 服务等级名称，支持模糊搜索
        fs_name: dtree 所属文件系统名称，支持模糊搜索
        fs_id: dtree 所属文件系统 ID，与 namespace_id 互斥
        namespace_name: dtree 所属命名空间名称
        namespace_id: dtree 所属命名空间 ID，与 fs_id 互斥
        quota_switch: 配额是否启用，true/false
        security_mode: 安全模式，mixed/native/ntfs/unix
        nas_locking_policy: NAS 锁策略，mandatory/advisory/unknown
        sort_key: 排序字段，nfs_count/cifs_count/dataturbo_count/name
        sort_dir: 排序方向，asc/desc
        page_no: 分页查询页码，默认 1
        page_size: 每页显示的数量，默认 20，1~1000
        dc_id: 数据中心 ID
        dc_name: 数据中心名称

    Returns:
        Dtree 列表
    """
    url = "/rest/fileservice/v1/dtrees/query"

    payload = {}

    if id_in_storage is not None:
        payload['id_in_storage'] = id_in_storage
    if name is not None:
        payload['name'] = name
    if device_name is not None:
        payload['device_name'] = device_name
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if zone_id is not None:
        payload['zone_id'] = zone_id
    if manufacturer is not None:
        payload['manufacturer'] = manufacturer
    if tier_name is not None:
        payload['tier_name'] = tier_name
    if fs_name is not None:
        payload['fs_name'] = fs_name
    if fs_id is not None:
        payload['fs_id'] = fs_id
    if namespace_name is not None:
        payload['namespace_name'] = namespace_name
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if quota_switch is not None:
        payload['quota_switch'] = quota_switch
    if security_mode is not None:
        payload['security_mode'] = security_mode
    if nas_locking_policy is not None:
        payload['nas_locking_policy'] = nas_locking_policy
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if dc_id is not None:
        payload['dc_id'] = dc_id
    if dc_name is not None:
        payload['dc_name'] = dc_name

    response = client.post(url, json=payload)
    return response


def dtree_show(client: DMEAPIClient, dtree_id: str) -> dict:
    """
    查询指定 Dtree 详情

    Args:
        client: DME API 客户端
        dtree_id: Dtree ID

    Returns:
        Dtree 详细信息
    """
    url = f"/rest/fileservice/v1/dtrees/{dtree_id}"

    response = client.get(url)
    return response


def dtree_create(client: DMEAPIClient, storage_id: str, create_dtrees_param: list,
                 fs_id: str = None, namespace_id: str = None, zone_id: str = None,
                 parent_dir: str = None, quota_switch: bool = None,
                 security_mode: str = None, nas_locking_policy: str = None,
                 create_nfs_share_param: dict = None, create_cifs_share_param: dict = None,
                 dataturbo_share: dict = None, create_worm_param: dict = None,
                 unix_permissions: str = None, task_remarks: str = None) -> dict:
    """
    创建并共享 Dtree

    创建 Dtree，同时将 Dtree 以 NFS、CIFS 或 DataTurbo 共享。

    Args:
        client: DME API 客户端
        storage_id: dtree 所属存储设备 ID
        create_dtrees_param: Dtree 名称和数量信息列表，每个元素包含 dtree_name 和 count
        fs_id: dtree 所属文件系统 ID，与 namespace_id 互斥，集中式存储时必填
        namespace_id: dtree 所属命名空间 ID，与 fs_id 互斥，分布式存储时必填
        zone_id: dtree 所属 zone 的 ID
        parent_dir: 目录父级，分布式存储时有效
        quota_switch: 配额开关，true/false，默认 false
        security_mode: 安全模式，mixed/native/ntfs/unix
        nas_locking_policy: NAS 锁策略，mandatory/advisory/unknown
        create_nfs_share_param: 创建 NFS 共享请求结构体
        create_cifs_share_param: 创建 CIFS 共享请求结构体
        dataturbo_share: DataTurbo 共享
        create_worm_param: 创建 WORM 请求结构体
        unix_permissions: Dtree 目录权限，如 755
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/dtrees"

    payload = {
        'storage_id': storage_id,
        'create_dtrees_param': create_dtrees_param
    }

    if fs_id is not None:
        payload['fs_id'] = fs_id
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if zone_id is not None:
        payload['zone_id'] = zone_id
    if parent_dir is not None:
        payload['parent_dir'] = parent_dir
    if quota_switch is not None:
        payload['quota_switch'] = quota_switch
    if security_mode is not None:
        payload['security_mode'] = security_mode
    if nas_locking_policy is not None:
        payload['nas_locking_policy'] = nas_locking_policy
    if create_nfs_share_param is not None:
        payload['create_nfs_share_param'] = create_nfs_share_param
    if create_cifs_share_param is not None:
        payload['create_cifs_share_param'] = create_cifs_share_param
    if dataturbo_share is not None:
        payload['dataturbo_share'] = dataturbo_share
    if create_worm_param is not None:
        payload['create_worm_param'] = create_worm_param
    if unix_permissions is not None:
        payload['unix_permissions'] = unix_permissions
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def dtree_delete(client: DMEAPIClient, dtree_ids: list, task_remarks: str = None) -> dict:
    """
    批量删除 Dtree

    Args:
        client: DME API 客户端
        dtree_ids: 待删除 Dtree ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/dtrees/delete"

    payload = {
        'dtree_ids': dtree_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def dtree_modify(client: DMEAPIClient, dtree_id: str, name: str = None,
                 quota_switch: bool = None, security_mode: str = None,
                 nas_locking_policy: str = None, unix_permissions: str = None,
                 task_remarks: str = None) -> dict:
    """
    修改指定 Dtree

    Args:
        client: DME API 客户端
        dtree_id: Dtree ID
        name: Dtree 名称
        quota_switch: 配额开关，true/false
        security_mode: 安全模式，mixed/native/ntfs/unix
        nas_locking_policy: NAS 锁策略，mandatory/advisory/unknown
        unix_permissions: Dtree 目录权限，如 755
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = f"/rest/fileservice/v1/dtrees/{dtree_id}"

    payload = {}

    if name is not None:
        payload['name'] = name
    if quota_switch is not None:
        payload['quota_switch'] = quota_switch
    if security_mode is not None:
        payload['security_mode'] = security_mode
    if nas_locking_policy is not None:
        payload['nas_locking_policy'] = nas_locking_policy
    if unix_permissions is not None:
        payload['unix_permissions'] = unix_permissions
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


# ============================================================================
# NFS 共享子主题相关动作
# ============================================================================

def nfs_share_list(client: DMEAPIClient, id_in_storage: str = None, name: str = None,
                   share_path: str = None, exact_share_path: str = None,
                   device_name: str = None, storage_id: str = None,
                   tier_name: str = None, owning_dtree_name: str = None,
                   fs_name: str = None, fs_id: str = None,
                   owning_dtree_id: str = None, vstore_name: str = None,
                   page_no: int = 1, page_size: int = 20, sort_key: str = None,
                   sort_dir: str = None, support_provisioning: bool = None,
                   namespace_id: str = None, namespace_name: str = None,
                   dc_id: str = None, dc_name: str = None,
                   zone_id: str = None, zone_name: str = None,
                   zone_ip: str = None) -> dict:
    """
    查询 NFS 共享列表

    查询 NFS 共享列表。

    Args:
        client: DME API 客户端
        id_in_storage: NFS 在存储侧的 ID
        name: 共享名称，支持模糊搜索
        share_path: 共享路径，支持模糊搜索
        exact_share_path: 精确搜索 NFS 共享路径
        device_name: 所属存储设备名称，支持模糊搜索
        storage_id: 所属存储设备 ID，支持过滤
        tier_name: 服务等级名称，支持模糊搜索
        owning_dtree_name: 所属 Dtree 名称，支持模糊搜索
        fs_name: 文件系统名称，支持模糊搜索
        fs_id: 文件系统 ID
        owning_dtree_id: 所属 Dtree Id，支持过滤
        vstore_name: NFS 共享所属 vStore 名称，支持模糊查询
        page_no: 分页查询页码，默认 1
        page_size: 每页显示的数量，默认 20
        sort_key: 按照指定字段排序，可选值：name, id_in_storage
        sort_dir: 指定排序方向，asc 或 desc，默认 asc
        support_provisioning: 是否支持业务发放
        namespace_id: 命名空间 ID（仅 OceanStor Pacific 系列支持）
        namespace_name: 命名空间名称（仅 OceanStor Pacific 系列支持）
        dc_id: 数据中心 ID
        dc_name: 数据中心名称
        zone_id: NFS 共享所属 zone ID
        zone_name: NFS 共享所属 zone 名称，支持模糊搜索
        zone_ip: NFS 共享所属 zone 管理 IP

    Returns:
        NFS 共享列表
    """
    url = "/rest/fileservice/v1/nfs-shares/query"

    payload = {}

    if id_in_storage is not None:
        payload['id_in_storage'] = id_in_storage
    if name is not None:
        payload['name'] = name
    if share_path is not None:
        payload['share_path'] = share_path
    if exact_share_path is not None:
        payload['exact_share_path'] = exact_share_path
    if device_name is not None:
        payload['device_name'] = device_name
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if tier_name is not None:
        payload['tier_name'] = tier_name
    if owning_dtree_name is not None:
        payload['owning_dtree_name'] = owning_dtree_name
    if fs_name is not None:
        payload['fs_name'] = fs_name
    if fs_id is not None:
        payload['fs_id'] = fs_id
    if owning_dtree_id is not None:
        payload['owning_dtree_id'] = owning_dtree_id
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
    if support_provisioning is not None:
        payload['support_provisioning'] = support_provisioning
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if namespace_name is not None:
        payload['namespace_name'] = namespace_name
    if dc_id is not None:
        payload['dc_id'] = dc_id
    if dc_name is not None:
        payload['dc_name'] = dc_name
    if zone_id is not None:
        payload['zone_id'] = zone_id
    if zone_name is not None:
        payload['zone_name'] = zone_name
    if zone_ip is not None:
        payload['zone_ip'] = zone_ip

    response = client.post(url, json=payload)
    return response


def nfs_share_show(client: DMEAPIClient, nfs_share_id: str) -> dict:
    """
    查询指定 NFS 共享详情

    Args:
        client: DME API 客户端
        nfs_share_id: NFS 共享 ID

    Returns:
        NFS 共享详细信息
    """
    url = f"/rest/fileservice/v1/nfs-shares/{nfs_share_id}"

    response = client.get(url)
    return response


def nfs_share_create(client: DMEAPIClient, create_nfs_share_param: dict,
                     task_remarks: str = None) -> dict:
    """
    创建 NFS 共享

    Args:
        client: DME API 客户端
        create_nfs_share_param: 创建 NFS 共享参数，包含如下属性：
            - name: NFS共享别名（可选）
            - description: 描述信息（可选）
            - share_path: 共享路径（必选）
            - character_encoding: 字符编码（可选）
            - audit_items: 支持审计的事件列表（可选）
            - show_snapshot_enable: 是否开启显示Snapshot（可选）。可选值：true/false
            - nfs_share_client_addition: NFS共享客户端权限列表（可选）
            - file_name_extension_filters: 文件扩展名过滤规则列表（可选）
            - fs_id: 文件系统的id，与namespace_id互斥
            - namespace_id: 命名空间的id，与fs_id互斥
        task_remarks: 异步任务备注信息

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v2/nfs-shares"

    payload = {
        'create_nfs_share_param': create_nfs_share_param
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def nfs_share_modify(client: DMEAPIClient, nfs_share_id: str,
                     description: str = None, character_encoding: str = None,
                     audit_items: list = None, show_snapshot_enable: bool = None,
                     nfs_share_client_addition: list = None,
                     nfs_share_client_modification: list = None,
                     nfs_share_client_deletion: list = None,
                     file_name_ex_filters: list = None,
                     task_remarks: str = None) -> dict:
    """
    修改指定 NFS 共享

    Args:
        client: DME API 客户端
        nfs_share_id: NFS 共享 ID
        description: 描述信息
        character_encoding: 字符编码，可选值：utf-8, zh, gbk 等
        audit_items: 支持审计的事件列表
        show_snapshot_enable: 是否开启显示 Snapshot 的功能
        nfs_share_client_addition: 需要新增的 NFS 共享客户端列表
        nfs_share_client_modification: 需要修改的 NFS 共享客户端列表
        nfs_share_client_deletion: 需要删除的 NFS 共享客户端列表
        file_name_ex_filters: 扩展名过滤规则列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据
    """
    url = f"/rest/fileservice/v2/nfs-shares/{nfs_share_id}"

    payload = {}

    if description is not None:
        payload['description'] = description
    if character_encoding is not None:
        payload['character_encoding'] = character_encoding
    if audit_items is not None:
        payload['audit_items'] = audit_items
    if show_snapshot_enable is not None:
        payload['show_snapshot_enable'] = show_snapshot_enable
    if nfs_share_client_addition is not None:
        payload['nfs_share_client_addition'] = nfs_share_client_addition
    if nfs_share_client_modification is not None:
        payload['nfs_share_client_modification'] = nfs_share_client_modification
    if nfs_share_client_deletion is not None:
        payload['nfs_share_client_deletion'] = nfs_share_client_deletion
    if file_name_ex_filters is not None:
        payload['file_name_ex_filters'] = file_name_ex_filters
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def nfs_share_delete(client: DMEAPIClient, nfs_share_ids: list,
                     task_remarks: str = None) -> dict:
    """
    批量删除 NFS 共享

    Args:
        client: DME API 客户端
        nfs_share_ids: 待删除 NFS 共享 ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/nfs-shares/delete"

    payload = {
        'nfs_share_ids': nfs_share_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


# ============================================================================
# CIFS 共享子主题相关动作
# ============================================================================

def cifs_list(client: DMEAPIClient, raw_id: str = None, name: str = None,
              share_path: str = None, exact_share_path: str = None,
              fs_id: str = None, fs_name: str = None, dtree_id: str = None,
              dtree_name: str = None, storage_id: str = None,
              storage_name: str = None, vstore_raw_id: str = None,
              vstore_name: str = None, manufacturer: str = None,
              op_lock_enabled: bool = None, notify_enabled: bool = None,
              offline_file_modes: list = None, file_extension_filter_enabled: bool = None,
              abe_enabled: bool = None, page_no: int = 1, page_size: int = 10,
              sort_key: str = None, sort_dir: str = None,
              namespace_id: str = None, namespace_name: str = None,
              support_provisioning: bool = None, dc_id: str = None,
              dc_name: str = None) -> dict:
    """
    批量查询 CIFS 共享

    批量查询 CIFS 共享，支持多种过滤条件。

    Args:
        client: DME API 客户端
        raw_id: CIFS 共享在存储设备上的 ID
        name: CIFS 共享名称，支持模糊查询
        share_path: CIFS 共享路径，支持模糊查询
        exact_share_path: 精确搜索 CIFS 共享路径
        fs_id: CIFS 共享所属文件系统的 ID
        fs_name: CIFS 共享所属文件系统名称，支持模糊查询
        dtree_id: CIFS 共享所属 Dtree 的 ID
        dtree_name: CIFS 共享所属 Dtree 名称，支持模糊查询
        storage_id: CIFS 共享所属存储设备的 ID
        storage_name: CIFS 共享所属存储设备名称，支持模糊查询
        vstore_raw_id: CIFS 共享所属 vStore 在存储设备上分配的 ID
        vstore_name: CIFS 共享所属 vStore 名称，支持模糊查询
        manufacturer: 所属存储设备厂商，huawei 或 third_party
        op_lock_enabled: CIFS 共享是否开启 Oplock
        notify_enabled: CIFS 共享是否开启 Notify
        offline_file_modes: CIFS 共享的离线缓存模式列表
        file_extension_filter_enabled: CIFS 共享是否开启文件扩展名过滤
        abe_enabled: CIFS 共享是否开启 ABE
        page_no: 分页页码，默认 1
        page_size: 每页数据条数，默认 10
        sort_key: 按照指定字段排序，name 或 raw_id
        sort_dir: 排序方向，asc 或 desc
        namespace_id: 命名空间 ID（仅 OceanStor Pacific 系列支持）
        namespace_name: 命名空间名称（仅 OceanStor Pacific 系列支持）
        support_provisioning: 是否支持业务发放
        dc_id: 数据中心 ID
        dc_name: 数据中心名称

    Returns:
        CIFS 共享列表
    """
    url = "/rest/fileservice/v1/cifs-shares/query"

    payload = {}

    if raw_id is not None:
        payload['raw_id'] = raw_id
    if name is not None:
        payload['name'] = name
    if share_path is not None:
        payload['share_path'] = share_path
    if exact_share_path is not None:
        payload['exact_share_path'] = exact_share_path
    if fs_id is not None:
        payload['fs_id'] = fs_id
    if fs_name is not None:
        payload['fs_name'] = fs_name
    if dtree_id is not None:
        payload['dtree_id'] = dtree_id
    if dtree_name is not None:
        payload['dtree_name'] = dtree_name
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if storage_name is not None:
        payload['storage_name'] = storage_name
    if vstore_raw_id is not None:
        payload['vstore_raw_id'] = vstore_raw_id
    if vstore_name is not None:
        payload['vstore_name'] = vstore_name
    if manufacturer is not None:
        payload['manufacturer'] = manufacturer
    if op_lock_enabled is not None:
        payload['op_lock_enabled'] = op_lock_enabled
    if notify_enabled is not None:
        payload['notify_enabled'] = notify_enabled
    if offline_file_modes is not None:
        payload['offline_file_modes'] = offline_file_modes
    if file_extension_filter_enabled is not None:
        payload['file_extension_filter_enabled'] = file_extension_filter_enabled
    if abe_enabled is not None:
        payload['abe_enabled'] = abe_enabled
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if namespace_name is not None:
        payload['namespace_name'] = namespace_name
    if support_provisioning is not None:
        payload['support_provisioning'] = support_provisioning
    if dc_id is not None:
        payload['dc_id'] = dc_id
    if dc_name is not None:
        payload['dc_name'] = dc_name

    response = client.post(url, json=payload)
    return response


def cifs_show(client: DMEAPIClient, cifs_share_id: str) -> dict:
    """
    查询指定 CIFS 共享详情

    Args:
        client: DME API 客户端
        cifs_share_id: CIFS 共享 ID

    Returns:
        CIFS 共享详细信息
    """
    url = f"/rest/fileservice/v1/cifs-shares/{cifs_share_id}"

    response = client.get(url)
    return response


def cifs_create(client: DMEAPIClient, create_cifs_param: dict, fs_id: str = None,
                namespace_id: str = None, task_remarks: str = None) -> dict:
    """
    创建单个 CIFS 共享

    Args:
        client: DME API 客户端
        create_cifs_param: 创建 CIFS 共享参数，属性如下：
            - name: 共享名称（必选）
            - description: 描述信息
            - share_path: 共享路径（必选）
            - op_lock_enabled: Oplock功能开关
            - notify_enabled: Notify功能开关
            - ca_enabled: Failover连续可用特性开关
            - offline_file_mode: 离线缓存模式。可选值：none（关闭），manual（手动），documents（文档），programs（程序）
            - ip_control_enabled: IP访问控制特性开关
            - abe_enabled: ABE功能开关
            - audititem_list: 支持审计的事件列表
            - apply_default_acl: 是否添加默认ACL
            - file_extension_filter_enabled: 是否开启文件扩展名过滤特性
            - show_previous_versions_enabled: 是否开启显示历史版本的功能
            - show_snapshot_enabled: 是否开启显示Snapshot的功能
            - user_and_user_group_info: 用户和用户组列表
            - ip_addresses_and_segments: IP地址和IP地址段列表
            - file_name_extension_filters: 文件扩展名过滤规则列表
            - smb3_encryption_enable: 是否开启SMB3加密功能
            - unencrypted_access: 是否允许未加密客户端访问
            - enable_lease: 是否开启租约锁定开关
        fs_id: 文件系统的 ID，与 namespace_id 互斥
        namespace_id: 命名空间的 ID，与 fs_id 互斥
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/cifs-shares"

    payload = {
        'create_cifs_param': create_cifs_param
    }

    if fs_id is not None:
        payload['fs_id'] = fs_id
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def cifs_modify(client: DMEAPIClient, cifs_share_id: str, description: str = None,
                op_lock_enabled: bool = None, notify_enabled: bool = None,
                ca_enabled: bool = None, offline_file_mode: str = None,
                ip_control_enabled: bool = None, abe_enabled: bool = None,
                audititem_list: list = None, apply_default_acl: bool = None,
                file_extension_filter_enabled: bool = None,
                show_previous_versions_enabled: bool = None,
                show_snapshot_enabled: bool = None,
                user_and_user_group_info: list = None,
                ip_and_segments: list = None,
                file_name_ex_filters: list = None,
                task_remarks: str = None, smb3_encryption_enable: bool = None,
                unencrypted_access: bool = None, enable_lease: bool = None) -> dict:
    """
    修改指定 CIFS 共享

    Args:
        client: DME API 客户端
        cifs_share_id: CIFS 共享 ID
        description: 描述信息
        op_lock_enabled: Oplock 功能开关
        notify_enabled: Notify 功能开关
        ca_enabled: Failover 连续可用特性开关
        offline_file_mode: 离线缓存模式，none/manual/documents/programs
        ip_control_enabled: IP 访问控制特性开关
        abe_enabled: ABE 功能开关
        audititem_list: 支持审计的事件列表
        apply_default_acl: 是否添加默认 ACL
        file_extension_filter_enabled: 是否开启文件扩展名过滤特性
        show_previous_versions_enabled: 是否开启显示以前的版本的功能
        show_snapshot_enabled: 是否开启显示 Snapshot 的功能
        user_and_user_group_info: 用户和用户组列表
        ip_and_segments: IP 地址和 IP 地址段列表
        file_name_ex_filters: 扩展名过滤规则列表
        task_remarks: 异步任务备注信息
        smb3_encryption_enable: 是否开启 SMB3 加密功能
        unencrypted_access: 是否允许未加密客户端访问
        enable_lease: 是否开启租约锁定开关

    Returns:
        响应数据，包含 task_id
    """
    url = f"/rest/fileservice/v1/cifs-shares/{cifs_share_id}"

    payload = {}

    if description is not None:
        payload['description'] = description
    if op_lock_enabled is not None:
        payload['op_lock_enabled'] = op_lock_enabled
    if notify_enabled is not None:
        payload['notify_enabled'] = notify_enabled
    if ca_enabled is not None:
        payload['ca_enabled'] = ca_enabled
    if offline_file_mode is not None:
        payload['offline_file_mode'] = offline_file_mode
    if ip_control_enabled is not None:
        payload['ip_control_enabled'] = ip_control_enabled
    if abe_enabled is not None:
        payload['abe_enabled'] = abe_enabled
    if audititem_list is not None:
        payload['audititem_list'] = audititem_list
    if apply_default_acl is not None:
        payload['apply_default_acl'] = apply_default_acl
    if file_extension_filter_enabled is not None:
        payload['file_extension_filter_enabled'] = file_extension_filter_enabled
    if show_previous_versions_enabled is not None:
        payload['show_previous_versions_enabled'] = show_previous_versions_enabled
    if show_snapshot_enabled is not None:
        payload['show_snapshot_enabled'] = show_snapshot_enabled
    if user_and_user_group_info is not None:
        payload['user_and_user_group_info'] = user_and_user_group_info
    if ip_and_segments is not None:
        payload['ip_and_segments'] = ip_and_segments
    if file_name_ex_filters is not None:
        payload['file_name_ex_filters'] = file_name_ex_filters
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    if smb3_encryption_enable is not None:
        payload['smb3_encryption_enable'] = smb3_encryption_enable
    if unencrypted_access is not None:
        payload['unencrypted_access'] = unencrypted_access
    if enable_lease is not None:
        payload['enable_lease'] = enable_lease

    response = client.put(url, json=payload)
    return response


def cifs_delete(client: DMEAPIClient, cifs_share_ids: list, task_remarks: str = None) -> dict:
    """
    批量删除 CIFS 共享

    Args:
        client: DME API 客户端
        cifs_share_ids: 需要删除 CIFS 共享的 ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/cifs-shares/delete"

    payload = {
        'cifs_share_ids': cifs_share_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def cifs_show_permissions(client: DMEAPIClient, cifs_share_id: str,
                          type: str = None,
                          user_or_user_group_name: str = None,
                          domain_type: str = None, permissions: list = None,
                          user_or_user_group_raw_id: str = None,
                          ip_addresses_or_segments: str = None,
                          ip_or_segments_raw_id: str = None,
                          rule_type: str = None,
                          file_name_extension: str = None,
                          file_extension_name_raw_id: str = None,
                          sort_key: str = None, sort_dir: str = None,
                          page_no: int = 1, page_size: int = 10) -> dict:
    """
    查询单个 CIFS 共享的权限列表

    查询 CIFS 共享的用户/用户组、IP 地址/IP 地址段、文件扩展名过滤规则等权限信息。

    Args:
        client: DME API 客户端
        cifs_share_id: CIFS 共享 ID
        type: 权限类型，可选值：user（用户/用户组）,ip（IP 地址/IP 地址段）,file（文件扩展名过滤规则）。
             不指定时返回所有类型的权限
        user_or_user_group_name: 用户/用户组名称（用于过滤）
        domain_type: 域类型，可选值：ad_domain, ldap_domain, local, nis_domain
        permissions: 权限过滤列表，每个元素包含 permission 字段
        user_or_user_group_raw_id: 用户/用户组在存储设备上的 ID
        ip_addresses_or_segments: IP 地址/IP 地址段（用于过滤）
        ip_or_segments_raw_id: IP 地址/IP 地址段在存储设备上的 ID
        rule_type: 规则类型，可选值：reject（只拒绝）, permit（只允许）
        file_name_extension: 文件扩展名（用于过滤）
        file_extension_name_raw_id: 文件扩展名过滤规则在存储上的 ID
        sort_key: 排序字段，可选值：raw_id, name
        sort_dir: 排序方向，可选值：asc, desc（默认 asc）
        page_no: 分页页码，默认 1
        page_size: 每页数据条数，默认 10

    Returns:
        权限列表
    """
    result = {'user': [], 'ip': [], 'file': []}

    # 根据 type 参数查询对应类型的权限
    if type is None or type == 'user':
        url = f"/rest/fileservice/v1/cifs-shares/{cifs_share_id}/auth-users/query"
        payload = {}
        if user_or_user_group_name is not None:
            payload['user_or_user_group_name'] = user_or_user_group_name
        if domain_type is not None:
            payload['domain_type'] = domain_type
        if permissions is not None:
            payload['permissions'] = permissions
        if user_or_user_group_raw_id is not None:
            payload['user_or_user_group_raw_id'] = user_or_user_group_raw_id
        if sort_key is not None:
            payload['sort_key'] = sort_key
        if sort_dir is not None:
            payload['sort_dir'] = sort_dir
        if page_no is not None:
            payload['page_no'] = page_no
        if page_size is not None:
            payload['page_size'] = page_size
        response = client.post(url, json=payload)
        if response.get('auth_users'):
            result['user'] = response.get('auth_users')

    if type is None or type == 'ip':
        url = f"/rest/fileservice/v1/cifs-shares/{cifs_share_id}/ip-access-rules/query"
        payload = {}
        if ip_addresses_or_segments is not None:
            payload['ip_addresses_or_segments'] = ip_addresses_or_segments
        if ip_or_segments_raw_id is not None:
            payload['ip_or_segments_raw_id'] = ip_or_segments_raw_id
        if sort_key is not None:
            payload['sort_key'] = sort_key
        if sort_dir is not None:
            payload['sort_dir'] = sort_dir
        if page_no is not None:
            payload['page_no'] = page_no
        if page_size is not None:
            payload['page_size'] = page_size
        response = client.post(url, json=payload)
        if response.get('ip_access_rules'):
            result['ip'] = response.get('ip_access_rules')

    if type is None or type == 'file':
        url = f"/rest/fileservice/v1/cifs-shares/{cifs_share_id}/file-filter-rules/query"
        payload = {}
        if rule_type is not None:
            payload['rule_type'] = rule_type
        if file_name_extension is not None:
            payload['file_name_extension'] = file_name_extension
        if file_extension_name_raw_id is not None:
            payload['file_extension_name_raw_id'] = file_extension_name_raw_id
        if sort_key is not None:
            payload['sort_key'] = sort_key
        if sort_dir is not None:
            payload['sort_dir'] = sort_dir
        if page_no is not None:
            payload['page_no'] = page_no
        if page_size is not None:
            payload['page_size'] = page_size
        response = client.post(url, json=payload)
        if response.get('file_filter_rules'):
            result['file'] = response.get('file_filter_rules')

    # 如果指定了 type，只返回对应类型的权限
    if type == 'user':
        return {'user_permissions': result['user']}
    elif type == 'ip':
        return {'ip_permissions': result['ip']}
    elif type == 'file':
        return {'file_permissions': result['file']}
    else:
        # 返回所有权限
        return {'user_permissions': result['user'], 'ip_permissions': result['ip'], 'file_permissions': result['file']}


# ============================================================================
# dataturbo_share (DataTurbo 共享) 子主题相关动作
# ============================================================================

def dataturbo_share_list(client: DMEAPIClient, page_no: int = 1, page_size: int = 10,
                   raw_id: str = None, share_path: str = None, fs_id: str = None,
                   fs_name: str = None, dtree_id: str = None, dtree_name: str = None,
                   vstore_id: str = None, vstore_raw_id: str = None, vstore_name: str = None,
                   storage_id: str = None, storage_name: str = None, zone_id: str = None,
                   zone_name: str = None, scope: str = None, sort_key: str = None,
                   sort_dir: str = None) -> dict:
    """
    查询 DataTurbo 共享列表

    查询 DataTurbo 共享列表，支持多种过滤条件。

    Args:
        client: DME API 客户端
        page_no: 分页页码，默认 1，范围 1~10000000
        page_size: 每页数据条数，默认 10，范围 1~1000
        raw_id: DataTurbo 共享在设备上 ID，精确查询
        share_path: 共享路径，支持模糊搜索
        fs_id: DataTurbo 共享所属文件系统 ID，精确查询
        fs_name: DataTurbo 共享所属文件系统名称，支持模糊搜索
        dtree_id: DataTurbo 共享所属 Dtree 的 ID，精确查询
        dtree_name: DataTurbo 共享所属 Dtree 名称，支持模糊查询
        vstore_id: DataTurbo 共享所属租户 ID，精确查询
        vstore_raw_id: DataTurbo 共享所属租户 RAW ID，精确查询
        vstore_name: DataTurbo 共享所属租户名称，支持模糊搜索
        storage_id: DataTurbo 共享所属存储设备 ID，精确查询
        storage_name: DataTurbo 共享所属存储设备名称，支持模糊搜索
        zone_id: DataTurbo 共享所属 zone ID，精确查询
        zone_name: DataTurbo 共享所属 zone 名称，支持模糊搜索
        scope: 资源所属范围，local_scale（本地）或 global_scale（全局）
        sort_key: 排序字段，取值范围：raw_id
        sort_dir: 排序方向，asc（升序）或 desc（降序），默认 asc

    Returns:
        DataTurbo 共享列表
    """
    url = "/rest/fileservice/v1/dpc-shares/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if raw_id is not None:
        payload['raw_id'] = raw_id
    if share_path is not None:
        payload['share_path'] = share_path
    if fs_id is not None:
        payload['fs_id'] = fs_id
    if fs_name is not None:
        payload['fs_name'] = fs_name
    if dtree_id is not None:
        payload['dtree_id'] = dtree_id
    if dtree_name is not None:
        payload['dtree_name'] = dtree_name
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if vstore_raw_id is not None:
        payload['vstore_raw_id'] = vstore_raw_id
    if vstore_name is not None:
        payload['vstore_name'] = vstore_name
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if storage_name is not None:
        payload['storage_name'] = storage_name
    if zone_id is not None:
        payload['zone_id'] = zone_id
    if zone_name is not None:
        payload['zone_name'] = zone_name
    if scope is not None:
        payload['scope'] = scope
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir

    response = client.post(url, json=payload)
    return response


def dataturbo_share_show(client: DMEAPIClient, dataturbo_share_id: str) -> dict:
    """
    查询指定 DataTurbo 共享详情

    Args:
        client: DME API 客户端
        dataturbo_share_id: DataTurbo 共享 ID

    Returns:
        DataTurbo 共享详细信息
    """
    url = f"/rest/fileservice/v1/dpc-shares/{dataturbo_share_id}"

    response = client.get(url)
    return response


def dataturbo_share_create(client: DMEAPIClient, charset: str, fs_id: str = None,
                     dtree_id: str = None, description: str = None,
                     dataturbo_share_auth: list = None, task_remarks: str = None) -> dict:
    """
    创建 DataTurbo 共享

    Args:
        client: DME API 客户端
        charset: 字符集编码，固定值 UTF_8
        fs_id: 需共享的文件系统的 ID，与 dtree_id 互斥，必传其中一个
        dtree_id: 需共享的 Dtree 的 ID，与 fs_id 互斥，必传其中一个
        description: DataTurbo 共享描述
        dataturbo_share_auth: DataTurbo 管理员列表，每个元素包含 dpc_user_id 和 permission
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/dpc-shares"

    payload = {
        'charset': charset
    }

    if fs_id is not None:
        payload['fs_id'] = fs_id
    if dtree_id is not None:
        payload['dtree_id'] = dtree_id
    if description is not None:
        payload['description'] = description
    if dataturbo_share_auth is not None:
        payload['dpc_share_auth'] = dataturbo_share_auth
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def dataturbo_share_modify(client: DMEAPIClient, dataturbo_share_id: str, description: str = None,
                     dataturbo_share_auth_addition: list = None,
                     dataturbo_share_auth_deletion: list = None,
                     task_remarks: str = None) -> dict:
    """
    修改指定 DataTurbo 共享

    Args:
        client: DME API 客户端
        dataturbo_share_id: DataTurbo 共享 ID
        description: DataTurbo 共享描述
        dataturbo_share_auth_addition: 要增加的 DataTurbo 管理员列表
        dataturbo_share_auth_deletion: 要删除的 DataTurbo 管理员 ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = f"/rest/fileservice/v1/dpc-shares/{dataturbo_share_id}"

    payload = {}

    if description is not None:
        payload['description'] = description
    if dataturbo_share_auth_addition is not None:
        payload['dpc_share_auth_addition'] = dataturbo_share_auth_addition
    if dataturbo_share_auth_deletion is not None:
        payload['dpc_share_auth_deletion'] = dataturbo_share_auth_deletion
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def dataturbo_share_delete(client: DMEAPIClient, dataturbo_share_ids: list,
                     task_remarks: str = None) -> dict:
    """
    批量删除 DataTurbo 共享

    Args:
        client: DME API 客户端
        dataturbo_share_ids: DataTurbo 共享 ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/dpc-shares/delete"

    payload = {
        'dpc_share_ids': dataturbo_share_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def dataturbo_share_show_permissions(client: DMEAPIClient, dataturbo_share_id: str,
                                      page_no: int = 1, page_size: int = 10,
                                      user_id: str = None, user_name: str = None,
                                      permission: str = None) -> dict:
    """
    查询 DataTurbo 共享管理员权限列表

    Args:
        client: DME API 客户端
        dataturbo_share_id: DataTurbo 共享 ID
        page_no: 分页页码，默认 1
        page_size: 每页数据条数，默认 10
        user_id: DataTurbo 管理员 ID（精确查询）
        user_name: DataTurbo 管理员名称（支持模糊搜索）
        permission: DataTurbo 管理员权限，可选值：read_and_write（读写）

    Returns:
        DataTurbo 共享管理员权限列表
    """
    url = f"/rest/fileservice/v1/dpc-shares/{dataturbo_share_id}/dpc-share-auths/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if user_id is not None:
        payload['user_id'] = user_id
    if user_name is not None:
        payload['user_name'] = user_name
    if permission is not None:
        payload['permission'] = permission

    response = client.post(url, json=payload)
    return response


# ============================================================================
# Quota (配额) 子主题相关动作
# ============================================================================

def quota_list(client: DMEAPIClient, page_no: int = 1, page_size: int = 20,
               ids: list = None, raw_ids: list = None, quota_type: str = None,
               parent_type: str = None, parent_raw_id: str = None,
               owner_name: str = None, vstore_id: str = None,
               vstore_raw_id: str = None, storage_id: str = None,
               sort_key: str = None, sort_dir: str = None,
               zone_id: str = None) -> dict:
    """
    查询配额列表

    查询配额列表，支持多种过滤条件。

    Args:
        client: DME API 客户端
        page_no: 分页查询页码，默认 1
        page_size: 每页数据条数，默认 20，范围 1~1000
        ids: 配额的 ID 列表
        raw_ids: 配额在存储设备上的 ID 列表
        quota_type: 配额类型，directory_quota（目录配额），user_quota（用户配额），user_group_quota（用户组配额）
        parent_type: 配额所属父对象类型，filesystem（文件系统或者命名空间），qtree（Quota Tree 或者 Dtree）
        parent_raw_id: 配额所属父对象在存储设备上的 ID
        owner_name: 配额关联的用户或者用户组名称，支持模糊查询
        vstore_id: 配额所属租户的 ID
        vstore_raw_id: 配额所属租户存储设备上的 ID
        storage_id: 配额所属存储设备的 ID
        sort_key: 查询的排序字段，id，space_hard_used_rate（空间使用率），file_hard_used_rate（文件使用率），默认 id
        sort_dir: 排序方向，asc（升序）或 desc（降序），默认 asc
        zone_id: Zone id，仅 OceanStor A800 存储支持

    Returns:
        配额列表
    """
    url = "/rest/fileservice/v1/quotas/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if ids is not None:
        payload['ids'] = ids
    if raw_ids is not None:
        payload['raw_ids'] = raw_ids
    if quota_type is not None:
        payload['quota_type'] = quota_type
    if parent_type is not None:
        payload['parent_type'] = parent_type
    if parent_raw_id is not None:
        payload['parent_raw_id'] = parent_raw_id
    if owner_name is not None:
        payload['owner_name'] = owner_name
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if vstore_raw_id is not None:
        payload['vstore_raw_id'] = vstore_raw_id
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if zone_id is not None:
        payload['zone_id'] = zone_id

    response = client.post(url, json=payload)
    return response


def quota_show(client: DMEAPIClient, quota_id: str) -> dict:
    """
    查询指定配额详情

    Args:
        client: DME API 客户端
        quota_id: 配额 ID

    Returns:
        配额详细信息
    """
    url = "/rest/fileservice/v1/quotas/query"

    payload = {
        'ids': [quota_id],
        'page_no': 1,
        'page_size': 1
    }

    response = client.post(url, json=payload)
    return response


def quota_create(client: DMEAPIClient, parent_id: str, parent_type: str,
                 quota_type: str, space_soft_quota: int = -1,
                 space_hard_quota: int = -1, space_advisory_quota: int = -1,
                 file_soft_quota: int = -1, file_hard_quota: int = -1,
                 file_advisory_quota: int = -1, snap_space_switch: bool = False,
                 soft_grace_time: int = None, quota_owner: dict = None,
                 dir_quota_target: str = None, task_remarks: str = None) -> dict:
    """
    创建配额

    Args:
        client: DME API 客户端
        parent_id: 父资源 ID（文件系统、Dtree 或命名空间的 ID）
        parent_type: 父资源类型，filesystem（文件系统），dtree（Dtree），namespace（命名空间）
        quota_type: 配额类型，directory_quota（目录配额），user_quota（用户配额），user_group_quota（用户组配额）
        space_soft_quota: 空间软配额，单位 Byte，-1 表示无效
        space_hard_quota: 空间硬配额，单位 Byte，-1 表示无效
        space_advisory_quota: 空间建议配额，单位 Byte，-1 表示无效（仅 OceanStor Pacific 支持）
        file_soft_quota: 文件数软配额，-1 表示无效
        file_hard_quota: 文件数硬配额，-1 表示无效
        file_advisory_quota: 文件数建议配额，-1 表示无效（仅 OceanStor Pacific 支持）
        snap_space_switch: 是否统计快照空间，true（统计），false（不统计）
        soft_grace_time: 超限时间，单位天（仅 OceanStor Pacific 支持）
        quota_owner: 配额用户，包含 name 和 type 字段（用户配额或用户组配额时必传）
        dir_quota_target: 目录配额作用目标，dtree（模板目录配额），filesystem（根目录配额）
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/quotas"

    payload = {
        'parent_id': parent_id,
        'parent_type': parent_type,
        'quota_type': quota_type,
        'space_soft_quota': space_soft_quota,
        'space_hard_quota': space_hard_quota,
        'space_advisory_quota': space_advisory_quota,
        'file_soft_quota': file_soft_quota,
        'file_hard_quota': file_hard_quota,
        'file_advisory_quota': file_advisory_quota,
        'snap_space_switch': snap_space_switch
    }

    if soft_grace_time is not None:
        payload['soft_grace_time'] = soft_grace_time
    if quota_owner is not None:
        payload['quota_owner'] = quota_owner
    if dir_quota_target is not None:
        payload['dir_quota_target'] = dir_quota_target
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def quota_modify(client: DMEAPIClient, quota_id: str,
                 space_soft_quota: int = None, space_hard_quota: int = None,
                 space_advisory_quota: int = None, file_soft_quota: int = None,
                 file_hard_quota: int = None, file_advisory_quota: int = None,
                 snap_space_switch: bool = None, soft_grace_time: int = None,
                 task_remarks: str = None) -> dict:
    """
    更新指定配额

    Args:
        client: DME API 客户端
        quota_id: 配额 ID
        space_soft_quota: 空间软配额，单位 Byte，-1 表示无效
        space_hard_quota: 空间硬配额，单位 Byte，-1 表示无效
        space_advisory_quota: 空间建议配额，单位 Byte，-1 表示无效（仅 OceanStor Pacific 支持）
        file_soft_quota: 文件数软配额，-1 表示无效
        file_hard_quota: 文件数硬配额，-1 表示无效
        file_advisory_quota: 文件数建议配额，-1 表示无效（仅 OceanStor Pacific 支持）
        snap_space_switch: 是否统计快照空间，true（统计），false（不统计）
        soft_grace_time: 超限时间，单位天（仅 OceanStor Pacific 支持）
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = f"/rest/fileservice/v1/quotas/{quota_id}"

    payload = {}

    if space_soft_quota is not None:
        payload['space_soft_quota'] = space_soft_quota
    if space_hard_quota is not None:
        payload['space_hard_quota'] = space_hard_quota
    if space_advisory_quota is not None:
        payload['space_advisory_quota'] = space_advisory_quota
    if file_soft_quota is not None:
        payload['file_soft_quota'] = file_soft_quota
    if file_hard_quota is not None:
        payload['file_hard_quota'] = file_hard_quota
    if file_advisory_quota is not None:
        payload['file_advisory_quota'] = file_advisory_quota
    if snap_space_switch is not None:
        payload['snap_space_switch'] = snap_space_switch
    if soft_grace_time is not None:
        payload['soft_grace_time'] = soft_grace_time
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response


def quota_delete(client: DMEAPIClient, quota_ids: list,
                 task_remarks: str = None) -> dict:
    """
    批量删除配额

    Args:
        client: DME API 客户端
        quota_ids: 待删除的配额 ID 列表
        task_remarks: 异步任务备注信息

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/quotas/delete"

    payload = {
        'ids': quota_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


# ============================================================================
# filesystem (文件系统) 子主题相关动作
# ============================================================================

def fs_list(client: DMEAPIClient, page_no: int = 1, page_size: int = 100,
                     sort_dir: str = None, sort_key: str = None, name: str = None,
                     fs_raw_id: str = None, storage_id: str = None) -> dict:
    """
    批量查询文件系统

    批量查询文件系统，返回文件系统概要信息列表。

    Args:
        client: DME API 客户端
        page_no: 分页查询页码，1~10000000，默认 1
        page_size: 每页显示的数量，1~1000，默认 100
        sort_dir: 排序方向，asc（升序）或 desc（降序）
        sort_key: 排序参数，可选值：capacity, available_capacity, capacity_usage_ratio,
                  nfs_count, cifs_count, dpc_count, dtree_count, name, allocate_pool_quota,
                  fs_raw_id, create_time, total_capacity_in_byte, available_capacity_in_byte,
                  alloc_capacity_in_byte, protection_capacity_in_byte, max_file_count, used_file_count
        name: 文件系统名称（支持模糊查询）
        fs_raw_id: 文件系统在存储设备上的 ID
        storage_id: 存储设备 ID

    Returns:
        文件系统列表
    """
    url = "/rest/fileservice/v1/filesystems/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if name is not None:
        payload['name'] = name
    if fs_raw_id is not None:
        payload['fs_raw_id'] = fs_raw_id
    if storage_id is not None:
        payload['storage_id'] = storage_id

    response = client.post(url, json=payload)
    return response


def fs_show(client: DMEAPIClient, filesystem_id: str) -> dict:
    """
    查询指定文件系统详情

    Args:
        client: DME API 客户端
        filesystem_id: 文件系统 ID

    Returns:
        文件系统详细信息
    """
    url = f"/rest/fileservice/v1/filesystems/{filesystem_id}"

    response = client.get(url)
    return response


def fs_delete(client: DMEAPIClient, filesystem_ids: list, task_remarks: str = None) -> dict:
    """
    批量删除文件系统

    Args:
        client: DME API 客户端
        filesystem_ids: 文件系统 ID 列表
        task_remarks: 异步任务备注信息（可选）

    Returns:
        响应数据，包含 task_id（异步任务）
    """
    url = "/rest/fileservice/v1/filesystems/delete"

    payload = {
        'file_system_ids': filesystem_ids
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def fs_batch_modify(client: DMEAPIClient, filesystems: list, task_remarks: str = None) -> dict:
    """
    批量修改文件系统

    仅支持修改名称。

    Args:
        client: DME API 客户端
        filesystems: 待修改的文件系统信息列表，每个元素包含 file_system_id 和 name
        task_remarks: 异步任务备注信息（可选）

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/filesystems/modify"

    payload = {
        'filesystems': filesystems
    }

    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.post(url, json=payload)
    return response


def fs_create(client: DMEAPIClient, storage_id: str, pool_raw_id: str,
                                 filesystem_specs: list, vstore_id: str = None,
                                 zone_id: str = None, task_remarks: str = None,
                                 gfs_group_id: str = None, automatic_update_time: bool = None,
                                 atime_update_mode: str = None, schedule_name: str = None,
                                 quota_switch: bool = None, vaai_switch: bool = None,
                                 initial_distribute_policy: str = None,
                                 capacity_threshold: int = None,
                                 tuning: dict = None) -> dict:
    """
    自定义创建文件系统

    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID
        pool_raw_id: 存储池在指定存储设备上的 ID
        filesystem_specs: 文件系统规格列表，格式：[{"name":"<名称>","count":<数量>,"start_suffix":<起始后缀编号>, "capacity":<容量>, "description":"<描述>"}, ...]，其中capacity单位为GB
        vstore_id: 租户 ID（可选）
        zone_id: 所属 zone 的 ID（可选）
        task_remarks: 异步任务备注信息（可选）
        gfs_group_id: 全局数据空间的 ID（可选）
        automatic_update_time: 是否更新访问时间（可选）
        atime_update_mode: Atime 更新频率，hour/day/close（可选）
        schedule_name: 定时 HyperCDP 计划名称（可选）
        quota_switch: 是否启用配额（可选）
        vaai_switch: VAAI 开关（可选）
        initial_distribute_policy: 容量初始分配策略，auto/highest_perf/performance/capacity（可选）
        capacity_threshold: 总空间容量告警阈值 50-99（可选）
        tuning: 调优参数（可选），格式为json字典，可设置如下参数：
            - deduplication_enabled: 是否开启重复数据删除，可选：true/false，默认false
            - compression_enabled: 是否开启数据压缩，可选：true/false，默认false
            - block_size: 文件系统块大小，单位KB，可选：4/8/16/32/64/128，默认64
            - allocation_type: 分配类型，取值：thin/thick，默认为thin
            - qos_policy_id: QoS策略ID

    Returns:
        响应数据，包含 task_id
    """
    url = "/rest/fileservice/v1/filesystems/customize-filesystems"

    payload = {
        'storage_id': storage_id,
        'pool_raw_id': pool_raw_id,
        'filesystem_specs': filesystem_specs
    }

    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if zone_id is not None:
        payload['zone_id'] = zone_id
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    if gfs_group_id is not None:
        payload['gfs_group_id'] = gfs_group_id
    if automatic_update_time is not None:
        payload['automatic_update_time'] = automatic_update_time
    if atime_update_mode is not None:
        payload['atime_update_mode'] = atime_update_mode
    if schedule_name is not None:
        payload['schedule_name'] = schedule_name
    if quota_switch is not None:
        payload['quota_switch'] = quota_switch
    if vaai_switch is not None:
        payload['vaai_switch'] = vaai_switch
    if initial_distribute_policy is not None:
        payload['initial_distribute_policy'] = initial_distribute_policy
    if capacity_threshold is not None:
        payload['capacity_threshold'] = capacity_threshold
    if tuning is not None:
        payload['tuning'] = tuning

    response = client.post(url, json=payload)
    return response


def fs_query_available(client: DMEAPIClient, feature_type: str,
                                local_storage_id: str, remote_storage_id: str = None,
                                name: str = None, page_no: int = 1,
                                page_size: int = 20, sort_key: str = None,
                                sort_dir: str = None) -> dict:
    """
    查询可用的文件系统

    查询可用于配置增删特性的文件系统。当前仅支持可配置远程复制的文件系统。

    Args:
        client: DME API 客户端
        feature_type: 特性类型，当前仅支持 remote_replication（远程复制）
        local_storage_id: 本端存储设备 ID
        remote_storage_id: 远端存储设备 ID（当 feature_type 为 remote_replication 时必选）
        name: 本端文件系统名称，支持模糊搜索
        page_no: 分页查询页码，默认 1
        page_size: 每页显示的数量，默认 20
        sort_key: 排序字段，name（文件系统名称）或 capacity（文件系统容量）
        sort_dir: 排序方向，asc（升序）或 desc（降序）

    Returns:
        可用文件系统列表
    """
    url = "/rest/fileservice/v1/filesystems/available-filesystems/query"

    payload = {
        'feature_type': feature_type,
        'local_storage_id': local_storage_id
    }

    if remote_storage_id is not None:
        payload['remote_storage_id'] = remote_storage_id
    if name is not None:
        payload['name'] = name
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


def fs_modify(client: DMEAPIClient, file_system_id: str, name: str = None,
           description: str = None, capacity: int = None,
           capacity_threshold: int = None, initial_distribute_policy: str = None,
           automatic_update_time: bool = None, atime_update_mode: str = None,
           quota_switch: bool = None, vaai_switch: bool = None,
           owning_controller: str = None, task_remarks: str = None) -> dict:
    """
    修改指定文件系统

    Args:
        client: DME API 客户端
        file_system_id: 文件系统唯一标识
        name: 文件系统名称（可选）
        description: 描述信息（可选）
        capacity: 文件系统容量，单位 GB（可选）
        capacity_threshold: 总空间容量告警阈值 50-99（可选）
        initial_distribute_policy: 容量初始分配策略，auto/highest_perf/performance/capacity（可选）
        automatic_update_time: 是否更新访问时间（可选）
        atime_update_mode: Atime 更新频率，hour/day/close（可选）
        quota_switch: 是否启用配额（可选）
        vaai_switch: VAAI 开关（可选）
        owning_controller: 所属控制器（可选）
        task_remarks: 异步任务备注信息（可选）

    Returns:
        响应数据，包含 task_id
    """
    url = f"/rest/fileservice/v1/filesystems/{file_system_id}"

    payload = {}

    if name is not None:
        payload['name'] = name
    if description is not None:
        payload['description'] = description
    if capacity is not None:
        payload['capacity'] = capacity
    if capacity_threshold is not None:
        payload['capacity_threshold'] = capacity_threshold
    if initial_distribute_policy is not None:
        payload['initial_distribute_policy'] = initial_distribute_policy
    if automatic_update_time is not None:
        payload['automatic_update_time'] = automatic_update_time
    if atime_update_mode is not None:
        payload['atime_update_mode'] = atime_update_mode
    if quota_switch is not None:
        payload['quota_switch'] = quota_switch
    if vaai_switch is not None:
        payload['vaai_switch'] = vaai_switch
    if owning_controller is not None:
        payload['owning_controller'] = owning_controller
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks

    response = client.put(url, json=payload)
    return response



# ============================================================================
# namespace (命名空间) 子主题相关动作
# ============================================================================

def namespace_list(client: DMEAPIClient, page_no: int = None, page_size: int = None,
         sort_dir: str = None, sort_key: str = None, name: str = None,
         vstore_name: str = None, vstore_raw_id: str = None, vstore_id: str = None,
         raw_id: str = None, pool_name: str = None, storage_id: str = None,
         enable_encrypt: bool = None, support_provisioning: bool = None,
         gfs_id: str = None, gfs_name: str = None, has_gfs: bool = None) -> dict:
    """
    批量查询命名空间
    
    批量查询命名空间信息，支持分页和多种过滤条件。
    
    Args:
        client: DME API 客户端
        page_no: 分页查询页码，最大 10000000
        page_size: 每页显示的数量，默认 100，范围 1~1000
        sort_dir: 排序方向，asc（升序）或 desc（降序）
        sort_key: 排序字段，可选值：name, space_used_rate, file_used_rate
        name: 命名空间名称，支持模糊查询（1~256 个字符）
        vstore_name: 命名空间所属租户名称，支持模糊查询（1~256 个字符）
        vstore_raw_id: 命名空间所属 vStore 在存储设备上分配的 ID（1~128 个字符）
        vstore_id: 命名空间所属 vStore 的 ID（1~128 个字符）
        raw_id: 命名空间在存储设备上的 ID（1~256 个字符）
        pool_name: 存储池名称，支持模糊查询（1~256 个字符）
        storage_id: 归属存储设备 ID（1~255 个字符）
        enable_encrypt: 是否开启加密
        support_provisioning: 是否支持业务发放，过滤不支持业务发放设备的资源
        gfs_id: 全局命名空间 ID（1~64 个字符）
        gfs_name: 全局命名空间名称（1~256 个字符）
        has_gfs: 是否包含所属全局命名空间的命名空间
    
    Returns:
        响应数据，包含：
        - total: 命名空间数量
        - namespace_list: 命名空间列表，包含 id, raw_id, name, storage_id, vstore_id 等信息
    """
    url = "/rest/fileservice/v1/namespaces/query"
    
    payload = {}
    
    if page_no is not None:
        payload['page_no'] = page_no
    if page_size is not None:
        payload['page_size'] = page_size
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if name is not None:
        payload['name'] = name
    if vstore_name is not None:
        payload['vstore_name'] = vstore_name
    if vstore_raw_id is not None:
        payload['vstore_raw_id'] = vstore_raw_id
    if vstore_id is not None:
        payload['vstore_id'] = vstore_id
    if raw_id is not None:
        payload['raw_id'] = raw_id
    if pool_name is not None:
        payload['pool_name'] = pool_name
    if storage_id is not None:
        payload['storage_id'] = storage_id
    if enable_encrypt is not None:
        payload['enable_encrypt'] = enable_encrypt
    if support_provisioning is not None:
        payload['support_provisioning'] = support_provisioning
    if gfs_id is not None:
        payload['gfs_id'] = gfs_id
    if gfs_name is not None:
        payload['gfs_name'] = gfs_name
    if has_gfs is not None:
        payload['has_gfs'] = has_gfs
    
    response = client.post(url, json=payload)
    return response


def namespace_show(client: DMEAPIClient, namespace_id: str) -> dict:
    """
    查询指定命名空间详情
    
    查询指定命名空间的详细信息。
    
    Args:
        client: DME API 客户端
        namespace_id: 命名空间 ID（必选，1~64 个字符）
    
    Returns:
        命名空间详细信息，包含：
        - id: 命名空间 ID
        - raw_id: 命名空间在存储设备上的 ID
        - name: 命名空间名称
        - storage_id: 存储设备 ID
        - vstore_id: 租户 ID
        - vstore_name: 租户名称
        - pool_id: 存储池 ID
        - pool_name: 存储池名称
        - running_status: 运行状态（NORMAL/UNKNOWN）
        - space_used_rate: 空间使用率
        - file_used_rate: 文件使用率
        - space_used: 已使用空间
        - file_used: 已使用文件数
        - trash_enable: 是否开启回收站
        - enable_encrypt: 是否开启加密
        - rdc: 数据冗余份数
        - acl_policy_type: 安全模式
        - gfs_id: 全局命名空间 ID
        - qos_policy: QoS 策略
        - worm: WORM 参数
        等详细信息
    """
    url = f"/rest/fileservice/v1/namespaces/{namespace_id}"
    
    response = client.get(url)
    return response


def namespace_create(client: DMEAPIClient, storage_id: str, pool_raw_id: str,
           namespace_specs: list = None, enable_update_atime: bool = None,
           trash_visible: bool = None, trash_enable: bool = None,
           interval_trash: int = None, dps_switch: bool = None,
           forbidden_dpc: bool = None, audit_log_switch: bool = None,
           audit_log_rule: list = None, atime_update_mode: int = None,
           acl_policy_type: str = None, enable_encrypt: bool = None,
           crypt_alg: str = None, case_sensitive: bool = None,
           show_snap_dir: bool = None, rdc: str = None, worm: dict = None,
           qos_policy: dict = None, public_network_qos_policy: dict = None,
           private_network_qos_policy: dict = None,
           create_s3_param: dict = None, application_type: dict = None,
           task_remarks: str = None) -> dict:
    """
    批量创建命名空间
    
    批量创建命名空间，支持一次创建最多 500 个命名空间。
    
    Args:
        client: DME API 客户端
        storage_id: 存储设备 ID（必填）
        pool_raw_id: 存储池在存储设备上的 ID（必填）
        namespace_specs: 命名空间批量参数（必填），列表格式，每个元素包含：
                        - name: 名称（必填，1~255 个字符）
                        - count: 数量（必填，1~500）
                        - start_suffix: 起始后缀编号（可选，0~9999）
                        - isInGfs: 是否在全局命名空间中（可选）
        enable_update_atime: 是否更新 Atime
        trash_visible: 回收站目录是否可见，默认不可见
        trash_enable: 回收站功能是否开启，默认不开启
        interval_trash: 回收站保护时长（分钟），0 表示永久保留，最大 4294967295
        dps_switch: 元数据检索开关，true 开启
        forbidden_dpc: 是否禁止 dpc 挂载
        audit_log_switch: 是否开启审计日志，默认关闭
        audit_log_rule: 审计日志规则列表，可选值：open, create, read, write, close, 
                       delete, rename, get_attr, set_attr, get_security, set_security,
                       get_xattr, set_xattr, list_dir, contact, mount_or_unmount, login_or_logoff
        atime_update_mode: atime 更新频率，4294967295 关闭，3600 1 小时，86400 1 天
        acl_policy_type: 安全模式，可选值：mixed, unix, native, ntfs，默认 unix
        enable_encrypt: 是否开启加密
        crypt_alg: 加密算法类型，可选值：XTS_AES_128, XTS_AES_256, XTS_SM4
        case_sensitive: 大小写是否敏感，默认不敏感
        show_snap_dir: 快照目录是否可见
        rdc: 数据冗余份数，可选值：redundancy_2, redundancy_3, redundancy_4
        worm: WORM 参数对象，包含 worm_mode, min_protect_period, max_protect_period 等
        qos_policy: QoS 策略参数对象
        public_network_qos_policy: 公网 QoS 参数对象
        private_network_qos_policy: 私网 QoS 参数对象
        create_s3_param: 创建 S3 协议参数对象
        application_type: 应用类型对象
        task_remarks: 异步任务备注信息
    
    Returns:
        响应数据，包含 task_id（异步任务 ID）
    """
    url = "/rest/fileservice/v1/namespaces"
    
    payload = {
        'storage_id': storage_id,
        'pool_raw_id': pool_raw_id
    }
    
    if namespace_specs is not None:
        payload['namespace_specs'] = namespace_specs
    if enable_update_atime is not None:
        payload['enable_update_atime'] = enable_update_atime
    if trash_visible is not None:
        payload['trash_visible'] = trash_visible
    if trash_enable is not None:
        payload['trash_enable'] = trash_enable
    if interval_trash is not None:
        payload['interval_trash'] = interval_trash
    if dps_switch is not None:
        payload['dps_switch'] = dps_switch
    if forbidden_dpc is not None:
        payload['forbidden_dpc'] = forbidden_dpc
    if audit_log_switch is not None:
        payload['audit_log_switch'] = audit_log_switch
    if audit_log_rule is not None:
        payload['audit_log_rule'] = audit_log_rule
    if atime_update_mode is not None:
        payload['atime_update_mode'] = atime_update_mode
    if acl_policy_type is not None:
        payload['acl_policy_type'] = acl_policy_type
    if enable_encrypt is not None:
        payload['enable_encrypt'] = enable_encrypt
    if crypt_alg is not None:
        payload['crypt_alg'] = crypt_alg
    if case_sensitive is not None:
        payload['case_sensitive'] = case_sensitive
    if show_snap_dir is not None:
        payload['show_snap_dir'] = show_snap_dir
    if rdc is not None:
        payload['rdc'] = rdc
    if worm is not None:
        payload['worm'] = worm
    if qos_policy is not None:
        payload['qos_policy'] = qos_policy
    if public_network_qos_policy is not None:
        payload['public_network_qos_policy'] = public_network_qos_policy
    if private_network_qos_policy is not None:
        payload['private_network_qos_policy'] = private_network_qos_policy
    if create_s3_param is not None:
        payload['create_s3_param'] = create_s3_param
    if application_type is not None:
        payload['application_type'] = application_type
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    
    response = client.post(url, json=payload)
    return response


def namespace_modify(client: DMEAPIClient, namespace_id: str,
           enable_update_atime: bool = None, show_snap_dir: bool = None,
           trash_visible: bool = None, trash_enable: bool = None,
           interval_trash: int = None, dps_switch: bool = None,
           forbidden_dpc: bool = None, audit_log_switch: bool = None,
           audit_log_rule: list = None, atime_update_mode: int = None,
           acl_policy_type: str = None, enable_encrypt: bool = None,
           qos_policy: dict = None, public_network_qos_policy: dict = None,
           private_network_qos_policy: dict = None,
           application_type: dict = None, task_remarks: str = None) -> dict:
    """
    修改指定命名空间
    
    修改指定命名空间的配置参数。
    
    Args:
        client: DME API 客户端
        namespace_id: 命名空间 ID（必选，1~64 个字符）
        enable_update_atime: 是否更新 Atime
        show_snap_dir: 快照目录是否可见
        trash_visible: 回收站目录是否可见
        trash_enable: 回收站功能是否开启
        interval_trash: 回收站保护时长（分钟）
        dps_switch: 元数据检索开关
        forbidden_dpc: 是否禁止 dpc 挂载
        audit_log_switch: 是否开启审计日志
        audit_log_rule: 审计日志规则列表
        atime_update_mode: atime 更新频率
        acl_policy_type: 安全模式，可选值：mixed, unix, native, ntfs
        enable_encrypt: 是否开启加密
        qos_policy: QoS 参数对象
        public_network_qos_policy: 公网 QoS 参数对象
        private_network_qos_policy: 私网 QoS 参数对象
        application_type: 应用类型对象
        task_remarks: 异步任务备注信息
    
    Returns:
        响应数据，包含 task_id（异步任务 ID）
    """
    url = f"/rest/fileservice/v1/namespaces/{namespace_id}"
    
    payload = {}
    
    if enable_update_atime is not None:
        payload['enable_update_atime'] = enable_update_atime
    if show_snap_dir is not None:
        payload['show_snap_dir'] = show_snap_dir
    if trash_visible is not None:
        payload['trash_visible'] = trash_visible
    if trash_enable is not None:
        payload['trash_enable'] = trash_enable
    if interval_trash is not None:
        payload['interval_trash'] = interval_trash
    if dps_switch is not None:
        payload['dps_switch'] = dps_switch
    if forbidden_dpc is not None:
        payload['forbidden_dpc'] = forbidden_dpc
    if audit_log_switch is not None:
        payload['audit_log_switch'] = audit_log_switch
    if audit_log_rule is not None:
        payload['audit_log_rule'] = audit_log_rule
    if atime_update_mode is not None:
        payload['atime_update_mode'] = atime_update_mode
    if acl_policy_type is not None:
        payload['acl_policy_type'] = acl_policy_type
    if enable_encrypt is not None:
        payload['enable_encrypt'] = enable_encrypt
    if qos_policy is not None:
        payload['qos_policy'] = qos_policy
    if public_network_qos_policy is not None:
        payload['public_network_qos_policy'] = public_network_qos_policy
    if private_network_qos_policy is not None:
        payload['private_network_qos_policy'] = private_network_qos_policy
    if application_type is not None:
        payload['application_type'] = application_type
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    
    response = client.put(url, json=payload)
    return response


def namespace_delete(client: DMEAPIClient, namespace_ids: list, task_remarks: str = None) -> dict:
    """
    批量删除命名空间
    
    批量删除命名空间，单次最多删除 100 个。
    
    Args:
        client: DME API 客户端
        namespace_ids: 命名空间 ID 列表（必选），数组最大 100 个，最小 1 个
        task_remarks: 异步任务备注信息（可选，0~1024 个字符）
    
    Returns:
        响应数据，包含 task_id（异步任务 ID）
    """
    url = "/rest/fileservice/v1/namespaces/delete"
    
    payload = {
        'namespace_ids': namespace_ids
    }
    
    if task_remarks is not None:
        payload['task_remarks'] = task_remarks
    
    response = client.post(url, json=payload)
    return response

ACTIONS = {
    'dtree_list': {
        'func': dtree_list,
        'description': '查询 Dtree 列表',
        'params': ['id_in_storage', 'name', 'device_name', 'storage_id', 'zone_id', 'manufacturer', 'tier_name', 'fs_name', 'fs_id', 'namespace_name', 'namespace_id', 'quota_switch', 'security_mode', 'nas_locking_policy', 'sort_key', 'sort_dir', 'page_no', 'page_size', 'dc_id', 'dc_name'],
        'subtopic': 'dtree'
    },
    'dtree_show': {
        'func': dtree_show,
        'description': '查询指定 Dtree 详情',
        'params': ['dtree_id'],
        'subtopic': 'dtree'
    },
    'dtree_create': {
        'func': dtree_create,
        'description': '创建并共享 Dtree',
        'params': ['storage_id', 'create_dtrees_param', 'fs_id', 'namespace_id', 'zone_id', 'parent_dir', 'quota_switch', 'security_mode', 'nas_locking_policy', 'create_nfs_share_param', 'create_cifs_share_param', 'dataturbo_share', 'create_worm_param', 'unix_permissions', 'task_remarks'],
        'subtopic': 'dtree'
    },
    'dtree_delete': {
        'func': dtree_delete,
        'description': '批量删除 Dtree',
        'params': ['dtree_ids', 'task_remarks'],
        'subtopic': 'dtree'
    },
    'dtree_modify': {
        'func': dtree_modify,
        'description': '修改指定 Dtree',
        'params': ['dtree_id', 'name', 'quota_switch', 'security_mode', 'nas_locking_policy', 'unix_permissions', 'task_remarks'],
        'subtopic': 'dtree'
    },
    # NFS share 子主题动作
    'nfs_share_list': {
        'func': nfs_share_list,
        'description': '查询 NFS 共享列表',
        'params': ['id_in_storage', 'name', 'share_path', 'exact_share_path', 'device_name', 'storage_id', 'tier_name', 'owning_dtree_name', 'fs_name', 'fs_id', 'owning_dtree_id', 'vstore_name', 'page_no', 'page_size', 'sort_key', 'sort_dir', 'support_provisioning', 'namespace_id', 'namespace_name', 'dc_id', 'dc_name', 'zone_id', 'zone_name', 'zone_ip'],
        'subtopic': 'nfs_share'
    },
    'nfs_share_show': {
        'func': nfs_share_show,
        'description': '查询指定 NFS 共享详情',
        'params': ['nfs_share_id'],
        'subtopic': 'nfs_share'
    },
    'nfs_share_create': {
        'func': nfs_share_create,
        'description': '创建 NFS 共享',
        'params': ['create_nfs_share_param', 'task_remarks'],
        'subtopic': 'nfs_share'
    },
    'nfs_share_modify': {
        'func': nfs_share_modify,
        'description': '修改指定 NFS 共享',
        'params': ['nfs_share_id', 'description', 'character_encoding', 'audit_items', 'show_snapshot_enable', 'nfs_share_client_addition', 'nfs_share_client_modification', 'nfs_share_client_deletion', 'file_name_ex_filters', 'task_remarks'],
        'subtopic': 'nfs_share'
    },
    'nfs_share_delete': {
        'func': nfs_share_delete,
        'description': '批量删除 NFS 共享',
        'params': ['nfs_share_ids', 'task_remarks'],
        'subtopic': 'nfs_share'
    },
    # CIFS 共享子主题动作
    'cifs_share_list': {
        'func': cifs_list,
        'description': '批量查询 CIFS 共享',
        'params': ['raw_id', 'name', 'share_path', 'exact_share_path', 'fs_id', 'fs_name', 'dtree_id', 'dtree_name', 'storage_id', 'storage_name', 'vstore_raw_id', 'vstore_name', 'manufacturer', 'op_lock_enabled', 'notify_enabled', 'offline_file_modes', 'file_extension_filter_enabled', 'abe_enabled', 'page_no', 'page_size', 'sort_key', 'sort_dir', 'namespace_id', 'namespace_name', 'support_provisioning', 'dc_id', 'dc_name'],
        'subtopic': 'cifs_share'
    },
    'cifs_share_show': {
        'func': cifs_show,
        'description': '查询指定 CIFS 共享详情',
        'params': ['cifs_share_id'],
        'subtopic': 'cifs_share'
    },
    'cifs_share_create': {
        'func': cifs_create,
        'description': '创建单个 CIFS 共享',
        'params': ['create_cifs_param', 'fs_id', 'namespace_id', 'task_remarks'],
        'subtopic': 'cifs_share'
    },
    'cifs_share_modify': {
        'func': cifs_modify,
        'description': '修改指定 CIFS 共享',
        'params': ['cifs_share_id', 'description', 'op_lock_enabled', 'notify_enabled', 'ca_enabled', 'offline_file_mode', 'ip_control_enabled', 'abe_enabled', 'audititem_list', 'apply_default_acl', 'file_extension_filter_enabled', 'show_previous_versions_enabled', 'show_snapshot_enabled', 'user_and_user_group_info', 'ip_and_segments', 'file_name_ex_filters', 'task_remarks', 'smb3_encryption_enable', 'unencrypted_access', 'enable_lease'],
        'subtopic': 'cifs_share'
    },
    'cifs_share_delete': {
        'func': cifs_delete,
        'description': '批量删除 CIFS 共享',
        'params': ['cifs_share_ids', 'task_remarks'],
        'subtopic': 'cifs_share'
    },
    'cifs_share_show_permissions': {
        'func': cifs_show_permissions,
        'description': '查询单个 CIFS 共享的权限列表（用户/IP/文件过滤）',
        'params': ['cifs_share_id', 'type', 'user_or_user_group_name', 'domain_type', 'permissions', 'user_or_user_group_raw_id', 'ip_addresses_or_segments', 'ip_or_segments_raw_id', 'rule_type', 'file_name_extension', 'file_extension_name_raw_id', 'sort_key', 'sort_dir', 'page_no', 'page_size'],
        'subtopic': 'cifs_share'
    },
    # dataturbo_share 子主题动作
    'dataturbo_share_list': {
        'func': dataturbo_share_list,
        'description': '查询 DataTurbo 共享列表',
        'params': ['page_no', 'page_size', 'raw_id', 'share_path', 'fs_id', 'fs_name', 'dtree_id', 'dtree_name', 'vstore_id', 'vstore_raw_id', 'vstore_name', 'storage_id', 'storage_name', 'zone_id', 'zone_name', 'scope', 'sort_key', 'sort_dir'],
        'subtopic': 'dataturbo_share'
    },
    'dataturbo_share_show': {
        'func': dataturbo_share_show,
        'description': '查询指定 DataTurbo 共享详情',
        'params': ['dataturbo_share_id'],
        'subtopic': 'dataturbo_share'
    },
    'dataturbo_share_create': {
        'func': dataturbo_share_create,
        'description': '创建 DataTurbo 共享',
        'params': ['charset', 'fs_id', 'dtree_id', 'description', 'dataturbo_share_auth', 'task_remarks'],
        'subtopic': 'dataturbo_share'
    },
    'dataturbo_share_modify': {
        'func': dataturbo_share_modify,
        'description': '修改指定 DataTurbo 共享',
        'params': ['dataturbo_share_id', 'description', 'dataturbo_share_auth_addition', 'dataturbo_share_auth_deletion', 'task_remarks'],
        'subtopic': 'dataturbo_share'
    },
    'dataturbo_share_delete': {
        'func': dataturbo_share_delete,
        'description': '批量删除 DataTurbo 共享',
        'params': ['dataturbo_share_ids', 'task_remarks'],
        'subtopic': 'dataturbo_share'
    },
    'dataturbo_share_show_permissions': {
        'func': dataturbo_share_show_permissions,
        'description': '查询 DataTurbo 共享管理员权限列表',
        'params': ['dataturbo_share_id', 'page_no', 'page_size', 'user_id', 'user_name', 'permission'],
        'subtopic': 'dataturbo_share'
    },
    # quota 子主题动作
    'quota_list': {
        'func': quota_list,
        'description': '查询配额列表',
        'params': ['page_no', 'page_size', 'ids', 'raw_ids', 'quota_type', 'parent_type', 'parent_raw_id', 'owner_name', 'vstore_id', 'vstore_raw_id', 'storage_id', 'sort_key', 'sort_dir', 'zone_id'],
        'subtopic': 'quota'
    },
    'quota_show': {
        'func': quota_show,
        'description': '查询指定配额详情',
        'params': ['quota_id'],
        'subtopic': 'quota'
    },
    'quota_create': {
        'func': quota_create,
        'description': '创建配额',
        'params': ['parent_id', 'parent_type', 'quota_type', 'space_soft_quota', 'space_hard_quota', 'space_advisory_quota', 'file_soft_quota', 'file_hard_quota', 'file_advisory_quota', 'snap_space_switch', 'soft_grace_time', 'quota_owner', 'dir_quota_target', 'task_remarks'],
        'subtopic': 'quota'
    },
    'quota_modify': {
        'func': quota_modify,
        'description': '更新指定配额',
        'params': ['quota_id', 'space_soft_quota', 'space_hard_quota', 'space_advisory_quota', 'file_soft_quota', 'file_hard_quota', 'file_advisory_quota', 'snap_space_switch', 'soft_grace_time', 'task_remarks'],
        'subtopic': 'quota'
    },
    'quota_delete': {
        'func': quota_delete,
        'description': '批量删除配额',
        'params': ['quota_ids', 'task_remarks'],
        'subtopic': 'quota'
    },
    # filesystem 子主题动作
    'filesystem_list': {
        'func': fs_list,
        'description': '批量查询文件系统',
        'params': ['page_no', 'page_size', 'sort_dir', 'sort_key', 'name', 'fs_raw_id', 'storage_id'],
        'subtopic': 'filesystem'
    },
    'filesystem_show': {
        'func': fs_show,
        'description': '查询指定文件系统详情',
        'params': ['filesystem_id'],
        'subtopic': 'filesystem'
    },
    'filesystem_delete': {
        'func': fs_delete,
        'description': '批量删除文件系统',
        'params': ['filesystem_ids', 'task_remarks'],
        'subtopic': 'filesystem'
    },
    'filesystem_batch_modify': {
        'func': fs_batch_modify,
        'description': '批量修改文件系统（支持批量修改名称）',
        'params': ['filesystems', 'task_remarks'],
        'subtopic': 'filesystem'
    },
    'filesystem_create': {
        'func': fs_create,
        'description': '自定义创建文件系统',
        'params': ['storage_id', 'pool_raw_id', 'filesystem_specs', 'vstore_id', 'zone_id', 'task_remarks', 'gfs_group_id', 'automatic_update_time', 'atime_update_mode', 'schedule_name', 'quota_switch', 'vaai_switch', 'initial_distribute_policy', 'capacity_threshold'],
        'subtopic': 'filesystem'
    },
    'filesystem_query_available': {
        'func': fs_query_available,
        'description': '查询可用的文件系统（支持远程复制）',
        'params': ['feature_type', 'local_storage_id', 'remote_storage_id', 'name', 'page_no', 'page_size', 'sort_key', 'sort_dir'],
        'subtopic': 'filesystem'
    },
    'filesystem_modify': {
        'func': fs_modify,
        'description': '修改指定文件系统（完整参数）',
        'params': ['file_system_id', 'name', 'description', 'capacity', 'capacity_threshold', 'initial_distribute_policy', 'automatic_update_time', 'atime_update_mode', 'quota_switch', 'vaai_switch', 'owning_controller', 'task_remarks'],
        'subtopic': 'filesystem'
    },
    # namespace 子主题动作
    'namespace_list': {
        'func': namespace_list,
        'description': '批量查询命名空间',
        'params': ['page_no', 'page_size', 'sort_dir', 'sort_key', 'name', 
                   'vstore_name', 'vstore_raw_id', 'vstore_id', 'raw_id',
                   'pool_name', 'storage_id', 'enable_encrypt', 
                   'support_provisioning', 'gfs_id', 'gfs_name', 'has_gfs'],
        'subtopic': 'namespace'
    },
    'namespace_show': {
        'func': namespace_show,
        'description': '查询指定命名空间详情',
        'params': ['namespace_id'],
        'subtopic': 'namespace'
    },
    'namespace_create': {
        'func': namespace_create,
        'description': '批量创建命名空间',
        'params': ['storage_id', 'pool_raw_id', 'namespace_specs', 
                   'enable_update_atime', 'trash_visible', 'trash_enable',
                   'interval_trash', 'dps_switch', 'forbidden_dpc',
                   'audit_log_switch', 'audit_log_rule', 'atime_update_mode',
                   'acl_policy_type', 'enable_encrypt', 'crypt_alg',
                   'case_sensitive', 'show_snap_dir', 'rdc', 'worm',
                   'qos_policy', 'public_network_qos_policy',
                   'private_network_qos_policy', 'create_s3_param',
                   'application_type', 'task_remarks'],
        'subtopic': 'namespace'
    },
    'namespace_modify': {
        'func': namespace_modify,
        'description': '修改指定命名空间',
        'params': ['namespace_id', 'enable_update_atime', 'show_snap_dir',
                   'trash_visible', 'trash_enable', 'interval_trash',
                   'dps_switch', 'forbidden_dpc', 'audit_log_switch',
                   'audit_log_rule', 'atime_update_mode', 'acl_policy_type',
                   'enable_encrypt', 'qos_policy', 'public_network_qos_policy',
                   'private_network_qos_policy', 'application_type', 'task_remarks'],
        'subtopic': 'namespace'
    },
    'namespace_delete': {
        'func': namespace_delete,
        'description': '批量删除命名空间',
        'params': ['namespace_ids', 'task_remarks'],
        'subtopic': 'namespace'
    },
    # dpc 子主题动作
    'dpc_list': {
        'func': dpc_list,
        'description': '批量查询并行客户端列表',
        'params': ['ids', 'hostname', 'ip', 'mgmt_status', 'status', 'sn', 'storage_id', 'dpc_om_id', 'dpc_type', 'client_version', 'page_no', 'page_size'],
        'subtopic': 'dpc'
    },
    'dpc_show': {
        'func': dpc_show,
        'description': '查询并行客户端详情',
        'params': ['dpc_id'],
        'subtopic': 'dpc'
    },
}