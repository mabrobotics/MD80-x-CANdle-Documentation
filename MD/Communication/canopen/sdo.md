(canopen_sdo)=
# Service Data Objects

SDO transfers are the request and response mechanism for reading and writing the object dictionary.
Every configuration task uses them. They are confirmed, so the drive answers each request with
either an acknowledgement or an abort carrying a reason code.

| Direction       | COB-ID      |
| --------------- | ----------- |
| Master to drive | 0x600 + node ID |
| Drive to master | 0x580 + node ID |

The drive implements the default server SDO only. There is no client SDO and no configurable second
server. Requests must be exactly 8 data bytes; anything shorter or longer is discarded without a
reply.

## Expedited transfer

Objects of 4 bytes or fewer are transferred expedited, with the value carried in the same frame as
the request. This covers almost everything in the dictionary: all setpoints, all limits, all gains
and all status registers.

Before the drive applies an expedited write it first reads the target object to learn its real size.
Two consequences follow. Writing to an index or sub-index that does not exist is rejected before any
value is touched, and a write whose declared size does not match the object is rejected rather than
truncated.

## Segmented transfer

Objects larger than 4 bytes use segmented transfer. In this dictionary that means the string
objects: Motor Name 0x2000:6, the commit hashes in 0x2021, and the identification strings in 0x1008,
0x1009 and 0x2020.

The drive stages segmented transfers in a single 32 byte buffer, so only one segmented transfer can
be in progress at a time and no object larger than 32 bytes can be transferred. Starting a second
one while the first is open aborts the first.

An idle segmented transfer is abandoned after **1000 ms**. The drive sends an abort with code
0x05040000 and frees the buffer.

```{note}
Attempting an expedited write to a string object is rejected with 0x06070013 rather than silently
writing four characters. Use segmented transfer for anything longer than 4 bytes.
```

## Abort codes

When the drive cannot serve a request it answers with an abort frame carrying one of the codes
below. The abort always echoes the index and sub-index that caused it, except for a segment request
arriving with no transfer open, where both are reported as zero.

| Code       | Meaning                                       | Typical cause on an MD drive                                               |
| ---------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| 0x05030000 | Toggle bit not alternated                     | A segmented transfer went out of sequence                                   |
| 0x05040000 | SDO protocol timed out                        | A segmented transfer stalled for more than one second                       |
| 0x05040001 | Invalid command specifier                     | A segment was sent with no transfer open, or a reserved command was used    |
| 0x05040005 | Out of memory                                 | The object is larger than the 32 byte staging buffer                        |
| 0x06010000 | Unsupported access to an object               | A PDO mapping entry was written while the mapping was still enabled         |
| 0x06010002 | Attempt to write a read-only object           | The object is measurement or identification data                            |
| 0x06020000 | Object does not exist                         | The index is not in the dictionary                                          |
| 0x06040041 | Object cannot be mapped to the PDO            | The object is not PDO mappable, or the mapped size does not match it        |
| 0x06040042 | Mapped objects exceed PDO length              | The mapping adds up to more than 64 bits                                    |
| 0x06070012 | Data type does not match, length too high     | More bytes were supplied than the object holds                              |
| 0x06070013 | Data type does not match, length too low      | Fewer bytes were supplied than the object needs, including expedited writes to strings |
| 0x06090011 | Sub-index does not exist                      | The index exists but the sub-index does not                                 |
| 0x06090030 | Value range of parameter exceeded             | The value is outside the range the firmware accepts, see the [object dictionary](canopen_od) |
| 0x08000020 | Data cannot be transferred or stored          | A per-mille torque or current object was accessed while its rated value is still zero, or 0x1010 or 0x1011 was written with the wrong signature |

```{important}
0x06090030 is the code you will meet most often during commissioning. The ranges the firmware
enforces are narrower than the data type suggests, and for some objects they are narrower than the
EDS declares. The per-object ranges are listed in the [object dictionary](canopen_od).
```

## Availability

SDO access follows the NMT state. It works in Pre-operational and Operational, and is refused in
Stopped, where the drive does not answer at all. See [Network Management](canopen_nmt).
