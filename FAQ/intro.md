<!--
FORMAT NOTE (humans + agents):
- One entry = one `###` heading with a stable `(faq-*)=` label.
- Troubleshooting entries use the fields **Symptom**, **Cause**, **Fix** where they apply.
- Commands assume candletool 1.5.1+. Older versions use slightly different syntax - check `candletool --help`.
- Placeholders: <id> = drive CAN ID, <file.cfg> = motor config path.
-->

(faq)=

# Common Issues and FAQ

## Quick triage

| Symptom | Go to |
|---|---|
| CANdle not detected by PC | [](faq-candle-not-detected) |
| MD not found by `discover` | [](faq-md-not-discovered) |
| "future version" / version mismatch error | [](faq-version-mismatch) |
| Firmware update hangs / bootloader not entered | [](faq-update-fails) |
| Drive has ID 100 after update/recovery | [](faq-id-100) |
| CAN ID / datarate not saved after power cycle | [](faq-can-not-persistent) |
| Calibration fails / pole pair detection failed | [](faq-calibration-failed) |
| `WARNING_LOW_ACCURACY` on main encoder | [](faq-low-accuracy) |
| Output (aux) encoder errors | [](faq-aux-encoder) |
| Motor does not move after enable | [](faq-enable-sequence) |
| Motor stops / disables during idle periods | [](faq-watchdog) |
| Motor temperature reads > 100 °C at room temp | [](faq-thermistor) |
| MOSFET / driver failure after hard braking | [](faq-regen) |
| CANopen: object missing, wrong mode, Set Zero no effect | [](faq-mdco-eds) |
| CANopen: new profile velocity applied one move late | [](faq-mdco-profile) |

---

## General

(faq-which-software)=
### Which software should I use?

