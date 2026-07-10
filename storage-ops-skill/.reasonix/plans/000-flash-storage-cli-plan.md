# 实施计划：flash-storage CLI

## 设计约束

- **不允许使用 pexpect**：通过系统 `expect` 命令实现 SSH 交互
- **后台 expect 进程**：`subprocess.Popen` 启动持久 expect 进程，通过 stdin/stdout 管道通信
- **严格遵循设计文档的 expect 交互样例**：不加额外的协议封装层
- **命令以 `\r` 结尾**：Python 向 expect 的 stdin 写入 `command\r`，不做 `\n` 或 `\r\n`
- **密码直接传递**：不做特殊处理
- **无人工注入标记**：通过设备提示符判断命令执行结束

## 架构概要

```
┌─────────────────────┐      stdin (command\r)       ┌─────────────────────────┐
│  FlashStorageCLI    │ ──────────────────────────▶  │  expect 后台进程         │
│  (Python)            │                              │  (persistent, via -c)   │
│                      │ ◀────────────────────────── │                         │
│  _current_mode      │   stdout (设备原始输出)      │  spawn ssh → login      │
│  _prompt             │                              │  → loop: expect_user    │
│  expect_process      │                              │    → send → expect      │
└─────────────────────┘                              └─────────────────────────┘
```

## 实施步骤

### 1. 创建目录结构

   - 创建 `storage-ops-skill/scripts/flash-storage/`
   - 创建 `storage-ops-skill/scripts/flash-storage/__init__.py`
   - 创建 `storage-ops-skill/scripts/flash-storage/cli.py`

### 2. 实现 expect 守护进程（嵌入在 cli.py 的 Python 字符串中）

   - 模板字符串 `_EXPECT_DAEMON_SCRIPT`，格式化注入参数
   - `spawn ssh` → `expect password:` → `send password` → `expect {username}:/>`
   - 主循环：`expect_user -re "(.*)\r"` 接收命令
   - `__QUIT__`：`send "exit\r"` → `expect "(y/n):"` → `send "y\r"` → `expect eof` → exit
   - 其他命令：`send "$command\r"` → multi-pattern expect `{(y/n) {send y; exp_continue} -re ":/>|/diagnose>|minisystem>" {输出 buffer} timeout {输出超时信息}}`
   - 仅 `==LOGIN_OK==` 用于 Python 确认登录完成

### 3. 实现 `FlashStorageCLI` 类

   - `__init__`：启动 expect 子进程，读取 `==LOGIN_OK==`，初始化状态
   - `switch_mode(mode)`：Python 侧管理完整退出/进入路由，严格按设计文档
   - `execute_command(command, mode)`：切换模式 → 发送命令 → 逐行读输出到提示符 → 取纯结果
   - `execute_commands(commands, mode)`：遍历调用 execute_command
   - `close()`：退到 normal → 发送 `__QUIT__` → 等待子进程结束

### 4. 实现 main 入口

   - argparse + 环境变量支持
   - 创建 CLI → 执行命令 → 打印 → 关闭

### 5. 语法验证

   - `python -m py_compile`
