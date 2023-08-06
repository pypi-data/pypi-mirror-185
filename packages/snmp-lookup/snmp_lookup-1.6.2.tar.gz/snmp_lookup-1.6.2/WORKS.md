# Raw mibs
# http://mibs.snmplabs.com/asn1/

mibdump:
    MIBS=....

    # Dump all data with json format
    mibdump.py --destination-format=json --rebuild \
        --generate-mib-texts \
        --cache-directory=/tmp/cache \
        --destination-directory=data/mibs/json $MIBS

    # Dump all data compiled to python classes
    mibdump.py --destination-format=pysnmp --rebuild \
        --cache-directory=/tmp/cache \
        --destination-directory=src/snmp_lookup/mibs/
         $MIBS


Dynamic resolving:

    https://www.zabbix.com/documentation/4.0/manual/config/items/itemtypes/snmp/dynamicindex

    

    HOST-RESOURCES-MIB::hrSWRunPerfMem["index","HOST-RESOURCES-MIB::hrSWRunPath", "/usr/sbin/apache2"]

     the index number will be looked up here:

    ...
    HOST-RESOURCES-MIB::hrSWRunPath.5376 = STRING: "/sbin/getty"
    HOST-RESOURCES-MIB::hrSWRunPath.5377 = STRING: "/sbin/getty"
    HOST-RESOURCES-MIB::hrSWRunPath.5388 = STRING: "/usr/sbin/apache2"
    HOST-RESOURCES-MIB::hrSWRunPath.5389 = STRING: "/sbin/sshd"
    ...

    Now we have the index, 5388. The index will be appended to the data OID in order to receive the value we are interested in:

    HOST-RESOURCES-MIB::hrSWRunPerfMem.5388 = INTEGER: 31468 KBytes


Basic data format is:

HEADER  |   snmp_mib    |   snmp_oid        |key_name           |   key_description | snmp_datatype | 
DATA    |   IF-MIB      |   ifSpeed         |interface_speed    |   "goes fast"     | INTEGER       |
DATA    |   IF-MIB      |   ifDescr         |description        |   human name      | STRING        |


            ifInErrors
            ifOutErrors
            ifInDiscards
            ifOutDiscards
            ifSpeed

key                                     |   NAME                | datatype   ==> val, timestamp     
snmp.Geeks.unifiAP.unifiVapChannel.1        "Modio NA Channel"    INTEGER          44 ,  
                                  .2        "Mdio IPV6 NA channel"  | INTEGER  =>     44

snmp_mib=FOO-MIB
snmp_table=fooTable
name_prefix={fooGuz} {fooGonk}: 
columns={
    "fooFoo": "Foo data",
    "fooBar": "Bar data",
    "fooBaz": "Human baz",
    "fooDaz": "Daz",
    "fooGuz": "Da Guzz",
}


"snmp.Device.foo.fooFoo.1", 0,  $DATE
"snmp.Device.foo.fooFoo.2", 2,  $DATE
"snmp.Device.foo.fooFoo.1", 0,  $DATE           => "Counter32", "Foo data"





FOO-MIB     | fooTable  | fooFoo | {fooGuz} {fooGonk}: "Foo data"       | Counter32     | 



snmp_mib          |  snmp_table      | snmp_column          |  key_template                               | name_template                                       | selector_
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapChannel      | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Channel              | 
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapExtChannel   | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Ext Channel
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapNumStations  | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Clients
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapTxDropped    | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Transmit Dropped
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapTxErrors     | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Transmit Errors
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapTxPackets    | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Transmit Packets

UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapRxDropped    | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Receive Dropped
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapRxErrors     | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Receive Errors
UBNT-UniFi-MIB    |  unifiVapTable   | unifiVapRxPackets    | snmp.{name}.{kind}.{snmp_column}.{index}    |{unifiVapEssId} {unifiVapRadio} Receive Packets



DISCOVERY       
    scan table

    MIB, TABLE, RULE,   
        

                => key, datatype, name, unit





snmp_mib          | snmp_table      | snmp_column           | key               |           name            | selector_column | selector_matches    | selector_column   | 
UBNT-UniFi-MIB    | unifiVapTable   | unifiVapChannel      | unifiVapChannel.modio5g    | Modio 5G Channel  | unifiVapEssId     |Modio              |   




Dynamic this means:
HEADER  | snmp_mib              |snmp_oid                       |key_name           |snmp_filter_mib        | snmp_filter_column |snmp_filter_matches   
DATA    | HOST-RESOURCES-MIB    |hrSWRunPerfMem                 |apache.mem_usage   |HOST-RESOURCES-MIB     | hrSWRunPath        |"/usr/bin/apache2     
DATA    | EtherLike-MIB         |dot3StatsDeferredTransmissions |deferred_xmit      |IF-MIB                 | ifDescr            |"CPU Interface for"   





