# show domain ad


##### Function

The **show domain ad** command is used to query the configuration of the AD domain controller and check whether the storage array has successfully joined the domain.

##### Format

**show domain ad**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the configuration of the AD domain controller.

```text
admin:/>show domain ad
Domain Status : Joined
Full Domain Name : auth2k12.com
Organization Unit : CN=Computers,DC=auth2k12,DC=com
System Name : storage
Site Name : china
Join Domain Error Info : Success
DDNS Enabled : Enable
DDNS TTL(s) : 86400
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                                                           |
|------------------------|-----------------------------------------------------------------------------------|
| Domain Status          | Status of the domain that the storage array joins.                                |
| Full Domain Name       | Name of the domain that the storage array joins.                                  |
| Organization Unit      | Organization unit that is added when the storage array joins the domain.          |
| System Name            | Machine account used by the storage array to join the domain.                     |
| Site Name              | Site where the domain controller resides when the storage array joins the domain. |
| Join Domain Error Info | Descriptions of the cause why the storage array fails to join the domain.         |
| DDNS Enable            | Whether the DNS server update is allowed.                                         |
| DDNS TTL(s)            | Validity period of the DNS cache.                                                 |
