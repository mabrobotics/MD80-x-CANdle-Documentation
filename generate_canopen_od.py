"""Generate MD/Communication/canopen/object_dictionary.md from the MD EDS file.

Usage:
    python generate_canopen_od.py [path/to/md_x.y.eds]

Defaults to _static/eds/md_1.2.eds and overwrites MD/Communication/canopen/object_dictionary.md.

The EDS supplies names, data types, access types, defaults and PDO mappability.
The prose in DESC and the value ranges in NOTE are maintained by hand, because the
firmware enforces limits the EDS does not declare. When the EDS changes, rerun this
script and review both dictionaries for entries that were added or removed.
"""

import configparser, re, sys
from pathlib import Path

EDS_DEFAULT = Path("_static/eds/md_1.2.eds")
OUT = Path("MD/Communication/canopen/object_dictionary.md")

DT = {1:"BOOLEAN",2:"INT8",3:"INT16",4:"INT32",5:"UINT8",6:"UINT16",7:"UINT32",
      8:"REAL32",9:"STRING",10:"OCTET_STRING",15:"DOMAIN",27:"UINT64"}
ACC = {"ro":"ro","rw":"rw","rww":"rww","const":"ro","wo":"wo"}

cp = configparser.ConfigParser(strict=False)
cp.optionxform = str
eds = Path(sys.argv[1]) if len(sys.argv) > 1 else EDS_DEFAULT
cp.read(eds)

def g(s,k,d=""):
    return cp[s].get(k,d) if cp.has_section(s) else d

