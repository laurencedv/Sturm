# REEPER

## General usage
REEPER is a Provisioning & Emergency Recovery system developped by [RealEE](http:// www.realee.tech). It includes computers software, embedded software and some hardware recovery mechanism.  
To use it you must first have a compatible hardware which is defined [here](WRITEME) then using the computer tools you would communicate with the target via one of the supported streaming interface (ie: Serial, USB, etc.)  
If all fails, you could use the hardware log retreiver to at least extract the log of the target with a [Scythe]  

### Naming explanation
The name comes from the proximity between REEPER and Reaper(as in [The Grim Reaper](https://en.wikipedia.org/wiki/Death_(personification))). Who is a spiritual being helping lifeform to transition between life and death (and sometimes the other way around n_n). Its tool of choice is a famous large scythe. As such, it is while using REEPER with a Scythe that you will be able transition your target from death to life.


## REEPER Protocol

### Communication structure
Communication is structured in transaction consisting a initial request and its response (if requested)
1. SEND a RESQUEST
2. RECV the RESPONSE (if asked)

### 1. PHY layer
* LVCMOS3.3 NRZ 8N1 115200 Serial full-duplex stream
* LVCMOS3.3 SPI 1-20MHz full-duplex stream
* USB 2.0 CDC full-duplex stream

### 2-7. ALLTHETHINGZ (ATZ) layer
| sync		| dest. address | src address	| resp	| cmd	  	 | datalen	 | data0, data1, data2	... data1023	|	validation	|
| ------- | ------------- | ----------- | ----- | -------- | --------- | ---------------------------------- | ----------- |
| 0x55		| 8bit          | 8bit        | 1bit	| 5bit		 | 10bit     | min: 0bit, max: 1024 * 8bit			  | CRC-16	  	|
| 1B		  | 1B            | 1B          | \\____|	__ 2B __ | ________/ | 0-1024B								            | 2B	      	|

#### Addresses
* 0x00: Reserved for broadcast, every device receiving this should feel concerned by the transaction
* 0x01-0xFE: Normal address range
* 0xFF: Reserved for the Host

#### Commands
The usage of REEPER is mainly for initial provisioning and operational control of an embedded system, thus the commands are divided into both those use-case.  

#### Operational
Supported commands:
* Response: Response packet
  * OpCode: 0b00000, 0x00, 0
  * Data0:
    * desc: command being responded to
    * type: uint8
  * Data1:
    * desc: CRC-16 of the packet being responded to
    * type: uint16
  * Data2:
    * desc: Status of the completed transaction (values TBD)
    * type: uint8
  * Data3+:
    * desc: Specific response content
    * type: uint8 * (datalen-4)
* Get Map: Request the Operational Register Bank Map (OpRegBank_map)
  * OpCode: 0b00001, 0x01, 1
  * Response content: transaction status, JSON of the register map (will be bigger than a packet, require sub-packaging mechanism)
* Set Reg: Write a new value to an Operational Register (OpReg_t)
  * OpCode: 0b00010, 0x02, 2
  * Data0:
    * desc: Register address to set
    * type: uint32
  * Response content:  transaction status
* Get Reg: Read from an Operational Register (OpReg_t)
  * OpCode: 0b00011, 0x03, 3
  * Data0:
    * desc: Register address to get
    * type: uint32
  * Response content:  transaction status, actual register content
* **Reboot**: Request a target reboot, mode can be bootloader or normal, needs **privilege**
  * OpCode: 0b01000, 0x08, 8
  * Data0:
    * desc: mode to reboot into (0: normal | 1: bootloader | other: reserved)
    * type: uint8
  * Data1:
    * desc: delay (in ms) to wait before rebooting
    * type: uint32
  * Response content: transaction status, mode being rebooted in
* **Set Time**: Set current time/data, used to synchronise target to real time, will reset to 0 RTOS usecTimestamper, needs **privilege**
  * OpCode: 0b01001, 0x09, 9
  * Data0:
    * desc: new current time in unix epoch (applied immediately)
    * type: uint32
  * Response content: transaction status, new current time (if for some reason, the response is sent more than a sec after the request, it will be the actual transmission time )
* **Factory Reset**: Reset to safe factory configuration, needs **privilege**
  * OpCode: 0b01010, 0x0A, 10
  * Response content: transaction status
* Help: Request the [help string](#help-string) (protocol info and supported commands)
  * OpCode: 0b01111, 0x0F, 15
  * Response content: transaction status, [help string](#help-string)

#### Provisionning
Those commands will only be accepted at initial provisioning (aka before you send a lock command)

Supported commands:
* Wipe: Remove any fw and configuration (except bootloader)
  * OpCode: 0b10000 , 0x10, 16
  * Response content: transaction status
* Password: Configure a secret password used for **privilege**ed commands, set to NULL for no password.
  * OpCode: 0b10001, 0x11, 17
  * Data0:
    * desc: new password to record
    * type: uint8 * datalen (password in ASCII char)
  * Response content: transaction status, password setted
* Config: Send a configuration file, setting OpRegs and others setup stuff (Content not defined, but abstract definition is fixed)
  * OpCode: 0b10010, 0x12, 18
  * Data0:
    * desc: configuration specific stuff
    * type: uint8 * datalen
  * Response content: transaction status
* Lock: Lock all configuration, once this is sent, you exit provisioning stage for the life of this fw. (can still be overwrote completly with a chip erase)
  * OpCode: 0b11111, 0x1F, 31
  * Response content: transaction status

#### Validation
Validation is done by a CRC-16 with polynom: , over the entire packet except the sync byte

**MAX Transmission time: 100ms**, worst case is 1024B data at 115200bps which is 89.4ms. This is kinda thigh, but this is also the retry rate, which boost the response time of the network.  
More relaxed timing may be implemented in the future.

### 7. APP layer
**Note:any protocol can be packaged in the *data* field of *ATZ* layer**

### Help String
COMING SOON

## Scythe
The Scythe is a dedicated hardware tool that connects to a target to provision or recover it.  
It is able to talk to an EFM32 MCU through multiple streaming interface, notably: 
  * Serial REEPER protocol (NOT IMPLEMENTED)
  * Serial EFM32 bootloader (NOT IMPLEMENTED)
  * SWD for programming and verifying (NOT IMPLEMENTED)
  * SPI-Master for black-box style log recovery (NOT IMPLEMENTED)


### Scythe connector pinout

| Desc            | pin | pin | Desc              |
|-----------------|-----|-----|-------------------|
| *VMCU*          | 1   | 2   | *SWDIO*           |
| *GND*           | 3   | 4   | *SWCLK*           |
| -               | 5   | 6   | *SWO*_WU          |
| **VMEM**        | 7   | 8   | **MCU_CS**/*TDI*  |
| **GNDMEM**      | 9   | 10  | *MCU_RESET*       |
| **MEM_CS**      | 11  | 12  | *ETMCLK*          |
| **MISO**        | 13  | 14  | *ETMD0*           |
| **MOSI**        | 15  | 16  | *ETMD1*           |
| **SCK**         | 17  | 18  | *ETMD2*           |
| *GND*           | 19  | 20  | *ETMD3*           |


*ARM SWD standard pinout*  
**REEPER specific pinout**  


