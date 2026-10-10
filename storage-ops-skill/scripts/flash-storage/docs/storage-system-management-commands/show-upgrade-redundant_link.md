# show upgrade redundant_link


##### Function

The **show upgrade redundant_link** command is used to query whether each controller has front-end redundant links.

##### Format

**show upgrade redundant_link**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query whether each controller has front-end redundant links.

```text
admin:/>show upgrade redundant_link
Name   Result
-----  ------
0A     True
0B     True
0C     True
0D     True
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Name | Controller name, for example: "0A", "0B", "1A", and "2B". |
| Result | Whether the controller has redundant links. <br>"True": There are redundant links.<br>"False": There are no redundant links. |
