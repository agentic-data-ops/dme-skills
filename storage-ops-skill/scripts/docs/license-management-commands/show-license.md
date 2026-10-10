# show license


##### Function

The **show license** command is used to query information about the function configuration of the imported license files.

##### Format

**show license**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information about the function configuration of the imported license files.

```text
admin:/>show license

CopyRight    : Huawei Technologies Co., Ltd.
All rights reserved.

License SN   : LIC20170710CAHM50
File Creator : Huawei Technologies Co., Ltd.
Created On   : 2017-07-10 17:30:52
Country      : English
Operator     : RD of Huawei Technologies Co., Ltd.
Region       : ShenZhen

Feature Name   : SmartThin
Feature ID     : 25
License Status : Valid
Open Status    : Open
Left Day(s)    : 138
Resource Limit : 0
--------------------------------------------
Feature Name   : SmartMigration
Feature ID     : 5
License Status : Valid
Open Status    : Open
Left Day(s)    : 138
Resource Limit : 0
--------------------------------------------
Feature Name   : HyperSnap
Feature ID     : 2
License Status : Valid
Open Status    : Open
Left Day(s)    : 138
Resource Limit : 0
--------------------------------------------
Feature Name   : HyperReplication
Feature ID     : 24
License Status : Valid
Open Status    : Open
Left Day(s)    : 138
Resource Limit : 0
--------------------------------------------
Feature Name   : SmartVirtualization
Feature ID     : 29
License Status : Valid
Open Status    : Open
Left Day(s)    : 138
Resource Limit : 0
--------------------------------------------
--More--
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                                           |
|----------------|-----------------------------------------------------------------------------------|
| Feature Name   | Feature name.                                                                     |
| Feature ID     | Feature ID.                                                                       |
| License Status | Status of a license file. The value can be "Valid", "To Be Expire", or "Expired". |
| Open Status    | Feature switch status.                                                            |
| Left Day(s)    | Days until a license file expires.                                                |
| Resource Limit | Resource limit.                                                                   |
