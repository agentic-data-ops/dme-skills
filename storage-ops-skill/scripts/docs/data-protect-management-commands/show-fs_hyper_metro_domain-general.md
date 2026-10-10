# show fs_hyper_metro_domain general


##### Function

The **show fs_hyper_metro_domain general** command is used to query a file system-based HyperMetro domain.

##### Format

**show fs_hyper_metro_domain general** \[ domain_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | ID of the file system-based HyperMetro domain. | To obtain the value, run the "show fs_hyper_metro_domain general" command. The value of the "domain_id" parameter contains 1 to 16 characters. |

##### Usage Guidelines

None

##### Example

Query information about all file system HyperMetro domains on a device.

```text
admin:/>show fs_hyper_metro_domain general
ID                Name                      Running Status  Service Status  Preferred Arbitration Role  Role    Description  Remote Device ID  Remote Device Name  Quorum ID  Quorum Name  Quorum Mode  Standby Quorum ID  Standby Quorum Name  Recover Policy  Work Mode    Is Share Authentication Sync  Is Network Sync  Logical Port Work Status  Access
----------------  ------------------------  --------------  --------------  --------------------------  ------  -----------  ----------------  ------------------  ---------  -----------  -----------  -----------------  -------------------  --------------  -----------  ----------------------------  ---------------  ------------------------  ---------
48ad083e9b9f0100  FileHyperMetroDomain_000  Normal          --              --                          Master               0                 B                   --         --           --           --                 --                   Auto            Synchronous  Yes                           No               Working                   Read and Write
```

Query information about the file system HyperMetro domain whose ID is "48ad083e9b9f0100".

```text
admin:/>show fs_hyper_metro_domain general domain_id=48ad083e9b9f0100
ID                           : 48ad083e9b9f0100
Name                         : FileHyperMetroDomain_000
Running Status               : Normal
Service Status               : --
Preferred Arbitration Role   : --
Role                         : Master
Description                  :
Remote Device ID             : 0
Remote Device Name           : B
Quorum ID                    : --
Quorum Name                  : --
Quorum Mode                  : --
Standby Quorum ID            : --
Standby Quorum Name          : --
Recover Policy               : Auto
Work Mode                    : Synchronous
Is Share Authentication Sync : Yes
Is Network Sync              : No
Logical Port Work Status     : Working
Access                       : Read and Write
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | Domain ID. |
| Name | Domain name. |
| Running Status | Running status. <br>normal;<br>restoring;<br>faulty;<br>split;<br>forcible start;<br>invalid. |
| Service Status | Service status. <br>The service is provided;<br>No service is provided. |
| Preferred Arbitration Role | Arbitration priority role. <br>non-preferred site;<br>preferred site. |
| Role | Configure the HyperMetro domain role. <br>secondary end;<br>primary end. |
| Description | Description of the HyperMetro domain. |
| Remote Device ID | ID of the remote storage device. |
| Remote Device Name | Name of the remote storage device. |
| Quorum ID | Quorum server ID. |
| Quorum Name | Quorum server name. |
| Quorum Mode | Arbitration mode. <br>quorum server;<br>static priority. |
| Standby Quorum ID | ID of the standby quorum server. |
| Standby Quorum Name | Name of the standby quorum server. |
| Recover Policy | Recovery policy of the HyperMetro domain. <br>automatic recovery;<br>manual recovery. |
| Work Mode | Working mode. <br>active-active;<br>synchronous. |
| Is Share Authentication Sync | Whether to synchronize shared authentication information. |
| Is Network Sync | Whether to synchronize network configurations. |
| Logical Port Work Status | Working status of the logical port. |
| Access | Access permission. |
