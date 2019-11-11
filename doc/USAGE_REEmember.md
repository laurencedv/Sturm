REEmember Usage Guide
====

General usage
---
REEmember is a framework to generate code, data types and all necessary definitions and functions for a Virtual Register Array (**VRA**).
* This array is accessible via direct functions call, but can also be chained to some REECLI commands and various other means
* It can address each register by it's key (name) or by it's absolute address (index in array)
* Each register can have an arbitrary type, with different optional parameters
* It is based on a modular system of JSON file and python utilities
* It will ignore any unknown keys found in the JSON input, but wathchout as they can increase significantly the size of the serialized object which is inserted into the *hex* file on the target memory

For a example of input/output file please check [inputJSON](doc/template_REEmember-map.json) and [outputHeader](doc/template_REEmember-map.h)


JSON syntax
---
**bold** register are absolute requirements  
*italic* register will be auto-created if not present at input  
normal register are completly optional  

### Top Level key
* **name** :	Globally unique register array name
* version :		Optional version numbering
* dict :		Optional key compression dictionnary
* **type** :	Complete list of type definitions present in this register array
* **reg** :		Actual register array, this **MUST** be an JSON array, as they are garanteed to keep their order (this key must also be present only once in a single input file, multiple input file can be used if needed)
* *time* :	    Automatically added buildtime (in unix epoch)

### Register's key
* **module** :  Special key, if present will be the only one considered, and it will be replaced entirely by the JSON content of the pointed file (path must be the value). This is mainly used to generate product-level complete register map assembled from many small register definitions (you can see it as an #include statement in C)
* **name** :    Register's locally unique name
* **type** :    Register's type, must be present in top-level type list
* **bit** :    bit size of one instance of this register's type
* *perm* :    Optional register's external access permission in 'RW' format (default: '  ')
* *number* :  Optional number of level in this register (think FIFO, shadow reg, etc) (default: 1)
* desc :    Optional human readable description for ui
* *static* :    Boolean meaning this register is non-volatile (default: false)
* struct :  Special key to enable hiearchy, contains another array of regs (for using this, you must set the type to 'struct' and it must be present in the global type list)
* *time* :    Optional boolean enabling timestamping on register write (with register number>1, each instance will have its associated timestamp)
* default : Optional default value of the register (default will depend on actual C implementation, assume garbage)
  * Static : This value will be set at provisioning
  * Non-Static : This value will be set at each reset
  * No Perm : This value will always be present (unlike dad)

### Supported types and standard dictionnary
#### Type
| key    | compressed key | name       | size       | extremum         |
| ------ | ---- | -------------------- | ---------- | ---------------- |
| bool   |  b   |   Boolean            | 1bit       | true | false
| uint   |  u   |   Unsigned integer   | 1-64bit    | 0 - UINT64_MAX
| int    |  i   |   Signed integer     | 1-64bit    | INT64_MIN - INT64_MAX
| float  |  f   |   floating point     | 32-128bit  | LDBL_MIN - LDBL_MAX
| struct |  s   |   Structure          | -          | - |

#### Standard compression dictionnary
| key       | compressed key |
| --------- | -------------- |
| reg       |	r            |
| default   |	a            |
| module    |   m            |
| name      |	n            | 
| number    |	e            |
| perm      |	p            | 
| type      |	t            | 
| desc      |	d            | 
| version   |	v            |
| key       |	k            |
| bit       |	b            |
| static    |	c            |
| time      |	t            |


Examples
---
### Generating a register array C definition

