# show service ndmp


##### Function

The **show service ndmp** command is used to view NDMP configurations.

##### Format

**show service ndmp**

##### Parameters

None

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the NDMP configuration.

```text
admin:/>show service ndmp
Is Enabled:Yes
User Name:--
Port:10000
IP:--
Restoring Quota(%):--
Support Snapshot:--
Version:4
Ignore CTime:No
Password Expired:--
PIM Buffer(MB):--
Prefetch Enable:--
Readdir Plus Enable:--
Data Connect Mode:--
FS Global Scope:Off
Ads Enable:--
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Is Enabled | Whether to enable NDMP. |
| User Name | NDMP user name. NOTE: This field is not supported in the current version and the command output is invalid. |
| Port | Port number. |
| IP | Listening IP address. NOTE: This field is not supported in the current version and the command output is invalid. |
| Restoring Quota(%) | Quota restored to the file system. NOTE: This field is not supported in this version and the command output is invalid. |
| Support Snapshot | Whether snapshots are supported. NOTE: This field is not supported in the current version and the command output is invalid. |
| Version | NDMP protocol version. |
| Ignore CTime | Whether to ignore ctime during backup. |
| Password Expired | Whether the password expires. NOTE: This field is not supported in the current version and the command output is invalid. |
| PIM Buffer(MB) | Buffer size of the PIM module. NOTE: This field is not supported in the current version and the command output is invalid. |
| Prefetch Enable | Whether the prefetch function is enabled. NOTE: This field is not supported in the current version and the command output is invalid. |
| Readdir Plus Enable | Whether the Readdir Plus function is enabled. NOTE: This field is not supported in the current version and the command output is invalid. |
| Data Connect Mode | LIF port mode is used for data connection. NOTE: This field is not supported in the current version and the command output is invalid. |
| FS Global Scope | Whether the vStore file system is globally visible. |
| Ads Enable | Whether the ADS function is enabled. NOTE: This field is not supported in the current version and the command output is invalid. |
