# show fs_hyper_metro_domain fs_pair


##### Function

The **show fs_hyper_metro_domain fs_pair** command is used to query file system-based HyperMetro pairs in a HyperMetro domain.

##### Format

**show fs_hyper_metro_domain fs_pair** domain_id=?

##### Parameters

| Parameter   | Description                                     | Value                                                                      |
|-------------|-------------------------------------------------|----------------------------------------------------------------------------|
| domain_id=? | ID of the HyperMetro domain of the file system. | To obtain the value, run the "show fs_hyper_metro_domain general" command. |

##### Usage Guidelines

OceanStor Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query all file system-based HyperMetro pairs in HyperMetro domain 10100.

```text
admin:/>show fs_hyper_metro_domain fs_pair domain_id=10100
ID Health Status Running Status Domain Name Type Size Role Local Name Remote Name
---------------- ------------- -------------- ------ ----- ------------ ------------------ - -------------------- --------
200bc79b99520000 Normal Normal HCD001 FS 100.000GB Preferred LUN001 extLun001
200bc79b99520002 Normal Normal HCD002 FS 10.000GB Non-preferred FS001 extFS001
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ID             | UUID of the HyperMetro pair, 64 bits.                                                                                                               |
| Health Status  | Health status. The value can be "Normal" or "Fault".                                                                                                |
| Running Status | Running Status: The value can be Normal, Synchronizing, To be synchronized, Paused, Forcibly started, Invalid, Deleting, or Creating.               |
| Domain Name    | Domain name.                                                                                                                                        |
| Type           | Resource type. The value can be "LUN" or "FS".                                                                                                      |
| Size           | Resource size.                                                                                                                                      |
| Role           | Whether the site is the primary/secondary or preferred/non-preferred site. A/P indicates active/passive, and A/A indicates arbitration is required. |
| Local Name     | Name of a local resource.                                                                                                                           |
| Remote Name    | Name of a remote resource.                                                                                                                          |
