# show share_permission nfs_count


##### Function

The **show share_permission nfs_count** command is used to query the number of NFS share permissions.

##### Format

**show share_permission nfs_count** { \[ share_id=? \] \| \[ access_name=? \] }

##### Parameters

| Parameter     | Description                                                                                             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| share_id=?    | NFS share ID.                                                                                           | The value is an integer ranging from 1 to 18446744073709551615.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| access_name=? | Access object, which can be an IP address, host name, network group, network segment, or asterisk (\*). | The value contains 1 to 256 characters. If the value is a network group, add an at sign (@) at the beginning of the network group name to distinguish it from host names. If the value is a host name: 1:The value can contain letters, digits, hyphens (-), periods (.), and underscores (\_). 2:The value must start with a letter or digit and cannot end with a hyphen (-) or underscore (\_). 3:The value cannot contain consecutive periods (.), or combination of a period and hyphen (.- or -.), or the combination of a period and underscore (.\_ or \_.). 4:The value cannot contain digits only. 5:You are advised to use a Fully qualified domain name (FQDN). |

##### Usage Guidelines

None

##### Example

To query the number of permissions of an NFS share, run the following command:

```text
admin:/>show share_permission nfs_count
Number : 5
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                          |
|-----------|----------------------------------|
| Number    | Number of NFS share permissions. |
