# change system write_policy


##### Function

The **change system write_policy** command is used to set the write protection switch and the period for a controller to run before the write policy is switched to write protection.

##### Format

**change system write_policy** { write_protect_switch=? \| write_protect_time=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| write_protect_switch=? | Switch of cache write protection. | The value can be: <br>"Enable": The cache write protect will be enabled.<br>"Disable": The cache write protect will not be enabled. |
| write_protect_time=? | Time lasted before the system write policy is converted to write protection. | The value is an integer ranging from 0 to 2160, expressed in hours. |

##### Usage Guidelines

-   The "**change system write_policy** write_protect_switch" command is used to enable or disable write protection for a system after it runs in a single-controller environment for a specified period of time.
-   The "**change system write_policy** write_protect_time" command is used to set the period for a controller to run before the write policy is converted to write protection.

##### Example

Enable the write protection function after the system runs in a single-controller environment for a specified period of time.

```text
admin:/>change system write_policy write_protect_switch=Enable
command executed successfully
```

Enable the system to run in a single controller environment for 1 hour before the cache policy is converted to write protection.

```text
admin:/>change system write_policy write_protect_time=1
command executed successfully
```

##### System Response

None
