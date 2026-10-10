# show iscsi target_name


##### Function

The **show iscsi target_name** command is used to query the name of the iSCSI target configured for the storage system.

##### Format

**show iscsi target_name** \[ eth_port_id=? \]

##### Parameters

| Parameter     | Description   | Value                                         |
|---------------|---------------|-----------------------------------------------|
| eth_port_id=? | ID of a port. | To obtain the value, run "show port general". |

##### Usage Guidelines

Initiators and targets are relative. In the scenario where storage systems A and B connect to each other in iSCSI mode, from the perspective of storage system A, storage system A is the initiator and storage system B is the target. Likewise, from the perspective of storage system B, storage system B is the initiator and storage system A is the target.

##### Example

Query the name of the iSCSI target configured for the storage system.

```text
admin:/>show iscsi target_name

iSCSI Target Name : iqn.2006-08.com.huawei:oceanstor:21000022a10515fe:configa
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning            |
|-------------------|--------------------|
| iSCSI Target Name | iSCSI target name. |
