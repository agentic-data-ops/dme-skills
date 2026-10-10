# create share_homedir_rule cifs


##### Function

The **create share_homedir_rule cifs** command is used to create a mapping rule for a Homedir share.

##### Format

**create share_homedir_rule cifs** share_id=? user_name=? path=? \[ priority=? \] \[ auto_create=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_id=? | Share ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| user_name=? | User name. | The value contains 1 to 255 characters. It can be a common user name or a domain user name. A domain user name is in the format of Domain name\Domain user name. Wildcard * is supported, while each user name can contain only one wildcard * at the end. A user name cannot contain special characters "/[]<>+:;,?=|@ and spaces, and cannot end with a period (.). |
| path=? | File system path of the user's home directory. | The value contains 1 to 1023 characters. |
| priority=? | Priority. | The value is an integer ranging from 1 to 1024 ("1" indicates the highest priority), and the default value is "32". Mapping rules are sorted in descending order of priority and those with the same priority are sorted based on the creation sequence. |
| auto_create=? | Whether to enable the function of creating a home directory automatically. | The value can be "yes" or "no", where: <br>"yes": enables the auto create function.<br>"no": disables the auto create function.<br> The default value is "yes". |

##### Usage Guidelines

Parameters "share_id", "user_name", and "path" must be entered at the same time.

##### Example

Create a mapping rule for a Homedir share.

```text
admin:/>create share_homedir_rule cifs share_id=3 user_name=china/* path=/fs0
WARNING: You are about to set rules for the Homedir to support the path mapping of multiple file systems. Creating rules with high priority and improving the rule priority may cause interruption of services accessed by users that have been configured with mapping rules of low priority. Deleting mapping rules and lowering priority of existing rules may cause interruption of services accessed by users that have been configured with these mapping rules.
Suggestion: Before performing this operation, confirm that users that have been configured with mapping rules of low priority do not access the share.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query the created mapping rules.

```text
admin:/>show share_homedir_rule cifs
Rule ID       Share ID  Name       FileSystem ID  Priority  Auto Create  Path
------------  --------  ---------  -------------  --------  -----------  -----
154618822789  36        #$%        0              32        Yes          /fs0/
154618822788  36        #%#$%      0              32        Yes          /fs0/
304942678150  71        1          0              32        No           /fs0/
287762808963  67        asdfsadf   0              1024      No           /fs0/
```

##### System Response

None
