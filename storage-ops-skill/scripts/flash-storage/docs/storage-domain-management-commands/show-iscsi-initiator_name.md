# show iscsi initiator_name


##### Function

The **show iscsi initiator_name** command is used to query the names of iSCSI initiators configured for the storage system.

##### Format

**show iscsi initiator_name**

##### Parameters

None

##### Usage Guidelines

Initiators and targets are relative. In the scenario where storage systems A and B connect to each other in iSCSI mode, from the perspective of storage system A, storage system A is the initiator and storage system B is the target. Likewise, from the perspective of storage system B, storage system B is the initiator and storage system A is the target.

##### Example

Query the names of iSCSI initiators configured for the storage system. The command output varies depending on a specific product.

```text
admin:/>show iscsi initiator_name

Controller  ISCSI Initiator Name
----------  ------------------------------------------------------------
0A           iqn.2006-08.com.huawei:oceanstor:21000022a10c0f45:notconfiga
0B           iqn.2006-08.com.huawei:oceanstor:21000022a10c0f45:notconfigb
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning               |
|----------------------|-----------------------|
| Controller           | Controller ID.        |
| ISCSI Initiator Name | iSCSI initiator name. |
