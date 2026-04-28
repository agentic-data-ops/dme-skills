#!/usr/bin/env python
"""
DME API Client - 用于 DME 软件的 REST API 调用
支持 login, get, put, post, delete, wait_task 等方法
"""

import argparse
import os
import sys
import requests
import time
from typing import Optional, Dict, Any


class DMEAPIClient:
    """DME API 客户端类"""

    def __init__(self, endpoint: str, username: str, password: str, 
                 auth_token: str = None, timeout: int = 10):
        """
        初始化 DME API 客户端

        Args:
            endpoint: DME API 端点地址，格式：https://<ip>:<port>
            username: 用户名
            password: 密码
            auth_token: 认证密钥（可选），如果提供则跳过登录直接使用
            timeout: 超时时间（秒），默认 10 秒
        """
        self.endpoint = endpoint.rstrip('/')
        self.username = username
        self.password = password
        self.auth_token = auth_token
        self.timeout = timeout
        self.access_session: Optional[str] = None
        self.roa_rand: Optional[str] = None

        # 设置默认 header
        self.default_headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }

        # 如果提供了认证密钥，直接设置
        if auth_token:
            self.default_headers['X-Auth-Token'] = auth_token

        # SSL 验证关闭
        self.verify_ssl = False

    def login(self) -> bool:
        """
        登录 DME 软件

        Returns:
            bool: 登录成功返回 True，失败返回 False
        """
        # 如果已有认证密钥，跳过登录
        if self.auth_token:
            self.access_session = self.auth_token
            return True

        url = f"{self.endpoint}/rest/plat/smapp/v1/sessions"

        # 正确的参数格式
        payload = {
            'grantType': 'password',
            'userName': self.username,
            'value': self.password
        }

        try:
            # 使用 PUT 请求
            response = requests.put(
                url,
                json=payload,
                headers=self.default_headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )

            if response.status_code == 200:
                data = response.json()
                self.access_session = data.get('accessSession')
                self.roa_rand = data.get('roaRand')
                
                # 设置认证 header
                self.default_headers['X-Auth-Token'] = self.access_session
                
                print(f"登录成功")
                return True
            else:
                print(f"登录失败：HTTP {response.status_code}")
                print(response.text)
                return False
        except Exception as e:
            print(f"登录异常：{e}")
            return False

    def get(self, url: str, query_params: dict = None) -> Optional[Dict]:
        """
        GET 请求

        Args:
            url: API URL（相对路径，如 /rest/storagemgmt/v1/storages）
            query_params: 查询参数字典

        Returns:
            响应数据字典，失败返回 None
        """
        full_url = f"{self.endpoint}{url}"
        
        try:
            response = requests.get(
                full_url,
                params=query_params,
                headers=self.default_headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"GET 请求失败：HTTP {response.status_code}")
                print(response.text)
                return None
        except Exception as e:
            print(f"GET 请求异常：{e}")
            return None

    def post(self, url: str, params: dict = None, json: dict = None) -> Optional[Dict]:
        """
        POST 请求

        Args:
            url: API URL（相对路径）
            params: 查询参数（可选）
            json: 请求体数据

        Returns:
            响应数据字典，失败返回 None
        """
        full_url = f"{self.endpoint}{url}"

        try:
            response = requests.post(
                full_url,
                params=params,
                json=json,
                headers=self.default_headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )

            if response.status_code in [200, 202]:
                # 处理空响应（某些接口成功但无返回内容）
                if not response.text or not response.text.strip():
                    return {}
                return response.json()
            else:
                print(f"POST 请求失败：HTTP {response.status_code}")
                print(response.text)
                return None
        except Exception as e:
            print(f"POST 请求异常：{e}")
            return None

    def put(self, url: str, json: dict = None) -> Optional[Dict]:
        """
        PUT 请求

        Args:
            url: API URL（相对路径）
            json: 请求体数据

        Returns:
            响应数据字典，失败返回 None
        """
        full_url = f"{self.endpoint}{url}"

        try:
            response = requests.put(
                full_url,
                json=json,
                headers=self.default_headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )

            if response.status_code in [200, 202]:
                # 处理空响应（某些接口成功但无返回内容）
                if not response.text or not response.text.strip():
                    return {}
                return response.json()
            else:
                print(f"PUT 请求失败：HTTP {response.status_code}")
                print(response.text)
                return None
        except Exception as e:
            print(f"PUT 请求异常：{e}")
            return None

    def delete(self, url: str) -> Optional[Dict]:
        """
        DELETE 请求

        Args:
            url: API URL（相对路径）

        Returns:
            响应数据字典，失败返回 None
        """
        full_url = f"{self.endpoint}{url}"
        
        try:
            response = requests.delete(
                full_url,
                headers=self.default_headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )

            if response.status_code in [200, 202]:
                # 处理空响应（某些接口成功但无返回内容）
                if not response.text or not response.text.strip():
                    return {}
                return response.json()
            else:
                print(f"DELETE 请求失败：HTTP {response.status_code}")
                print(response.text)
                return None
        except Exception as e:
            print(f"DELETE 请求异常：{e}")
            return None

    def wait_task(self, task_id: str, timeout: int = 300, poll_interval: int = 2) -> Optional[Dict]:
        """
        等待异步任务完成

        Args:
            task_id: 任务 ID
            timeout: 超时时间（秒），默认 300 秒
            poll_interval: 轮询间隔（秒），默认 2 秒

        Returns:
            任务结果数据，失败返回 None
        """
        url = f"/rest/plat/smapp/v1/task/{task_id}"
        start_time = time.time()

        print(f"等待任务 {task_id} 完成...")

        while True:
            elapsed = time.time() - start_time
            if elapsed > timeout:
                print(f"任务等待超时（{timeout}秒）")
                return None

            result = self.get(url)
            
            if result is None:
                print("查询任务状态失败")
                return None

            task_status = result.get('taskStatus')
            progress = result.get('progress', 0)

            if task_status == 'SUCCESS':
                print(f"任务完成 (进度：{progress}%)")
                return result
            elif task_status == 'FAILED':
                print(f"任务失败 (进度：{progress}%)")
                print(f"错误信息：{result.get('errorMsg', '未知错误')}")
                return None
            else:
                # 任务进行中
                print(f"任务进行中... (进度：{progress}%, 已等待：{int(elapsed)}秒)", end='\r')
                time.sleep(poll_interval)


