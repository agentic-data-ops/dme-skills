# show service cifs


##### Function

The **show service cifs** command is used to query information about the CIFS share service.

##### Format

**show service cifs**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query information about the CIFS share service.

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
SMB2 Enabled for DC Connections     : No
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

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Running Status | Status of the CIFS share service. |
| Security Model | Authentication mode. The value can be "Local Attestation", "Domain Attestation", or "All Attestation". The default value is "All Attestation". |
| Guest Enabled | Whether guest access is allowed. The default value is "FALSE". |
| Anonymous Enabled | Whether anonymous access is allowed. |
| Signing Required | Whether the CIFS client must support the signature. |
| Signing Enabled | Whether to enable the signature for the CIFS protocol. |
| Oplock Enabled | Whether to enable opportunistic locking (Oplock) (after a protocol is locked, the file system does not require a lock). |
| Oplock Timeout(s) | Timeout period of oplock, expressed in seconds. |
| Notify Enabled | Whether to enable Notify. |
| Durable Handle Enabled | Whether to enable durable handle. |
| Durable Handle Timeout(s) | Timeout period of durable handles, expressed in seconds. |
| ABSE Enabled | Whether access based on share enumeration is allowed. |
| SMB1 Enabled | Whether to enable SMB1. |
| SMB2 Enabled | Whether to enable SMB2. |
| Global Namespace Capacity | Global namespace capacity. |
| Default Dir Mode | Default mode of the new directory when no ACL is inherited. |
| Default File Mode | Default mode of the new file when no ACL is inherited. |
| Global Namespace Forward Enabled | Whether to enable global namespace forward. |
| SMB2 Enabled for DC Connections | Whether connecting domain controller over SMB2 is enabled. |
| LeaseV2 Enabled | Whether to enable LeaseV2. |
| Smb1 Enabled for Linux | Whether to enable SMB1 for Linux operating systems. |
| Max Sessions Display | Maximum number of returned sessions queried through MMC. |
| Max Open Files Display | Maximum number of returned open files queried through MMC. |
| Domain Name Configurable Enable | Whether to enable the function of using a system name as a resource user's domain name. |
| Administrators Privilege | Privilege configuration of the Administrators group. |
| Cifs Symlink Enable | Whether to enable the function of CIFS symlink. |
| Client Session Security For AD LDAP | LDAP client signing level of an AD domain. |
| SMB1 Priority for DC Connections | Whether connecting domain controller over SMB1 preferentially is enabled. |
| Inherit Parent Mode Enable | Whether to inherit the mode of the parent directory in the case of no ACL permissions. |
| NTFS SetAcl Chown Disable | Whether to keep the owner unchanged during NT ACL setting when the configured security style is NTFS and effective security style is UNIX mode. |
