# show fs_hyper_metro_domain vstore_pair


##### Function

The **show fs_hyper_metro_domain vstore_pair** command is used to query vStore pairs in a file system-based HyperMetro domain.

##### Format

**show fs_hyper_metro_domain vstore_pair** domain_id=?

##### Parameters

| Parameter | Description                                    | Value                                                                      |
|-----------|------------------------------------------------|----------------------------------------------------------------------------|
| domain_id | ID of the file system-based HyperMetro domain. | To obtain the value, run the "show fs_hyper_metro_domain general" command. |

##### Usage Guidelines

None

##### Example

Query all vStore pairs in file system-based HyperMetro domain 10100.

```text
admin:/>show fs_hyper_metro_domain vstore_pair domain_id=10100
ID                                Health Status  Running Status  Config Status       Link Status  Domain Name  Local Vstore Name  Remote Vstore Name
--------------------------------  -------------  --------------  ------------------  -----------  -----------  -----------------  ------------------
21007cc3855e80330000000600000000  Normal         Normal          To Be Synchronized  Linkup       domain       vstore0            vstore0
21007cc3855e80330000000600000001  Normal         Normal          To Be Synchronized  Linkup       domain       vstore1            vstore0
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                                                            |
|--------------------|------------------------------------------------------------------------------------|
| ID                 | UUID of the vStore pair, 64 bits.                                                  |
| Health Status      | Health status, which can be normal or faulty.                                      |
| Running Status     | Running status, which can be normal, unsynchronized, forced start, or invalid.     |
| Config Status      | Synchronization status, which can be normal, synchronizing, or to be synchronized. |
| Link Status        | Link status. The value can be "Linkup" or "Linkdown".                              |
| Domain ID          | ID of the HyperMetro domain.                                                       |
| Domain Name        | Name of the HyperMetro domain.                                                     |
| Local Vstore ID    | ID of the local vStore.                                                            |
| Local Vstore Name  | Name of the local vStore.                                                          |
| Remote Vstore ID   | ID of the remote vStore.                                                           |
| Remote Vstore Name | Name of the remote vStore.                                                         |
