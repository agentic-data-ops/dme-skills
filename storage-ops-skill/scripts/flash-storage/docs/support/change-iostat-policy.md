# change iostat policy


##### Function

The **change iostat policy** command is used to set an I/O statistical policy.

##### Format

**change iostat policy** \[ forward_seek_range=? \] \[ backward_seek_range=? \] \[ read_io_size_range=? \] \[ write_io_size_range=? \] \[ read_io_size=? \] \[ write_io_size=? \] \[ io_delay_range=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| forward_seek_range=? | Forward seek range. | The value contains five increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 99, expressed in percentage.<br>The default value is "0,20,40,60,80". |
| backward_seek_range=? | Backward seek range. | The value contains five increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 99, expressed in percentage.<br>The default value is "0,20,40,60,80". |
| read_io_size_range=? | Read I/O range. | The value contains five increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 4,294,967,295, expressed in KB.<br> Example: 1,100,1000,10000,100000. |
| write_io_size_range=? | Write I/O range. | The value contains five increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 4,294,967,295, expressed in KB.<br> Example: 1,100,1000,10000,100000. |
| read_io_size=? | Read I/O size. | The value contains nine increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 4,294,967,295, expressed in KB.<br> Example: 2,4,8,16,32,64,128,256,512. |
| write_io_size=? | Write I/O size. | The value contains nine increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 4,294,967,295, expressed in KB.<br> Example: 2,4,8,16,32,64,128,256,512. |
| io_delay_range=? | I/O latency range. | The value contains five increasing integers, which are separated by commas (,).<br>Each integer ranges from 0 to 4,294,967,295, expressed in ms.<br> Example: 50,100,200,400,800. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 3000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Set the forward seek range to "0,30,50,70,80".

```text
admin:/change iostat policy forward_seek_range=0,30,50,70,80
Command executed successful
```

##### System Response

None
