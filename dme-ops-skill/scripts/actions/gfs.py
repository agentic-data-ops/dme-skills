"""
GFS (Global File System) 相关操作
"""

import sys
import os

# 添加父目录到路径，以便导入 dme_api_client
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dme_api_client import DMEAPIClient


# ============================================================================
# Dataspace 子主题相关动作
# ============================================================================

def dataspace_list(client: DMEAPIClient, name: str = None, id: str = None,
                   raw_id: str = None, max_site_num: int = None,
                   page_no: int = 1, page_size: int = 100) -> dict:
    """
    批量查询 Omni-Dataverse

    批量查询 Omni-Dataverse，支持多种过滤条件。

    Args:
        client: DME API 客户端
        name: Omni-Dataverse 名称，支持模糊查询
        id: Omni-Dataverse id
        raw_id: Omni-Dataverse 在设备侧的 id
        max_site_num: Omni-Dataverse 下数据服务站点最大数量
        page_no: 分页查询的页码，默认 1，范围 1~10000
        page_size: 分页查询的个数，默认 100，范围 1~1000

    Returns:
        Omni-Dataverse 列表
    """
    url = "/rest/fileservice/v1/gfs-groups/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if name is not None:
        payload['name'] = name
    if id is not None:
        payload['id'] = id
    if raw_id is not None:
        payload['raw_id'] = raw_id
    if max_site_num is not None:
        payload['max_site_num'] = max_site_num

    response = client.post(url, json=payload)
    return response


def dataspace_show(client: DMEAPIClient, id: str = None, name: str = None) -> dict:
    """
    查询指定 Omni-Dataverse 的容量统计信息

    Args:
        client: DME API 客户端
        id: Omni-Dataverse 的 ID，与 name 不能同时为空，都有值时优先使用 ID
        name: Omni-Dataverse 名称，与 id 不能同时为空，都有值时优先使用 ID

    Returns:
        Omni-Dataverse 容量统计信息
    """
    url = "/rest/fileservice/v1/gfs-groups/query-summary"

    payload = {}

    if id is not None:
        payload['id'] = id
    if name is not None:
        payload['name'] = name

    response = client.post(url, json=payload)
    return response


def dataspace_site_list(client: DMEAPIClient, raw_id: str = None,
                        site_role: dict = None, gfs_group_id: str = None,
                        storage_name: str = None, storage_pool_name: str = None,
                        account_name: str = None, page_no: int = 1,
                        page_size: int = 100) -> dict:
    """
    查询 Omni-Dataverse 数据服务站点

    查询 Omni-Dataverse 数据服务站点列表。

    Args:
        client: DME API 客户端
        raw_id: 数据服务站点在设备侧的 id
        site_role: 数据服务站点角色，包含 site_role 字段，取值范围：ORDINARY(普通站点)，METASTORE(元数据服务站点)
        gfs_group_id: Omni-Dataverse id
        storage_name: 根据存储名称查询数据服务站点，支持模糊查询
        storage_pool_name: 根据存储池名称查询数据服务站点，支持模糊查询
        account_name: 根据账户名称查询数据服务站点，支持模糊查询
        page_no: 分页查询的页码，默认 1，范围 1~10000
        page_size: 分页查询的个数，默认 100，范围 1~1000

    Returns:
        数据服务站点列表
    """
    url = "/rest/fileservice/v1/data-service-sites/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if raw_id is not None:
        payload['raw_id'] = raw_id
    if site_role is not None:
        payload['site_role'] = site_role
    if gfs_group_id is not None:
        payload['gfs_group_id'] = gfs_group_id
    if storage_name is not None:
        payload['storage_name'] = storage_name
    if storage_pool_name is not None:
        payload['storage_pool_name'] = storage_pool_name
    if account_name is not None:
        payload['account_name'] = account_name

    response = client.post(url, json=payload)
    return response


# ============================================================================
# Namespace 子主题相关动作
# ============================================================================

