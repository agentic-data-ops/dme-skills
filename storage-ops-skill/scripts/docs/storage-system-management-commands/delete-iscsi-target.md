# delete iscsi target


##### Function

The **delete iscsi target** command is used to delete an iSCSI target.

##### Format

**delete iscsi target** iscsi_id=? local_control_id=?

##### Parameters

| Parameter          | Description          | Value                                                                                                                          |
|--------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------|
| iscsi_id=?         | The iSCSI link ID.   | To obtain the value, run "show iscsi target" without parameters.                                                               |
| local_control_id=? | Local controller ID. | The value is in the format of "XA", "XB", "XC", "XD",where the "X" is an integer ranging from 0 to 3, for example: "0A", "1C". |

##### Usage Guidelines

None.

##### Example

To delete target "0" of the iSCSI link on local controller 0A, run the following command:

```text
admin:/>delete iscsi target iscsi_id=0 local_control_id=0A
Command executed successfully.
```

##### System Response

None
