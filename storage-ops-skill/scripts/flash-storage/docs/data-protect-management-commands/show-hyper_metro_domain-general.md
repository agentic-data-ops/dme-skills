# show hyper_metro_domain general


##### Function

The **show hyper_metro_domain general** command is used to query HyperMetro domains.

##### Format

**show hyper_metro_domain general** \[ domain_id=? \]

##### Parameters

| Parameter   | Description                  | Value                                                                                                                                                                                                                                                                                 |
|-------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| domain_id=? | ID of the HyperMetro domain. | Run the "**show hyper_metro_domain general**" command obtain the value.The value of the "domain_id" parameter contains 1 to 16 characters. |

##### Usage Guidelines

None

##### Example

Query all the HyperMetro domains in the device.

```text
admin:/>show hyper_metro_domain general

ID Name Running Status Remote Device ID Remote Device Name Quorum Server ID Quorum Server Name
-- ---- ---------------- ------------------ ---------------- ----------------- ------------------
1 BJ-TJ Normal 1 array_s5000 2 service-win
2 BJ-SH Normal 2 array_s6000 2 service-win
```

Query HyperMetro domain "1".

```text
admin:/>show hyper_metro_domain general domain_id=1
ID : 1
Name : BJ-TJ
Running Status : Normal
Description : beijing-tianjin
Remote Device ID : 1
Remote Device Name : ARRAY-S5000
Quorum Server ID : 1
Quorum Server Name : SERVICE-WIN
Quorum Mode : Quorum Server
Is Arb Opt Switch : Open
Standby Quorum Server ID : 2
Standby Quorum Server Name : SERVICE-LINUX
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                           |
|----------------------------|---------------------------------------------------|
| Remote Device Name         | Name of remote storage device.                    |
| Quorum Server Name         | Name of the quorum server.                        |
| Running Status             | Running status: Normal,Invalid,To Be Recovered.   |
| Remote Device ID           | ID of remote storage device.                      |
| Quorum Server ID           | ID of the quorum server.                          |
| Quorum Mode                | Mode of quorum: Quorum Server or Static Priority. |
| ID                         | ID of the HyperMetro domain.                      |
| Name                       | Name of the HyperMetro domain.                    |
| Description                | Description of the HyperMetro domain.             |
| Is Arb Opt Switch          | Arbitration optimization switch.                  |
| Standby Quorum ID          | ID of the standby quorum server.                  |
| Standby Quorum Server Name | Name of standby quorum server.                    |
