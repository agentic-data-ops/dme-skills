# show domain controller


##### Function

The **show domain controller** command is used to query the domain controller list.

##### Format

**show domain controller** \[ type=? \] \[ domain_controller_ip_address=? \] \[ controller=? \]

##### Parameters

| Parameter    | Description    | Value                                                                                                                                                                |
|--------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| controller=? | Controller ID. | The value format can be "XA", "XB", "XC", and "XD", where "X" can be an integer ranging from 0 to 3. To obtain the value, run the "show controller general" command. |

##### Usage Guidelines

None

##### Example

Query the domain controller list.

```text
admin:/>show domain controller controller=0A
Domain Controller Name FQDN Name Priority Weight Write Enabled Prime Domain Controller Enabled Is Available Controller IP Address
---------------------- ----------------------- -------- ------ ------------- ------------------------------- ----------------------- -------------------------------
WIN-6KF39LUH71U win-6kf39luh71u.qqq.com 0 100 Yes Yes Yes 10.178.130.7:1,192.168.130.7:1
```

Query information about a domain controller using its IP address.

```text
developer:/>show domain controller type=one_domain_controller domain_controller_ip_address=10.178.130.7 controller=0A
Domain Controller Name FQDN Name Priority Weight Write Enabled Prime Domain Controller Enabled Is Available Controller IP Address
---------------------- ----------------------- -------- ------ ------------- ------------------------------- ----------------------- -------------------------------
WIN-6KF39LUH71U win-6kf39luh71u.qqq.com 0 100 Yes Yes Yes 10.178.130.7:1,192.168.130.7:1
```

Query information about all domain controllers using DNS.

```text
developer:/>show domain controller type=all_domain_controller controller=0A
FQDN Name                Priority Weight  IP Address
-----------------------  -------- ------  -------------------------------
win-6kf39luh71u.qqq.com  0        100     10.178.130.7:1,192.168.130.7:1
```

##### System Response

The following table describes the parameter meanings.

| Parameter                       | Meaning                                                  |
|---------------------------------|----------------------------------------------------------|
| Domain Controller Name          | Name of the domain controller.                           |
| FQDN Name                       | FQDN of the domain controller.                           |
| Priority                        | Priority of the domain controller.                       |
| Weight                          | Domain controller weight.                                |
| Write Enabled                   | Whether the domain controller allows writes.             |
| Prime Domain Controller Enabled | Whether the domain controller is the primary controller. |
| Is Available Controller         | Whether the domain controller is available.              |
| IP Address                      | Domain controller IP address.                            |