def namespace_list(client: DMEAPIClient, name: str = None, gfs_group_name: str = None,
                   gfs_group_id: str = None, gfs_type: str = None,
                   sort_key: str = None, sort_dir: str = None,
                   page_no: int = 1, page_size: int = 20) -> dict:
    """
    批量查询全局命名空间

    批量查询全局命名空间，支持多种过滤条件。

    Args:
        client: DME API 客户端
        name: 全局命名空间的名称，支持模糊搜索
        gfs_group_name: 全局数据空间的名称，支持模糊搜索
        gfs_group_id: 所属全局数据空间的 ID
        gfs_type: 全局命名空间类型，enable_object_multi_version（支持对象多版本），disable_object_multi_version（不支持对象多版本）
        sort_key: 按照指定字段排序，child_name_space_num
        sort_dir: 指定排序方向，asc（升序），desc（降序），默认 asc
        page_no: 分页起始页，默认 1，范围 1~1000
        page_size: 每页查询的数量，默认 20，范围 1~1000

    Returns:
        全局命名空间列表
    """
    url = "/rest/fileservice/v1/gfs/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size
    }

    if name is not None:
        payload['name'] = name
    if gfs_group_name is not None:
        payload['gfs_group_name'] = gfs_group_name
    if gfs_group_id is not None:
        payload['gfs_group_id'] = gfs_group_id
    if gfs_type is not None:
        payload['gfs_type'] = gfs_type
    if sort_key is not None:
        payload['sort_key'] = sort_key
    if sort_dir is not None:
        payload['sort_dir'] = sort_dir

    response = client.post(url, json=payload)
    return response


def namespace_show(client: DMEAPIClient, id: str = None, name_locator: str = None) -> dict:
    """
    查询全局命名空间详情

    Args:
        client: DME API 客户端
        id: 全局命名空间的 ID，与 name_locator 不能同时为空，都有值时优先使用 ID
        name_locator: 名称定位器，格式为：全局命名空间的名称@全局数据空间的名称

    Returns:
        全局命名空间详细信息
    """
    url = "/rest/fileservice/v1/gfs/detail/query"

    payload = {}

    if id is not None:
        payload['id'] = id
    if name_locator is not None:
        payload['name_locator'] = name_locator

    response = client.post(url, json=payload)
    return response


def namespace_create(client: DMEAPIClient, name: str, gfs_group_id: str = None,
                     gfs_group_name: str = None, gfs_mode: str = 'smart_share',
                     single_write_switch: dict = None,
                     smart_share_members: list = None) -> dict:
    """
    创建全局命名空间

    Args:
        client: DME API 客户端
        name: 全局命名空间名称，只支持数字、字母、下划线，特殊字符支持"."、"-"，必须包含字母或数字
        gfs_group_id: 全局数据空间 id，与 gfs_group_name 不能同时为空
        gfs_group_name: 全局数据空间名称，与 gfs_group_id 不能同时为空
        gfs_mode: 全局命名空间模式，默认 smart_share
        single_write_switch: 单写模式开关，包含 switch 字段，取值 close(任意成员可写入)，open(只有一个成员可写入)
        smart_share_members: SmartShare 成员列表，当 gfs_mode 取值为 smart_share 时必选

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs"

    payload = {
        'name': name,
        'gfs_mode': gfs_mode
    }

    if gfs_group_id is not None:
        payload['gfs_group_id'] = gfs_group_id
    if gfs_group_name is not None:
        payload['gfs_group_name'] = gfs_group_name
    if single_write_switch is not None:
        payload['single_write_switch'] = single_write_switch
    if smart_share_members is not None:
        payload['smart_share_members'] = smart_share_members

    response = client.post(url, json=payload)
    return response


def namespace_modify(client: DMEAPIClient, id: str = None, name_locator: str = None,
                     smart_share_members: list = None) -> dict:
    """
    修改指定全局命名空间

    Args:
        client: DME API 客户端
        id: 全局命名空间的 ID，与 name_locator 不能同时为空
        name_locator: 名称定位器，格式为：全局命名空间的名称@全局数据空间的名称
        smart_share_members: SmartShare 成员列表

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs/modify"

    payload = {}

    if id is not None:
        payload['id'] = id
    if name_locator is not None:
        payload['name_locator'] = name_locator
    if smart_share_members is not None:
        payload['smart_share_members'] = smart_share_members

    response = client.post(url, json=payload)
    return response


