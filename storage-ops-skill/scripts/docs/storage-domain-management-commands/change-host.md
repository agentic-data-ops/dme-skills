# change host


##### Function

The **change host** command is used to modify the attributes of a host, including the host name, location, operating system type, and IP address.

##### Format

**change host** { host_id=? \| host_name=? } { name=? \| operating_system=? \| location=? \| model=? \| ip=? \| network_name=? \| access_mode=? \| hyper_metro_path_optimized=? \| command_device=? } \* \[ force=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | ID of a host whose attributes you want to modify. | To obtain the value, run "show host general". |
| host_name=? | Name of a host whose attributes you want to modify. | To obtain the value, run "show host general". |
| name=? | Updated name of a host. | The value contains 1 to 255 characters, including letters, digits, hyphens (-), underscores (_), and periods (.). |
| operating_system=? | Type of an operating system running on a host. | The value can be: <br>"Linux"<br>"Windows"<br>"Solaris"<br>"HP-UX"<br>"AIX"<br>"XenServer"<br>"Mac_OS"<br>"VIS6000"<br>"VMware_ESX"<br>"Windows_Server_2012"<br>"Oracle_VM"<br>"OpenVMS"<br>"Oracle_VM_Server_for_x86"<br>"Oracle_VM_Server_for_SPARC"<br> NOTE: Parameter "Windows_Server_2012" is discarded and is equal to "Windows". Parameter "Oracle_VM" is discarded and is equal to "Oracle_VM_Server_for_x86". |
| location=? | Updated location of a host. | The value contains 1 to 31 characters. |
| model=? | Model of a host. | The value contains 1 to 31 characters. |
| ip=? | IP address of a host. | - |
| network_name=? | Name of the network on which a host resides. | The value contains 1 to 31 characters. |
| access_mode=? | Host access mode. | The value can be "balanced" or "asymmetric", where: "balanced": balanced mode. "asymmetric": asymmetric mode. |
| hyper_metro_path_optimized=? | Whether the host path to the local HyperMetro array is preferred. | The value can be "no" or "yes", where: <br>"no": The host path to the local HyperMetro array is not preferred.<br>"yes": The host path to the local HyperMetro array is preferred. |
| command_device=? | Whether to enable the in-band command function. | The value can be "disable" or "enable", where: <br>"disable": disables in-band commands.<br>"enable": enables in-band commands. |
| force=? | Whether to change the host configuration forcibly. | The value is "true", indicating to change the host configuration forcibly. |

##### Usage Guidelines

None

##### Example

For the host whose ID is "1", modify its name to "newhost002" and location to "otherlocation".

```text
admin:/>change host host_id=1 name=newhost002 location=otherlocation
Command executed successfully.
```

Change the name of host "HostName1" to "HostName2".

```text
admin:/>change host host_name=HostName1 name=HostName2
Command executed successfully.
```

##### System Response

None
