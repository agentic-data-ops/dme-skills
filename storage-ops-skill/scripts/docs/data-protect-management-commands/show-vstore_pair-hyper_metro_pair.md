# show vstore_pair hyper_metro_pair


##### Function

The **show vstore_pair hyper_metro_pair** command is used to query HyperMetro pairs in a vStore pair.

##### Format

**show vstore_pair hyper_metro_pair** vstore_pair_id=?

##### Parameters

| Parameter        | Description          | Value                                                                   |
|------------------|----------------------|-------------------------------------------------------------------------|
| vstore_pair_id=? | ID of a vStore pair. | You can run the "show vstore_pair general" command to obtain the value. |

##### Usage Guidelines

OceanStor Dorado 3000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query all HyperMetro pairs in vStore pair 1.

```text
admin:/>show vstore_pair hyper_metro_pair vstore_pair_id=1
ID Health Status Running Status Domain Name Type Size Role Local Name Remote Name
---------------- ------------- -------------- ------ ----- ------------ ------------------ - -------------------- --------
200bc79b99520000 Normal Normal HCD001 FS 100.000GB --  LUN001 extLun001
200bc79b99520002 Normal Normal HCD002 FS 10.000GB --  FS001 extFS001
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID             | Pair UUID, 64 bits.                                                                                                                                           |
| Health Status  | Health status: normal or faulty.                                                                                                                              |
| Running Status | Running Status: The value can be Normal, Synchronizing, To be synchronized, Paused, Forcibly started, Invalid, Deleting, or Creating.                         |
| Domain Name    | Name of a domain.                                                                                                                                             |
| Type           | Resource type. The options are LUN and FS.                                                                                                                    |
| Size           | Resource size.                                                                                                                                                |
| Role           | Whether the site is the primary or preferred site. The A/P mode indicates the master/slave relationship, and the A/A mode indicates the arbitration priority. |
| Local Name     | Name of a local resource.                                                                                                                                     |
| Remote Name    | Name of a remote resource.                                                                                                                                    |
