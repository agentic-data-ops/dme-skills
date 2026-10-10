# change effective_capacity general


##### Function

The **change effective_capacity general** command is used to modify the attributes of the effective capacity.

##### Format

**change effective_capacity general** { insufficient_threshold=? \| used_up_threshold=? \| delay_day=? }

##### Parameters

| Parameter                | Description                                                             | Value                                    |
|--------------------------|-------------------------------------------------------------------------|------------------------------------------|
| insufficient_threshold=? | Alarm threshold indicating that the effective capacity is insufficient. | The value ranges from 1 to 95 (unit: %). |
| used_up_threshold=?      | Alarm threshold indicating that the effective capacity is used up.      | The value ranges from 2 to 99 (unit: %). |

##### Usage Guidelines

The **change effective_capacity general** command is used to modify the attributes of the effective capacity, including the alarm thresholds indicating the insufficient capacity and used up capacity, and days after the grace period.

##### Example

Modify the alarm thresholds for the effective capacity.

```text
admin:/>change effective_capacity general insufficient_threshold=80 used_up_threshold=90
Command executed successfully.
```

##### System Response

None