def namespace_delete(client: DMEAPIClient, id: str = None, name_locator: str = None,
                     is_delete_child: bool = True) -> dict:
    """
    删除指定的全局命名空间

    Args:
        client: DME API 客户端
        id: 全局命名空间的 ID，与 name_locator 不能同时为空
        name_locator: 名称定位器，格式为：全局命名空间的名称@全局数据空间的名称
        is_delete_child: 是否删除子命名空间，默认 true

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs/delete"

    payload = {
        'is_delete_child': is_delete_child
    }

    if id is not None:
        payload['id'] = id
    if name_locator is not None:
        payload['name_locator'] = name_locator

    response = client.post(url, json=payload)
    return response


# ============================================================================
# Migration Task 子主题相关动作
# ============================================================================

def migration_task_list(client: DMEAPIClient, gfs_id: str = None,
                        task_name: str = None, task_id: str = None,
                        target_storage_name: str = None, namespace_name: str = None,
                        namespace_id: str = None, namespace_raw_id: str = None,
                        local_path: str = None, status: list = None,
                        task_mode: list = None, execute_mode: list = None,
                        page_no: int = 1, page_size: int = 20,
                        sort_dir: str = 'desc', sort_key: str = None) -> dict:
    """
    批量查询 Omni-Dataverse 数据迁移任务

    Args:
        client: DME API 客户端
        gfs_id: 全局命名空间 ID
        task_name: 任务名称，支持模糊查询
        task_id: 数据迁移任务在设备侧的 ID
        target_storage_name: 目标站点名称
        namespace_name: 命名空间名称，支持模糊查询
        namespace_id: 命名空间 ID
        namespace_raw_id: 命名空间在设备侧 ID
        local_path: 命名空间下的路径，默认值为"/"，支持模糊查询
        status: 任务状态列表，not_run, synchronizing, completed, suspended, faulty, to_be_scheduled, partially_success, failed, unknown
        task_mode: 任务模式列表，pre_fetch, tier
        execute_mode: 执行模式列表，interval, one_time
        page_no: 分页查询页码，默认 1，范围 1~1000
        page_size: 每页显示的数量，默认 20，范围 1~1000
        sort_dir: 指定排序方向，asc（升序），desc（降序），默认 desc
        sort_key: 排序参数，progress, real_start_time, real_finish_time

    Returns:
        数据迁移任务列表
    """
    url = "/rest/fileservice/v1/gfs/migration-tasks/query"

    payload = {
        'page_no': page_no,
        'page_size': page_size,
        'sort_dir': sort_dir
    }

    if gfs_id is not None:
        payload['gfs_id'] = gfs_id
    if task_name is not None:
        payload['task_name'] = task_name
    if task_id is not None:
        payload['task_id'] = task_id
    if target_storage_name is not None:
        payload['target_storage_name'] = target_storage_name
    if namespace_name is not None:
        payload['namespace_name'] = namespace_name
    if namespace_id is not None:
        payload['namespace_id'] = namespace_id
    if namespace_raw_id is not None:
        payload['namespace_raw_id'] = namespace_raw_id
    if local_path is not None:
        payload['local_path'] = local_path
    if status is not None:
        payload['status'] = status
    if task_mode is not None:
        payload['task_mode'] = task_mode
    if execute_mode is not None:
        payload['execute_mode'] = execute_mode
    if sort_key is not None:
        payload['sort_key'] = sort_key

    response = client.post(url, json=payload)
    return response


def migration_task_show(client: DMEAPIClient, id: str) -> dict:
    """
    查询 Omni-Dataverse 数据迁移任务详情

    Args:
        client: DME API 客户端
        id: 数据迁移任务 ID

    Returns:
        数据迁移任务详细信息
    """
    url = f"/rest/fileservice/v1/gfs/migration-tasks/{id}"

    response = client.get(url)
    return response


def migration_task_create(client: DMEAPIClient, gfs_id: str, task_mode: dict,
                          start_mode: dict, max_bandwidth: int,
                          target_namespace_id: str, task_name: str = None,
                          execute_mode: dict = None, execute_time: int = None,
                          execute_time_unit: dict = None, start_time: int = None,
                          period_start_day: str = None, period_end_day: str = None,
                          period_time: str = None, period_max_bandwidth: str = None,
                          local_path: str = None, src_namespace_ids: list = None,
                          atime_operator: dict = None, atime: int = None,
                          atime_unit: dict = None, mtime_operator: dict = None,
                          mtime: int = None, mtime_unit: dict = None,
                          ctime_operator: dict = None, ctime: int = None,
                          ctime_unit: dict = None, crtime_operator: dict = None,
                          crtime: int = None, crtime_unit: dict = None,
                          name_operator: dict = None, name_filter: str = None,
                          size_operator: dict = None, file_size: int = None,
                          tag: str = None, file_paths: list = None,
                          authentication_type: dict = None, user_operator: dict = None,
                          user_name: str = None, group_operator: dict = None,
                          group_name: str = None, files_filter: dict = None) -> dict:
    """
    创建 Omni-Dataverse 数据迁移任务

    Args:
        client: DME API 客户端
        gfs_id: 全局命名空间 ID
        task_mode: 任务模式，包含 task_mode 字段，取值 pre_fetch(预取缓存), tier(数据拉取)
        start_mode: 启动模式，包含 start_mode 字段
        max_bandwidth: 最大同步速率，单位 MB/s，范围 1~10240
        target_namespace_id: 全局命名空间下目标命名空间 ID
        task_name: 任务名称
        execute_mode: 执行模式，包含 execute_mode 字段，取值 interval(周期性), one_time(一次性)
        execute_time: 周期性任务执行时间间隔
        execute_time_unit: 周期性任务执行时间间隔单位
        start_time: 任务启动的 UTC 时间戳，单位秒
        period_start_day: 指定时间段的起始日期，格式 YYYY-MM-DD
        period_end_day: 指定时间段的结束日期，格式 YYYY-MM-DD
        period_time: 指定时间段的起止时间
        period_max_bandwidth: 指定时间段的带宽上限
        local_path: 命名空间下的路径，默认"/"
        src_namespace_ids: 全局命名空间下源站点命名空间 ID 列表
        atime_operator: 文件的访问时间匹配规则
        atime: 文件的访问时间间隔
        atime_unit: 文件的访问时间间隔单位
        mtime_operator: 文件的修改时间匹配规则
        mtime: 文件的修改时间间隔
        mtime_unit: 文件的修改时间间隔单位
        ctime_operator: 文件的状态修改时间匹配规则
        ctime: 文件的状态修改时间间隔
        ctime_unit: 文件的状态修改时间间隔单位
        crtime_operator: 文件的创建时间匹配规则
        crtime: 文件的创建时间间隔
        crtime_unit: 文件的创建时间间隔单位
        name_operator: 文件名匹配规则
        name_filter: 文件名称过滤规则
        size_operator: 文件大小的匹配规则
        file_size: 文件的大小，单位 KB
        tag: 对象标签匹配规则
        file_paths: 按文件列表过滤策略上传的文件标识列表
        authentication_type: 认证类型
        user_operator: 用户名匹配规则
        user_name: 用户名
        group_operator: 用户组名匹配规则
        group_name: 用户组名
        files_filter: 按文件列表过滤请求参数

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs/migration-tasks"

    payload = {
        'gfs_id': gfs_id,
        'task_mode': task_mode,
        'start_mode': start_mode,
        'max_bandwidth': max_bandwidth,
        'target_namespace_id': target_namespace_id
    }

    if task_name is not None:
        payload['task_name'] = task_name
    if execute_mode is not None:
        payload['execute_mode'] = execute_mode
    if execute_time is not None:
        payload['execute_time'] = execute_time
    if execute_time_unit is not None:
        payload['execute_time_unit'] = execute_time_unit
    if start_time is not None:
        payload['start_time'] = start_time
    if period_start_day is not None:
        payload['period_start_day'] = period_start_day
    if period_end_day is not None:
        payload['period_end_day'] = period_end_day
    if period_time is not None:
        payload['period_time'] = period_time
    if period_max_bandwidth is not None:
        payload['period_max_bandwidth'] = period_max_bandwidth
    if local_path is not None:
        payload['local_path'] = local_path
    if src_namespace_ids is not None:
        payload['src_namespace_ids'] = src_namespace_ids
    if atime_operator is not None:
        payload['atime_operator'] = atime_operator
    if atime is not None:
        payload['atime'] = atime
    if atime_unit is not None:
        payload['atime_unit'] = atime_unit
    if mtime_operator is not None:
        payload['mtime_operator'] = mtime_operator
    if mtime is not None:
        payload['mtime'] = mtime
    if mtime_unit is not None:
        payload['mtime_unit'] = mtime_unit
    if ctime_operator is not None:
        payload['ctime_operator'] = ctime_operator
    if ctime is not None:
        payload['ctime'] = ctime
    if ctime_unit is not None:
        payload['ctime_unit'] = ctime_unit
    if crtime_operator is not None:
        payload['crtime_operator'] = crtime_operator
    if crtime is not None:
        payload['crtime'] = crtime
    if crtime_unit is not None:
        payload['crtime_unit'] = crtime_unit
    if name_operator is not None:
        payload['name_operator'] = name_operator
    if name_filter is not None:
        payload['name_filter'] = name_filter
    if size_operator is not None:
        payload['size_operator'] = size_operator
    if file_size is not None:
        payload['file_size'] = file_size
    if tag is not None:
        payload['tag'] = tag
    if file_paths is not None:
        payload['file_paths'] = file_paths
    if authentication_type is not None:
        payload['authentication_type'] = authentication_type
    if user_operator is not None:
        payload['user_operator'] = user_operator
    if user_name is not None:
        payload['user_name'] = user_name
    if group_operator is not None:
        payload['group_operator'] = group_operator
    if group_name is not None:
        payload['group_name'] = group_name
    if files_filter is not None:
        payload['files_filter'] = files_filter

    response = client.post(url, json=payload)
    return response