def main():
    """测试入口"""
    parser = argparse.ArgumentParser(description='DME API 客户端测试')
    parser.add_argument('--endpoint', '-e', required=True, help='DME API 端点')
    parser.add_argument('--user', '-u', help='用户名')
    parser.add_argument('--password', '-p', help='密码')
    parser.add_argument('--token', help='认证密钥（可选）')
    parser.add_argument('--test', '-t', choices=['login', 'storages'], help='测试功能')

    args = parser.parse_args()

    # 从环境变量获取
    endpoint = args.endpoint
    username = args.user or os.environ.get('DME_API_USERNAME')
    password = args.password or os.environ.get('DME_API_PASSWORD')
    auth_token = args.token or os.environ.get('DME_API_AUTH_TOKEN')

    if not auth_token and not (username and password):
        print("错误：需要提供用户名和密码，或者认证密钥")
        sys.exit(1)

    # 创建客户端
    client = DMEAPIClient(
        endpoint=endpoint,
        username=username,
        password=password,
        auth_token=auth_token
    )

    # 测试登录
    if args.test == 'login' or not auth_token:
        if not client.login():
            print("登录失败")
            sys.exit(1)

    # 测试查询存储
    if args.test == 'storages':
        result = client.get('/rest/storagemgmt/v1/storages', {'limit': 5})
        if result:
            print(f"查询到 {result.get('total', 0)} 台存储设备")
            for storage in result.get('datas', []):
                print(f"  - {storage.get('name')} ({storage.get('ip')})")


if __name__ == '__main__':
    main()
