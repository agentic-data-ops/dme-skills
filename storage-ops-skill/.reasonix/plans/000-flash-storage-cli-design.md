# 目标
生成脚本scripts/flash-storage/cli.py，实现一个FlashStorageCLI类，通过python调用expect，实现ssh远程登录闪存存储设备CLI，交互式执行命令

## 构造函数

入参：
- address：设备地址
- username：用户名
- password：密码
- mode：命令行模式，可选，默认值：normal，支持枚举：normal（普通模式），developer（开发者模式）, engineer（工程师模式），debug（诊断模式），minisystem（小系统模式））
- timeout: 命令超时时间，可选，默认值：60秒

具体实现：

1. 启动后台进程expect，设置默认超时时间，发送ssh命令登录设备，输入密码，等待命令行提示符"{username}:/>"，例如：

    ```
    set timeout 30
    spawn ssh -o StrictHostKeyChecking=no {username}@{address}
    expect "password:"
    send "{password}\r"
    expect "{username}:/>"
    ```

2. 根据mode参数，设置命令行模式：

- normal：普通模式，不设置任何参数，命令行提示符为"{username}:/>"

- engineer：工程师模式，设置参数：change user_mode current_mode user_mode=engineer，命令行提示符为"engineer:/>"

    ```
    send "change user_mode current_mode user_mode=engineer\r"
    expect "engineer:/>"
    ```

- developer：开发者模式，设置参数：change user_mode current_mode user_mode=developer，接受风险提示，命令行提示符为"developer:/>"

    ```
    send "change user_mode current_mode user_mode=developer\r"
    expect "(y/n)"
    send "y\r"
    expect "(y/n)"
    send "y\r"
    expect "developer:/>"
    ```

- debug: 诊断模式，进入developer模式之后再输入：debug，命令行提示符为"{username}:/diagnose>"

    ```
    send "debug\r"
    expect "{username}:/diagnose>"
    ```

- minisystem：小系统模式，进入developer模式之后再输入：minisystem，命令行提示符为"Storage: minisystem>"

    ```
    send "minisystem\r"
    expect "Storage: minisystem>"
    ```

## 切换模式

入参：
- mode：命令行模式，可选，支持枚举：normal（普通模式），developer（开发者模式）, engineer（工程师模式），debug（诊断模式），minisystem（小系统模式）

具体实现：

1. 如果切换的模式与当前模式不一致，首先退出当前模式到normal模式：

- engineer：退出工程师模式到normal模式，直接输入：exit，等待命令行提示符"{username}:/>"，例如：

    ```
    send "exit\r"
    expect "{username}:/>"
    ```

- developer：退出开发者模式到normal模式，直接输入：exit，等待命令行提示符"{username}:/>"，例如：

    ```
    send "exit\r"
    expect "{username}:/>"
    ```

- debug: 退出诊断模式到normal模式，需要先退出到developer模式，再输入：exit，等待命令行提示符"{username}:/>"，例如：

    ```
    send "exit\r"
    expect "developer:/>"
    send "exit\r"
    expect "{username}:/>"
    ```

- minisystem：退出小系统模式到normal模式，需要先退出到developer模式，再输入：exit，等待命令行提示符"{username}:/>"，例如：

    ```
    send "exit\r"
    expect "(y/n)"
    send "y\r"
    expect "developer:/>"
    send "exit\r"
    expect "{username}:/>"
    ```

2. 根据mode参数，进入命令行模式（同构造函数）

## 执行单条命令

入参：
- command：要执行的命令
- mode：命令行模式，可选，默认值：normal，支持枚举：normal（普通模式），developer（开发者模式）, engineer（工程师模式），debug（诊断模式），minisystem（小系统模式））

具体实现：

1. 发送命令到设备，等待命令执行完成，如果有风险提示则接受，例如：


    ```
    send "{command}\r"
    expect {
        "(y/n)" {
            send "y\r"
            exp_continue
        }
        "{prompt[mode]}" {}
    }
    ```

2. 返回命令执行结果


## 执行多条命令

入参：
- commands：要执行的命令列表
- mode：命令行模式，可选，默认值：normal，支持枚举：normal（普通模式），developer（开发者模式）, engineer（工程师模式），debug（诊断模式），minisystem（小系统模式）

具体实现：

1. 循环执行命令列表中的命令，调用执行单条命令函数，例如：

    ```
    for command in commands:
        self.execute_single_command(command, mode)
    ```

2. 返回命令执行结果


## 关闭连接

具体实现：

1. 退出当前模式到normal模式（同切换模式函数）
2. 发送exit命令退出命令行，等待命令执行完成，例如：

    ```
    send "exit\r"
    expect "(y/n):"
    send "y\r"
    expect eof
    ```

3. 关闭后台进程expect


## main 函数

具体实现：

1. 解析命令行参数，获取设备地址（可通过STORAGE_ADDRESS环境变量传入）、用户名（可通过STORAGE_USERNAME环境变量传入）、密码（可通过STORAGE_PASSWORD环境变量传入）、超时时间（可通过STORAGE_TIMEOUT环境变量传入）、模式、命令（通过换行符\n拆分为多个命令）
2. 创建FlashStorageCLI对象，调用执行多条命令函数，打印命令执行结果
3. 调用关闭连接函数，关闭连接
