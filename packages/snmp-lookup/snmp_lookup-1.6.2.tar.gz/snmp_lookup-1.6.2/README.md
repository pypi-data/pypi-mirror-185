# snmp_lookup

Modio SNMP metadata system


# Directory layout

`CUSTOM_MIBS/` should contain all our mib files, downloaded and checked in
without much extra data in it.

`data/mibs` is automatically generated with `make mibs` it uses `mibcopy.py`
from [PySMI](https://github.com/etingof/pysmi) to place the mibs in proper
search paths and so on.

`src/snmp_lookup/data`  contains a list of `.csv` files for our snmp
monitoring. These are parsed, and combined with the files in `data/mibs` to
generate the files in `src/snmp_lookup/mibs`

`src/snmp_lookup/mibs/` contains all our mib files, generated with `make mibs`
but in pysnmp's `python` format.  These files are generated and should be
checked in for differences when adding new mibs to places.

--- 

`data/mibs` is automatically generated with `make mibs`, it uses
`mibcocpier.py` to parse, and normalize names of the mibs we have.

Compiled mibs (into python format) are done with `mibcompiler.py` on the
normalized names. This compiles only the mibs we _need_ in our system to keep
the size of our codebase down.

---  

# config usage

>>> from snmp_lookup import KINDS
>>> assert "kind" in KINDS

KINDS is an sequence/set of strings, each one a supported device type

---

>>> from snmp_lookup import valid_name
>>> valid_name("Sven Björne") => False

Validates a name according to some internal rules ( submit/Zabbix/afase -aware)


# afase usage (not implemented)

>>> from snmp_lookup import kind_presentable
>>> kind_presentable(kind="UNIFI")  

Returns a text-string suitable for User interfaces of a more human readable
name for the kind, suitable for use in web-ui dropdowns etc.

---

See examples from "config" usage as well


# logger usage

>>> from snmp_lookup import get_points
>>> get_points(kind="KIND")

Returns a sequence of Pointss for the type `KIND`.

# Logger fix cache/singleton

Due to implementation details in pysnmp, it's important to use a singleton
`SnmpEngine()`  for the entire software, which in turn needs to have access to
MIB modules in order to load and set things up as needed.

Add the mibs _once_ to the engine's builder, doing it again won't harm more
than causing an increasingly slow runtime that uses more and more RAM.

>>> from snmp_lookup import get_points
>>> from snmp_lookup.point import add_mibs, resolve_with_mibs
>>> from pysnmp.hlapi import SnmpEngine
>>> KINDS = ["printer", "unifiSW"]
>>> cache = {}
>>> engine = SnmpEngine()
>>> add_mibs(engine)
>>> for kind in KINDS:
>>>     points = get_points(kind=kind)
>>>     resolve_with_mibs(points, cache, engine)
>>> del cache

The cache is just a dict and can be discarded once all kinds have been loaded.
It's important that the same engine is used to load as is used to parse
PDU's, to make sure that all the MIB's are loaded and resolved.

The `resolve_with_mibs` will modify all points in place and ensure that it has
a `point.oi`  attribute that is an fully resolved `ObjectIdentity` that is
hashable and can be used to resolve data in replies back to other data.

-- 

# NOT IMPLEMENTED

>>> from snmp_lookup import oid_to_key
>>> oid_to_key(kind="KIND", oid=XXXX, kind="KIND", name="NAME") => >>> "snmp.NAME.KIND.foo.bar.baz"

Takes an OID, Kind, Name  and returns a suitable key for storing data as.



# submit usage

>>> from snmp_lookup import valid_key
>>> valid_key(key="snmp.NAME.KIND.foo.bar.baz")   => True

Validates a key according to some internal rules

--  


>>> from snmp_lookup import get_validator
>>> validator = get_validator(key="snmp.NAME.KIND.foo.bar.baz")

get_validator returns a validator function that can be reused (cached) and
tests if a value is valid for the type that the key `snmp.foo.bar.baz` runs for


--  

>>> from snmp_lookup import get_snmp_type
>>> get_snmp_type(key="snmp.foo.bar.baz")  => "IPAddress"

Convenience wrapper that calls `get_type` and then `type2zabbix` and returns
the resulting data.
