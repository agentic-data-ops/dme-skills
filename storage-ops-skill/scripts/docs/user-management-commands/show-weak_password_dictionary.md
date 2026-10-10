# show weak_password_dictionary


##### Function

The **show weak_password_dictionary** command is used to query weak passwords in the weak password dictionary.

##### Format

**show weak_password_dictionary**

##### Parameters

None

##### Usage Guidelines

After this command is executed successfully, the system displays all weak passwords in the current weak password dictionary.

##### Example

Query weak passwords in an empty weak password dictionary.

```text
admin:/>show weak_password_dictionary
Weak Password
-------------
--
```

Query weak passwords in the weak password dictionary, which contains three weak passwords: "Admin@storage", "Changeme_123", and "1234567890abcdefg".

```text
admin:/>show weak_password_dictionary
Weak Password
-----------------
Admin@storage
Changeme_123
1234567890abcdefg
--
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                |
|---------------|--------------------------------------------------------|
| Weak Password | Weak password in the current weak password dictionary. |