# Object-level prose. Keyed by uppercase 4-hex index.
DESC = {
"1000":"Identifies the device profile. Reads 0x00020192: profile 402 in the low word, servo drive in the high word.",
"1001":"One byte summary of active faults. See [Diagnostics](canopen_diagnostics) for the bit meanings.",
"1010":"Saves the configuration to flash, the CiA 301 equivalent of Save Config 0x2023:1. Write-only: reading any sub-index other than 0 aborts with 0x05040001.",
"1011":"Restores factory defaults and saves them, the CiA 301 equivalent of Revert Factory Settings 0x2023:7. Only sub-index 4 is implemented. Write-only: reading any sub-index other than 0 aborts with 0x05040001.",
"1005":"Identifier the drive listens on for SYNC. Fixed at 0x80; the drive never produces SYNC itself.",
"1008":"Device name string.",
"1009":"Hardware version string.",
"1014":"Identifier the drive transmits emergency messages on.",
"1016":"Watchdog on another node. Bits 0-15 are the timeout in milliseconds, bits 16-23 the node ID to watch. A timeout raises a communication error and commands a quick stop. See [Network Management](canopen_nmt).",
"1017":"Heartbeat period in milliseconds. 0 disables the heartbeat.",
"1018":"Vendor, product, revision and serial identification. The vendor ID is 0 because MAB Robotics has no CiA-assigned vendor ID yet.",
"1400":"Communication parameters for RPDO1. The COB-ID is stored and read back but is not used for filtering; RPDO1 is always received on 0x200 plus the node ID. See [PDO](canopen_pdo).",
"1401":"Communication parameters for RPDO2, received on 0x300 plus the node ID.",
"1402":"Communication parameters for RPDO3, received on 0x400 plus the node ID.",
"1403":"Communication parameters for RPDO4, received on 0x500 plus the node ID.",
"1600":"Mapping for RPDO1. Default: Target Position and Target Torque.",
"1601":"Mapping for RPDO2. Default: Target Velocity and Target Torque.",
"1602":"Mapping for RPDO3. Default: Controlword, Target Position and Target Torque.",
"1603":"Mapping for RPDO4. Default: Controlword, Target Velocity and Target Torque.",
"1800":"Communication parameters for TPDO1. The COB-ID is used exactly as stored, with no node ID offset. See [PDO](canopen_pdo).",
"1801":"Communication parameters for TPDO2.",
"1802":"Communication parameters for TPDO3.",
"1803":"Communication parameters for TPDO4.",
"1A00":"Mapping for TPDO1. Default: Statusword and Quick Status.",
"1A01":"Mapping for TPDO2. Default: Position Actual Value and Velocity Actual Value.",
"1A02":"Mapping for TPDO3. Default: Torque Actual Value, Power Stage Temperature and Motor Temperature.",
"1A03":"Mapping for TPDO4. Default: DC Link Circuit Voltage.",
"2000":"Motor and actuator identity. These values describe the physical motor and are needed before calibration can run. Sub-index 0 reports 10.",
"2001":"Onboard commutation encoder.",
"2002":"Optional encoder on the output shaft. See [Encoders](aux_encoders).",
"2003":"Optional external torque sensor. See [External Torque Sensor](md_torque_sensor).",
"2004":"Measured temperatures.",
"2010":"Position loop gains, used in Cyclic Synchronous Position. See [Position PID](position-pid).",
"2011":"Velocity loop gains, used in Cyclic Synchronous Velocity and by both profile modes. See [Velocity PID](velocity-pid).",
"2012":"Impedance mode stiffness and damping. See [Impedance PD](impedance-pd).",
"2020":"Read-only board identification, programmed during production.",
"2021":"Read-only firmware and bootloader identification.",
"2022":"Manufacturer status registers. Bit meanings are documented in [Status](status) and summarised in [Diagnostics](canopen_diagnostics).",
"2023":"Manufacturer commands. Trigger one by writing 1; any other value aborts with 0x06090030. Several of these reboot the drive.",
"2024":"The two user GPIO pins. See [GPIO](GPIO) for the electrical limits.",
"603F":"CiA 402 code for the most recent fault. Latches until the drive is reset.",
"6040":"Commands the CiA 402 state machine. See [State Machine](canopen_state_machine).",
"6041":"Reports the CiA 402 state. Carries the state bits only.",
"6060":"Selects the active controller. See [Modes of Operation](canopen_modes).",
"6061":"Reports the active mode. Gives the same answer as reading 0x6060.",
"6064":"Measured output shaft position.",
"6067":"Tolerance used to decide that a position move has arrived. Reported through bit 15 of Quick Status.",
"606C":"Measured output shaft velocity.",
"606D":"Tolerance used to decide that a velocity command has been reached.",
"6071":"Torque setpoint, and the feed-forward torque in Impedance mode.",
"6072":"Torque limit applied to every mode.",
"6073":"Phase current limit.",
"6075":"Nameplate current of the motor. Must be non-zero before 0x6073 can be used.",
"6076":"Nameplate torque of the motor. Must be non-zero before 0x6071, 0x6072 or 0x6077 can be used.",
"6077":"Measured torque at the output shaft.",
"6079":"Measured DC link voltage.",
"607A":"Position setpoint. In Profile Position it is the destination; in Cyclic Synchronous Position it is applied directly; in Impedance it is the equilibrium point.",
"607B":"Hard bounds of the position representation. Read only, and fixed to the full INT32 range.",
"607D":"Software position limits. Setting both sub-indices to the same value disables limiting.",
"6080":"Speed limit applied to every mode, and the clamp on the position loop output.",
"6083":"Acceleration used by the trajectory generator in both profile modes.",
"6084":"Deceleration used by the trajectory generator in both profile modes.",
"6085":"Deceleration used for quick stop, including the automatic quick stop on a heartbeat timeout.",
"6091":"Gearbox ratio. All shaft quantities are computed with it applied.",
"60A8":"Declares the position unit, micro-revolutions. Read only.",
"60A9":"Declares the velocity unit, micro-revolutions per second. Read only.",
"60AA":"Declares the acceleration unit, micro-revolutions per second squared. Read only.",
"60FF":"Velocity setpoint. In Profile Velocity it is the target; in Profile Position it is the cruise velocity; in Cyclic Synchronous Velocity it is applied directly; in Impedance it is the equilibrium velocity.",
"6502":"Bit field of supported CiA 402 modes. Reads 0x00000185.",
}