def migration_task_modify(client: DMEAPIClient, id: str, task_name: str = None,
                          start_mode: dict = None, start_time: int = None,
                          execute_time: int = None, execute_time_unit: dict = None,
                          max_bandwidth: int = None, period_start_day: str = None,
                          period_end_day: str = None, period_time: str = None,
                          period_max_bandwidth: str = None) -> dict:
    """
    修改 Omni-Dataverse 数据迁移任务

    Args:
        client: DME API 客户端
        id: 数据迁移任务 ID
        task_name: 任务名称
        start_mode: 启动模式
        start_time: 任务启动的 UTC 时间戳，单位秒
        execute_time: 周期性任务执行时间间隔
        execute_time_unit: 周期性任务执行时间间隔单位
        max_bandwidth: 最大同步速率，单位 MB/s
        period_start_day: 指定时间段的起始日期
        period_end_day: 指定时间段的结束日期
        period_time: 指定时间段的起止时间
        period_max_bandwidth: 指定时间段的带宽上限

    Returns:
        响应数据
    """
    url = f"/rest/fileservice/v1/gfs/migration-tasks/{id}"

    payload = {}

    if task_name is not None:
        payload['task_name'] = task_name
    if start_mode is not None:
        payload['start_mode'] = start_mode
    if start_time is not None:
        payload['start_time'] = start_time
    if execute_time is not None:
        payload['execute_time'] = execute_time
    if execute_time_unit is not None:
        payload['execute_time_unit'] = execute_time_unit
    if max_bandwidth is not None:
        payload['max_bandwidth'] = max_bandwidth
    if period_start_day is not None:
        payload['period_start_day'] = period_start_day
    if period_end_day is not None:
        payload['period_end_day'] = period_end_day
    if period_time is not None:
        payload['period_time'] = period_time
    if period_max_bandwidth is not None:
        payload['period_max_bandwidth'] = period_max_bandwidth

    response = client.put(url, json=payload)
    return response


