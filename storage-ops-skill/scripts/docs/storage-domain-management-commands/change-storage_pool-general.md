# change storage_pool general


##### Function

The **change storage_pool general** command is used to modify the attributes of a storage pool, including the name, capacity alarm threshold, capacity exhaustion threshold, capacity, provisioning limit, low threshold of protection capacity, high threshold of protection capacity, and automatic deletion switch.

##### Format

**change storage_pool general** { pool_id=? \| pool_name=? } { name=? \| full_threshold=? \| used_up_threshold=? \| provisioning_limit_switch=? \| provisioning_limit=? \| protection_low_threshold=? \| protection_high_threshold=? \| automatic_deletion_switch=? } \* \[ description=? \| clear_description=? \]

**change storage_pool general** { pool_id=? \| pool_name=? } capacity=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pool_id=? | Storage pool ID. | To obtain the value, run "show storage_pool general". |
| pool_name=? | Name of the storage pool to be modified. | To obtain the value, run the "show storage_pool general" command. |
| name=? | New name of a storage pool. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| full_threshold=? | Capacity alarm threshold. | The value ranges from 1 to 95, expressed in %. |
| used_up_threshold=? | Capacity exhaustion threshold. | The value ranges from ("full_threshold" + 1) to 99, expressed in percentage. |
| capacity=? | Capacity of the storage pool. | The value is in the format of "capacity value + unit". The unit can be GB or TB.<br>The value ranges from 1 GB to 12864 TB.<br>You can run the "show disk_domain general disk_domain_id=xxx" command to view the free capacity of the disk domain to which the storage pool belongs.<br>The value "all" indicates that the capacity of a storage pool is changed to the available capacity of a disk domain. |
| description=? | Description. | - |
| clear_description=? | Clears the description. | The value can be: "enable": clears the description. |
| provisioning_limit_switch=? | Switch of setting the thin LUN provisioning limit. | The value can be "off" (default value) or "on", where: <br>"off": turns off the switch.<br>"on": turns on the switch. |
| provisioning_limit=? | Thin LUN provisioning limit. | The value ranges from 0 to 65535. |
| protection_low_threshold=? | Low threshold of the storage pool protection capacity. | The value ranges from 1 to 95, expressed in percentage (%). |
| protection_high_threshold=? | High threshold of the storage pool protection capacity. | The value ranges from (protection_low_threshold+1) to 99, expressed in percentage (%). |
| automatic_deletion_switch=? | Automatic deletion switch of a storage pool. | The value can be: <br>"off": disables the function of automatically reclaiming the protected space (scheduled HyperCDP object and scheduled HyperCDP consistency group) in the storage pool.<br>"on": enables the function of automatically reclaiming the protected space (scheduled HyperCDP object and scheduled HyperCDP consistency group) in the storage pool. |

##### Usage Guidelines

The following command is not recommended: "**change storage_pool general** pool_id=? capacity=?".

##### Example

Change the provisioning limit of storage pool "0" to 200.

```text
admin:/>change storage_pool general pool_id=0 provisioning_limit_switch=on provisioning_limit=200
Command executed successfully.
```

Change the automatic deletion switch of storage pool "0" to "on".

```text
admin:/>change storage_pool general pool_id=0 automatic_deletion_switch=on
CAUTION: You are about to enable the automatic deletion function of data protection capacity for a storage pool. If the automatic deletion function is enabled, when the protection capacity or used capacity of the storage pool reaches the threshold, an exception may occur when the HyperCDP object and HyperCDP consistency group are created because the storage pool protection capacity cannot be applied for. In addition, the created scheduled HyperCDP object and scheduled HyperCDP consistency group will be automatically deleted until the used capacity falls below the lower threshold.
Suggestion: Before performing this operation, confirm that the automatic deletion function of data protection capacity for a storage pool needs to be enabled.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
