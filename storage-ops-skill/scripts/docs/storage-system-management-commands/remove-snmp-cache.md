# remove snmp cache


##### Function

The **remove snmp cache** command is used to remove an SNMP cache object.

##### Format

**remove snmp cache** object_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| object_type | Name of the SNMP cache object. | The value can be "disk", "lun", "fc", or "pcie", where: <br>"disk": indicates a cache object of the disk.<br>"lun": indicates a cache object of the LUN.<br>"fc": indicates a cache object of the Fibre Channel port.<br>"pcie": indicates a cache object of the PCIe port. |

##### Usage Guidelines

You can use the cache object type as a parameter to remove corresponding cache objects.

##### Example

Remove the SNMP cache object of a disk.

```text
admin:/>remove snmp cache object_type=disk
Command executed successfully.
```

##### System Response

None
