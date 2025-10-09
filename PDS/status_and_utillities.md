# Status & utillities

## Status and status clear words
The terms 'Status' and 'Status Clear' indicate basic binary states or events within a module, such as whether it is enabled or a limit has been exceeded. The U32 bitwise type means that each bit in the value represents a different purpose rather than a singular numerical value. Like properties, status bits are module-specific—each module defines its own set, which may or may not align with those of othermodules.

<style>
  body {
    font-family: Arial, sans-serif;
    padding: 10px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    table-layout: auto;
    min-width: 600px;
    margin: 0 auto;
  }

  th, td {
    padding: 10px;
    font-size: 14px;
  }
</style>

<table>
  <tr>
    <th rowspan = "2"> NAME</th>
    <th rowspan = "2"> BIT POSITION</th>
    <th rowspan = "2"> DESCRIPTION</th>
    <th colspan = "4"> AVAILABILITY ON MODULES</th>
  </tr>
  <tr>
    <th> CB</th>
    <th> PS</th>
    <th> BR</th>
    <th> IC</th>
  </tr>
  <tr>
    <td> Enabled</td>
    <td> 0</td>
    <td> Indicates whenever the module is enabled or not. Note that in case of Control board it indicates entire device power on status.</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> Over temperature</td>
    <td> 1</td>
    <td> The temperature limit of the module has been exceeded</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> Over current</td>
    <td> 2</td>
    <td> The current limit of the module has been exceeded (OCD state )</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> STO1</td>
    <td> 10</td>
    <td> Safe Turn Off at input 1 has been triggered</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> STO2</td>
    <td> 11</td>
    <td> Safe Turn Off at input 2 has been triggered</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> FDCAN Timeout</td>
    <td> 12</td>
    <td> CAN message processing timeout</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 1 error</td>
    <td> 13</td>
    <td rowspan = "6"> Some error occurs on the module connected to the socket ( 1 - 6 ). Refer to the particular module status word for more details about the issue</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 2 error</td>
    <td> 14</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 3 error</td>
    <td> 15</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 4 error</td>
    <td> 16</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 5 error</td>
    <td> 17</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 6 error</td>
    <td> 18</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Charger detection</td>
    <td> 19</td>
    <td> Indicates whenever charger has been connected to the device</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Shutdown schedule</td>
    <td> 20</td>
    <td> Indicates that the PDS device shutdown has been scheduled and the PDS device is about to be turned off within the time specified in the "Shutdown time" property of the control board.</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
</table>