def migration_task_delete(client: DMEAPIClient, ids: list) -> dict:
    """
    批量删除 Omni-Dataverse 数据迁移任务

    Args:
        client: DME API 客户端
        ids: 数据迁移任务 ID 列表

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs/migration-tasks/delete"

    payload = {
        'ids': ids
    }

    response = client.post(url, json=payload)
    return response


def migration_task_operate(client: DMEAPIClient, ids: list, operate_type: dict) -> dict:
    """
    批量暂停或者启动 Omni-Dataverse 数据迁移任务

    Args:
        client: DME API 客户端
        ids: 数据迁移任务 ID 列表
        operate_type: 操作类型，包含 operate_type 字段，取值 start(启动), stop(停止)

    Returns:
        响应数据
    """
    url = "/rest/fileservice/v1/gfs/migration-tasks/operate"

    payload = {
        'ids': ids,
        'operate_type': operate_type
    }

    response = client.post(url, json=payload)
    return response


# 动作列表，用于 CLI 帮助
ACTIONS = {
    # Dataspace 子主题动作
    'dataspace_list': {
        'func': dataspace_list,
        'description': '批量查询 Omni-Dataverse',
        'params': ['name', 'id', 'raw_id', 'max_site_num', 'page_no', 'page_size'],
        'subtopic': 'dataspace'
    },
    'dataspace_show': {
        'func': dataspace_show,
        'description': '查询指定 Omni-Dataverse 的容量统计信息',
        'params': ['id', 'name'],
        'subtopic': 'dataspace'
    },
    'dataspace_site_list': {
        'func': dataspace_site_list,
        'description': '查询 Omni-Dataverse 数据服务站点',
        'params': ['raw_id', 'site_role', 'gfs_group_id', 'storage_name', 'storage_pool_name', 'account_name', 'page_no', 'page_size'],
        'subtopic': 'dataspace'
    },
    # Namespace 子主题动作
    'namespace_list': {
        'func': namespace_list,
        'description': '批量查询全局命名空间',
        'params': ['name', 'gfs_group_name', 'gfs_group_id', 'gfs_type', 'sort_key', 'sort_dir', 'page_no', 'page_size'],
        'subtopic': 'namespace'
    },
    'namespace_show': {
        'func': namespace_show,
        'description': '查询全局命名空间详情',
        'params': ['id', 'name_locator'],
        'subtopic': 'namespace'
    },
    'namespace_create': {
        'func': namespace_create,
        'description': '创建全局命名空间',
        'params': ['name', 'gfs_group_id', 'gfs_group_name', 'gfs_mode', 'single_write_switch', 'smart_share_members'],
        'subtopic': 'namespace'
    },
    'namespace_modify': {
        'func': namespace_modify,
        'description': '修改指定全局命名空间',
        'params': ['id', 'name_locator', 'smart_share_members'],
        'subtopic': 'namespace'
    },
    'namespace_delete': {
        'func': namespace_delete,
        'description': '删除指定的全局命名空间',
        'params': ['id', 'name_locator', 'is_delete_child'],
        'subtopic': 'namespace'
    },
    # Migration Task 子主题动作
    'migration_task_list': {
        'func': migration_task_list,
        'description': '批量查询 Omni-Dataverse 数据迁移任务',
        'params': ['gfs_id', 'task_name', 'task_id', 'target_storage_name', 'namespace_name', 'namespace_id', 'namespace_raw_id', 'local_path', 'status', 'task_mode', 'execute_mode', 'page_no', 'page_size', 'sort_dir', 'sort_key'],
        'subtopic': 'migration_task'
    },
    'migration_task_show': {
        'func': migration_task_show,
        'description': '查询 Omni-Dataverse 数据迁移任务详情',
        'params': ['id'],
        'subtopic': 'migration_task'
    },
    'migration_task_create': {
        'func': migration_task_create,
        'description': '创建 Omni-Dataverse 数据迁移任务',
        'params': ['gfs_id', 'task_mode', 'start_mode', 'max_bandwidth', 'target_namespace_id', 'task_name', 'execute_mode', 'execute_time', 'execute_time_unit', 'start_time', 'period_start_day', 'period_end_day', 'period_time', 'period_max_bandwidth', 'local_path', 'src_namespace_ids', 'atime_operator', 'atime', 'atime_unit', 'mtime_operator', 'mtime', 'mtime_unit', 'ctime_operator', 'ctime', 'ctime_unit', 'crtime_operator', 'crtime', 'crtime_unit', 'name_operator', 'name_filter', 'size_operator', 'file_size', 'tag', 'file_paths', 'authentication_type', 'user_operator', 'user_name', 'group_operator', 'group_name', 'files_filter'],
        'subtopic': 'migration_task'
    },
    'migration_task_modify': {
        'func': migration_task_modify,
        'description': '修改 Omni-Dataverse 数据迁移任务',
        'params': ['id', 'task_name', 'start_mode', 'start_time', 'execute_time', 'execute_time_unit', 'max_bandwidth', 'period_start_day', 'period_end_day', 'period_time', 'period_max_bandwidth'],
        'subtopic': 'migration_task'
    },
    'migration_task_delete': {
        'func': migration_task_delete,
        'description': '批量删除 Omni-Dataverse 数据迁移任务',
        'params': ['ids'],
        'subtopic': 'migration_task'
    },
    'migration_task_operate': {
        'func': migration_task_operate,
        'description': '批量暂停或者启动 Omni-Dataverse 数据迁移任务',
        'params': ['ids', 'operate_type'],
        'subtopic': 'migration_task'
    },
}
