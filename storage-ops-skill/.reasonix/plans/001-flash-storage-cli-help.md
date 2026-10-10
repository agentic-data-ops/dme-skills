# 实施计划：flash-storage CLI 帮助文档解析与命令行帮助参数

## 目标

1. 生成解析脚本 `parse-docs.py`，将参考文档 `../reference/flash-storage/command-reference.md` 解析为主题列表、主题命令列表、命令帮助文件
2. 执行解析脚本并验证结果
3. 在 `cli.py` 中新增 `--list-topics`、`--list-topic-commands`、`--show-command-help` 三个参数，直接读取解析产物提供命令行帮助

## 设计约束

- **工作目录**：`storage-ops-skill/scripts/`
- **代码语言**：英文（注释、docstring、帮助文本、错误信息）
- **解析产物目录**：`storage-ops-skill/scripts/docs/`（与 `parse-docs.py` 同级）
- **参考文档路径**：`../reference/flash-storage/command-reference.md`（相对 scripts/ 目录）
- **只读解析**：parse-docs.py 不修改参考文档
- **帮助由脚本直接读取解析产物提供**：README/SKILL 不再引用参考文档路径（已移除）

## 参考文档结构（已确认）

```
# OceanStor Dorado 6.1.2 Command Reference      (h1)
## <主题>                                       (h2, 17 个；排除 About/CLI Use Guidance 后 15 个)
    <主题解释段落>
    - [<命令组>](#slug)                          (命令组链接列表)
### <命令组>                                    (h3, 110 个)
    <命令组解释段落>
    - [<命令>](#slug)                            (命令链接列表)
#### <命令>                                    (h4, 969 个)
##### Function / Format / Parameters / ...     (h5 小节)
```

统计基准（对照 catalog）：主题 15 个、命令组 110 个、命令 969 个。

## 目录结构（解析产物）

```
scripts/
├── parse-docs.py
└── docs/
    ├── _topics.md                        # 主题列表 + 主题解释（去链接）
    ├── alarm-management-and-notification-management-commands/
    │   ├── _index.md                     # 命令组列表 + 命令列表（含功能描述）
    │   ├── alarm.md                      # 命令帮助（h4 全部小节）
    │   └── add-notification-receiver.md  # 命令帮助，命令空格→-
    ├── basic-operation-commands/
    │   ├── _index.md
    │   └── create-lun.md
    └── ...                               # 共 15 个主题文件夹
```

**命名规则**：
- 主题文件夹：主题标题（h2）小写 + 空格转 `-`（与命令文件名规则一致，便于命令行传参，例如 `--list-topic-commands "basic-operation-commands"`）
- 命令文件：命令名（h4）空格转 `-` + `.md`
- `docs/<topic>/_index.md` 中保留原始标题文字（可读性），路径使用 slug

## 实施步骤

### 1. 生成 parse-docs.py

**输入**：`../reference/flash-storage/command-reference.md`

**解析逻辑**（按行扫描，维护当前标题层级）：

1. **主题列表 → `docs/_topics.md`**
   - 匹配 `^## `（正则 `/^## /`），**排除** `## About This Document` 与 `## CLI Use Guidance`
   - 提取该 h2 到下一个同级或更高级标题之间的内容：
     - 主题解释：h2 后的首个非空段落（到链接列表前）
     - 主题列表：区间内 `- [text](#slug)` 链接行，**去链接只保留文字**（提取 `[text]` 部分）
   - 写入格式：
     ```markdown
     ## <主题标题>
     <主题解释>
     - <命令组1>
     - <命令组2>
     ```

2. **主题命令列表 → `docs/<topic>/_index.md`**
   - 对每个主题区间，匹配 `^### `（h3 命令组），提取 h3 到下一个 h3/h2 之间的命令链接 `- [text](#slug)`，**去链接只保留文字**
   - 不在 `_topics.md` 中的章节自动排除（按主题区间遍历天然满足）
   - 初始写入格式：
     ```markdown
     ## <主题标题>
     ### <命令组1>
     - <命令1>
     - <命令2>
     ```

3. **命令帮助文件 → `docs/<topic>/<command-slug>.md`**
   - 遍历 `docs/<topic>/_index.md` 中的命令列表，在参考文档中定位 `#### <命令>` 区间（到下一个 h4/h3/h2）
   - 提取 h4 下全部小节内容（`##### Function/Format/Parameters/Usage Guidelines/Example/System Response`），原样写入命令文件
   - **文件名冲突处理**：命令 slug 化后可能重复（如 `change hyper_metro_pair general` 存在两个变体页面），第二个及后续加后缀 `-2`、`-3`（记录冲突清单供核对）

4. **更新 `_index.md` 命令描述**
   - 从命令文件的 `##### Function` 小节提取功能描述（小节首个段落）
   - 去掉冗余前缀 `The **<command>** command is used to `（大小写不敏感，去掉后保留句子其余部分）
   - 更新 `_index.md` 中对应命令行为：`- <command>: <command-function>`

5. **输出统计**：解析完成后打印主题数、命令组数、命令数、生成文件数，便于验证

**健壮性**：
- slug 化函数统一处理（小写、非字母数字转 `-`、连续 `-` 合并、去首尾 `-`）
- 找不到对应区间的命令记录警告，不中断

### 2. 执行解析脚本并验证

- 运行 `python3 parse-docs.py`
- 验证项：
  - 主题文件夹 15 个，`_topics.md` 主题条目 15 个
  - `_index.md` 命令总数 = 969（与参考文档 h4 数一致）
  - 命令文件总数 = 969（含冲突后缀）
  - 抽查：`create lun`、`delete lun`、`show alarm` 的命令文件内容完整（含 Function/Format/Parameters/Example）
  - 抽查 `_index.md` 描述格式：`create lun: create LUNs. After creating...`（无冗余前缀）
  - 冲突清单核对

### 3. cli.py 新增 `--list-topics`

- 读取 `docs/_topics.md`（路径基于脚本位置：`os.path.join(os.path.dirname(__file__), "..", "docs", "_topics.md")`）
- 文件不存在时给出友好错误
- 打印文件内容

### 4. cli.py 新增 `--list-topic-commands`

- 新增参数 `--list-topic-commands <topic>`（主题 slug）
- 读取 `docs/<topic>/_index.md` 并打印
- 主题不存在（文件夹缺失）时给出可用的主题列表提示

### 5. cli.py 新增 `--show-command-help`

- 新增参数 `--show-command-help <command>`（命令名，空格转 `-` 处理）
- 搜索：遍历 `docs/*/` 查找 `<command-slug>.md`（命令名 slug 化后匹配文件名）
- 找到则打印文件内容；未找到给出提示（含可选相近命令）

**参数交互说明**：
- 三个帮助参数均**不需要连接设备**（与现有执行命令逻辑互斥：传了帮助参数则跳过 SSH 执行）
- 帮助参数优先级：`--show-command-help` > `--list-topic-commands` > `--list-topics`（任一存在即走帮助分支）
- `--list-topic-commands` / `--show-command-help` 缺参时报错

## 验证方法

1. **解析验证**（步骤 2 的统计项）
2. **CLI 验证**（无需设备，本地运行）：
   ```bash
   python3 flash-storage/cli.py --list-topics
   python3 flash-storage/cli.py --list-topic-commands basic-operation-commands
   python3 flash-storage/cli.py --show-command-help "create lun"
   ```
   逐一核对输出与 docs/ 文件内容一致
3. 无参数/缺少子参数的错误提示检查
4. `python3 -m py_compile` 语法检查