# Per-entry unit / range notes, keyed by "INDEX" or "INDEX:sub".
NOTE = {
"1010:0":"always reports 4, although only sub-index 1 is implemented",
"1010:1":"write the signature 0x65766173, ASCII \"save\"; any other value aborts with 0x08000020",
"1011:0":"always reports 4, although only sub-index 4 is implemented",
"1011:4":"write the signature 0x64616F6C, ASCII \"load\"; any other value aborts with 0x08000020",
"1016:1":"ms in bits 0-15, node ID in bits 16-23",
"1017":"ms",
"2000:1":"10 to 127",
"2000:2":"2 to 42",
"2000:3":"H, 5e-9 to 0.1",
"2000:4":"ohm, 0.005 to 20",
"2000:5":"Hz, 10 to 2500",
"2000:6":"up to 24 characters, segmented transfer only",
"2000:7":"degrees C, 10 to 120",
"2000:8":"stored, not currently acted on by the firmware",
"2000:9":"Nm/A, must be greater than 0",
"2000:10":"RPM/V, must be greater than 0; writing it recomputes 0x2000:9 and is stored as a whole number",
"2001:1":"encoder type identifier, see [Setting Up a New Motor](canopen_setup)",
"2001:2":"-1.0 or 1.0 only",
"2002:1":"encoder type identifier, see [Setting Up a New Motor](canopen_setup)",
"2002:2":"-1.0 or 1.0 only",
"2002:3":"0 none, 1 startup, 2 motion, 3 report; takes effect after reboot",
"2002:4":"0 full, 1 direction only",
"2002:5":"micro-revolutions",
"2002:6":"micro-revolutions per second",
"2003:1":"0 none, 1 XJC sensor",
"2003:2":"Nm",
"2004:1":"degrees C",
"2004:2":"degrees C",
"2010:1":"must be 0 or positive",
"2010:2":"must be 0 or positive",
"2010:3":"must be 0 or positive",
"2010:4":"must be 0 or positive",
"2011:1":"must be 0 or positive",
"2011:2":"must be 0 or positive",
"2011:3":"must be 0 or positive",
"2011:4":"must be 0 or positive",
"2012:1":"must be 0 or positive",
"2012:2":"must be 0 or positive",
"2024:1":"0 input, 1 brake",
"6064":"micro-revolutions",
"6067":"micro-revolutions",
"606C":"micro-revolutions per second",
"606D":"micro-revolutions per second",
"6071":"1/1000 of 0x6076",
"6072":"1/1000 of 0x6076",
"6073":"1/1000 of 0x6075",
"6075":"mA",
"6076":"mNm",
"6077":"1/1000 of 0x6076",
"6079":"mV",
"607A":"micro-revolutions",
"607B:1":"micro-revolutions",
"607B:2":"micro-revolutions",
"607D:1":"micro-revolutions",
"607D:2":"micro-revolutions",
"6080":"micro-revolutions per second",
"6083":"micro-revolutions per second squared",
"6084":"micro-revolutions per second squared",
"6085":"micro-revolutions per second squared",
"60FF":"micro-revolutions per second",
}

PDO_SUB_NOTE = {
    "comm": {"0":"always reports 5", "1":"COB-ID", "2":"0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven",
             "3":"accepted but not enforced", "5":"ms, transmit PDOs only", "6":"declared in the EDS but not implemented"},
    "map":  {"0":"number of mapped objects, 0 to 8, write 0 before changing entries"},
}

def dtype(sec):
    raw = g(sec,"DataType","")
    try: return DT.get(int(raw,16), raw)
    except Exception: return raw

