# delete share_homedir_rule cifs


##### Function

The **delete share_homedir_rule cifs** command is used to delete a mapping rule from a Homedir share.

##### Format

**delete share_homedir_rule cifs** rule_id=?

##### Parameters

| Parameter | Description | Value                                                                 |
|-----------|-------------|-----------------------------------------------------------------------|
| rule_id=? | Rule ID.    | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |

##### Usage Guidelines

None

##### Example

Delete a mapping rule for a Homedir share.

```text
admin:/>delete share_homedir_rule cifs rule_id=3
WARNING: You are about to set rules for the Homedir to support the path mapping of multiple file systems. Creating rules with high priority and improving the rule priority may cause interruption of services accessed by users that have been configured with mapping rules of low priority. Deleting mapping rules and lowering priority of existing rules may cause interruption of services accessed by users that have been configured with these mapping rules.
Suggestion: Before performing this operation, confirm that users that have been configured with mapping rules of low priority do not access the share.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
