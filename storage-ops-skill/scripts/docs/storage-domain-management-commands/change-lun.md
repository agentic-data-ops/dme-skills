# change lun


##### Function

The **change lun** command is used to modify LUN settings, including the name and capacity.

##### Format

**change lun** { lun_id=? \| lun_name=? } { name=? \| write_policy=? \| owner_controller=? \| io_priority=? \| dif_switch=? \| thresholds_switch=? \| thresholds_percent=? } \* \[ description=? \| clear_description=? \]

**change lun** { lun_id=? \| lun_name=? } { name=? \| write_policy=? \| owner_controller=? \| io_priority=? \| dif_switch=? \| thresholds_switch=? \| thresholds_percent=? \| mirror_policy=? \| zero_data_enabled=? \| work_controller=? } \* \[ description=? \| clear_description=? \]

**change lun** { lun_id=? \| lun_name=? \| lun_id_list=? \| lun_name_list=? } capacity=?

**change lun** { lun_id_list=? \| lun_name_list=? } { write_policy=? \| owner_controller=? \| io_priority=? \| dif_switch=? \| thresholds_switch=? \| thresholds_percent=? } \* \[ description=? \| clear_description=? \]

**change lun** { lun_id_list=? \| lun_name_list=? } { write_policy=? \| owner_controller=? \| io_priority=? \| dif_switch=? \| thresholds_switch=? \| thresholds_percent=? \| mirror_policy=? \| zero_data_enabled=? \| work_controller=? } \* \[ description=? \| clear_description=? \]

**change lun** { lun_id=? \| lun_name=? \| lun_id_list=? \| lun_name_list=? } { silence_check_period=? \| silence_check_count=? \| silence_keep_time=? } \[ description=? \| clear_description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id=? | ID of a LUN that you want to modify. | To obtain the value, run "show lun general". |
| lun_name=? | Name of the LUN whose settings are to be modified. | To obtain the value, run "show lun general". |
| lun_id_list=? | ID list of LUNs that you want to modify. | To obtain the value, run "show lun general". Multiple IDs are separated by commas (,), or you can specify a LUN ID range using a hyphen (-). |
| lun_name_list | Name list of the LUNs whose settings are to be modified. | To obtain the value, run "show lun general". |
| name=? | New name of a LUN. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| capacity=? | Updated capacity of a LUN. | The value is in the format of capacity+unit, where the unit can be KB, MB, GB, TB, or Blocks, or you can set the value to "all" to allocate all free capacity to a LUN. <br>The value ranges from 512 KB to 256 TB.<br>One block equals 512 bytes.<br>When the unit is GB or TB, a decimal number can be used.<br>"all" is used to expand the capacity of an eDevLUN. |
| write_policy=? | Cache write policy. | Possible values are: <br>"write_through": indicates write through. The system considers that a data write is successful only after data is written to disks. Disks are accessed in each data write.<br>"write_back": indicates write back. After data is written to the cache of the local controller, the system considers that a data write is successful. In addition, the data will be written to the cache of the peer controller as a mirror. When certain conditions are met, the caches write data to disks. |
| owner_controller=? | Owning controller of a LUN. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. |
| work_controller=? | Work controller of a LUN. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. |
| io_priority=? | I/O priority of a LUN. | Possible values are: <br>"Low": indicates the low priority.<br>"Middle": indicates the medium priority.<br>"High": indicates the high priority. |
| thresholds_switch=? | Switch of the function that triggers an alarm when the threshold of a thin LUN is reached. | Possible values are: <br>"off": disables the alarm function.<br>"on": enables the alarm function. |
| thresholds_percent=? | Threshold that will trigger an alarm in a thin LUN. | The value ranges from 50 to 99, expressed in %. |
| dif_switch=? | Whether or not to enable the DIF function. | Possible values are: <br>"yes": The DIF function will be enabled.<br>"no": The DIF function will not be enabled. |
| description=? | Description. | - |
| clear_description=? | Clears the description. | The value can be: "enable": clears the description. |

##### Usage Guidelines

-   Before running this command, ensure that the selected LUN is exactly the one you want to modify.
-   Before running this command, clear the cache of the application service that has been mapped to the selected LUN.
-   Before modifying the owning controller of a block device or disabling a block device, ensure that the container service has been stopped for all global image repository LUNs, local image repository LUNs, and container configuration LUNs.

##### Example

Change the capacity of LUN "1" to "300MB".

```text
admin:/>change lun lun_id=1 capacity=300MB
CAUTION: You are about to perform a LUN expansion. This operation expands the capacity of the LUN.
Suggestion: Rescan for the LUN on the server after the capacity expansion.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
