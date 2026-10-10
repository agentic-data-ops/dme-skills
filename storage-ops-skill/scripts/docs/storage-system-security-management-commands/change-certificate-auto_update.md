# change certificate auto_update


##### Function

The **change certificate auto_update** command is used to modify the automatic certificate update configuration.

##### Format

**change certificate auto_update** type=? \[ enabled=? \] \[ common_name=? \] \[ valid_period=? \] \[ subject_alt_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate type. | Possible values are: <br>"domain_authentication": domain authentication.<br>"email_authentication": email server authentication.<br>"devicemanager_authentication": DeviceManager authentication.<br>"OTP_email_authentication": OTP email server authentication.<br>"file_service_domain_authentication": file service domain authentication.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol. |
| enabled | Whether to enable automatic certificate update. | The value can be: <br>"yes": enables automatic certificate update.<br>"no": disables automatic certificate update. |
| common_name | common name field in the certificate subject. | The value is a non-null string containing a maximum of 256 characters. |
| valid_period | Validity period of the certificate after automatic update. | The value can be: <br>"10": 10 years.<br>"3": 3 years.<br>"1": 1 year. |
| subject_alt_name | SubjectAltName of the issued certificate. | The value is a non-null string containing a maximum of 256 characters. |

##### Usage Guidelines

Run the **change certificate auto_update** command to modify the automatic certificate update configuration.

##### Example

Modify the automatic certificate update configuration in the corresponding scenario.

```text
admin/>change certificate auto_update type=email_authentication enabled=yes valid_period=10 common_name=Storage subject_alt_name=test
WARNING: You are about to enable the automatic certificate update function. After this operation, the certificate will be automatically updated before it expires, which may interrupt services that use the certificate.
Suggestion: Before performing this operation, check whether the risk is acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
