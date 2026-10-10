# create hyper_cdp general


##### Function

The **create hyper_cdp general** command is used to create a HyperCDP object. You can create a point-in-time backup for a LUN by running this command.

##### Format

**create hyper_cdp general** lun_id_list=? name=? \[ cdp_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id_list=? | Source LUN ID. | The value is an integer ranging from 0 to 65535.<br>To obtain the value, run the "show lun general" command.<br>You can specify multiple source LUN IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8. |
| name=? | Name of a HyperCDP object. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (_), and periods (.). NOTE: When you create HyperCDP objects in a batch, the length of "name=?" cannot exceed 27 characters. |
| cdp_id=? | ID of a HyperCDP object. You can set an ID for the newly created HyperCDP object. The ID cannot be changed after you specify it. The storage system can automatically assign an ID to the HyperCDP object when you do not specify the ID. | The value is an integer ranging from 0 to 1999999. |

##### Usage Guidelines

You can create multiple HyperCDP objects for different LUNs at the same time.

##### Example

Create a HyperCDP object for LUN "5". The HyperCDP object name is "new_cdp".

```text
admin:/>create hyper_cdp general lun_id_list=5 name=new_cdp
create HyperCDP object new_cdp successfully.
```

Create three HyperCDP objects, each for LUNs "1", "3", and "4".

```text
admin:/>create hyper_cdp general lun_id_list=1,3,4 name=new_cdp
create HyperCDP object new_cdp0000 successfully.
create HyperCDP object new_cdp0001 successfully.
create HyperCDP object new_cdp0002 successfully.
```

##### System Response

None
