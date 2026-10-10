# change smart_cache_pool switch


##### Function

The **change smart_cache_pool switch** command is used to enable or disable a SmartCache pool.

##### Format

**change smart_cache_pool switch** smartCacheSwitch=? \[ id=? \| name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| smartCacheSwitch | Whether to enable or disable a SmartCache pool. | The value can be "close" or "open", where: <br>"close": disables a SmartCache pool.<br>"open": enables a SmartCache pool. |
| id | ID of a SmartCache pool. | The value is an integer ranging from 1 to 16. |
| name | Name of a SmartCache pool. | The value contains 1 to 255 characters, including letters, digits, underscores (_), periods (.), and hyphens (-). |

##### Usage Guidelines

Running the "**change smart_cache_pool switch**" command requires you to specify the ID or name of a SmartCache pool and whether you want to enable or disable the SmartCache pool.

##### Example

Enable a SmartCache pool by ID.

```text
admin:/>change smart_cache_pool switch smartCacheSwitch=close id=1
WARNING: You are about to modify the SmartCache pool switch configuration. This operation will delete the cache data of the SmartCache pool without affecting the main memory data, and will change the original SmartCache policy.
Suggestion: Before performing this operation, read the SmartCache pool switch prompt carefully.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable a SmartCache pool by name.

```text
admin:/>change smart_cache_pool switch smartCacheSwitch=close name=newsmartcache
WARNING: You are about to modify the SmartCache pool switch configuration. This operation will delete the cache data of the SmartCache pool without affecting the main memory data, and will change the original SmartCache policy.
Suggestion: Before performing this operation, read the SmartCache pool switch prompt carefully.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
