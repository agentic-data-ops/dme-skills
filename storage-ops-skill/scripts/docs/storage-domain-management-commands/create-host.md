# create host


##### Function

The **create host** command is used to **create host**s.

##### Format

**create host** name=? operating_system=? \[ ip=? \| network_name=? \| location=? \| model=? \| host_id=? \| access_mode=? \| hyper_metro_path_optimized=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a host. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (_), and periods (.). |
| operating_system=? | Type of an operating system running on a host. | The value can be any of the following: <br>Linux<br>Windows<br>Solaris<br>HP-UX<br>AIX<br>XenServer<br>Mac_OS<br>VIS6000<br>VMware_ESX<br>Windows_Server_2012<br>Oracle_VM<br>OpenVMS<br>Oracle_VM_Server_for_x86<br>Oracle_VM_Server_for_SPARC<br> NOTE: Parameter "Windows_Server_2012" is discarded, equal to "Windows". Parameter "Oracle_VM" is discarded, equal to "Oracle_VM_Server_for_x86". |
| ip=? | IP address of a host. | - |
| network_name=? | Name of the network on which a host resides. | The value contains 1 to 31 characters. |
| location=? | Location of a host. | The value contains 1 to 31 characters. |
| model=? | Model of a host. | The value contains 1 to 31 characters. |
| host_id=? | ID of a host. | The value is an integer ranging from 0 to 24575. If you do not specify this parameter, the system automatically allocates an ID for a new host. |
| access_mode=? | Host access mode. | The value can be "balanced" or "asymmetric", where: "balanced": indicates the balanced mode. "asymmetric": indicates the asymmetric mode. |
| hyper_metro_path_optimized=? | Whether the host path to the local HyperMetro array is preferred. | The value can be "no" or "yes", where: <br>"no": The host path to the local HyperMetro array is not preferred.<br>"yes": The host path to the local HyperMetro array is preferred. |

##### Usage Guidelines

None

##### Example

Create a host whose name is "newhost000" and operating system is "Windows".

```text
admin:/>create host name=newhost000 operating_system=Windows
CAUTION:1.Before performing this operation, confirm that the operating system type of the host to be created is the same as that of the service host.
2.If the operating system of the service host is Windows, and all thin LUN functions are required to get better experience, select Windows Server 2012.
Suggestion: Confirm again that the correct operating system type has been specified.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Create a host whose name is "newhost001", operating system is "Linux", location is "newlocation", model is "2058", network name is "newnetwork", IP address is "192.168.3.53", and ID is "1".

```text
admin:/>create host name=newhost001 operating_system=Linux location=newlocation model=2058 network_name=newnetwork ip=192.168.3.53 host_id=1
CAUTION:1.Before performing this operation, confirm that the operating system type of the host to be created is the same as that of the service host.
2.If the operating system of the service host is Windows, and all thin LUN functions are required to get better experience, select Windows Server 2012.
Suggestion: Confirm again that the correct operating system type has been specified.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
