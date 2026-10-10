# change share_homedir_rule cifs


##### Function

The **change share_homedir_rule cifs** command is used to modify the mapping rule of a Homedir share.

##### Format

**change share_homedir_rule cifs** rule_id=? \[ priority=? \] \[ auto_create=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rule_id=? | Rule ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| priority=? | Priority. | The value is an integer ranging from 1 to 1024 ("1" indicates the highest priority), and the default value is "32". Mapping rules are sorted in descending order of priority and those with the same priority are sorted based on the creation sequence. |
| auto_create=? | Whether to enable the function of creating a home directory automatically. | The value can be "yes" or "no", where: <br>"yes": enables the auto create function.<br>"no": disables the auto create function.<br> The default value is "yes". |

##### Usage Guidelines

None

##### Example

Modify a mapping rule for a Homedir share.

```text
admin:/>change share_homedir_rule cifs rule_id=3 priority=16 auto_create=no
WARNING: You are about to set rules for the Homedir to support the path mapping of multiple file systems. Creating rules with high priority and improving the rule priority may cause interruption of services accessed by users that have been configured with mapping rules of low priority. Deleting mapping rules and lowering priority of existing rules may cause interruption of services accessed by users that have been configured with these mapping rules.
Suggestion: Before performing this operation, confirm that users that have been configured with mapping rules of low priority do not access the share.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