| Stack | Status | Notes |
|---|---|---|
| **CANdle-SDK** (candletool, candlelib, Python module) | **Active** | Linux + Windows. Use for all new projects. [GitHub](https://github.com/mabrobotics/CANdle-SDK) |
| mdtool + legacy CANdle library / pyCandle | Legacy (EOL) | Linux only. Supported, not developed. |
| CANdleduino | Getting-started only | AVR, Renesas, Teensy. Not optimized for production. |
| candle_ros2 | Active | ROS2 wrapper over SDK. |

- No official MATLAB binding - customers have connected via Python module.
- No auto-tune tool.

(faq-fdcan-vs-canopen)=
### Should I use FDCAN (MD protocol) or CANopen?

FDCAN (MD protocol) is recommended unless your system already uses CANopen. CANopen is an
established industry standard, but it is more complex and has lower bandwidth (CAN 2.0, 8 bytes per
frame) and flexibility. See [Communication Overview](/MD/Communication/intro.md).

- Both protocols **cannot** share one bus - they interfere with each other.
- CANdle / CANdle HAT can talk CANopen through `candletool mdco` and the [MDCO module](mdco) of
  CANdle-SDK. Like the rest of the CANdle ecosystem it is meant for configuration, testing and
  development - see [CANdle purpose & limitations](candle_and_hat).

(faq-units)=
### What units are used?

SI units everywhere in MD protocol / CANdle-SDK: rad, rad/s, Nm, A. Example: 10.0 rad/s ≈ 95 RPM.
CANopen uses different units for some objects - see [System Units](canopen_units) and the EDS.

---

## CANdle and connection

(faq-candle-not-detected)=
### CANdle not detected by the PC

**Symptom:** candletool reports no CANdle; device missing in `lsusb`.

**Fix:**
1. Swap the USB cable - charge-only or poor cables are the most common cause. Try a different USB-A↔USB-C cable.
2. Check enumeration:
   ```bash
   lsusb | grep -i mab
   # expected: ID 0069:1000 MAB Robotics MD USB-TO-CAN
   ```
3. Linux permissions: install udev rules (see [SDK README](https://github.com/mabrobotics/CANdle-SDK)) or run once with `sudo` to confirm.
   Windows: run `candlesdk-win-driver.exe` once as administrator (see [SDK README](https://github.com/mabrobotics/CANdle-SDK)).
4. Update CANdle firmware:
   ```bash
   candletool candle update latest
   ```
5. Try another USB port / host. Avoid VMs and Docker ([CANdle-SDK](candle-sdk)). Intermittent drops
   on one specific host can be a kernel driver or USB hardware issue on the host side.

**Note:** CANdle is powered from USB. It does not need power from the PDS/PSU - the 6-pin Molex cable carries both power and CAN, only passed through.

(faq-md-not-discovered)=
### MD not detected by `candletool md discover`

1. **Power** - MD LEDs (under connectors, near PCB edge) must blink.
2. **LED pattern:**

   | LED | Meaning | Action |
   |---|---|---|
   | Red + green blinking fast (longer than the first few seconds) | Firmware corrupted / stuck in bootloader | Recovery update ([](faq-update-fails)) |
   | Red solid, green 1 s blink | Error present | `candletool md info -i <id>` |
   | Green 1 s blink only | OK | Check cabling, termination, datarate |

3. **Termination** - [](faq-termination).
4. **Datarate** - all drives on bus must use the same datarate ([](faq-datarate)). Run `discover`
   with the drive's datarate, e.g. `candletool md discover -d 8M`. Drives may ship configured at
   8 Mbps for long chains.
5. **Protocol** - a CANopen (MDCO) drive is not found by `md discover`. Use `candletool mdco discover`.
6. **Old CANdle firmware** - update CANdle ([](faq-candle-not-detected), step 4).

(faq-termination)=
### FDCAN termination

**Symptom:** communication errors, missing drives, random frame loss (especially on long chains / high datarate).

**Fix:**
- 120 Ω at **both physical ends** of the bus → 60 Ω measured between CANH and CANL (power off).
- CANdle has a built-in 120 Ω terminator switched on/off with a physical switch.
- Other end: MAB terminator plug, or a PDS control board CAN input (termination built in).
- Topology example: `CANdle (term ON) — MD — MD — … — MD — terminator`.
- Missing termination causes ringing - errors may appear only at higher datarates.

(faq-datarate)=
### Different datarates between actuators

All drives on one bus must use the same datarate. Mixed datarates cause communication to fail or not start.

- CAN-FD arbitration phase is always 1 Mbps. Data phase is 1, 2, 5 or 8 Mbps (configured).
- Fix per drive (connect one at a time if needed). `-d` = datarate the drive uses **now**:
  ```bash
  candletool md can -d <current> --id <id> --new_datarate 1M --save
  ```

(faq-can-id)=
### How do I change the CAN ID?

```bash
# MD (FDCAN), valid IDs 10-2000
candletool md can --id <old_id> --new_id <new_id> --save
# MD CANopen, valid node IDs 10-127
candletool mdco can -i <old_id> --new_id <new_id> --save
```
Connect **only one** drive with a given ID at a time. Factory default IDs are often identical.

(faq-can-not-persistent)=
### CAN ID / datarate / watchdog not saved after power cycle

**Cause:** CAN-related registers live in a separate working memory region. Writing the register alone does not apply it - `save` stores a snapshot of the old values.

**Fix (raw register writes):** write `runCanReinit` (0x08D) after changing CAN ID, datarate or watchdog, then save **using the new ID**:
```bash
candletool md -i 100 -d 1M register write 0x001 101   # canId
candletool md -i 100 -d 1M register write 0x08D 1     # runCanReinit
candletool md -i 101 -d 1M save
```
Prefer `candletool md can ... --save` which does this for you.

(faq-third-party-host)=
### Can I control MD without CANdle (own MCU, PLC, Arduino)?

Yes. MD protocol is documented ([MD Protocol](md_protocol)). Requirements:
1. CAN-FD transceiver (not classic CAN only) + correct termination.
2. Update MD firmware to latest first (legacy firmware < 2.5 uses a different frame format).
3. Configure drive with candletool/CANdle beforehand (config, calibration, CAN ID).
4. Follow [](faq-enable-sequence) and keep frames flowing faster than the watchdog ([](faq-watchdog)).

Firmware updates still require CANdle or CANdle HAT.

---

## Firmware and updates

(faq-version-mismatch)=
### "Firmware is a future version" / version mismatch

**Cause:** mdtool < 1.5.4 requires strict mdtool ↔ firmware version match.

**Fix:** update to mdtool 1.5.4 (relaxed check) or - recommended - switch to candletool (CANdle-SDK).

(faq-update-md)=
### How do I update MD firmware?

```bash
candletool md update latest --id <id>
candletool mdco update latest --id <id>    # CANopen drive
candletool candle update latest            # CANdle itself
```
- Requires CANdle or CANdle HAT. Not possible via third-party CAN adapters.
- Files, offline update (`-p <file.mab>`) and legacy flashers: [Downloads](downloads).
- Firmware v3.x requires a board with the new bootloader, introduced around March-April 2026.
  Older boards can only run v2.5.x - contact support for a factory update.

(faq-update-fails)=
### Update fails / "Failed to initialize bootloader" / hangs at "power-cycle the driver"

**Fix - recovery mode:**
1. Connect **only one** drive.
2. Remove power from the drive (wait ≥ 3 s, all LEDs off).
3. Run:
   ```bash
   candletool md update latest -r --id 9      # MD (FDCAN) target
   candletool mdco update latest -r --id 9    # CANopen target
   ```
4. Power the drive. Flashing starts when the bootloader appears. May need 2-3 attempts.
5. Check the drive's ID and config afterwards ([](faq-id-100)).

ID 9 is the bootloader ID - this is not the drive ID.

(faq-id-100)=
### Drive appears with ID 100 / lost its configuration

**Cause:** factory reset (`candletool md config factory-reset`), `update --force-erase` or a recovery
update restores defaults (ID 100, default config).

**Fix:**
```bash
candletool md info -i 100
candletool md config upload -i 100 <file.cfg>    # also saves
candletool md reset -i 100
candletool md calibration -i 100
candletool md can --id 100 --new_id <new_id> --save
```
Configs: [motor_configs](https://github.com/mabrobotics/motor_configs). For MAB actuators ask support for the exact config - CubeMars motor parameters change between batches.

(faq-switch-protocol)=
### Switching FDCAN ↔ CANopen

Requires firmware v3.0.0+ and candletool v1.5.1+. Full procedure: [Communication Overview](/MD/Communication/intro.md).

| Direction | Command |
|---|---|
| MD → CANopen (MDCO) | Set ID to 10-127 first ([](faq-can-id)), then `candletool md update --mdco latest --id <id>` |
| CANopen → MD | `candletool mdco update --md latest --id <id>` - drive must be the **only device on the bus** |
| Legacy MDCO 2.5.x → MDCO 3.x | `candletool mdco update latest -i <id> --legacy-migration` |
| Fallback (drive does not respond) | Recovery ([](faq-update-fails)) |

Validate with `candletool mdco info -i <id>` / `candletool md info -i <id>`. After
`--legacy-migration` the configuration is mostly dropped: upload config and recalibrate. CANopen
parameters use different units - convert config values ([System Units](canopen_units)).

---

## Calibration and encoders

(faq-calibration-failed)=
### Calibration failed

| Error | Likely cause | Fix |
|---|---|---|
| `ERROR_CALIBRATION` + `ERROR_PARAM_IDENT` | Phase wires not soldered correctly / identification glitch | Check soldering ([](faq-soldering)), rerun calibration |
| `ERROR_POLE_PAIR_DET` | Wrong `pole pairs` in .cfg, shaft loaded/blocked, very low KV motor | Set correct pole pairs (or `0` to autodetect), unload shaft. Optionally skip check: `[motor] calibration mode = NOPPDET` |
| `ERROR_POLE_PAIR_DET` on a previously working actuator | **Power stage fault** (MOSFET or current sensing) | Contact support - do not force with NOPPDET |
| `ERROR_CALIBRATION` (eccentricity step) | Load on shaft, encoder not axial to magnet | Unload shaft, fix encoder/magnet alignment |
| R/L readings erratic between runs | Pole pair mismatch | Fix pole pairs first |

See [Configuration & Calibration](config).

```{warning}
`NOPPDET` skips validation only - a wrong `pole pairs` value gives wrong commutation: stalls, current spikes (> 10 A), noise.
```

(faq-soldering)=
### Motor terminals not soldered properly

Hobby motors often have several parallel strands per phase. Solder **all** strands. One loose strand causes phase imbalance → failed calibration, cogging, motor stuck in one position.

```{warning}
Operating an improperly connected motor can damage the driver and is hazardous.
```

(faq-low-accuracy)=
### `WARNING_LOW_ACCURACY` on main encoder

**Cause:** magnet too far / off-axis from the encoder IC.

- Present on all MA-p-100-30 units by design - compensated in calibration, safe to operate.
- Custom builds - magnet spec:
  - 6 mm Ø × 2.5 mm, diametrically magnetized
  - air gap **1 mm ± 0.25 mm** (1 mm optimal), magnet on the same axis as the encoder IC
  - loose fit + glue (magnet tolerance up to ±0.1 mm)
  - calibration compensates off-axis error up to ~1 mm
- Check with `candletool md test encoder main --id <id>`.

(faq-aux-encoder)=
### Output (aux) encoder issues

- Max **2 encoders active**: main (commutation) + output/aux (post-gearbox position or monitoring).
- After config change run aux calibration:
  ```bash
  candletool md calibration -e aux --id <id>
  ```
  Fixes `ERROR_WRONG_DIRECTION`. Check accuracy with `candletool md test encoder aux --id <id>`.
- RLS AksIM-2 / high-quality encoders: set `[output encoder] output encoder calibration mode = DIRONLY`
  (skips eccentricity compensation meant for cheaper encoders). Not possible with off-axis encoders.
- RLS mounting is strict - 3D-printed brackets often not precise enough. RLS LED must stay **solid green** while slowly rotating. Any red/yellow flash = mounting problem or damaged disc (avoid magnetized tools near the disc).
- Config shows `ONBOARD` despite setting output encoder → check the `[output encoder]` section was not overwritten with `0`.
- Example configs: MA-D-HS-GL60 (RLS as main), MA-H (RLS as output) in [motor_configs](https://github.com/mabrobotics/motor_configs).
- Set Zero affects all position readings, including output encoder.
- Motor direction cannot be reversed in firmware - MAB follows the right-hand rule.

See [Encoders](aux_encoders).

(faq-rl-values)=
### Motor R/L differ from the .cfg file

R and L are measured by the drive during factory assembly and stored in non-volatile memory. Keep
factory values. Firmware 2.5.x does not load R/L from .cfg (v3.x does - 0 means auto-detect during
calibration). Re-measurement via `candletool md calibration --autodetect` is possible but not
recommended.

(faq-motor-check)=
### How do I check if my motor works properly?

1. `candletool md info -i <id>` - error fields empty / `ALL OK`.
2. `candletool md test relative ...` - hold position 0, rotate rotor by hand: no excessive cogging.
3. Run Python/C++ example, compare position, velocity, torque against expectation.
4. Still suspicious → [](faq-support).

---

## Control and motion

(faq-enable-sequence)=
### Motor does not move after sending commands

**Cause:** drive not enabled, or disabled again by watchdog/fault.

**Enable sequence (MD protocol):**
1. Set mode: `motionModeCommand` (0x140), e.g. `0x02` = velocity PID.
2. Enable: write `0x27` to `state` (0x142).
3. Loop: write target, read `quickStatus` (0x805, errors) + feedback - faster than watchdog period.

| `state` value | Meaning |
|---|---|
| 0x27 (39) | Operation enabled |
| 0x40 (64) | Disabled |

- Mode returns to idle every time the drive disables → re-send mode before enable.
- Enable is refused if a fault is active - read `quickStatus` first.
- "Choppy" motion = drive toggling enabled/disabled due to watchdog.

See [State Machine](md_state_machine) and [MD Protocol](md_protocol).

(faq-watchdog)=
### Motor stops or disables during idle periods (watchdog)

**Cause:** no valid frame within `canWatchdog` period (default 200 ms) → drive decelerates
(`quickStopDeceleration`, 0x123) and disables. See [Communication Watchdog](watchdog).

**Options:**
1. **Recommended:** keep sending frames (any valid frame) faster than the watchdog.
2. Host-side timer per drive: if idle > watchdog, re-run enable sequence before next move.
3. `disable()` after a move, enable sequence before the next one.
4. Change the timeout: `candletool md can --id <id> --new_timeout <ms> --save`. `0` disables the
   watchdog - **not recommended**, drive keeps executing last command if host fails.

Explicit disable and watchdog disable are the same internal procedure.

(faq-zero-mode-change)=
### Must I disable the drive before set zero / mode change?

Not strictly required, but recommended - both cause a torque discontinuity.

(faq-tuning)=
### Tuning: slow response, overshoot, knocking in position mode

- Position PID is cascaded on velocity PID - tune velocity PID first for acceleration/response.
- Factory gains are for unloaded demo movement only - tune for your load.
- Profile Position: tune profile velocity/acceleration/deceleration for smooth moves.
- No auto-tune available. See [Motion Control](motion_modes).

(faq-torque-bandwidth)=
### Too-low torque bandwidth

Low torque bandwidth → slow current loop → poor behavior in dynamic scenarios (impacts). Increase bandwidth in .cfg or register, then recalibrate. Trade-off: higher bandwidth = more audible hiss.

(faq-update-rate)=
### What update rate can I achieve?

Limited by CAN throughput (datarate × frame length × number of drives) and the host. Single drive,
simple read/write on x86 Linux: ~2 kHz, dropping with every drive added; Windows is noticeably
slower. Measured values: [Response Time](/CANdle-SDK/candlelib/ResponseTimes.md). Raspberry Pi:
SDK build takes long (heavy templates) - expected.

(faq-torque-reading)=
### Reading torque

Register `torque` (0x064, float32, Nm) = estimated output torque. Torque constant `Kt` is a physical motor parameter - do not change it to limit power, use current/torque limits instead.

---

## Power and hardware protection

(faq-regen)=
### MOSFET / driver failure during hard braking

**Cause:** regenerative energy pumps bus voltage above rating. Most MOSFET failures seen in tests happened during regenerative braking.

**Fix:**
- Use a supply that can absorb regen (two-quadrant), or a brake resistor ([PDS Brake Resistor](pds_br)).
- Limit deceleration and max velocity.
- Unidirectional bench PSUs cannot sink current.

See [Recuperation](md_safety).

(faq-thermistor)=
### Motor temperature reads > 100 °C at room temperature

**Cause:** damaged/disconnected motor thermistor. Thermal shutdown triggers falsely.

- Thermal shutdown works only with a thermistor connected (`[motor] shutdown temp`, 25-127 °C, default 80 °C).
- Contact support for repair. Temporary workaround (at own risk, removes protection; helps only if
  the false reading stays below the new limit):
  ```bash
  candletool md register write motorShutdownTemp 127 -i <id>
  candletool md save -i <id>
  ```

(faq-current-rating)=
### Cable and connector current ratings

| Item | Rating |
|---|---|
| MD80 / MD80 60V Micro-Fit connector | 10 A RMS max input current. 6-pin connector: 2× VCC, 2× GND |
| MD20 connector | 3.1 A max input current |
| MAB daisy-chain cables | 10 A RMS continuous, 15 A bursts < 100 ms |

DC bus current is usually much lower than motor phase current - size wiring for bus current. For long chains feed power at several points.

(faq-power-supply)=
### Erratic behavior, resets during motion

Check power supply capacity first - insufficient current or voltage sag resets the drive mid-motion (looks like calibration or communication failure).

---

## CANdle-SDK / candletool / Python

(faq-sdk-windows)=
### Building CANdle-SDK on Windows

MSVC is not supported. Use `launch/buildForWindows.bat` (w64devkit, MinGW-w64 GCC) or the pre-built
Windows installers from [Releases](https://github.com/mabrobotics/CANdle-SDK/releases). Windows +
`mdco`: use latest release.

(faq-cli-syntax)=
### candletool command not found / wrong syntax

CLI changed between versions. `-i/--id` and `-d` may be placed before or after the subcommand
(`candletool md --id 100 calibration` = `candletool md calibration -i 100`). Run `candletool --help`
/ `candletool md <cmd> --help`. Typical typo: missing `md` → `candletool md register write ...`.
See [Commands](candletool_commands).

---

## MD CANopen (MDCO)

(faq-mdco-eds)=
### Which EDS? Object missing / documentation does not match

| Firmware | EDS | Documentation |
|---|---|---|
| MDCO 2.5.x (legacy) | `md_1.1.eds` | [CANopen \[LEGACY\]](md_canopen_co25) |
| MDCO 3.0.1 | `md_1.2.eds` | [CANopen](md_canopen) |
| MDCO 3.0.2+ | `md_1.3.eds` | [CANopen](md_canopen). Recommended. |

- The two generations are **not compatible** - same indices, different meaning (e.g. 0x2003 is
  System Command on 2.5.x, Torque Sensor on 3.x). Use the EDS as source of truth.
- candletool auto-switches EDS based on reported firmware version (`candletool mdco eds` to select manually).
- Check version: `candletool mdco info -i <id>`, or SDO read 0x2021:2 (2.5.x aborts with 0x06020000).
  Update: [](faq-switch-protocol).

**Legacy 2.5.x gotchas:**
- `0x2007`, `0x2008`, `0x2009` are MD-protocol objects - present in OD but **inert** in CANopen builds.
- `0x2003` = system commands (LED blink, reset, set zero…), `0x2004` = system status (encoders, calibration, …).
- System commands (incl. Set Zero `0x2003:05`) require Switch On Disabled + Service mode (write `-2` to `0x6060`).
  `0x6061` displays `-1` - drive is still in service mode.
- `0x2005:03 Mode = 4` = aux encoder used as main (default on MA-D-HS series).
- `0x6071` in 2.5.4 ignores value/sign (applies max torque) - fixed in hotfix 2.5.5.x / 3.0.x. Contact support.
- Velocity `0x606C` resolution = 1 RPM (3.x: µrev/s).
- "Internal limit" bit in statusword = position/velocity/torque/acceleration clipped by config limits - not an error.

**MDCO 3.x:** system commands are in `0x2023`, status in `0x2022`, aux encoder in `0x2002` - see
[Object Dictionary](canopen_od). Calibration does not require Service mode.

(faq-mdco-profile)=
### Profile Position: new velocity applied one move late / start timing jitter

**Cause (legacy 2.5.x firmware):**
- `0x6081`, `0x6083`, `0x6084` are copied to the motion controller only in **Switch On Disabled**.
- Profile velocity is read only when a new target `0x607A` arrives - changing velocity mid-move is not supported.
- Mode 1 starts motion as soon as `0x607A` arrives - controlword bit 4 handshake not used, statusword bit 12 not set.

**Fix:** update to MDCO 3.x ([](faq-switch-protocol)) - see [Modes of Operation](canopen_modes).

**Workaround on 2.5.x - new velocity:**
1. Controlword `0x0000` (Switch On Disabled).
2. Write `0x6081` (+ `0x6083`/`0x6084`).
3. Enable: `0x0006` → `0x000F`.
4. Send target + SYNC.

```{warning}
Torque is removed between moves - make sure the axis can be safely unpowered.
```

**Synchronized multi-axis start:**
1. Map `0x607A` to an RPDO, transmission type = 1 (`0x140x:02`).
2. Send targets to all drives, then one SYNC (COB-ID 0x80, **DLC = 0**, `0x1019 = 0`).
3. Residual skew ≤ ~1.5 ms. Tighter: use CSP (`0x6060 = 8`) with host-side trajectory.

- Drive must be NMT Operational.
- 2.5.x: PDO mapping is **not** stored by `0x1010` - rewrite after every power-up / comm reset.
  3.x: save it with Save Config `0x2023:1` ([PDO](canopen_pdo)).

(faq-mdco-node-id)=
### CANopen: all drives have the same node ID

Factory default node ID is identical on all drives. Set IDs (10-127) one drive at a time:
```bash
candletool mdco can -i 100 --new_id 11 --save
```

(faq-mdco-update-legacy)=
### `SDO abort 0x06020000 on 0x2021:02` during mdco update

The drive runs legacy 2.5.x CANopen firmware, which has no 0x2021 firmware-version object. Use the
legacy migration:
```bash
candletool mdco update latest -i <id> --legacy-migration
```
Then upload config, calibrate, set node ID. If that fails, use recovery ([](faq-update-fails)). If
the bootloader never answers, the board has the old bootloader → v3.x not possible in field, contact
support.

---

(faq-support)=
## Contacting support

Send to [support@mabrobotics.pl](mailto:support@mabrobotics.pl):
1. Output of `candletool md info -i <id>` (or `candletool mdco info -i <id>`).
2. Versions: candletool, CANdle firmware, MD firmware, OS.
3. Your .cfg file.
4. Log with `--verbosity=3` for failing command.
5. Photo/video of setup and LED state if hardware-related.
