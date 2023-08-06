.PHONY: all
all: check test lint


# if set to --rebuild will recompile all python files.
MIBFLAGS = --rebuild
MIBFLAGS =

# A default list of "good to have" mibs.
MIBS += SNMPv2-MIB
MIBS += RMON-MIB
MIBS += IP-MIB
MIBS += UDP-MIB
MIBS += TCP-MIB
MIBS += IF-MIB
MIBS += IANAifType-MIB
MIBS += HOST-RESOURCES-MIB
MIBS += UCD-SNMP-MIB
MIBS += UPS-MIB
MIBS += SNMP-VIEW-BASED-ACM-MIB

# Synology
MIBS += SYNOLOGY-SMART-MIB
MIBS += SYNOLOGY-STORAGEIO-MIB
MIBS += SYNOLOGY-RAID-MIB
MIBS += SYNOLOGY-SYSTEM-MIB
# Used by unifi
MIBS += FROGFOOT-RESOURCES-MIB
MIBS += FASTPATH-SWITCHING-MIB
MIBS += UBNT-UniFi-MIB
# Printers
MIBS += Printer-MIB
# LiuIT
MIBS += ENOC-MIB
MIBS += SOCOMECUPS-MIB
MIBS += BACS2-MIB

# Append all mibs mentioned in our data
# MIBS += $(shell snmp_lookup_maintain mibs)
#

.PHONY: mibs
mibs: data/mibs/.marker src/snmp_lookup/mibs/index.py

# use `mibcopy` to copy all CUSTOM_MIBS to ./data/mibs.
# This ensures that the names are canonical, and that any dependencies listed
# in a MIB file are present.
data/mibs/.marker: ./STANDARD_MIBS ./CUSTOM_MIBS
	$(Q)mkdir -p data/mibs
	$(Q)mibcopy.py \
		--mib-source=file:///usr/share/snmp \
		--mib-source=http://mibs.snmplabs.com/asn1/@mib@ \
		./STANDARD_MIBS/ ./CUSTOM_MIBS/ data/mibs
	touch $@


src/snmp_lookup/mibs/index.py:  data/mibs/.marker Makefile
	# Dump the named mibs (hardcoded for now) into python format in
	# src/snmp_lookup/mibs
	$(Q)mibdump.py $(MIBFLAGS) \
		--build-index \
		--no-python-compile \
		--generate-mib-texts \
		--destination-format=pysnmp  \
		--cache-directory=/tmp/pysnmp_cache \
		--destination-directory=src/snmp_lookup/mibs \
		--mib-source=./data/mibs/ \
		--mib-borrower=data/mibs $(MIBS)

.PHONY: test
test: selftest
	$(Q)pytest tests/

.PHONY: selftest
selftest:
	$(Q)snmp_lookup_maintain check
	$(Q)snmp_lookup_selftest

.PHONY: black
black:
	$(Q)black --check src/ scripts/


.PHONY: check
check: black
	$(Q)flake8 src/


.PHONY: mypy
mypy:
	$(Q)mypy --disallow-untyped-defs --disallow-incomplete-defs src/

.PHONY: lint
lint: mypy
	$(Q)pylint src/snmp_lookup/
#	$(Q)pylint scripts/


.PHONY: blacken
blacken:
	$(Q)black src/ scripts/ tests/

.PHONY: clean
clean:
	rm -rf data/mibs
	rm -f src/snmp_lookup/mibs/.marker

