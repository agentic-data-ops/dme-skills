# add remote_support user_contact


##### Function

The **add remote_support user_contact** command is used to add the contacts of eService.

##### Format

**add remote_support user_contact** first_name=? last_name=? email=? country_calling_code=? mobile=?

##### Parameters

| Parameter            | Description                               | Value                                                                                                            |
|----------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| first_name           | First name of the user contact.           | The value contains 1 to 63 characters including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| last_name            | Last name of the user contact.            | The value contains 1 to 63 characters including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| email                | Email of the user contact.                | The value consists of 5 to 127 ASCII characters.                                                                 |
| country_calling_code | Country calling code of the user contact. | The value contains 1 to 31 characters including digits and symbols (\* \# + - ( )).                              |
| mobile               | Mobile phone number of the user contact.  | The value contains 1 to 31 characters including digits and symbols (\* \# + - ( )).                              |

##### Usage Guidelines

This command is used to add the contacts of eService. You can query the existing contacts of a storage system by running the "show remote_support user_contact" command.

##### Example

Add the contacts of eService.

```text
admin:/>add remote_support user_contact first_name=Abc last_name=Zhang email=abc@bar.com country_calling_code=+86 mobile=7654321
Command executed successfully.
```

##### System Response

None