def rows(idx):
    subs = sorted([x for x in cp.sections() if re.fullmatch(re.escape(idx)+r"sub[0-9A-Fa-f]+", x, re.I)],
                  key=lambda x: int(x.lower().split("sub")[1],16))
    if not subs:
        return [(None, idx)]
    return [(int(x.lower().split("sub")[1],16), x) for x in subs]

def note_for(idx, sub):
    key = f"{idx.upper()}:{sub}" if sub is not None else idx.upper()
    if key in NOTE: return NOTE[key]
    if idx.upper() in NOTE and sub is None: return NOTE[idx.upper()]
    i = int(idx,16)
    if 0x1400 <= i <= 0x1403 or 0x1800 <= i <= 0x1803:
        return PDO_SUB_NOTE["comm"].get(str(sub),"")
    if 0x1600 <= i <= 0x1603 or 0x1A00 <= i <= 0x1A03:
        return PDO_SUB_NOTE["map"].get(str(sub),"" if sub == 0 else "index, sub-index, length in bits")
    return ""

out = []
out.append("(canopen_od)=")
out.append("# Object Dictionary")
out.append("")
out.append("Complete reference for object dictionary revision 1.2. The machine readable version is")
out.append("`md_1.2.eds`, available from [Downloads](device_firmware).")
out.append("")
out.append("The dictionary is split into three ranges:")
out.append("")
out.append("- **0x1000 to 0x1FFF, communication area.** CiA 301 objects: identification, heartbeat, SYNC and PDO configuration.")
out.append("- **0x2000 to 0x5FFF, manufacturer specific area.** MAB objects: motor parameters, encoders, controller gains, status and commands.")
out.append("- **0x6000 to 0x9FFF, profile specific area.** CiA 402 objects: state machine, modes, setpoints and limits.")
out.append("")
out.append("Access types are `ro` read only, `wo` write only, `rw` read and write over SDO, and `rww`")
out.append("read and write over SDO or through a receive PDO. The PDO column says whether the entry can")
out.append("be mapped into a PDO.")
out.append("")
out.append("```{note}")
out.append("Ranges in the notes column are the ones the **firmware** enforces. They are sometimes narrower")
out.append("than the data type allows and, in a few places, narrower than the EDS declares. A value outside")
out.append("the enforced range is rejected with SDO abort code 0x06090030.")
out.append("```")
out.append("")

AREAS = [("communication-area","Communication Area",0x1000,0x1FFF),
         ("manufacturer-specific-area","Manufacturer Specific Area",0x2000,0x5FFF),
         ("profile-specific-area","Profile Specific Area",0x6000,0x9FFF)]

idxs = sorted([s for s in cp.sections() if re.fullmatch(r"[0-9A-Fa-f]{4}", s)], key=lambda s:int(s,16))

for anchor, title, lo, hi in AREAS:
    out.append(f"({anchor})=")
    out.append(f"## {title}")
    out.append("")
    for idx in idxs:
        i = int(idx,16)
        if not (lo <= i <= hi): continue
        name = g(idx,"ParameterName")
        out.append(f"### 0x{idx.upper()} {name}")
        out.append("")
        d = DESC.get(idx.upper())
        if d:
            out.append(d)
            out.append("")
        out.append("| Sub | Name | Type | Access | Default | PDO | Notes |")
        out.append("| --- | ---- | ---- | ------ | ------- | --- | ----- |")
        for sub, sec in rows(idx):
            pname = g(sec,"ParameterName")
            dv = g(sec,"DefaultValue") or "-"
            acc = ACC.get(g(sec,"AccessType"), g(sec,"AccessType"))
            pdo = "yes" if g(sec,"PDOMapping") == "1" else "no"
            subtxt = "-" if sub is None else str(sub)
            out.append(f"| {subtxt} | {pname} | {dtype(sec)} | {acc} | {dv} | {pdo} | {note_for(idx, sub)} |")
        out.append("")

OUT.write_text("\n".join(out) + "\n")
print(f"wrote {OUT} from {eds}: {len(idxs)} objects")
