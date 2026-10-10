# show container_application general


##### Function

The **show container_application general** command is used to query the list of available chart packages or the list or details of deployed applications.

##### Format

**show container_application general** \[ name=? \]

##### Parameters

| Parameter | Description                                 | Value                                                                                                                                                          |
|-----------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Application name of a deployed application. | The value contains 1 to 255 ASCII characters, including lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a letter or digit. |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query details about a deployed application.

```text

admin:/>show container_application general name=dataprotect

Name                          : dataprotect
Namespace                     : dpa
Revision                      : 7
Updated                       : 2021-04-17 20:47:55
Status                        : deployed
Chart Name                    : oceanprotect-dataprotect
Description                   : OceanProtect-DataProtect Software
Appliction Subscribe Capacity : 2.351TB
Appliction Image Name List    : kafka:1.0.RC1.039,redis:1.0.RC1.039,dme_initcontainer:1.0.RC1.039
Net Plane List                : archiveNetPlane,backupNetPlane
PodList:

Pod Name                             Pod Status  Pod Restart Times  Pod Cpu Percent(%)  Pod Memory Percent(%)  Pod Belong Node  Pod Namespace  Pod Is Ready
-----------------------------------  ----------  -----------------  ---------------     ------------------     ---------------  -------------  ------------
dataenableengine-proxy-0             Running     0                  --                  --                     node-1           dpa            true
dataenableengine-server-0            Pending     0                  8.95                9.94                   node-0           dpa            true
infrastructure-0                     Running     0                  21.05               14.56                  node-1           dpa            true
protect-engine-a-business-control-0  Running     0                  26.32               21.17                  node-1           dpa            true
Dynamic Config :

Config Name                        Config Value
---------------------------------  -------------------
data-enable-engine.enabled         true
global.archiveNetPlane             1
global.backupNetPlane              2
global.environment                 Dorado
global.replicas                    2
global.updateAppTimestamp.default  1618663675696544020
Lun List:

Lun Name  Lun States  Lun Capacity
--------  ----------  ------------
db-block  Online      50.000GB
File System List:

File System Name  File System States  File System Capacity
----------------  ------------------  --------------------
dma-nas           Online              100.000GB
dme-nas           Online              100.000GB
Net Infomation:

Net Plane Name   Pod Name               Pod Namespace  Business IP
---------------  ---------------------  -------------  -------------
archiveNetPlane  protectengine-e-dms-0  dpa            172.168.50.13
Node List:

Node Name  Node Status  Node Role  Node Cpu Percent(%)  Node Memory Percent(%)
---------  -----------  ---------  ------------------   ----------------------
node-1     Ready        master     25.94                62.31
node-0     Ready        master     17.05                44.00

```

Query the list of deployed applications.

```text

admin:/>show container_application general

Name         Namespace  Revision  Updated              Status   Cpu Percent(%)  Memory Percent(%)
-----------  ---------  --------  -------------------  -------  --------------  ----------------
dataprotect  dpa        7         2021-04-17 20:47:55  Degrade  11.71           7.74

```

##### System Response

The following table describes the parameter meanings.

| Parameter                      | Meaning                                          |
|--------------------------------|--------------------------------------------------|
| Name                           | Application name.                                |
| Appliction Image Name List     | Application image name.                          |
| Application Subscribe Capacity | Space occupied by an application.                |
| Namespace                      | Application namespace.                           |
| Revision                       | Application version number.                      |
| Description                    | Application description.                         |
| Chart Name                     | Application package name.                        |
| Updated                        | Application update time.                         |
| Status                         | Application status.                              |
| Net Plane List                 | List of network planes bound to the application. |
| Node Status                    | Node status.                                     |
| Node Name                      | Node name.                                       |
| Node Memory Percent(%)         | Memory usage of a node, in percentage.           |
| Node Cpu Percent(%)            | CPU usage of a node, in percentage.              |
| Node Role                      | Node role.                                       |
| Pod Name List                  | Name list of pods to which the volume belongs.   |
| Pod Name                       | Pod name.                                        |
| Pod Status                     | Pod status.                                      |
| Pod Restart Times              | Number of pod restart times.                     |
| Pod Cpu Percent(%)             | CPU usage of a pod.                              |
| Pod Memory Percent(%)          | Memory usage of a pod.                           |
| Pod Belong Node                | Node to which a pod belongs.                     |
| Pod Namespace                  | Namespace of a pod.                              |
| Pod Is Ready                   | Whether a pod is ready.                          |
| Config Name                    | Configuration item name.                         |
| Config Value                   | Value of a configuration item.                   |
| Lun List                       | LUN list.                                        |
| Lun Name                       | Name of a LUN.                                   |
| Lun States                     | LUN status.                                      |
| Lun Capacity                   | Allocated LUN capacity.                          |
| File System List               | File system list.                                |
| File System Capacity           | File system capacity.                            |
| File System Name               | Name of a file system.                           |
| File System States             | File system status.                              |
| Net Information                | Network information.                             |
| Net Plane Name                 | Network plane name.                              |
| Business IP                    | Service IP address.                              |
