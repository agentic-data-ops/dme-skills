# show weak_password_switch


##### Function

The show weak_password_dictionary switch command is used to check whether the weak password dictionary function is enabled.

##### Format

**show weak_password_switch**

##### Parameters

None

##### Usage Guidelines

After this command is executed successfully, the system displays the status of the weak password dictionary function. Value "On" indicates that the weak password dictionary function is enabled, and "Off" indicates that the weak password dictionary function is disabled.

OceanStor Dorado 18000 V6, Dorado 3000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the weak password dictionary status.

```text
admin:/>show weak_password_dictionary switch
Switch
------
On
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                                   |
|-----------|-----------------------------------------------------------|
| Switch    | Whether the weak password dictionary function is enabled. |
