
Dynamic discovery needs to happen in two ways:


1. Index matching
   this is where you have a `selector` of some kind:
        MIB, OID, "text-string" 
   that resolves to an table Index  (.65,  .3457, etc)

    This index is then used to extract data from this or OTHER tables, and is
    NOT used as part of the name or key.

    Data format suggestion:

    selector_mib="IF-MIB"   selector_oid="processPath"  selector_match="/usr/bin/apache2" mib="FOO-MIB" oid="procMemory"    key=".apache.mem"   name="apache memory"


2. Table Matching
    This is where you scan a single table, and wish to build "stable" names for
    things, but without having to express a LONG LONG list of keys to have
    
    A suggested data-model is this:

    @dataclass
    class Discovery:
        mib: str
        table: str
        key_columns: List[str]
        columns: Dict[str, str]

    this would in practice look like below:

    Discovery(
        mib="UBNT-UniFi-MIB",
        table="unifiVapTable",
        key_columns = [
            "unifiVapEssId",
            "unifiVapRadio",
        ],

        columns = {
            "unifiVapChannel":      "{}: Channel",
            "unifiVapExtChannel":   "{}: ExtChannel",
            "unifiVapNumStations":  "{}: Clients",
            "unifiVapRxPackets":    "{}: RX Packets",
        }
    )

    What it does is maybe best exposed with a pseudocode example:
    

    for row in read_table(mib, table):
        prefix = " ".join(row[x] for x in key_columns)
        key_id = sha1sum(prefix)[:4]
        for col in columns:
           key = "snmp.AP4.unifiAP.{column}.{key_id}".format(col, key_id)
           val = row[col]
           name = columns[col].format(prefix)

    
    This could would then generate data like:

    key                                         name                    value
    snmp.AP4.unifiAP.unifiVapChannel.ABCD       Modio ng: Channel       44
    snmp.AP4.unifiAP.unifiVapNumStations.ABCD   Modio ng: Clients       4
    snmp.AP4.unifiAP.unifiVapNumStations.CDEF   De Klomp ac: Clients    4
    snmp.AP4.unifiAP.unifiVapNChannel.CDEF      De Klomp ac: Channel    12


    We probably want to specify the "key" part  as part of the column listing
    too


    


Go from OID => type
Go from OID => zabbix validator

Go from Kind/name => OID
Go from kind to list of OID
