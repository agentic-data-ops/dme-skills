# show identity_mapping config


##### Function

The **show identity_mapping config** command is used to check user mapping configurations.

##### Format

**show identity_mapping config**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the identity_mapping configurations.

```text
admin:/>show identity_mapping config
Provider                 : LOCAL
IDMU Base DN             : --
IDMU Timeout(s)          : 15
IDMU Windows Objectclass : user
IDMU Unix Objectclass    : user
Default Windows User     : admin
Default Unix User        : root
Same Name Switch         : on
```

##### System Response

Information about user mapping configurations.

| Parameter                | Meaning                                                    |
|--------------------------|------------------------------------------------------------|
| Provider                 | Provider of user mapping rules.                            |
| IDMU Base DN             | Base DN queried by the IDMU.                               |
| IDMU Timeout(s)          | Timeout of IDMU query.                                     |
| IDMU Windows Objectclass | objectclass used by the Windows user searched by the IDMU. |
| IDMU Unix Objectclass    | objectclass used by the Unix user searched by the IDMU.    |
| Default Windows User     | Default windows user.                                      |
| Default Unix User        | Default unix user.                                         |
| Same Name Switch         | The switch of use a mapping with the same name.            |
