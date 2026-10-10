# show license_active


##### Function

The **show license_active** command is used to query information about active licenses.

##### Format

**show license_active**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information about active licenses.

```text
admin:/>show license_active

LICENSE ESN               : 210235G7FLZ0D4000035
LICENSE SERVICE AUTH TYPE : DEMO
LICENSE SWM TIME          : 0000-00-00
LICENSE HWM TIME          : 0000-00-00
LICENSE SFUPDATE TIME     : 0000-00-00
LICENSE VERSION           : V100R001
LICENSE LIBVER            : AdaptiveLMV100R002C05SPC007
LICENSE COMMENT           :
IS TEMP LICENSE           : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                                      |
|---------------------------|--------------------------------------------------------------|
| LICENSE ESN               | Indicates hardware serial number (SN) or unique software SN. |
| LICENSE SERVICE AUTH TYPE | Indicates the authorization type.                            |
| LICENSE SWM TIME          | Indicates the software maintenance end time.                 |
| LICENSE HWM TIME          | Indicates the hardware maintenance end time.                 |
| LICENSE SFUPDATE TIME     | Expiration date of free software upgrade.                    |
| LICENSE VERSION           | Indicates the product version.                               |
| LICENSE LIBVER            | Indicates the License file format version.                   |
| LICENSE COMMENT           | Indicates the comments related to the product.               |
| IS TEMP LICENSE           | Indicates whether a file is a temporary license file.        |
