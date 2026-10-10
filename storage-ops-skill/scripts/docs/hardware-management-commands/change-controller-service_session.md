# change controller service_session


##### Function

The **change controller service_session** command is used to change the service duration of a controller.

##### Format

**change controller service_session** controller_id=? session=?

##### Parameters

| Parameter       | Description       | Value                                               |
|-----------------|-------------------|-----------------------------------------------------|
| controller_id=? | Controller ID.    | To obtain the value, run "show controller general". |
| session         | Service duration. | The value ranges from 0 to 600, in months.          |

##### Usage Guidelines

The service time of the controller electronic insurance policy must be consistent with that in the contract. The unit of the service time of the controller electronic insurance policy is month. The value ranges from 0 to 600.

##### Example

Change the service life of the controller electronic insurance policy.

```text
admin:/>change controller service_session controller_id=0A session=50
CAUTION: You are about to modify the service duration of the controller. The value ranges from 0 to 600, in months. This operation may cause extra alarms or errors.
Suggestion: To prevent extra alarms or errors, ensure that the entered information is consistent with the contract information and that the entered parameters are valid.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
