# show remote_lun single_link


##### Function

The **show remote_lun single_link** command is used to check whether a remote LUN in use is connected by a single link.

##### Format

**show remote_lun single_link**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Check whether a remote LUN in use is connected by a single link.

```text
admin:/>show remote_lun single_link
LUN WWN                                          Is Single Link  Capacity  Device ID  Device SN             Vendor    Model
-----------------------------------------------  --------------  --------  ---------  --------------------  --------  ----------------
6f:50:20:31:00:04:05:06:41:60:f1:d5:00:00:00:06  Yes             80.000GB  513        ST000000000000000172  HUAWEI    XSG1
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                            |
|----------------|------------------------------------|
| LUN WWN        | LUN WWN.                           |
| Is Single Link | Connected by a single link or not. |
| Capacity       | Capacity.                          |
| Device ID      | Device ID.                         |
| Device SN      | Device SN.                         |
| Vendor         | Vendor.                            |
| Model          | Model.                             |
