# change service cifs


##### Function

The **change service cifs** command is used to modify the settings of the CIFS share service.

##### Format

**change service cifs** { status=? \| security_model=? \| guest_enabled=? \| anonymous_enabled=? \| signing_required_enabled=? \| signing_enabled=? \| oplock_enabled=? \| oplock_timeout=? \| notify_enabled=? \| durable_handle_enabled=? \| durable_handle_timeout=? \| abse_enabled=? \| smb1_enable=? \| smb2_enable=? \| global_namespace_capacity=? \| global_namespace_forward_enabled=? \| smb2_enabled_for_dc_connections=? \| leasev2_enable=? \| smb1_enabled_for_linux=? \| max_sessions_displays=? \| max_open_files_display=? \| domainname_configurable_enable=? \| administrators_privilege=? \| cifs_symlink_enable=? \| session_security_for_ad_ldap=? \| inherit_parent_mode_enable=? \| default_dir_mode=? \| default_file_mode=? \| ntfs_set_acl_chown_disable=? \| notify_time_interval=? \| smb_session_expire_time=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| status=? | Running status of the CIFS share service. | The value can be "stop" or "start", where: <br>"stop": The CIFS share service stops.<br>"start": The CIFS share service starts. |
| security_model=? | Authentication mode. | The value can be "local_attestation", "domain_attestation", or "all_attestation", where: <br>"local_attestation": local authentication.<br>"domain_attestation": domain authentication.<br>"all_attestation": local authentication and domain authentication. |
| guest_enabled=? | Whether guest access is allowed. | The value can be "yes" or "no", where: <br>"yes": Guest access is allowed.<br>"no": Guest access is forbidden. |
| anonymous_enabled=? | Whether anonymous access is allowed. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": Anonymous access is allowed.<br>"no": Anonymous access is forbidden. |
| signing_required_enabled=? | Whether the CIFS client must support the signature. | The value can be "yes" or "no", where: <br>"yes": The signature must be supported.<br>"no": The signature cannot be supported. |
| signing_enabled=? | Whether to enable the signature function for CIFS. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": The signature is enabled.<br>"no": The signature is disabled. |
| oplock_enabled=? | Whether to enable opportunistic locking (Oplock) (with a protocol lock, the file system does not require a lock). | The value can be "yes" or "no", where: <br>"yes": Oplock is enabled.<br>"no": Oplock is disabled. |
| oplock_timeout=? | Timeout period of oplock. | The value ranges from 5 to 35. |
| notify_enabled=? | Whether to enable Notify. | The value can be "yes" or "no", where: <br>"yes": Notify is enabled.<br>"no": Notify is disabled. |
| durable_handle_enabled=? | Whether to enable durable handle. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": Durable handle is enabled.<br>"no": Durable handle is disabled. |
| durable_handle_timeout=? | Timeout period of durable handles. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value ranges from 60 to 960. |
| abse_enabled=? | Whether access based on share enumeration is allowed. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": Access based on share enumeration is allowed.<br>"no": Access based on share enumeration is forbidden. |
| smb1_enable=? | Whether to enable SMB1. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": SMB1 is enabled.<br>"no": SMB1 is disabled. |
| smb2_enable=? | Whether to enable SMB2. | The value can be "yes" or "no", where: <br>"yes": SMB2 is enabled.<br>"no": SMB2 is disabled. |
| default_dir_mode=? | Default mode of a new directory when no inherited ACL is available. | The value ranges from 000 to 777. |
| default_file_mode=? | Default mode of a new file when no inherited ACL is available. | The value ranges from 000 to 777. |
| global_namespace_capacity=? | Global namespace capacity. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value is in the format of "capacity value + unit of capacity". The unit can be MB, GB, or TB.<br>The value ranges from 1 MB to 16,384 TB. |
| global_namespace_forward_enabled=? | Whether to enable global namespace forward. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": The global namespace forward function is enabled.<br>"no": The global namespace forward function is disabled. |
| smb2_enabled_for_dc_connections=? | Whether connecting domain controller over SMB2 is enabled. | The value can be "yes" or "no", where: <br>"yes": connecting domain controller over SMB2 is enabled.<br>"no": connecting domain controller over SMB2 is disabled. |
| leasev2_enable=? | Whether to enable LeaseV2. | The value can be "yes" or "no", where: <br>"yes": LeaseV2 is enabled.<br>"no": LeaseV2 is disabled. |
| smb1_enabled_for_linux=? | Whether to enable the SMB1 switch that supports Linux. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": SMB1 for Linux is enabled.<br>"no": SMB1 for Linux is disabled. |
| max_sessions_displays=? | Maximum number of sessions that can be queried by the MMC. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value ranges from 0 to 4294967295. |
| max_open_files_display=? | Maximum number of open files that can be queried by the MMC. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value ranges from 0 to 4294967295. |
| domainname_configurable_enable=? | Whether to use the system name as the resource user domain name. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value is "yes" or "no", where: 1"yes": enables the domainname_configurable_enable function. <br>"no": disables the domainname_configurable_enable function. |
| administrators_privilege=? | Configure permissions for the administrator group. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "admin", "default_group", or "owner", where: <br>"admin": The members in the "Administrators" user group have privileges as administrators.<br>"default_group": The members in the "Administrators" user group do not have any privileges.<br>"owner": The members in the "Administrators" user group have the privileges of querying and setting the file or directory access control list (ACL), and modifying the file or directory owner. |
| cifs_symlink_enable | Whether to enable the function of CIFS symlink. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the cifs_symlink_enable function.<br>"no": disables the cifs_symlink_enable function. |
| session_security_for_ad_ldap | LDAP client signing level of an AD domain. | The value can be "none", "sign", or "seal", where: <br>"none": The LDAP BIND request is not signed.<br>"sign": The LDAP BIND request is signed.<br>"seal": The LDAP BIND request is sealed. |
| smb1_priority_for_dc_connections=? | Whether to enable the function of preferentially connecting SMB1 to the domain controller. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": connecting domain controller over SMB1 preferentially is enabled.<br>"no": connecting domain controller over SMB1 preferentially is disabled. |
| inherit_parent_mode_enable=? | Whether to inherit the parent mode when there is no ACL. | The value can be "yes" or "no", where: <br>"yes": enables the inherit_parent_mode function.<br>"no": disables the inherit_parent_mode function. |
| ntfs_set_acl_chown_disable | Whether to keep the current owner unchanged during NT ACL setting when the configuration mode is NTFS and the effective mode is UNIX. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": changes the owner.<br>"no": does not change the owner. |

##### Usage Guidelines

None

##### Example

Query the CIFS share service before the modification.

```text
admin:/>show service cifs
Running Status                      : Start
Security Model                      : All Attestation
Guest Enabled                       : No
Anonymous Enabled                   : No
Signing Required                    : No
Signing Enabled                     : No
Oplock Enabled                      : Yes
Oplock Timeout(s)                   : 35
Notify Enabled                      : Yes
Durable Handle Enabled              : No
Durable Handle Timeout(s)           : 60
ABSE Enabled                        : No
SMB1 Enabled                        : No
SMB2 Enabled                        : Yes
Default Dir Mode                    : 755
Default File Mode                   : 744
Global Namespace Capacity           : 16.000PB
Global Namespace Forward Enabled    : No
SMB2 Enabled for DC Connections     : Yes
LeaseV2 Enabled                     : Yes
Smb1 Enabled for Linux              : No
Max Sessions Display                : 0
Max Open Files Display              : 0
Domain Name Configurable Enable     : No
Administrators Privilege            : --
Cifs Symlink Enable                 : --
Client Session Security For AD LDAP : None
SMB1 Priority for DC Connections    : --
Inherit Parent Mode Enable          : Yes
NTFS SetAcl Chown Disable           : --

```

Modify the CIFS share service.

```text
admin:/>change service cifs oplock_timeout=15
Command executed successfully.
```

Query the CIFS share service after the modification.

```text
admin:/>show service cifs
Running Status                      : Start
Security Model                      : All Attestation
Guest Enabled                       : No
Anonymous Enabled                   : No
Signing Required                    : No
Signing Enabled                     : No
Oplock Enabled                      : Yes
Oplock Timeout(s)                   : 15
Notify Enabled                      : Yes
Durable Handle Enabled              : No
Durable Handle Timeout(s)           : 60
ABSE Enabled                        : No
SMB1 Enabled                        : No
SMB2 Enabled                        : Yes
Default Dir Mode                    : 755
Default File Mode                   : 744
Global Namespace Capacity           : 16.000PB
Global Namespace Forward Enabled    : No
SMB2 Enabled for DC Connections     : Yes
LeaseV2 Enabled                     : Yes
Smb1 Enabled for Linux              : No
Max Sessions Display                : 0
Max Open Files Display              : 0
Domain Name Configurable Enable     : No
Administrators Privilege            : --
Cifs Symlink Enable                 : --
Client Session Security For AD LDAP : None
SMB1 Priority for DC Connections    : --
Inherit Parent Mode Enable          : Yes
NTFS SetAcl Chown Disable           : --

```

Disable the SMB1 protocol.

```text
admin:/>change service cifs smb1_enable=no
WARNING: You are about to disable the CIFS SMB1/SMB2 service. This operation causes the CIFS SMB1/SMB2 sharing service provided by the storage device unavailable.
Suggestion: Before performing this operation, ensure that the CIFS SMB1/SMB2 sharing service is no longer needed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable the global namespace forward function.

```text
admin:/>change service cifs global_namespace_forward_enabled=yes
WARNING:You are about to enable the global namespace forward function. This operation will cause the DNS load balancing function to fail.
Suggestion: Before performing this operation, you are advised to disable the DNS load balancing function.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable LeaseV2.

```text
admin:/>change service cifs leasev2_enable=yes
WARNING: You are about to enable the version 2 of the lease function. Enabling the lease function may cause interruption of the SMB3 failover service.
Suggestion: Confirm that you need to enable the version 2 of the lease function.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable the SMB1 protocol for Linux operating systems.

```text
admin:/>change service cifs smb1_enabled_for_linux=yes
WARNING: You are about to enable the SMB1 protocol for Linux operating systems. This operation will allow incompatible clients to access the NAS server through the SMB1 protocol. As a result, exceptions may occur.
Suggestion: Confirm that you need to enable the SMB1 protocol for Linux operating systems.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable the function of CIFS symlink.

```text
admin:/>change service cifs cifs_symlink_enable=yes
Command executed successfully.
```

Modify the LDAP client signing level of an AD domain.

```text
admin:/>change service session_security_for_ad_ldap=sign
Command executed successfully.
```

Inherit the mode of the parent directory in the case of no ACL permissions.

```text
admin:/>change service cifs inherit_parent_mode_enable=yes
Command executed successfully.
```

Disable the function of changing the owner.

```text
admin:/>change service cifs ntfs_acl_chown_disable=yes
WARNING: You are about to turn off the Owner switch. After this operation, permission authentication and quota statistics may be abnormal.
Suggestion: Ensure that you need to perform this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable the CIFS service.

```text
admin:/>change service cifs status=start
WARNING:You are about to enable the CIFS service. This operation will not enable SMB1 automatically. SMB1 is disabled to ensure storage security.
Suggestion: If you need to enable SMB1, use CLI commands.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the Notify notification interval.

```text
developer:/>change service cifs notify_time_interval=10000
Command executed successfully.
```

##### System Response

None
