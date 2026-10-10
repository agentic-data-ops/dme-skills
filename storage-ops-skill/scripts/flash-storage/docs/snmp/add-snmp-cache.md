# add snmp cache


##### Function

The **add snmp cache** command is used to add an SNMP cache object. No cache object is added by default.

##### Format

**add snmp cache** object_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| object_type | Name of the SNMP cache object. | The value can be "disk", "lun", "fc", or "pcie", where: <br>"disk": indicates a cache object of the disk.<br>"lun": indicates a cache object of the LUN.<br>"fc": indicates a cache object of the Fibre Channel port.<br>"pcie": indicates a cache object of the PCIe port. |

##### Usage Guidelines

You can use the cache object type as a parameter to add corresponding cache objects.

##### Example

Add the SNMP cache object of a disk.

```text
admin:/>add snmp cache object_type=disk
Command executed successfully.
```

##### System Response

None
