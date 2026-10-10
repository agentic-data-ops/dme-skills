# show vstore_pair general


##### Function

The **show vstore_pair general** command is used to query information about vStore pairs.

##### Format

**show vstore_pair general** \[ pair_id=? \]

##### Parameters

| Parameter | Description          | Value                                                                                                                                                                                                    |
|-----------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pair_id=? | ID of a vStore pair. | You can run the "**show vstore_pair general**" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Query information about all vStore pairs on a device.

```text
admin:/>show vstore_pair general
ID                                Health Status  Running Status  Config Status       Link Status  Domain Name  Local Vstore Name  Remote Vstore Name
--------------------------------  -------------  --------------  ------------------  -----------  -----------  -----------------  ------------------
2100d100000405060000000600000000  Normal         Normal          To Be Synchronized  Linkup       test         System_vStore      System_vStore
```

Query details about vStores in a specified pair. The pair ID is "2100d100000405060000000600000000".

```text
admin:/>show vstore_pair general pair_id=2100d100000405060000000600000000
ID                 : 2100d100000405060000000600000000
Health Status      : Normal
Running Status     : Normal
Config Status      : To Be Synchronized
Link Status        : Linkup
Domain ID          : 10100
Domain Name        : test
Local Vstore ID    : 0
Local Vstore Name  : System_vStore
Remote Vstore ID   : 0
Remote Vstore Name : System_vStore
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| ID                 | Pair UUID (64-bit).                                                                  |
| Health Status      | Health status: normal or faulty.                                                     |
| Running Status     | Running status: normal, unsynchronized, forcibly started, and invalid.               |
| Config Status      | Configuration synchronization status: normal, synchronizing, and to be synchronized. |
| Link Status        | Link status, which can be Linkup or Linkdown.                                        |
| Domain ID          | HyperMetro domain ID.                                                                |
| Domain Name        | HyperMetro domain name.                                                              |
| Local Vstore ID    | Local vStore ID.                                                                     |
| Local Vstore Name  | Local vStore name.                                                                   |
| Remote Vstore ID   | Remote vStore ID.                                                                    |
| Remote Vstore Name | Remote vStore name.                                                                  |
