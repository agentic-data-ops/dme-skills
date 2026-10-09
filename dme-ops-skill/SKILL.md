---
name: dme-ops-skill
description: DME operations skill for day-to-day storage device administration, including storage monitoring, analysis, and configuration operations.
---

# DME Operations Skill

DME operations skill for day-to-day storage device administration, including storage monitoring, analysis, and configuration operations.

## Install Dependencies

```bash
pip install git+https://github.com/agentic-data-ops/dme-python-sdk.git
```

## Set Environment Variables

```
DME_API_ENDPOINT=https://dme-float-ip:26335
DME_API_USERNAME=your-username
DME_API_PASSWORD=your-password
```

## Set Comment Language

The CLI supports bilingual comments. Set the language via the DME_CLI_LANG environment variable or the --lang argument:

```bash
# Chinese (default)
export DME_CLI_LANG=zh_CN

# English
export DME_CLI_LANG=en_US

# Or pass --lang per invocation (takes precedence over the environment variable)
pydme --lang en_US storage list --help
```

## Standard Workflow

1. **Get help information**: Run `pydme --list-topics` to list all available topics and actions
2. **Plan execution steps**: Plan the execution steps based on the user's request
3. **Execute action steps**:
   - Run `pydme <topic> <subtopic> <action> --help` to get action parameter help
   - Run `pydme <topic> <subtopic> <action> --param1 value1 --param2 value2` to execute the action (ask the user for confirmation before executing change operations)
   - If the action returns an asynchronous task ID, run `pydme system task wait` to wait for the task to complete
   - Plan the subsequent actions
4. **Summarize output**: Format the output information and provide a summary
5. **Suggest next steps**: Based on the output and the help information of related topics, suggest next steps to the user

## Notes

1. **Pagination**: Some interfaces support pagination; set an appropriate `page_size`
2. **Asynchronous tasks**: Some operations (such as add, delete, modify) return an asynchronous task ID, which can be tracked with `pydme system task wait`
3. **Environment variables**: DME connection settings can be provided via environment variables to avoid entering them every time
4. **Risk confirmation**: Risky actions are intercepted by the pydme CLI; you must obtain user confirmation before re-running with `--accept-risk`
5. **Filter queries**: Get the action help before querying object lists and use filters where possible to avoid large result sets
6. **Complex parameter formats**: If an action's CLI help shows a parameter with internal structure, specify it as a JSON string; JSON parameters must use double quotes

## Reference

- `reference/dme-python-sdk/README.md` - DME Python SDK reference documentation

## Command Line Tool

### Command Format

The CLI supports two command formats, determined automatically by the API URI hierarchy:

**Two-level structure** (direct action):
```bash
pydme <topic> <action> --param1 value1 --param2 value2
```

**Three-level structure** (subtopic action):
```bash
pydme <topic> <subtopic> <action> --param1 value1 --param2 value2
```

### Arguments

**Global arguments**:
- `--endpoint` / `-e`: DME API access address, format: `https://<dme_ip_address>:<dme_port>`, can be passed via the `DME_API_ENDPOINT` environment variable
- `--user` / `-u`: DME API username, can be passed via the `DME_API_USERNAME` environment variable
- `--password` / `-p`: DME API password, can be passed via the `DME_API_PASSWORD` environment variable
- `--timeout`: API request timeout in seconds, default 90 seconds
- `--list-topics`: List all available topics (tree structure)
- `--accept-risk`: Confirm acceptance of risk, can be passed via the `DME_ACCEPT_RISK` environment variable (not recommended via environment variable)

**Positional arguments**:
- `topic`: Action topic, e.g.: `storage`, `storagepool`, `lun`, `filesystem`, `host`, `task`, `system`
- `subtopic`: Subtopic (optional), e.g.: `disk`, `fan`, `node`, `pool`, `snapshot`, `initiator`
- `action`: Action name, e.g.: `list`, `create`, `delete`, `show`, `modify`

### Help

```bash
# View all topics and actions (tree structure)
pydme --list-topics

# View topic help (shows all direct actions and subtopics)
pydme <topic> --help

# View subtopic help
pydme <topic> <subtopic> --help

# View action parameter help
pydme <topic> <action> --help
pydme <topic> <subtopic> <action> --help
```
