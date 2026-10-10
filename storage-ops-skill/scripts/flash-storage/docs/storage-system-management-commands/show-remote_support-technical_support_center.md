# show remote_support technical_support_center


##### Function

The **show remote_support technical_support_center** command is used to query information about the technical support center.

##### Format

**show remote_support technical_support_center**

##### Parameters

None

##### Usage Guidelines

Running this command displays information about the technical support center.

##### Example

Query information about the technical support center.

```text
admin:/>show remote_support technical_support_center

ID        Technical Support Center             Server URL
--------  -----------------------------------  ---------------------------------
CenterCC  Carrier in Chinese mainland          icloudservice-cn.huawei.com
CenterCR  Carrier outside Chinese mainland     itr-eservicero-carrier.huawei.com
CenterEC  Enterprise in Chinese mainland       ecloudService-cn.huawei.com
CenterER  Enterprise outside Chinese mainland  itr-eservicero-ent.huawei.com
```

##### System Response

The following table describes the parameter meanings.

| Parameter                | Meaning                               |
|--------------------------|---------------------------------------|
| ID                       | ID.                                   |
| Technical Support Center | Name of the technical support center. |
| Server URL               | Server URL.                           |
