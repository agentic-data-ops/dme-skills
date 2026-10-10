# change devicemanager web_config


##### Function

The **change devicemanager web_config** command is used to configure the web_config SameSite field used by the DeviceManager service.

##### Format

**change devicemanager web_config** attribute_name=? value=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| attribute_name=? | attribute name. | same_site. |
| value=? | SameSite Cookie mode. | The value can be: <br>"lax": lax mode.<br>"strict": strict mode. |

##### Usage Guidelines

After this operation, SameSite Cookie will be set to the Lax or Strict mode.

##### Example

Set SameSite Cookie to the "lax" mode.

```text
admin:/>change devicemanager web_config attribute_name=same_site value=lax
Command executed successfully.
```

Set SameSite Cookie to the "strict" mode.

```text
change devicemanager web_config attribute_name=same_site value=strict
Command executed successfully.
```

##### System Response

None
