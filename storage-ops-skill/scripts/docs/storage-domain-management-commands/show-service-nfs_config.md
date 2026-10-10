# show service nfs_config


##### Function

The **show service nfs_config** command is used to query the NFS common configuration.

##### Format

**show service nfs_config**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the NFS common configuration.

```text
admin:/>show service nfs_config
Communication Thread Number   : 100
Work Thread Number            : 100
Max Block Size(byte)          : 10240
Listen IP                     : permit *
Client List                   : permit *
Communication Thread Priority : normal
Transcode Switch Status       : Disabled
Silent Time(s)                : 60
Fileid Length(bit)            : 32
Nsm Query Dns Switch Status   : Enabled
NFSv3 Automount Switch        : Enabled
NFSv4 Automount Switch        : Enabled
NFSv4.1 Automount Switch      : Enabled
Extended Groups Switch        : Disabled
Extended Groups Limit         : 32
Slow I/O Percent(%)           : 50
Nobody UID                    : 65534
Default Windows User          : win_user
Flow Control Switch           : Disabled
Flow Control Percent(%)       : 50
Flow Control Timedelay(ms)    : 200
Ignore NT ACL For Root        : Enabled
Global v4 Acl Preserve        : use_nfs_share_permission
Global Ntfs Unix Security Ops : use_nfs_share_permission
Touch check with ACL          : Enabled
Nfsv41 Service Status         : Enabled
Chown Mode                    : use_nfs_share_permission
Map V4 Everyone Ace To Other Modebits : Adjusted Mappping
```

Query the NFS configuration of a vStore.

```text
admin@vstore1:/>show service nfs_config
NFSv3 Automount Switch        : Enabled
NFSv4 Automount Switch        : Enabled
NFSv4.1 Automount Switch      : Enabled
Extended Groups Switch        : Disabled
Extended Groups Limit         : 32
Nobody UID                    : 65534
Default Windows User          : win_user
Ignore NT ACL For Root        : Enabled
Global v4 Acl Preserve        : use_nfs_share_permission
Global Ntfs Unix Security Ops : use_nfs_share_permission
Touch check with ACL          : Enabled
Chown Mode                    : use_nfs_share_permission
Map V4 Everyone Ace To Other Modebits : Adjusted Mappping
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Communication Thread Number | Number of NFS-based communication threads. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Work Thread Number | Number of NFS-based working threads. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Max Block Size(byte) | NFS MTU. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Listen IP | Blacklist and whitelist of NFS listening IP addresses. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Client List | Blacklist and whitelist of NFS clients. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Communication Thread Priority | Priority of NFS-based communication threads. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Transcode Switch Status | Switch of NFS transcoding. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Silent Time(s) | NFS silent period. |
| Fileid Length(bit) | NFS file ID length. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Nsm Query Dns Switch Status | Whether to enable or disable the function of NSM to query DNS host names. NOTE: This field is not supported by the current version. The execution result is invalid. |
| NFSv3 Automount Switch | Whether to enable or disable the function of automatically mounting directories for NFSv3. NOTE: This field is not supported by the current version. The execution result is invalid. |
| NFSv4 Automount Switch | Whether to enable or disable the function of automatically mounting directories for NFSv4. NOTE: This field is not supported by the current version. The execution result is invalid. |
| NFSv4.1 Automount Switch | Whether to enable or disable the function of automatically mounting directories for NFSv4.1. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Extended Groups Switch | Whether to enable the extended user group function. |
| Extended Groups Limit | Number of extended user groups. |
| Slow I/O Percent(%) | Percentage of slow I/O requests. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Nobody UID | ID of the nobody user. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Default Windows User | Default Windows user of the NFS user mapping. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Flow Control Switch | Switch of NFS I/O flow control. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Flow Control Percent(%) | Percentage of the number of NFS slow I/O requests to the total number of requests in flow control. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Flow Control Timedelay(ms) | Delay threshold of NFS I/O flow control. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Ignore NT ACL For Root | Whether to ignore the NT ACL check for NFS user "root". |
| Global V4 Acl Preserve | Tenant-level NFSv4 ACL protection. |
| Global Ntfs Unix Security Ops | Tenant-level NTFS UNIX security options. |
| Touch check with ACL | Whether to use ACL authentication when you modify the time of a file or directory by running the "touch" command on a Linux client. NOTE: This field is not supported by the current version. The execution result is invalid. |
| Nfsv41 Service Status | Running status of the NFSv4.1 service. |
| Chown Mode | Change the ownership (owner or group) mode. |
| Map V4 Everyone Ace To Other Modebits | Mapping between NFSv4 Everyone@ACE and mode bits during conversion between NFSv4 ACLs and mode bits. |
