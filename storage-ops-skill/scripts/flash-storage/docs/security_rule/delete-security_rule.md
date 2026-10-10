# delete security_rule


##### Function

The **delete security_rule** command is used to delete security rules.

##### Format

**delete security_rule** rule_id=?

##### Parameters

| Parameter | Description            | Value                                                                               |
|-----------|------------------------|-------------------------------------------------------------------------------------|
| rule_id=? | ID of a security rule. | To obtain the value, run "show security_rule".The value is an integer from 1 to 32. |

##### Usage Guidelines

Deleted security rules cannot be restored.

##### Example

Delete security rule "31".

```text
admin:/>delete security_rule rule_id=31
WARNING: You are about to delete an IP address white list. This operation will make the IP addresses in this IP address white list unable to access the storage system when the IP address security rule is enabled.
Suggestion: Confirm that you need to delete this IP address white list.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
