# change hyper_metro_pair pause


##### Function

The **change hyper_metro_pair pause** command is used to pause a HyperMetro pair.

##### Format

**change hyper_metro_pair pause** pair_id=? \[ stop_role=? \]

**change hyper_metro_pair pause** pair_id_list=? \[ stop_role=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | HyperMetro pair ID. | Run the "show hyper_metro_pair general" command to obtain the value. |
| pair_id_list=? | HyperMetro pair ID list. | You can run the "show hyper_metro_pair general" command to obtain the IDs.<br>IDs of multiple pairs are separated by commas (,).<br>A maximum of 100 IDs can be entered. |
| stop_role=? | Site whose services you want to stop (When the running status of a HyperMetro pair is "Synchronizing" or "To Be Synchronized", you cannot stop services at the site that uniquely provides host read and write services). | The value can be "Preferred" or "Non-preferred", where: <br>"Preferred": Preferred site.<br>"Non-preferred": Non-preferred site. |

##### Usage Guidelines

None

##### Example

Pause HyperMetro pair "1".

```text
admin:/>change hyper_metro_pair pause pair_id=1
CAUTION: You are about to pause a HyperMetro pair.
Once a HyperMetro pair is paused, cross-site real-time data mirroring stops. Member resource in the HyperMetro pair can only be accessed unidirectionally.
Suggestion: Before performing this operation, ensure that the storage arrays at the two data centers are connected to hosts properly to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Pause HyperMetro pairs 1 and 2.

```text
admin:/>change hyper_metro_pair pause pair_id_list=1,2
CAUTION: You are about to pause a HyperMetro pair.
Once a HyperMetro pair is paused, cross-site real-time data mirroring stops. Member resource in the HyperMetro pair can only be accessed unidirectionally.
Suggestion: Before performing this operation, ensure that the storage arrays at the two data centers are connected to hosts properly to prevent service exceptions.
Do you wish to continue?(y/n)y
Change hyper metro pair pause 1 successfully.
Change hyper metro pair pause 2 successfully.
```

##### System Response

None
