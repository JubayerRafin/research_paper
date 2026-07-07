<!-- page: 1 -->
![image_p1_00](images/image_p1_00.png)

![image_p1_01](images/image_p1_01.png)

## Cisco MDS 9148S Multilayer Hardware
Installation Guide

**Cisco Systems, Inc.
www.cisco.com**

Cisco has more than 200 offices worldwide.
Addresses, phone numbers, and fax numbers
are listed on the Cisco website at
www.cisco.com/go/offices.

Text Part Number: OL-29583-01


<!-- page: 2 -->
THE SPECIFICATIONS AND INFORMATION REGARDING THE PRODUCTS IN THIS MANUAL ARE SUBJECT TO CHANGE WITHOUT NOTICE. ALL
STATEMENTS, INFORMATION, AND RECOMMENDATIONS IN THIS MANUAL ARE BELIEVED TO BE ACCURATE BUT ARE PRESENTED WITHOUT
WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. USERS MUST TAKE FULL RESPONSIBILITY FOR THEIR APPLICATION OF ANY PRODUCTS.

THE SOFTWARE LICENSE AND LIMITED WARRANTY FOR THE ACCOMPANYING PRODUCT ARE SET FORTH IN THE INFORMATION PACKET THAT
SHIPPED WITH THE PRODUCT AND ARE INCORPORATED HEREIN BY THIS REFERENCE. IF YOU ARE UNABLE TO LOCATE THE SOFTWARE LICENSE
OR LIMITED WARRANTY, CONTACT YOUR CISCO REPRESENTATIVE FOR A COPY.

The following information is for FCC compliance of Class A devices: This equipment has been tested and found to comply with the limits for a ClassA digital device, pursuant
to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference when the equipment is operated in a commercial
environment. This equipment generates, uses, and can radiate radio-frequency energy and, if not installed and used in accordance with the instruction manual, may cause
harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference, in which case users will be required
to correct the interference at their own expense.

The following information is for FCC compliance of Class B devices: This equipment has been tested and found to comply with the limits for a ClassB digital device, pursuant
to part 15 of the FCC rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation. This equipment generates,
uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications.
However, there is no guarantee that interference will not occur in a particular installation. If the equipment causes interference to radio or television reception, which can be
determined by turning the equipment off and on, users are encouraged to try to correct the interference by using one or more of the following measures:
• Reorient or relocate the receiving antenna.
(cid:129) Increase the separation between the equipment and receiver.
(cid:129) Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
(cid:129) Consult the dealer or an experienced radio/TV technician for help.
Modifications to this product not authorized by Cisco could void the FCC approval and negate your authority to operate the product.

The Cisco implementation of TCP header compression is an adaptation of a program developed by the University of California, Berkeley (UCB) as part of UCB’s public
domain version of the UNIX operating system. All rights reserved. Copyright © 1981, Regents of the University of California.

NOTWITHSTANDING ANY OTHER WARRANTY HEREIN, ALL DOCUMENT FILES AND SOFTWARE OF THESE SUPPLIERS ARE PROVIDED “AS IS” WITH
ALL FAULTS. CISCO AND THE ABOVE-NAMED SUPPLIERS DISCLAIM ALL WARRANTIES, EXPRESSED ORIMPLIED, INCLUDING, WITHOUT
LIMITATION, THOSE OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OR ARISING FROM A COURSE OF
DEALING, USAGE, OR TRADE PRACTICE.

IN NO EVENT SHALL CISCO OR ITS SUPPLIERS BE LIABLE FOR ANY INDIRECT, SPECIAL, CONSEQUENTIAL, OR INCIDENTAL DAMAGES, INCLUDING,
WITHOUT LIMITATION, LOST PROFITS OR LOSS OR DAMAGE TO DATA ARISING OUT OF THE USE OR INABILITY TO USE THIS MANUAL, EVEN IF CISCO
OR ITS SUPPLIERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Ciscoand the Ciscologo are trademarks or registered trademarks of Ciscoand/or its affiliates in the U.S. and other countries. To view a list of Ciscotrademarks, go to this
URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership
relationship between Ciscoand any other company. (1721R)

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display
output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in
illustrative content is unintentional and coincidental.

© 2014 Cisco Systems, Inc. All rights reserved.


<!-- page: 3 -->
![Cisco MDS 9148S Multilayer Hardware](images/image_p3_00.png)

**C O N T E N T S**

Preface
Audience ix
Organization ix
Document Conventions x
Related Documentation xii
Release Notes xii
Regulatory Compliance and Safety Information xii
Compatibility Information xii
Hardware Installation xii
Software Installation and Upgrade xiii
Cisco NX-OS xiii
Cisco Data Center Network Manager xiii
Command-Line Interface xiv
Intelligent Storage Networking Services Configuration Guides xiv
Troubleshooting and Reference xiv

**Product Overview 1
CHAPTER**

Power Supplies 1-3
Fan Modules 1-4
Cisco MDS 9148S Multilayer Switch Ports 1-4
Switch LEDs 1-4
Supported SFP Transceivers 1-6

**Installing the Cisco MDS 9148S Switch 2
CHAPTER**

Preinstallation 2-2
Installation Options 2-2
Installation Guidelines 2-3
Required Equipment 2-4
Unpacking and Inspecting the Switch 2-4
Front-Facing Installation 2-6
Installing the Switch in a Cabinet with Insufficient Front Clearance 2-9
Installing Front Rack-Mount Brackets for Cabinets with 26 Inches or Greater of Rail Spacings 2-11

**Cisco MDS 9148S Multilayer Switch Hardware Installation Guide
OL-20185-01**


<!-- page: 4 -->
Installing Front Rack-Mount Brackets for Cabinets with Less Than 26 Inches of Rail Spacings 2-12
Installing Cisco MDS 9148S Switch Rear-Facing into Cabinet 2-13
Grounding the Switch 2-17
Starting Up the Switch 2-18
Removing and Installing Components 2-20
Removing and Installing AC Power Supplies 2-21
Removing Power Supplies 2-21
Installing Power Supplies 2-22
Installing Power Supplies 2-23
Removing and Installing Fan Modules 2-23
Removing a Fan Module on the Cisco MDS9148S Switch 2-23
Installing a Fan Module 2-25
Verifying the Fan Module 2-26

**Connecting the Cisco MDS 9148S Switch 3
CHAPTER**

Preparing for Network Connections 3-1
Connecting the Console Port 3-1
Connecting the Console Port to a PC 3-2
Connecting a Modem to a Console Port 3-3
Connecting the 10/100 Ethernet Management Port 3-4
Connecting to a Fibre Channel Port 3-4
Removing and Installing SFP Transceivers 3-4
Installing an SFP Transceiver 3-5
Removing an SFP Transceiver 3-6
Removing and Installing Cables into SFP Transceivers 3-6
Installing a Cable into an SFP Transceiver 3-6
Removing a Cable from an SFP Transceiver 3-7
Maintaining SFP Transceivers and Fiber-Optic Cables 3-8

**Cabinet and Rack Installation A
APPENDIX**

Cabinet and Rack Requirements A-1
General Requirements for Cabinets and Racks A-1
Requirements Specific to Perforated Cabinets A-2
Reference Perforated Cabinet A-2
Requirements Specific to Solid-Walled Cabinets A-3
Requirements Specific to Standard Open Racks A-3
Requirements Specific to Telco Racks A-3
Cisco MDS 9000 Family Telco and EIA Shelf Bracket A-3


<!-- page: 5 -->
Rack-Mounting Guidelines A-4
Before Installing the Shelf Brackets A-5
Required Equipment A-5
Installing the Shelf Bracket Kit into a Two-Post Telco Rack A-5
Installing the Shelf Bracket Kit into a Four-Post EIA Rack A-7
Installing the Switch on the Shelf Brackets A-8
Removing the Shelf Bracket Kit (Optional) A-9

**Technical Specifications B
APPENDIX**

Switch Specifications B-1
Power Specifications B-2
General Power Supply Specifications B-2
Power Supply Requirements and Heat Dissipation Specifications B-3
Connection Guidelines for AC-Powered Systems B-3
SFP Transceiver Specifications B-3
Cisco Fibre Channel SFP Transceivers B-4
General Specifications for Cisco Fibre Channel SFP Transceivers B-4
Environmental and Electrical Specifications for Cisco Fibre Channel SFP Transceivers B-5
Optical Specifications for Cisco CWDM SFP Transceivers B-5

**Cable and Port Specifications C
APPENDIX**

Cables and Adapters C-1
Console Port C-2
Console Port Pinouts C-2
Connecting the Console Port to a Computer Using the DB-25 Adapter C-2
Connecting the Console Port to a Computer Using the DB-9 Adapter C-3
MGMT 10/100 Ethernet Port C-3
Supported Power Cords and Plugs C-4
Power Cords 4
Jumper Power Cord C-5

**Site Planning and Maintenance Records D
APPENDIX**

Site Preparation Checklist D-1
Contact and Site Information D-3
Chassis and Network Information D-4

**Cisco MDS 9148S Multilayer Switch Hardware Installation Guide**


<!-- page: 7 -->
![Cisco MDS 9148S Multilayer Switch Hardware Installation](images/image_p7_00.png)

# Preface

Cisco MDS 9148S Multilayer This preface describes the audience, organization, and conventions of the
Switch Hardware Installation Guide . It also provides information on how to obtain related
documentation.

# Audience

To use this installation guide, you need to be familiar with electronic circuitry and wiring practices and
preferably be an electronic or electromechanical technician.

```json
{
  "page": 7,
  "table_index": 0,
  "headers": [
    "Chapter",
    "Title",
    "Description"
  ],
  "rows": [
    {
      "Chapter": "Chapter 1",
      "Title": "Product Overview",
      "Description": "Provides an overview of the Cisco MDS 9148S Multilayer Fabric switch and its components."
    },
    {
      "Chapter": "Chapter 2",
      "Title": "Installing the Cisco MDS 9148S Switch",
      "Description": "Describes how to install the Cisco MDS 9148S Multilayer Fabric switch, and includes how to install power supplies and fan modules."
    },
    {
      "Chapter": "Chapter 1",
      "Title": "Connecting the Cisco MDS 9148S Switch",
      "Description": "Describes how to connect the Cisco MDS 9148S Multilayer Fabric switch."
    },
    {
      "Chapter": "Appendix 1",
      "Title": "Cabinet and Rack Installation",
      "Description": "Provides guidelines for selecting an enclosed cabinet, and the procedure for installing a switch using the optional Telco and EIA Shelf Bracket Kit."
    },
    {
      "Chapter": "Appendix 1",
      "Title": "Technical Specifications",
      "Description": "Lists the Cisco MDS 9148S Multilayer Fabric switch specifications, and includes safety information, site requirements, and power connections."
    }
  ],
  "source": "docling"
}
```

# Organization

This guide is organized as follows:

Chapter Description
Chapter 1 Provides an overview of the CiscoMDS
9148S Multilayer Fabric switch and its
components.
Chapter 2 Describes how to install the CiscoMDS
9148S Multilayer Fabric switch, and
includes how to install power supplies and
fan modules.
Chapter 1 Describes how to connect the CiscoMDS
9148S Multilayer Fabric switch.

Appendix 1 Provides guidelines for selecting an
enclosed cabinet, and the procedure for
installing a switch using the optional Telco
and EIA Shelf Bracket Kit.
Appendix 1 Lists the CiscoMDS 9148S Multilayer
Fabric switch specifications, and includes
safety information, site requirements, and
power connections.


<!-- page: 8 -->
```json
{
  "page": 8,
  "table_index": 1,
  "headers": [
    "Chapter",
    "Title",
    "Description"
  ],
  "rows": [
    {
      "Chapter": "Appendix 1",
      "Title": "Cable and Port Specifications",
      "Description": "Lists cable and port specifications for the Cisco MDS 9148S Multilayer Fabric switch."
    },
    {
      "Chapter": "Appendix",
      "Title": "Site Planning and Maintenance Records",
      "Description": "Provides site planning and maintenance records."
    }
  ],
  "source": "docling"
}
```


<!-- page: 9 -->
Ce symbole d'avertissement indique un danger. Vous vous trouvez dans une Attention
situation pouvant causer des blessures ou des dommages corporels. Avant de
travailler sur un équipement, soyez conscient des dangers posés par les
circuits électriques et familiarisez-vous avec les procédures couramment
utilisées pour éviter les accidents. Pour prendre connaissance des
traductions d’avertissements figurant dans cette publication, consultez le
document Regulatory Compliance and Safety Information (Conformité aux
règlements et consignes de sécurité) qui accompagne cet appareil.

Dieses Warnsymbol bedeutet Gefahr. Sie befinden sich in einer Situation, die Warnung
zu einer Körperverletzung führen könnte. Bevor Sie mit der Arbeit an
irgendeinem Gerät beginnen, seien Sie sich der mit elektrischen
Stromkreisen verbundenen Gefahren und der Standardpraktiken zur
Vermeidung von Unfällen bewußt. Übersetzungen der in dieser
Veröffentlichung enthaltenen Warnhinweise finden Sie im Dokument
Regulatory Compliance and Safety Information (Informationen zu
behördlichen Vorschriften und Sicherheit), das zusammen mit diesem Gerät
geliefert wurde.

Questo simbolo di avvertenza indica un pericolo. La situazione potrebbe Avvertenza
causare infortuni alle persone. Prima di lavorare su qualsiasi
apparecchiatura, occorre conoscere i pericoli relativi ai circuiti elettrici ed
essere al corrente delle pratiche standard per la prevenzione di incidenti. La
traduzione delle avvertenze riportate in questa pubblicazione si trova nel
documento Regulatory Compliance and Safety Information (Conformità alle
norme e informazioni sulla sicurezza) che accompagna questo dispositivo.

Dette varselsymbolet betyr fare. Du befinner deg i en situasjon som kan føre Advarsel
til personskade. Før du utfører arbeid på utstyr, må du vare oppmerksom på de
faremomentene som elektriske kretser innebærer, samt gjøre deg kjent med
vanlig praksis når det gjelder å unngå ulykker. Hvis du vil se oversettelser av
de advarslene som finnes i denne publikasjonen, kan du se i dokumentet
Regulatory Compliance and Safety Information (Overholdelse av forskrifter og
sikkerhetsinformasjon) som ble levert med denne enheten.

Este símbolo de aviso indica perigo. Encontra-se numa situação que lhe Aviso
poderá causar danos físicos. Antes de começar a trabalhar com qualquer
equipamento, familiarize-se com os perigos relacionados com circuitos
eléctricos, e com quaisquer práticas comuns que possam prevenir possíveis
acidentes. Para ver as traduções dos avisos que constam desta publicação,
consulte o documento Regulatory Compliance and Safety Information
(Informação de Segurança e Disposições Reguladoras) que acompanha este
dispositivo.

Este símbolo de aviso significa peligro. Existe riesgo para su integridad física. ¡Advertencia!
Antes de manipular cualquier equipo, considerar los riesgos que entraña la
corriente eléctrica y familiarizarse con los procedimientos estándar de
prevención de accidentes. Para ver una traducción de las advertencias que
aparecen en esta publicación, consultar el documento titulado Regulatory
Compliance and Safety Information (Información sobre seguridad y
conformidad con las disposiciones reglamentarias) que se acompaña con
este dispositivo.


<!-- page: 10 -->
Denna varningssymbol signalerar fara. Du befinner dig i en situation som kan Varning!
leda till personskada. Innan du utför arbete på någon utrustning måste du vara
medveten om farorna med elkretsar och känna till vanligt förfarande för att
förebygga skador. Se förklaringar av de varningar som förkommer i denna
publikation i dokumentet Regulatory Compliance and Safety Information
(Efterrättelse av föreskrifter och säkerhetsinformation), vilket medföljer
denna anordning.

# Related Documentation

The documentation set for the Cisco MDS 9000 Family includes the following documents. To find a
document online, use the Cisco MDS NX-OS Documentation Locator at:

http://www.cisco.com/en/US/docs/storage/san_switches/mds9000/roadmaps/doclocater.htm

## Release Notes

Cisco MDS 9000 Family Release Notes for Cisco MDS NX-OS Releases (cid:129)
Cisco MDS 9000 Family Release Notes for MDS SAN-OS Releases (cid:129)
Cisco MDS 9000 Family Release Notes for Storage Services Interface Images (cid:129)
Cisco MDS 9000 Family Release Notes for Cisco MDS 9000 EPLD Images (cid:129)
Release Notes for Cisco MDS 9000 Family Fabric Manager (cid:129)

## Regulatory Compliance and Safety Information

**Regulatory Compliance and Safety Information for the Cisco MDS 9000 Family (cid:129)**

## Compatibility Information

Cisco Data Center Interoperability Support Matrix (cid:129)
Cisco MDS 9000 NX-OS Hardware and Software Compatibility Information and Feature Lists (cid:129)
Cisco MDS NX-OS Release Compatibility Matrix for Storage Service Interface Images (cid:129)
Cisco MDS 9000 Family Switch-to-Switch Interoperability Configuration Guide (cid:129)
Cisco MDS NX-OS Release Compatibility Matrix for IBM SAN Volume Controller Software for (cid:129)
Cisco MDS 9000
Cisco MDS SAN-OS Release Compatibility Matrix for VERITAS Storage Foundation for Networks (cid:129)
Software

## Hardware Installation

**Cisco MDS 9700 Series Hardware Installation Guide (cid:129)**


<!-- page: 11 -->
Cisco MDS 9500 Series Hardware Installation Guide (cid:129)
Cisco MDS 9250i Multiservice Switch Installation Guide (cid:129)
Cisco MDS 9200 Series Hardware Installation Guide (cid:129)
Cisco MDS 9124 and Cisco MDS 9134 Multilayer Fabric Switch Quick Start Guide (cid:129)
Cisco MDS 9148 Multilayer Fabric Switch Quick Start Guide (cid:129)
Cisco MDS 9148S Multilayer Fabric Switch Quick Start Guide (cid:129)

## Software Installation and Upgrade

Cisco MDS 9000 NX-OS Release 6.2(x) and SAN-OS 3(x) Software Upgrade and Downgrade Guide (cid:129)
Cisco MDS 9000 Family Storage Services Interface Image Install and Upgrade Guide (cid:129)
Cisco MDS 9000 Family Storage Services Module Software Installation and Upgrade Guide (cid:129)

## Cisco NX-OS

Cisco MDS 9000 Family NX-OS Licensing Guide (cid:129)
Cisco MDS 9000 Family NX-OS Fundamentals Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS System Management Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Interfaces Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Fabric Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Quality of Service Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Security Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS IP Services Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Intelligent Storage Services Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS High Availability and Redundancy Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Inter-VSAN Routing Configuration Guide (cid:129)
Cisco MDS 9000 Family NX-OS Configuration Limits (cid:129)

## Cisco Data Center Network Manager

Cisco DCNM Fundamentals Guide (cid:129)
Fabric Configuration Guide, Cisco DCNM for SAN (cid:129)
High Availability and Redundancy Configuration Guide, Cisco DCNM for SAN (cid:129)
Intelligent Storage Services Configuration Guide, Cisco DCNM for SAN (cid:129)
Inter-VSAN Routing Configuration Guide, Cisco DCNM for SAN (cid:129)
IP Services Configuration Guide, Cisco DCNM for SAN (cid:129)
Quality of Service Configuration Guide, Cisco DCNM for SAN (cid:129)
Security Configuration Guide, Cisco DCNM for SAN (cid:129)


<!-- page: 12 -->
**System Management Configuration Guide, Cisco DCNM for SAN (cid:129)**

## Command-Line Interface

**Cisco MDS 9000 Family Command Reference (cid:129)**

## Intelligent Storage Networking Services Configuration Guides

Cisco MDS 9000 I/O Acceleration Configuration Guide (cid:129)
Cisco MDS 9000 Family SANTap Deployment Guide (cid:129)
Cisco MDS 9000 Family Data Mobility Manager Configuration Guide (cid:129)
Cisco MDS 9000 Family Storage Media Encryption Configuration Guide (cid:129)
Cisco MDS 9000 Family Secure Erase Configuration Guide (cid:129)
Cisco MDS 9000 Family Cookbook for Cisco MDS SAN-OS (cid:129)

## Troubleshooting and Reference

Cisco NX-OS System Messages Reference (cid:129)
Cisco MDS 9000 Family NX-OS Troubleshooting Guide (cid:129)
Cisco MDS 9000 Family NX-OS MIB Quick Reference (cid:129)
Cisco MDS 9000 Family NX-OS SMI-S Programming Reference (cid:129)
Cisco MDS 9000 Family Fabric Manager Server Database Schema (cid:129)


<!-- page: 13 -->
![Troubleshooting and Reference](images/image_p13_00.png)

# 1
C H A P T E R

# Product Overview

The Cisco MDS 9148S Multilayer Fabric Switch (DS-C9148S48PK9) is the next generation of the
highly reliable and flexible Cisco MDS 9100 Series switches. A powerful compact one rack-unit (1RU)
form factor can scale from 12 to 48 line-rate 16-Gbps Fibre Channel ports.
The Cisco MDS 9148S switch meets the requirements for a:
Standalone storage area network (SAN) in small departmental storage environments (cid:129)
Stop-of-the-rack switch in medium-sized redundant fabrics (cid:129)
Edge switch in enterprise data center core-edge topologies (cid:129)
The Cisco MDS 9148S switch has the following major features:
12, 24, and 48, default licensed ports and an 12-port on-demand license (cid:129)
2-, 4-, 8- and, 16-Gbps full line rates (cid:129)
Port interfaces that support field-replaceable, hot-swappable small form-factor pluggable (SFP) (cid:129)
transceivers
Redundant hot-swappable power supplies and fan trays, PortChannels for Inter-Switch Link (ISL) (cid:129)
resiliency, and F-port channeling for resiliency on uplinks from a Cisco MDS 9148S operating in
NPV mode
Enterprise class features such as In-Service Software Upgrades (ISSU), Virtual SANs (VSANs), (cid:129)
security features, and quality of service (QoS)
PowerOn Auto Provisioning (POAP) to automate software image upgrades and configuration file (cid:129)
installation on newly deployed switches
Intelligent diagnostics (cid:129)
Full compatibility with the Cisco MDS 9000 Family. (cid:129)
This chapter contains the following topics:
Chassis Components, page1-7 (cid:129)
Power Supplies, page1-12 (cid:129)
Fan Modules, page1-12 (cid:129)
Cisco MDS 9148S Multilayer Switch Ports, page1-13 (cid:129)

# Chassis Components

This section describes the different views of the chassis.


<!-- page: 14 -->
**Front View, page1-8 (cid:129)
Rear View, page1-8 (cid:129)
Switch LEDs, page1-10 (cid:129)**

## Front View

The front of the Cisco MDS 9148S switch contains the LEDs, the console and management ports, and
48 16-Gbps Fibre Channel Ports. See Figure1.

**Figure1 Front View of the Cisco MDS 9148S Multilayer Fabric Switch**

![Front View](images/image_p14_00.png)

```json
{
  "page": 14,
  "table_index": 2,
  "headers": [
    "0",
    "1",
    "2"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Console port",
      "2": "5 USB port"
    },
    {
      "0": "2",
      "1": "Status LED",
      "2": "6 Ethernet port"
    },
    {
      "0": "3",
      "1": "Power supply LED",
      "2": "7 Fibre Channel ports"
    },
    {
      "0": "4",
      "1": "FAN LED",
      "2": ""
    }
  ],
  "source": "docling"
}
```

## Rear View

The rear of the Cisco MDS 9148S switch contains the redundant power supplies, the AC power
receptacle, and the fans. See Figure 2.


<!-- page: 15 -->
**Figure2 Rear View of the Cisco MDS 9148S Multilayer Fabric Switch**

```json
{
  "page": 15,
  "table_index": 4,
  "headers": [
    "0",
    "1",
    "2"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Power supply 2",
      "2": "3 Fan module (fans 3 and 1)"
    },
    {
      "0": "2",
      "1": "Fan module (fans 4 and 2)",
      "2": "4 Power supply 1"
    }
  ],
  "source": "docling"
}
```

**1
2
3 Power
4 Power**

```json
{
  "page": 15,
  "table_index": 3,
  "headers": [
    "0",
    "1",
    "2",
    "3"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Captive screw",
      "2": "5",
      "3": "Power module handle"
    },
    {
      "0": "2",
      "1": "On/Off switch",
      "2": "6",
      "3": "Fan module (fans 4 & 2)"
    },
    {
      "0": "3",
      "1": "Power receptable",
      "2": "7",
      "3": "Fan module (fans 3 & 1)"
    },
    {
      "0": "4",
      "1": "Power supply 2",
      "2": "8",
      "3": "Power supply 1"
    }
  ],
  "source": "docling"
}
```

**Figure3 Rear Panel Slot Numbering of Cisco MDS 9148S Multilayer Fabric Switch**

![Rear View](images/image_p15_00.png)

**1 Power
2 Fan**


<!-- page: 16 -->
![1 Power](images/image_p16_00.png)

```json
{
  "page": 16,
  "table_index": 5,
  "headers": [
    "0",
    "1",
    "2",
    "3"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Switch status LED",
      "2": "4",
      "3": "10/100/1000 Ethernet management port link LED"
    },
    {
      "0": "2",
      "1": "Power supply LED",
      "2": "5",
      "3": "10/100/1000 Ethernet management port activity LED"
    },
    {
      "0": "3",
      "1": "Fan module status LED",
      "2": "",
      "3": ""
    }
  ],
  "source": "docling"
}
```


<!-- page: 17 -->
Table1-1 describes the front panel LEDs for the Cisco MDS 9148S switch.

**Table1-1 Switching Module LEDs**

**LED
Switch status**

Power supply
status

Fan module
status

Port link

1. The flashing green light turns on automatically when an external loopback is detected that causes the interfaces to be isolated.
The flashing green light overrides the beacon mode configuration. The state of the LED is restored to reflect the beacon mode
configuration after the external loopback is removed.

```json
{
  "page": 17,
  "table_index": 6,
  "headers": [
    "LED",
    "Status",
    "Description"
  ],
  "rows": [
    {
      "LED": "Switch status",
      "Status": "Green",
      "Description": "All diagnostics pass. The module is operational. (normal initialization sequence)."
    },
    {
      "LED": "Switch status",
      "Status": "Orange",
      "Description": "The module is booting or running diagnostics (normal initialization sequence) An over temperature condition has occurred. (A minor temperature threshold has been exceeded during environmental monitoring.)"
    },
    {
      "LED": "Switch status",
      "Status": "Red Blinking",
      "Description": "The diagnostic test failed. The module is not operational because a fault occurred during the initialization sequence. An over temperature condition has occurred. (A major temperature threshold has been exceeded during environmental monitoring.)"
    },
    {
      "LED": "Switch status",
      "Status": "Red",
      "Description": "Board is power on, but didn't boot up Diag or iSAN image."
    },
    {
      "LED": "Switch status",
      "Status": "Off",
      "Description": "The module is not receiving power."
    },
    {
      "LED": "Power supply status",
      "Status": "Green",
      "Description": "Both power supplies are working."
    },
    {
      "LED": "Power supply status",
      "Status": "Orange",
      "Description": "One power supply has failed or has been removed. Note that from Cisco NX-OS Release 6.2.13 and later, the power supply status changes to Red when the power supply fails on a module."
    },
    {
      "LED": "Power supply status",
      "Status": "Red or all LEDs off",
      "Description": "Both power supplies have failed."
    },
    {
      "LED": "Fan module status",
      "Status": "Green",
      "Description": "Both fan modules are working properly."
    },
    {
      "LED": "Fan module status",
      "Status": "Red",
      "Description": "One or both fan modules have failed."
    },
    {
      "LED": "Port link",
      "Status": "Solid green",
      "Description": "Link is up."
    },
    {
      "LED": "Port link",
      "Status": "Steady flashing green",
      "Description": "Link is up (beacon used to identify port). 1"
    },
    {
      "LED": "Port link",
      "Status": "Intermittent flashing green",
      "Description": "Link is up (traffic on port)."
    },
    {
      "LED": "Port link",
      "Status": "Solid orange",
      "Description": "Link is disabled by software."
    },
    {
      "LED": "Port link",
      "Status": "Flashing orange",
      "Description": "A fault condition exists."
    }
  ],
  "source": "docling"
}
```


<!-- page: 18 -->
Table1-2 describes the management port LEDs for the Cisco MDS 9148S switch.

```json
{
  "page": 18,
  "table_index": 7,
  "headers": [
    "LED",
    "Status",
    "Description"
  ],
  "rows": [
    {
      "LED": "Left",
      "Status": "Off",
      "Description": "There is no link."
    },
    {
      "LED": "",
      "Status": "Solid Green",
      "Description": "Indicates a physical link."
    },
    {
      "LED": "Right",
      "Status": "Off",
      "Description": "There is no link."
    },
    {
      "LED": "",
      "Status": "Solid Amber",
      "Description": "There is no link traffic."
    },
    {
      "LED": "",
      "Status": "Blinking Amber",
      "Description": "Indicates link traffic."
    }
  ],
  "source": "docling"
}
```


<!-- page: 19 -->
**Chapter1 Product Overview
Cisco MDS 9148S Multilayer Switch Ports**

Procedures for replacing and installing the fan modules are available in the Removing and Installing Fan


<!-- page: 21 -->
![Step 1: The flashing green light turns on automatically](images/image_p21_00.png)

# 2
C H A P T E R


<!-- page: 22 -->
**Chapter2 Installing the Cisco MDS 9148S Switch
Preinstallation**


<!-- page: 23 -->
Ensure there is adequate space around the switch to allow for servicing the switch and for adequate (cid:129)
airflow (airflow requirements are listed in Appendix1, “Technical Specifications”).
Ensure the air-conditioning meets the heat dissipation requirements listed in Appendix1, “Technical (cid:129)
Specifications.”
Ensure the cabinet or rack meets the requirements listed in Appendix1, “Cabinet and Rack (cid:129)
Installation.”

If the front cabinet mounting rails are not offset from the front door or bezel panel by a minimum Note
of 3inch (7.6cm), and a minimum of 5inch. (12.7cm) if cable management brackets are
installed on the front of the chassis, the chassis should be mounted rear-facing to ensure the
minimum bend radius for fiber-optic cables. See the “Installing the Switch in a Cabinet with
Insufficient Front Clearance” section on page2-21.

**Jumper power cords are available for use in a cabinet. For more information, see the “Jumper Note
Power Cord” section on page1-69.**

Ensure the chassis is adequately grounded. If the switch is not mounted in a grounded rack, we (cid:129)
recommend connecting both the system ground on the chassis and the power supply ground to an
earth ground.
Ensure the site power meets the power requirements listed in Appendix1, “Technical (cid:129)
Specifications.” If available, you can use an uninterrupted power supply (UPS) to protect against
power failures.

Avoid UPS types that use ferro-resonant technology. These UPS types can become unstable Caution
with systems such as the CiscoMDS 9000 Family, which can have substantial current draw
fluctuations because of fluctuating data traffic patterns.

Ensure that circuits are sized according to local and national codes. (cid:129)
For North America, the 300-W power supplies require a 20-A circuit. If you are using a 200- or
240-VAC power source in North America, the circuit must be protected by a two-pole circuit
breaker.

**To prevent loss of input power, ensure the total maximum loads on the circuits supplying Caution
power to the switch are within current ratings for wiring and breakers.**

As you install and configure the switch, record the information listed in the “Site Planning and (cid:129)
Maintenance Records” section on page1-71.
Use the following screw torques when installing the switch: (cid:129)
Captive screws: 4 in-lb –
M3 screws: 4 in-lb –
M4 screws: 12 in-lb –
10-32 screws: 20 in-lb –
12-24 screws: 30 in-lb –


<!-- page: 25 -->
**Any optional items ordered (cid:129)**


<!-- page: 26 -->
**Use the tape measure and level to verify that the rails are horizontal and at the same height. b.**

**Figure2-1 Installing the Slider Rails**

![2](images/image_p26_00.png)

**Figure2-2 Installing the Notched Slider Rails**

![Figure2-2 Installing the Notched Slider Rails](images/image_p26_01.png)


<!-- page: 27 -->
**Chapter2 Installing the Cisco MDS 9148S Switch
Installing the Switch in a Cabinet with Insufficient Front Clearance**

Insert the switch into the rack: Step5
By using both hands, position the switch with the back of the switch between the front a.
rack-mounting rails as shown in Figure2-3.
Align the two C brackets on either side of the switch with the slider rails installed in the rack. Slide b.
the C brackets onto the slider rails, and then gently slide the switch all the way into the rack. If the
switch does not slide easily, try realigning the C brackets on the slider rails.
Stabilize the switch in the rack by attaching the front rack-mount brackets to the front rack-mounting Step6
rails:
Insert two screws (12-24 or 10-32, depending on rack type) and through the cage nuts and the holes a.
in one of the front rack-mount brackets and into the threaded holes in the rack-mounting rail.
Repeat for the front rack-mount bracket on the other side of the switch. b.
If you are installing the optional cable guides, place the cable guides in front of the front rack-mount
brackets, and then pass the screws through the cable guides, front rack-mount brackets, and mounting
rail. You can install one or both cable guides; if installing a single cable guide, it can be installed on
either side.

**Figure2-3 Attaching the Switch to the Rack**

# Installing the Switch in a Cabinet with Insufficient Front
Clearance

This section describes how to use the rack-mount kit provided with the switch to install the Cisco MDS
9148S switch into a cabinet with insufficient front-facing clearance. The Cisco MDS 9148S switch is
installed rear-facing to provide adequate clearance for the fiber-optic cables. This cabinet meets the
requirements described in Appendix1, “Cabinet and Rack Installation,” except the cabinet has less than
three-inch clearance between the inside of the front door or bezel panel and the front cabinet mounting
rails. This rear-facing installation is necessary to ensure that the minimum bend radius for the fiber-optic


<!-- page: 28 -->
cables is maintained. In these cabinets, the Cisco MDS 9148S switch is mounted backwards, with the

```json
{
  "page": 28,
  "table_index": 8,
  "headers": [
    "Description",
    "Quantity"
  ],
  "rows": [
    {
      "Description": "30- to 36-inch slider rails",
      "Quantity": "2 per kit"
    },
    {
      "Description": "24- to 30-inch slider rails",
      "Quantity": "2 per kit"
    },
    {
      "Description": "18- to 24-inch slider rails",
      "Quantity": "2 per kit"
    },
    {
      "Description": "Front rack-mount brackets",
      "Quantity": "2 per kit"
    },
    {
      "Description": "12-24 x 3/4-inch Phillips binder-head screws",
      "Quantity": "10 per kit"
    },
    {
      "Description": "10-32 x 3/4-inch Phillips binder-head screws",
      "Quantity": "10 per kit"
    },
    {
      "Description": "M4 x 6-mm Phillips flat-head screws",
      "Quantity": "6 per kit"
    },
    {
      "Description": "12-24 cage nuts",
      "Quantity": "10 per kit"
    }
  ],
  "source": "docling"
}
```


<!-- page: 31 -->
**Stabilize the switch in the rack by attaching the front rack-mount brackets to the rear rack-mounting Step4**

![Installing the Switch in a Cabinet](images/image_p31_00.png)


<!-- page: 32 -->
**Chapter2 Installing the Cisco MDS 9148S Switch
Grounding the Switch**

![Chapter2 Installing the Cisco MDS 9148S Switch](images/image_p32_00.png)


<!-- page: 33 -->
**Chapter2 Installing the Cisco MDS 9148S Switch
Starting Up the Switch**


<!-- page: 34 -->
Depending on the outlet receptacle on your power distribution unit, you may need the optional Note
jumper power cord to connect the Cisco MDS 9148S switch to your outlet receptacle. See the
“Jumper Power Cord” section on page1-69.

Connect the other end of the power cables to an AC power source. Step3
Ensure that the switch is adequately grounded as described in the “Installing the Switch in a Cabinet with Step4
Insufficient Front Clearance” section on page2-21, and that the power cables are connected to outlets
that have the required AC power voltages (provided in the “Installing the Switch in a Cabinet with
Insufficient Front Clearance” section on page2-21).
Flip the power switches on the power supplies to the on (|) position. The switch boots automatically. Step5
Listen for the fans; they should begin operating as soon as the switch is powered on. Step6

Do not operate the switch without a functioning fan module except for during the brief fan Caution
module replacement procedure. The Cisco MDS 9000 Family switches can operate for only a
few minutes without any functioning fan modules before they begin to overheat.

Verify that the LED behavior is as follows when the switch has finished booting: Step7
Fan status LED is green. (cid:129)
Each power supply LED is green. (cid:129)
The Switch status LED is green. If this LED is orange or red, then one or more environmental (cid:129)
monitors is reporting a problem.
The Ethernet port Link LEDs should not be on unless the cable is connected. (cid:129)

**The LEDs for the Fibre Channel ports remain orange until the ports are enabled, and the LED Note
for the MGMT 10/100/1000 Ethernet port remains off until the port is connected.**

If any LEDs other than the Fibre Channel port LEDs are orange or red after the initial boot processes are
Cisco MDS 9000 Family Troubleshooting Guide complete, see the .
Try removing and reinstalling a component that is not operating properly. If it still does not operate Step8
correctly, contact your customer service representative for a replacement.

If you purchased Cisco support through a Cisco reseller, contact the reseller directly. If you Note
purchased support directly from Cisco, contact Cisco Technical Support at this URL:
http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html

Verify that the system software has booted and the switch has initialized without error messages. If any Step9
Cisco MDS 9000 Family Troubleshooting Guide Cisco MDS 9000 Family problems occur, see the or the
System Messages Guide . If you cannot resolve an issue, contact your customer service representative.
Complete the worksheets provided in Appendix1, “Site Planning and Maintenance Records” for future Step10
reference.


<!-- page: 35 -->
**Chapter2 Installing the Cisco MDS 9148S Switch
Removing and Installing Components**


<!-- page: 36 -->
**Figure2-6 Rear View of the Cisco MDS 9148S Switch**

```json
{
  "page": 36,
  "table_index": 9,
  "headers": [
    "0",
    "1",
    "2",
    "3"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Power Supply 2",
      "2": "4",
      "3": "AC Power receptacle"
    },
    {
      "0": "2",
      "1": "Fan Module 2 (Fans 2 and 4)",
      "2": "5",
      "3": "Switch On/Off"
    },
    {
      "0": "3",
      "1": "Fan Module 1 (Fans 1 and 3)",
      "2": "6",
      "3": "Power Supply 1"
    }
  ],
  "source": "docling"
}
```

**Cisco MDS 9148S Multilayer Switch Hardware Installation Guide
2-30 OL-20185-01**


<!-- page: 37 -->
**Make sure the power cord is disconnected before installing the power supply. Step2**


<!-- page: 38 -->
**Pull the fan module out of the switch and put it in a safe place. Step4**

![Pull the fan module out of the](images/image_p38_00.png)


<!-- page: 41 -->
![Pull the fan module out of the](images/image_p41_00.png)

# Connecting the Cisco MDS 9148S Switch

The Cisco MDS 9148S switch provides the following types of ports:
Console port (Interface Module)—An RS-232 port that you can use to create a local management (cid:129)
connection.
MGMT 10/100 Ethernet port (Interface Module)—An Ethernet port that you can use to access and (cid:129)
manage the switch by IP address, such as through the CLI or Fabric Manager.
Fibre Channel ports (Supervisor and Switching Modules)— Fibre Channel ports that you can use to (cid:129)
connect to the SAN, or for in-band management.
This chapter describes how to connect the various components of the Cisco MDS 9148S switch, and it
includes the following information:
Preparing for Network Connections, page1-35 (cid:129)
Connecting the Console Port, page1-35 (cid:129)
Connecting the 10/100/1000 Ethernet Management Port, page1-38 (cid:129)
Connecting to a Fibre Channel Port, page1-38 (cid:129)

# Preparing for Network Connections

When preparing your site for network connections to the Cisco MDS 9148S switch, consider the
following for each type of interface:
Cabling required for each interface type (cid:129)
Distance limitations for each signal type (cid:129)
Additional interface equipment needed (cid:129)
Before installing the component, have all additional external equipment and cables available.

# Connecting the Console Port

This section describes how to connect the RS-232 console port to a PC. The console port allows you to
perform the following functions:
Configure the switch from the CLI. (cid:129)
Monitor network statistics and errors. (cid:129)
Configure SNMP agent parameters. (cid:129)


<!-- page: 42 -->
**Chapter1 Connecting the Cisco MDS 9148S Switch
Connecting the Console Port**

**Download software updates to the switch or distribute software images residing in flash memory to (cid:129)**

![Connecting the Console Port](images/image_p42_00.png)


<!-- page: 43 -->
**Connect the supplied RJ-45 to DB-9 female adapter or RJ-45 to DB-25 female adapter (depending on Step2**


<!-- page: 44 -->
**Chapter1 Connecting the Cisco MDS 9148S Switch
Connecting the 10/100/1000 Ethernet Management Port**


<!-- page: 45 -->
**Chapter1 Connecting the Cisco MDS 9148S Switch
Connecting to a Fibre Channel Port**

![Chapter1 Connecting the Cisco MDS 9148S Switch](images/image_p45_00.png)

![Chapter1 Connecting the Cisco MDS 9148S Switch](images/image_p45_01.png)


<!-- page: 46 -->
**Insert or leave the dust plug in the cable end of the transceiver if a cable is not being installed in the Step5**


<!-- page: 47 -->
To install a cable into a transceiver, follow these steps:

![To install a cable](images/image_p47_00.png)


<!-- page: 48 -->
**Insert a dust plug onto the end of the cable. Step4**


<!-- page: 49 -->
![Insert a dust plug](images/image_p49_00.png)


<!-- page: 50 -->
**Chapter1 Cabinet and Rack Installation
Cabinet and Rack Requirements**

**For four-post EIA cabinets (perforated or solid-walled): (cid:129)**


<!-- page: 51 -->
**Chapter1 Cabinet and Rack Installation
Cisco MDS 9000 Family Telco and EIA Shelf Bracket**

## Requirements Specific to Solid-Walled Cabinets

In addition to the requirements listed in the “General Requirements for Cabinets and Racks” section on
page1-43, solid-walled cabinets must meet the following requirements:
A roof-mounted fan tray and an air cooling scheme in which the fan tray pulls air in at the bottom (cid:129)
of the cabinet and exhausts it out the top, with a minimum of 500 cfm of airflow exiting the cabinet
roof through the fan tray.
Nonperforated (solid and sealed) front and back doors and side panels so that air travels predictably (cid:129)
from bottom to top.
The overall cabinet depth should be 36 to 42 in. (91.4 to 106.7 cm) to allow the doors to close and (cid:129)
adequate airflow.
A minimum of 150 sq. in. (968 sq. cm) of open area at the floor air intake of the cabinet. (cid:129)
The lowest piece of equipment should be installed a minimum of 1.75 in. (4.4cm) above the floor (cid:129)
openings to prevent blocking the floor intake.

## Requirements Specific to Standard Open Racks

## Requirements Specific to Telco Racks

# Cisco MDS 9000 Family Telco and EIA Shelf Bracket

The optional Telco and EIA Shelf Bracket Kit (part number DS-SHELF=) can temporarily or
permanently support the Cisco MDS 9148S switch during installation. Once the front rack-mount
brackets are securely attached to the rack-mounting rails, the shelf bracket can be removed.
This kit supports the following configurations:
A Cisco MDS 9148S Switch in a two-post Telco rack (cid:129)
A Cisco MDS 9148S Switch in a four-post EIA rack (cid:129)


<!-- page: 52 -->
```json
{
  "page": 52,
  "table_index": 10,
  "headers": [
    "Rack Type",
    "MDS 9148S"
  ],
  "rows": [
    {
      "Rack Type": "EIA (4-post)",
      "MDS 9148S": "7.5 lb"
    },
    {
      "Rack Type": "Telco (2 post)",
      "MDS 9148S": "15 lb"
    }
  ],
  "source": "docling"
}
```


<!-- page: 53 -->
## Before Installing the Shelf Brackets

```json
{
  "page": 53,
  "table_index": 12,
  "headers": [
    "0",
    "1",
    "2",
    "3"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Rack-mounting rail (2x)",
      "2": "3",
      "3": "10-32 screws (2x)"
    },
    {
      "0": "2",
      "1": "Shelf bracket (2x)",
      "2": "4",
      "3": "Crossbar"
    }
  ],
  "source": "docling"
}
```

Before installing the shelf brackets, inspect the contents of your kit. Table1-1 lists the contents of the
shelf bracket kit.

**Table1-1 Contents of Shelf Bracket Kit**

### Required Equipment

**You need the following equipment for this installation:
Number 2 Phillips screwdriver (cid:129)
Tape measure and level (to ensure shelf brackets are level) (cid:129)**

### Installing the Shelf Bracket Kit into a Two-Post Telco Rack

Figure1-1 shows the installation of the shelf bracket kit into a two-post Telco rack.

**Figure1-1 Installing the Shelf Bracket Kit into a Telco Rack**

![Installing the Shelf Bracket Kit](images/image_p53_00.png)

![Figure1-1 Installing the Shelf Bracket Kit](images/image_p53_01.png)

```json
{
  "page": 53,
  "table_index": 11,
  "headers": [
    "Quantity",
    "Part Description"
  ],
  "rows": [
    {
      "Quantity": "2",
      "Part Description": "Slider brackets"
    },
    {
      "Quantity": "2",
      "Part Description": "Shelf brackets"
    },
    {
      "Quantity": "1",
      "Part Description": "Crossbar"
    },
    {
      "Quantity": "2",
      "Part Description": "10-32 x 3/8-in. Phillips pan-head screws"
    },
    {
      "Quantity": "16",
      "Part Description": "12-24 x 3/4-in. Phillips screws"
    },
    {
      "Quantity": "16",
      "Part Description": "10-24 x 3/4-in. Phillips screws"
    }
  ],
  "source": "docling"
}
```

**1 10-32 screws (2x)
2 Crossbar**


<!-- page: 54 -->
To install the shelf brackets in a Telco rack, follow these steps:


<!-- page: 55 -->
```json
{
  "page": 55,
  "table_index": 13,
  "headers": [
    "0",
    "1",
    "2",
    "3"
  ],
  "rows": [
    {
      "0": "1",
      "1": "Rack-mounting rail (4x)",
      "2": "4",
      "3": "Crossbar"
    },
    {
      "0": "2",
      "1": "Shelf bracket (2x)",
      "2": "5",
      "3": "10-32 screws (2x)"
    },
    {
      "0": "3",
      "1": "Slider rail (2)",
      "2": "",
      "3": ""
    }
  ],
  "source": "docling"
}
```


<!-- page: 56 -->
**Attach the crossbar to the shelf brackets as shown in Figure1-2, using the 10-32 screws. Step4**


<!-- page: 59 -->
![Attach the crossbar to the shelf brackets](images/image_p59_00.png)

```json
{
  "page": 59,
  "table_index": 15,
  "headers": [
    "Description",
    "Specification"
  ],
  "rows": [
    {
      "Description": "Cisco MDS 9148S Switch Dimensions",
      "Specification": "Width = 17.16 inch (43.59 centimeter) Height = 1.72 inch (4.37 centimeter) Depth = 16.34 inch (41.50 centimeter)"
    },
    {
      "Description": "Rack Unit (RU)",
      "Specification": "Chassis requires 1 RU (1.75 in. or 4.45 cm)"
    }
  ],
  "source": "docling"
}
```

# Technical Specifications

This appendix includes the following technical specifications for the Cisco MDS 9148S switch:
Switch Specifications, page1-53 (cid:129)
Power Specifications, page1-54 (cid:129)
SFP Transceiver Specifications, page1-56 (cid:129)

# Switch Specifications

Table1-1 lists the environmental specifications for the Cisco MDS 9148S switch.

```json
{
  "page": 59,
  "table_index": 14,
  "headers": [
    "Description",
    "Specification"
  ],
  "rows": [
    {
      "Description": "Temperature, ambient operating",
      "Specification": "32 to 104°F (0 to 40°C)"
    },
    {
      "Description": "Temperature, ambient nonoperating and storage",
      "Specification": "-40 to 158°F (-40 to 70°C)"
    },
    {
      "Description": "Humidity (RH), ambient (noncondensing) operating",
      "Specification": "10 to 90%"
    },
    {
      "Description": "Humidity (RH), ambient (noncondensing) nonoperating and storage",
      "Specification": "5 to 95%"
    },
    {
      "Description": "Altitude, operating",
      "Specification": "-197 to 6500 ft (-60 to 2000 m)"
    },
    {
      "Description": "Noise levels",
      "Specification": "60 dB"
    }
  ],
  "source": "docling"
}
```

**Cisco MDS 9148S switch Table1-1 Environmental Specifications for the**

Description Specification
Temperature, ambient operating 32 to 104°F (0 to 40°C)
-40 to 158°F (-40 to 70°C) Temperature, ambient nonoperating and
storage
Humidity (RH), ambient (noncondensing) 10 to 90%
operating
Humidity (RH), ambient (noncondensing) 5 to 95%
nonoperating and storage
Altitude, operating -197 to 6500 ft (-60 to 2000 m)
Noise levels 60 dB

Table1-2 lists the physical specifications for the Cisco MDS 9148S switch.

**Table1-2 Cisco MDS 9148S Switch Specifications**

Description Specification
CiscoMDS9148S Width = 17.16 inch (43.59 centimeter)
Switch Dimensions Height = 1.72 inch (4.37 centimeter)
Depth = 16.34 inch (41.50 centimeter)
Rack Unit (RU) Chassis requires 1 RU (1.75 in. or 4.45 cm)


<!-- page: 60 -->
**Table1-2 Cisco MDS 9148S Switch Specifications (continued)**

Description Specification
Weight 19.84 lb (9 kg) (with two fan modules and two power
supplies installed)
Power Supply 300-W AC for each power supply
(fixed)
Part Number: DS-C48S-300AC
Power cord: Notched C15 socket connector connecting to
C16 plug on power supply
100 to 240V AC (10% range)
50 to 60 Hz (nominal)
Airflow Back to front.
200 linear feet per minute (LFM) through the system and a
maximum of 380 LMDM.
Cisco recommends that you maintain a minimum air space
of 2.5 in. (6.4 cm) between walls and chassis air vents and a
minimum horizontal separation of 6 in. (15.2 cm) between
two chassis to prevent overheating.

```json
{
  "page": 60,
  "table_index": 17,
  "headers": [
    "AC Input Power Supply",
    "Specification"
  ],
  "rows": [
    {
      "AC Input Power Supply": "AC input voltage",
      "Specification": "Minimum = 90 VAC Nominal = 100 to 240 VAC Maximum = 264 VAC"
    },
    {
      "AC Input Power Supply": "AC input current rating (maximum)",
      "Specification": "4.7 A at 85 VAC 3.6 A at 110 VAC 1.8 A at 220 VAC Note For plug current rating, see the 'Jumper Power Cord' section on page 1-69."
    },
    {
      "AC Input Power Supply": "AC input frequency",
      "Specification": "Nominal = 50 to 60 Hz"
    }
  ],
  "source": "docling"
}
```

# Power Specifications

This section includes the following information:
General Power Supply Specifications, page1-54 (cid:129)
Power Supply Requirements Specifications, page1-55 (cid:129)
Connection Guidelines for AC-Powered Systems, page1-56 (cid:129)

## General Power Supply Specifications

Table1-3 lists the specifications for the Cisco MDS 9148S switch AC input power supply.

**Table1-3 Cisco MDS 9148S Switch AC Input Power Supply Specifications**

AC Input Power Supply Specification
AC input voltage Minimum = 90 VAC
Nominal = 100 to 240 VAC
Maximum = 264 VAC
AC input current rating 4.7 A at 85 VAC
(maximum) 3.6 A at 110 VAC
1.8 A at 220 VAC
For plug current rating, see the Note
“Jumper Power Cord” section on
page1-69.
AC input frequency Nominal = 50 to 60 Hz

```json
{
  "page": 60,
  "table_index": 16,
  "headers": [
    "Description",
    "Specification"
  ],
  "rows": [
    {
      "Description": "Weight",
      "Specification": "19.84 lb (9 kg) (with two fan modules and two power supplies installed)"
    },
    {
      "Description": "Power Supply (fixed)",
      "Specification": "300-W AC for each power supply Part Number: DS-C48S-300AC Power cord: Notched C15 socket connector connecting to C16 plug on power supply 100 to 240V AC (10% range) 50 to 60 Hz (nominal)"
    },
    {
      "Description": "Airflow",
      "Specification": "Back to front. 200 linear feet per minute (LFM) through the system and a maximum of 380 LMDM. Cisco recommends that you maintain a minimum air space of 2.5 in. (6.4 cm) between walls and chassis air vents and a minimum horizontal separation of 6 in. (15.2 cm) between two chassis to prevent overheating."
    }
  ],
  "source": "docling"
}
```


<!-- page: 61 -->
```json
{
  "page": 61,
  "table_index": 20,
  "headers": [
    "Part Number",
    "PID",
    "Type",
    "Fuse Rated AMP",
    "I2T",
    "Fuse Melting Time"
  ],
  "rows": [
    {
      "Part Number": "341-0706-02",
      "PID": "DS-C48S-300AC",
      "Type": "Time-Lag",
      "Fuse Rated AMP": "6.3 A",
      "I2T": "144.869",
      "Fuse Melting Time": "27.7 hrs@8 A, 0.9 s@20 A"
    }
  ],
  "source": "docling"
}
```

```json
{
  "page": 61,
  "table_index": 19,
  "headers": [
    "Cisco MDS 9148S Switch",
    "AC Power (Volt)",
    "AC Power (Watt)"
  ],
  "rows": [
    {
      "Cisco MDS 9148S Switch": "",
      "AC Power (Volt)": "220",
      "AC Power (Watt)": "125.08"
    },
    {
      "Cisco MDS 9148S Switch": "Typical Case",
      "AC Power (Volt)": "220",
      "AC Power (Watt)": "125.08"
    },
    {
      "Cisco MDS 9148S Switch": "",
      "AC Power (Volt)": "110",
      "AC Power (Watt)": "127.72"
    },
    {
      "Cisco MDS 9148S Switch": "50C/NV",
      "AC Power (Volt)": "220",
      "AC Power (Watt)": "144.8"
    },
    {
      "Cisco MDS 9148S Switch": "",
      "AC Power (Volt)": "110",
      "AC Power (Watt)": "145.87"
    },
    {
      "Cisco MDS 9148S Switch": "50C/HV",
      "AC Power (Volt)": "220",
      "AC Power (Watt)": "155.3"
    },
    {
      "Cisco MDS 9148S Switch": "",
      "AC Power (Volt)": "110",
      "AC Power (Watt)": "158.48"
    },
    {
      "Cisco MDS 9148S Switch": "Worst Case",
      "AC Power (Volt)": "220",
      "AC Power (Watt)": "183.11"
    },
    {
      "Cisco MDS 9148S Switch": "",
      "AC Power (Volt)": "110",
      "AC Power (Watt)": "187.66"
    }
  ],
  "source": "docling"
}
```

```json
{
  "page": 61,
  "table_index": 18,
  "headers": [
    "AC Input Power Supply",
    "Specification"
  ],
  "rows": [
    {
      "AC Input Power Supply": "Power supply output capacity",
      "Specification": "300W"
    },
    {
      "AC Input Power Supply": "Power supply output voltage",
      "Specification": "12 V +/- 6% up to 25 A"
    },
    {
      "AC Input Power Supply": "Output holdup time",
      "Specification": "20ms when input > 100 VAC"
    }
  ],
  "source": "docling"
}
```


<!-- page: 62 -->
**Chapter1 Technical Specifications
SFP Transceiver Specifications**

**The environment (temperature) outside the chassis (cid:129)
Internal chassis temperature (cid:129)
Any hardware component failure in the chassis (cid:129)
Average switching traffic levels (cid:129)**

**Table1-6 Power Requirements and Heat Dissipation for the Cisco MDS 9148S Switch**

**220 VAC
(amps)
0.65**

## Connection Guidelines for AC-Powered Systems

For connecting the Cisco MDS 9148S switch AC power supplies to the site power source, follow these
basic guidelines:
Each power supply should have its own dedicated branch circuit. (cid:129)
For international, circuits should be sized according to local and national codes. (cid:129)
The AC power receptacles used to plug in the chassis must be the grounding type. The grounding (cid:129)
conductors that connect to the receptacles should connect to protective earth ground at the service
equipment.

# SFP Transceiver Specifications

The Cisco MDS 9148S switch is compatible with SFP transceivers and cables that have LC connectors.
Each transceiver must match the transceiver on the other end of the cable in terms of wavelength, and
the cable must not exceed the stipulated cable length for reliable communications.
Cisco SFP transceivers provide the uplink interfaces, laser transmit (TX), and laser receive (RX), and
they support 850 to 1610 nm nominal wavelengths, depending upon the transceiver.
Use only Cisco SFP transceivers on the Cisco MDS 9148S switch. Each Cisco SFP transceiver is
encoded with model information that enables the switch to verify that the SFP transceiver meets the
requirements for the switch. For the list of supported SFP transceivers, see the release notes.
Use only genuine Cisco SFP+ transceivers in Cisco MDS series switches. Each Cisco SFP+ transceiver
is encoded with serial number, vendor name, and other parameters that enable Cisco NX-OS to verify
that the transceiver meets the requirements of the switch. If discrepancies are found, the SFP+ will be
allowed to function, if possible, but will cause a warning syslog message to be generated. Cisco TAC
does not support switch ports populated with non-Cisco SFP+ transceivers.
For details of SFP transceivers see the data sheet at the following location:
http://www.cisco.com/en/US/prod/collateral/ps4159/ps6409/ps4358/product_data_sheet09186a00801b
c698.html
This section provides the following information:
Cisco Fibre Channel SFP+ Transceivers, page1-57 (cid:129)

```json
{
  "page": 62,
  "table_index": 21,
  "headers": [
    "Module Type / Product Number",
    "Power Required (watts)",
    "Heat Dissipation (BTU/hr)",
    "Input Current.85 VAC (amps)",
    "Input Current.110 VAC (amps)",
    "Input Current.220 VAC (amps)"
  ],
  "rows": [
    {
      "Module Type / Product Number": "Cisco MDS 9148S16G Multilayer Fabric Switch",
      "Power Required (watts)": "140 maximum",
      "Heat Dissipation (BTU/hr)": "478",
      "Input Current.85 VAC (amps)": "1.68",
      "Input Current.110 VAC (amps)": "1.28",
      "Input Current.220 VAC (amps)": "0.65"
    }
  ],
  "source": "docling"
}
```


<!-- page: 63 -->
Optical Specifications for Cisco CWDM SFP Transceivers, page1-61 (cid:129)
Regulatory Compliance and For information about safety, regulatory, and standards compliance, see the
Safety Information for the Cisco MDS 9000 Family .

## Cisco Fibre Channel SFP+ Transceivers

Table1-7 lists the Fibre Channel SFP+ transceivers available through Cisco Systems for the
CiscoMDS9148S switch.

**Table1-7 Cisco Fibre Channel SFP + Transceivers for the CiscoMDS9148S Switch**

**Part Number
DS-SFP-FC16G-SW**

DS-SFP-FC16G-LW

DS-SFP-FC8G-SW

DS-SFP-FC8G-LW

DS-SFP-FC8G-ER

DS-CWDM8Gxxxx

### General Specifications for Cisco Fibre Channel 16 Gbps SFP+ Transceivers

Table1-8 summarizes cabling specifications for 16 Gbps.

```json
{
  "page": 63,
  "table_index": 22,
  "headers": [
    "Part Number",
    "Description",
    "Type"
  ],
  "rows": [
    {
      "Part Number": "DS-SFP-FC16G-SW",
      "Description": "Cisco MDS 4/8/16-Gbps Fibre Channel SW SFP+, LC",
      "Type": "Short wavelength"
    },
    {
      "Part Number": "DS-SFP-FC16G-LW",
      "Description": "Cisco MDS 4/8/16-Gbps Fibre Channel LW SFP+, LC",
      "Type": "Long wavelength"
    },
    {
      "Part Number": "DS-SFP-FC8G-SW",
      "Description": "Cisco MDS 2/4/8-Gbps Fibre Channel SW SFP+, LC",
      "Type": "Short wavelength"
    },
    {
      "Part Number": "DS-SFP-FC8G-LW",
      "Description": "Cisco MDS 2/4/8-Gbps Fibre Channel LW SFP+, LC",
      "Type": "Long wavelength"
    },
    {
      "Part Number": "DS-SFP-FC8G-ER",
      "Description": "Cisco MDS 2/4/8-Gbps Fibre Channel Extended Reach SFP+, LC",
      "Type": "Extended Reach"
    },
    {
      "Part Number": "DS-CWDM8Gxxxx",
      "Description": "Cisco MDS 2/4/8-Gbps CWDM Long Distance SFP, LC",
      "Type": "Long Distance"
    }
  ],
  "source": "docling"
}
```


<!-- page: 64 -->
**Table1-8 Cisco 16-Gbps Fibre Channel SFP+ Cabling Specifications**

**Cable Distance**

15 m (49 ft) (OM1)
35 m (115 ft) (OM2)
100 m (328 ft)
(OM3)
125 m (410 ft)
(OM4)
21 m (69 ft) (OM1)
50 m (164 ft) (OM2)
150 m (492 ft)
(OM3)
190 m (623 ft)
(OM4)
70 m (230 ft) (OM1)
150 m (492 ft)
(OM2)
380 m (1247 ft)
(OM3)
400 m (1312 ft)
(OM4)
10 km (6.2 mi)
10 km (6.2 mi)
10 km (6.2 mi)

```json
{
  "page": 64,
  "table_index": 23,
  "headers": [
    "SFP+",
    "Wavelength (nanometers)",
    "Fiber Type",
    "Core Size (microns)",
    "Baud Rate",
    "Cable Distance"
  ],
  "rows": [
    {
      "SFP+": "DS-SFP-FC16G-S W",
      "Wavelength (nanometers)": "850",
      "Fiber Type": "MMF",
      "Core Size (microns)": "62.5 50.0 50.0 50.0 62.5 50.0 50.0 50.0 62.5 50.0 50.0 50.",
      "Baud Rate": "(GBd) 14.025 14.025 14.025 14.025 8.5 8.5 8.5 8.5 4.25 4.25 4.25 4.25",
      "Cable Distance": "15 m (49 ft) (OM1) 35 m(115 ft) (OM2) 100 m (328 ft) (OM3) 125 m (410 ft) (OM4) 21 m (69 ft) (OM1) 50 m(164 ft) (OM2) 150 m (492 ft) (OM3) 190 m (623 ft) (OM4) 70 m(230 ft) (OM1) 150 m (492 ft) (OM2) 380 m (1247 ft) (OM3) 400 m (1312 ft) (OM4)"
    },
    {
      "SFP+": "DS-SFP-FC16G-L W",
      "Wavelength (nanometers)": "1310",
      "Fiber Type": "SMF",
      "Core Size (microns)": "9.0 9.0 9.0",
      "Baud Rate": "14.025 8.5 4.25",
      "Cable Distance": "10 km (6.2 mi) 10 km (6.2 mi) 10 km (6.2 mi)"
    }
  ],
  "source": "docling"
}
```


<!-- page: 65 -->
```json
{
  "page": 65,
  "table_index": 25,
  "headers": [
    "SFP+.",
    "Operating.Max",
    "Operating.Min",
    "Storage.Max",
    "Storage.Min"
  ],
  "rows": [
    {
      "SFP+.": "DS-SFP-FC16G-SW",
      "Operating.Max": "40°C",
      "Operating.Min": "0°C",
      "Storage.Max": "85°C",
      "Storage.Min": "-40°C"
    },
    {
      "SFP+.": "DS-SFP-FC16G-LW",
      "Operating.Max": "40°C",
      "Operating.Min": "0°C",
      "Storage.Max": "85°C",
      "Storage.Min": "-40°C"
    }
  ],
  "source": "docling"
}
```

```json
{
  "page": 65,
  "table_index": 24,
  "headers": [
    "SFP+.",
    "Average Transmit Power (dBm).Max",
    "Average Transmit Power (dBm).Min",
    "Average Receive Power (dBm).Max",
    "Average Receive Power (dBm).Min",
    "Fiber Loss Budget (dB).62.5 microns [OM1])",
    "Fiber Loss Budget (dB).(50.0 microns [OM2])",
    "Fiber Loss Budget (dB).(50.0 microns [OM3])"
  ],
  "rows": [
    {
      "SFP+.": "DS-SFP-FC16G-SW",
      "Average Transmit Power (dBm).Max": "-1.3",
      "Average Transmit Power (dBm).Min": "7, 8",
      "Average Receive Power (dBm).Max": "0",
      "Average Receive Power (dBm).Min": "-10.3",
      "Fiber Loss Budget (dB).62.5 microns [OM1])": "2.08 (4 Gbps) 1.68 (8 Gbps) 1.63 (16 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM2])": "2.08 (4 Gbps) 1.68 (8 Gbps) 1.63 (16 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM3])": "2.88 (4 Gbps) 2.04 (8 Gbps) 1.86 (16 Gbps)"
    },
    {
      "SFP+.": "DS-SFP-FC16G-LW",
      "Average Transmit Power (dBm).Max": "2.0",
      "Average Transmit Power (dBm).Min": "-5.0",
      "Average Receive Power (dBm).Max": "2.0",
      "Average Receive Power (dBm).Min": "10",
      "Fiber Loss Budget (dB).62.5 microns [OM1])": "7.8 (4 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM2])": "7.8 (4 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM3])": "7.8 (4 Gbps)"
    }
  ],
  "source": "docling"
}
```


<!-- page: 66 -->
**Table1-11 Cisco 8-Gbps Fibre Channel SFP+ Cabling Specifications**

150 m (492 ft)
70 m (230 ft)
21 m (69 ft)
300 m (984 ft)
150 m (492 ft)
50 m (164 ft)
500 m (1640 ft)
380 m (1246 ft)
150 m (492 ft)
520 m (1706 ft)
400 m (1312 ft)
190 m (623 ft)
10 km (6.2 mi)
10 km (6.2 mi)
10 km (6.2 mi)
40 km (24.85 mi)
40 km (24.85 mi)
40 km (24.85 mi)

```json
{
  "page": 66,
  "table_index": 26,
  "headers": [
    "SFP+",
    "Wavelength (nanometers)",
    "Fiber Type",
    "Core Size (microns)",
    "Baud Rate (GBd)",
    "Cable Distance"
  ],
  "rows": [
    {
      "SFP+": "DS-SFP-FC8G-SW",
      "Wavelength (nanometers)": "850",
      "Fiber Type": "MMF",
      "Core Size (microns)": "62.5 62.5 62.5 50.0 (OM2) 50.0 (OM2) 50.0 (OM2) 50.0 (OM3) 50.0 (OM3) 50.0 (OM3) 50.0 (OM4) 50.0 (OM4)",
      "Baud Rate (GBd)": "2.125 4.250 8.500 2.125 4.250 8.500 2.125 4.250 8.500 2.125 4.250",
      "Cable Distance": "150 m (492 ft) 70 m (230 ft) 21 m (69 ft) 300 m (984 ft) 150 m (492 ft) 50 m (164 ft) 500 m (1640 ft) 380 m (1246 ft) 150 m (492 ft) 520 m (1706 ft) 400 m (1312 ft)"
    },
    {
      "SFP+": "DS-SFP-FC8G-LW",
      "Wavelength (nanometers)": "1310",
      "Fiber Type": "SMF",
      "Core Size (microns)": "50.0 (OM4) 9.0 9.0",
      "Baud Rate (GBd)": "8.500 2.125 4.250",
      "Cable Distance": "190 m (623 ft) 10 km (6.2 mi) 10 km (6.2 mi)"
    },
    {
      "SFP+": "",
      "Wavelength (nanometers)": "",
      "Fiber Type": "",
      "Core Size (microns)": "9.0 9.0",
      "Baud Rate (GBd)": "8.500",
      "Cable Distance": "10 km (6.2 mi)"
    },
    {
      "SFP+": "DS-SFP-FC8G-ER",
      "Wavelength (nanometers)": "1550",
      "Fiber Type": "SMF",
      "Core Size (microns)": "9.0 9.0",
      "Baud Rate (GBd)": "2.125 4.250 8.500",
      "Cable Distance": "40 km (24.85 mi) 40 km (24.85 mi) 40 km (24.85 mi)"
    }
  ],
  "source": "docling"
}
```


<!-- page: 67 -->
```json
{
  "page": 67,
  "table_index": 28,
  "headers": [
    "SFP+.",
    "Operating.Max",
    "Operating.Min",
    "Storage.Max",
    "Storage.Min"
  ],
  "rows": [
    {
      "SFP+.": "DS-SFP-FC16G-SW",
      "Operating.Max": "40°C",
      "Operating.Min": "0°C",
      "Storage.Max": "85°C",
      "Storage.Min": "-40°C"
    },
    {
      "SFP+.": "DS-SFP-FC16G-LW",
      "Operating.Max": "40°C",
      "Operating.Min": "0°C",
      "Storage.Max": "85°C",
      "Storage.Min": "-40°C"
    }
  ],
  "source": "docling"
}
```

```json
{
  "page": 67,
  "table_index": 27,
  "headers": [
    "SFP+.",
    "Average TransmitPower (dBm).Max",
    "Average TransmitPower (dBm).Min",
    "Average Receive Power (dBm).Max",
    "Average Receive Power (dBm).Min",
    "Fiber Loss Budget (dB).62.5 microns [OM1])",
    "Fiber Loss Budget (dB).(50.0 microns [OM2])",
    "Fiber Loss Budget (dB).(50.0 microns [OM3])"
  ],
  "rows": [
    {
      "SFP+.": "DS-SFP-FC8G-SW",
      "Average TransmitPower (dBm).Max": "-1.3",
      "Average TransmitPower (dBm).Min": "-10 (2 Gbps) -9 (4 Gbps) -8.2 (8 Gbps)",
      "Average Receive Power (dBm).Max": "0",
      "Average Receive Power (dBm).Min": "-",
      "Fiber Loss Budget (dB).62.5 microns [OM1])": "2.10 (2 Gbps) 1.78 (4 Gbps) 1.58 (8 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM2])": "2.08 (4 Gbps) 1.68 (8 Gbps) 1.63 (16 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM3])": "3.31 (2 Gbps) 2.88 (4 Gbps) 2.04 (8 Gbps"
    },
    {
      "SFP+.": "DS-SFP-FC8 G-LW",
      "Average TransmitPower (dBm).Max": "-3 (2 Gbps) -1 (4 Gbps) 0.5 (8 Gbps)",
      "Average TransmitPower (dBm).Min": "-11.7 (2 Gbps) -8.4 (4 Gbps) -8.4 (8 Gbps",
      "Average Receive Power (dBm).Max": "-3 (2 Gbps) -1 (4 Gbps) 0.5 (8 Gbps)",
      "Average Receive Power (dBm).Min": "-",
      "Fiber Loss Budget (dB).62.5 microns [OM1])": "-7.8 (2 Gbps) 7.8 (4 Gbps) 6.4 (8 Gbps)",
      "Fiber Loss Budget (dB).(50.0 microns [OM2])": "",
      "Fiber Loss Budget (dB).(50.0 microns [OM3])": ""
    },
    {
      "SFP+.": "DS-SFP-FC8G-ER",
      "Average TransmitPower (dBm).Max": "4",
      "Average TransmitPower (dBm).Min": "-4.7",
      "Average Receive Power (dBm).Max": "-1",
      "Average Receive Power (dBm).Min": "-",
      "Fiber Loss Budget (dB).62.5 microns [OM1])": "",
      "Fiber Loss Budget (dB).(50.0 microns [OM2])": "10.9",
      "Fiber Loss Budget (dB).(50.0 microns [OM3])": ""
    }
  ],
  "source": "docling"
}
```


<!-- page: 68 -->
```json
{
  "page": 68,
  "table_index": 29,
  "headers": [
    "Parameter",
    "Symbol",
    "Min.",
    "Typical",
    "Max.",
    "Units",
    "Notes"
  ],
  "rows": [
    {
      "Parameter": "Transmitter central wavelength",
      "Symbol": " c",
      "Min.": "(x-4)",
      "Typical": "(x+1)",
      "Max.": "(x+7)",
      "Units": "nm",
      "Notes": "Available center wavelengths: 1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610 nm"
    },
    {
      "Parameter": "Wavelength temperature dependence",
      "Symbol": "",
      "Min.": "",
      "Typical": "0.08",
      "Max.": "0.1",
      "Units": "nm/° C",
      "Notes": ""
    },
    {
      "Parameter": "Side-mode suppression ratio",
      "Symbol": "SMSR",
      "Min.": "30",
      "Typical": "",
      "Max.": "",
      "Units": "dB",
      "Notes": ""
    },
    {
      "Parameter": "Transmitter optical output power",
      "Symbol": "P out",
      "Min.": "0.0",
      "Typical": "",
      "Max.": "5.0",
      "Units": "dBm",
      "Notes": "Averagepower coupled into single-mode fiber"
    },
    {
      "Parameter": "Receiver optical input power (BER <10 -12 with PRBS 2 -7 -1)",
      "Symbol": "P in",
      "Min.": "-28.0",
      "Typical": "",
      "Max.": "-7.0",
      "Units": "dBm",
      "Notes": "@2.12 Gbps, 140°F (60°C) case temp."
    },
    {
      "Parameter": "Receiver optical input wavelength",
      "Symbol": " in",
      "Min.": "1450",
      "Typical": "",
      "Max.": "1620",
      "Units": "Nm",
      "Notes": ""
    },
    {
      "Parameter": "Transmitter extinction ratio",
      "Symbol": "OMI",
      "Min.": "9",
      "Typical": "",
      "Max.": "",
      "Units": "dB",
      "Notes": ""
    },
    {
      "Parameter": "Dispersion penalty at 60 km",
      "Symbol": "",
      "Min.": "",
      "Typical": "",
      "Max.": "2",
      "Units": "dB",
      "Notes": ""
    },
    {
      "Parameter": "Dispersion penalty at 100 km",
      "Symbol": "",
      "Min.": "",
      "Typical": "",
      "Max.": "2",
      "Units": "db",
      "Notes": "@1.25 Gbps"
    },
    {
      "Parameter": "Dispersion penalty at 100 km",
      "Symbol": "",
      "Min.": "",
      "Typical": "",
      "Max.": "3",
      "Units": "dB",
      "Notes": "@2.12 Gbps"
    }
  ],
  "source": "docling"
}
```


<!-- page: 69 -->
![General Specifications for Cisco Fibre Channel 16](images/image_p69_00.png)


<!-- page: 70 -->
# Console Port

The console port is an asynchronous RS-232 serial port with an RJ-45 connector. You can use the
RJ-45toRJ-45 rollover cable and the RJ-45 to DB-9 female adapter or the RJ-45toDB-25 female DTE
adapter (depending on your computer serial port) to connect the console port to a computer running
terminal emulation software.

## Console Port Pinouts

Table1-1 lists the pinouts for the console port on the Cisco MDS 9148S Switch.

**Table1-1 Console Port Pinouts**

```json
{
  "page": 70,
  "table_index": 31,
  "headers": [
    "Console Port.Signal",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1",
    "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin",
    "Console Device.Signal"
  ],
  "rows": [
    {
      "Console Port.Signal": "RTS",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "1",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "8",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "5",
      "Console Device.Signal": "CTS"
    },
    {
      "Console Port.Signal": "DTR",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "2",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "7",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "6",
      "Console Device.Signal": "DSR"
    },
    {
      "Console Port.Signal": "TxD",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "3",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "6",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "3",
      "Console Device.Signal": "RxD"
    },
    {
      "Console Port.Signal": "GND",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "4",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "5",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "7",
      "Console Device.Signal": "GND"
    },
    {
      "Console Port.Signal": "GND",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "5",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "4",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "7",
      "Console Device.Signal": "GND"
    },
    {
      "Console Port.Signal": "RxD",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "6",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "3",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "2",
      "Console Device.Signal": "TxD"
    }
  ],
  "source": "docling"
}
```

**Pin Signal
1 1 RTS
2 DTR
3 TxD
4 GND
5 GND
6 RxD
7 DSR
8 CTS**

1. Pin 1 is connected internally to pin 8.

## Connecting the Console Port to a Computer Using the DB-25 Adapter

You can use the RJ-45toRJ-45 rollover cable and RJ-45toDB-25 female DTE adapter (labeled
“Terminal”) to connect the console port to a computer running terminal emulation software. Table1-2
lists the pinouts for the console port, the RJ-45toRJ-45 rollover cable, and the RJ-45toDB-25 female
DTE adapter.

**Table1-2 Port Mode Signaling and Pinouts with DB-25 Adapter**

```json
{
  "page": 70,
  "table_index": 30,
  "headers": [
    "Pin",
    "Signal"
  ],
  "rows": [
    {
      "Pin": "1 1",
      "Signal": "RTS"
    },
    {
      "Pin": "2",
      "Signal": "DTR"
    },
    {
      "Pin": "3",
      "Signal": "TxD"
    },
    {
      "Pin": "4",
      "Signal": "GND"
    },
    {
      "Pin": "5",
      "Signal": "GND"
    },
    {
      "Pin": "6",
      "Signal": "RxD"
    },
    {
      "Pin": "7",
      "Signal": "DSR"
    },
    {
      "Pin": "8",
      "Signal": "CTS"
    }
  ],
  "source": "docling"
}
```

**Console
Console Port Device
Signal Signal
RTS CTS
DTR DSR
TxD RxD
GND GND
GND GND
RxD TxD**


<!-- page: 71 -->
**Chapter1 Cable and Port Specifications
MGMT 10/100 Ethernet Port**

**Table1-2 Port Mode Signaling and Pinouts with DB-25 Adapter (continued)**

**Console
Console Port Device
Signal Signal
DSR DTR
CTS RTS**

## Connecting the Console Port to a Computer Using the DB-9 Adapter

You can use the RJ-45toRJ-45 rollover cable and RJ-45toDB-9 female DTE adapter (labeled
“Terminal”) to connect the console port to a computer running terminal emulation software. Table1-3
lists the pinouts for the console port, the RJ-45toRJ-45 rollover cable, and the RJ-45toDB-9 female
DTE adapter.

**Table1-3 Port Mode Signaling and Pinouts with DB-9 Adapter**

**Console
Console Port Device
Signal Signal
RTS CTS
DTR DSR
TxD RxD
GND GND
GND GND
RxD TxD
DSR DTR
CTS RTS**

```json
{
  "page": 71,
  "table_index": 33,
  "headers": [
    "Console Port.Signal",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin",
    "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin",
    "Console Device.Signal"
  ],
  "rows": [
    {
      "Console Port.Signal": "RTS",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "1",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "8",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "8",
      "Console Device.Signal": "CTS"
    },
    {
      "Console Port.Signal": "DTR",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "2",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "7",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "6",
      "Console Device.Signal": "DSR"
    },
    {
      "Console Port.Signal": "TxD",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "3",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "6",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "2",
      "Console Device.Signal": "RxD"
    },
    {
      "Console Port.Signal": "GND",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "4",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "5",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "5",
      "Console Device.Signal": "GND"
    },
    {
      "Console Port.Signal": "GND",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "5",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "4",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "5",
      "Console Device.Signal": "GND"
    },
    {
      "Console Port.Signal": "RxD",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "6",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "3",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "3",
      "Console Device.Signal": "TxD"
    },
    {
      "Console Port.Signal": "DSR",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "7",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "2",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "4",
      "Console Device.Signal": "DTR"
    },
    {
      "Console Port.Signal": "CTS",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pins": "8",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "1",
      "RJ-45 to DB-9 Terminal Adapter.DB-9 Pin": "7",
      "Console Device.Signal": "RTS"
    }
  ],
  "source": "docling"
}
```

# MGMT 10/100 Ethernet Port

Use a modular, RJ-45, straight-through UTP cable to connect the 10/100 management Ethernet port to
external hubs and switches. To connect to a router, use a crossover cable. (See Figure1-1.)

**Figure1-1 RJ-45 Interface Cable Connector**

![MGMT 10/100 Ethernet Port](images/image_p71_00.png)

RJ-45 (both ends)

```json
{
  "page": 71,
  "table_index": 32,
  "headers": [
    "Console Port.Signal",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin",
    "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1",
    "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin",
    "Console Device.Signal"
  ],
  "rows": [
    {
      "Console Port.Signal": "DSR",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "7",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "2",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "20",
      "Console Device.Signal": "DTR"
    },
    {
      "Console Port.Signal": "CTS",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin": "8",
      "RJ-45 to RJ-45 Rollover Cable.RJ-45 Pin_1": "1",
      "RJ-45 to DB-25 Terminal Adapter.DB-25 Pin": "4",
      "Console Device.Signal": "RTS"
    }
  ],
  "source": "docling"
}
```


<!-- page: 72 -->
**Chapter1 Cable and Port Specifications
Supported Power Cords and Plugs**

Table1-4 lists the connector pinouts and signal names for a 10/100BASE-T management port (MDI)

![Table1-4 lists the connector pinouts](images/image_p72_00.png)

```json
{
  "page": 72,
  "table_index": 34,
  "headers": [
    "Pin",
    "Signal"
  ],
  "rows": [
    {
      "Pin": "1",
      "Signal": "TD+"
    },
    {
      "Pin": "2",
      "Signal": "TD-"
    },
    {
      "Pin": "3",
      "Signal": "RD+"
    },
    {
      "Pin": "6",
      "Signal": "RD-"
    },
    {
      "Pin": "4",
      "Signal": "Not used"
    },
    {
      "Pin": "5",
      "Signal": "Not used"
    },
    {
      "Pin": "7",
      "Signal": "Not used"
    },
    {
      "Pin": "8",
      "Signal": "Not used"
    }
  ],
  "source": "docling"
}
```


<!-- page: 73 -->
![Table1-4 lists the connector pinouts](images/image_p73_00.png)

![Table1-4 lists the connector pinouts](images/image_p73_01.png)

![Table1-4 lists the connector pinouts](images/image_p73_02.png)

![Table1-4 lists the connector pinouts](images/image_p73_03.png)

![Table1-4 lists the connector pinouts](images/image_p73_04.png)

```json
{
  "page": 73,
  "table_index": 35,
  "headers": [
    "Locale",
    "Power Cord Part Number",
    "Source Plug Type",
    "Cordset Rating",
    "Length in Meters",
    "Power Plug Reference Illustration"
  ],
  "rows": [
    {
      "Locale": "Argentina",
      "Power Cord Part Number": "CAB-9K10A- AR",
      "Source Plug Type": "IRAM 2073 plug (10 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "North America",
      "Power Cord Part Number": "CAB-9K12A- NA",
      "Source Plug Type": "NEMA 5-15P plug (15 A)",
      "Cordset Rating": "15 A, 125 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Australia and New Zealand",
      "Power Cord Part Number": "CAB-9K10A- AU",
      "Source Plug Type": "SAA/3 plug, AS/NZS 3112-1993 (10 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Europe",
      "Power Cord Part Number": "CAB-9K10A-E U",
      "Source Plug Type": "VIIG Plug, CEE (7) VII (16 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Italy",
      "Power Cord Part Number": "CAB-9K10A-I T",
      "Source Plug Type": "1/3G plug, CEI 23-16 (10 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "United Kingdom",
      "Power Cord Part Number": "CAB-9K10A- UK",
      "Source Plug Type": "BS89/13, BS 1363/A (13 A; replaceable fuse)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    }
  ],
  "source": "docling"
}
```

![Table1-4 lists the connector pinouts](images/image_p73_05.png)


<!-- page: 74 -->
**Table1-5 Supported Power Cords and Power Plugs for the CiscoMDS 9100 Series**

![Table1-5 Supported Power Cords](images/image_p74_00.png)

![Table1-5 Supported Power Cords](images/image_p74_01.png)

## Jumper Power Cord

Figure1-3 shows the C14 and C15 connectors on the optional jumper power cord for the
CiscoMDS9148S Switch. The C15 connector connects into the C14 inlet on the CiscoMDS9148S
Switch power supply, while the C14 connector connects into the C13 receptacle of a power distribution
unit for a cabinet.

```json
{
  "page": 74,
  "table_index": 36,
  "headers": [
    "Locale",
    "Power Cord Part Number",
    "Source Plug Type",
    "Cordset Rating",
    "Length in Meters",
    "Power Plug Reference Illustration"
  ],
  "rows": [
    {
      "Locale": "South Africa",
      "Power Cord Part Number": "CAB-9K10A-S A",
      "Source Plug Type": "EL 208, SABS 164-1 (10 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "1.82",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Switzerland",
      "Power Cord Part Number": "CAB-9K10A-S W",
      "Source Plug Type": "12G SEV 1011 (10 A)",
      "Cordset Rating": "10 A, 250 V",
      "Length in Meters": "2.5",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Japan",
      "Power Cord Part Number": "CAB-C15-CB N-JP",
      "Source Plug Type": "C14-C15",
      "Cordset Rating": "12 A, 250 VAC",
      "Length in Meters": "3.05",
      "Power Plug Reference Illustration": ""
    },
    {
      "Locale": "Cabinet Jumper Power Cord",
      "Power Cord Part Number": "CAB-C19-CB N",
      "Source Plug Type": "C 20-C19",
      "Cordset Rating": "16 A 250 VAC",
      "Length in Meters": "2.74",
      "Power Plug Reference Illustration": ""
    }
  ],
  "source": "docling"
}
```


<!-- page: 75 -->
**Figure1-3 Connectors on Jumper Power Cord for CiscoMDS 9148S Switch**

![Jumper Power Cord](images/image_p75_00.png)

![Figure1-3 Connectors on Jumper Power Cord for](images/image_p75_01.png)

5
6
1
3
1
1 C14


<!-- page: 77 -->
![image_p77_00](images/image_p77_00.png)


<!-- page: 78 -->
**Chapter1 Site Planning and Maintenance Records
Site Preparation Checklist**

```json
{
  "page": 78,
  "table_index": 37,
  "headers": [
    "Task No.",
    "Planning Activity",
    "Verified By",
    "Time",
    "Date"
  ],
  "rows": [
    {
      "Task No.": "1",
      "Planning Activity": "Space evaluation: • Space and layout • Floor covering • Impact and vibration • Lighting • Maintenance access",
      "Verified By": "",
      "Time": "",
      "Date": ""
    },
    {
      "Task No.": "2",
      "Planning Activity": "Environmental evaluation: • Ambient temperature • Humidity • Altitude • Atmospheric contamination",
      "Verified By": "",
      "Time": "",
      "Date": ""
    },
    {
      "Task No.": "3",
      "Planning Activity": "Power evaluation: • Input power type • Power receptacles 1 • Receptacle proximity to the equipment • Dedicated circuit for power supply • Dedicated (separate) circuits for redundant power supplies • UPS 2 for power failures",
      "Verified By": "",
      "Time": "",
      "Date": ""
    },
    {
      "Task No.": "4",
      "Planning Activity": "Grounding evaluation: • Circuit breaker size • CO ground (AC- powered systems)",
      "Verified By": "",
      "Time": "",
      "Date": ""
    },
    {
      "Task No.": "5",
      "Planning Activity": "Cable and interface equipment evaluation: • Cable type • Connector type • Cable distance limitations • Interface equipment (transceivers)",
      "Verified By": "",
      "Time": "",
      "Date": ""
    },
    {
      "Task No.": "6",
      "Planning Activity": "Electromagnetic interference (EMI) evaluation: • Distance limitations for signaling • Site wiring • RFI 3 levels",
      "Verified By": "",
      "Time": "",
      "Date": ""
    }
  ],
  "source": "docling"
}
```


<!-- page: 79 -->
**Chapter1 Site Planning and Maintenance Records
Contact and Site Information**

# Contact and Site Information

Use the following worksheet to record contact and site information.

**Table1-2 Contact and Site Information**

**Contact person**

**Contact phone**

**Contact E-Mail**

**Building/site name**

**Data center location**

**Floor location**

**Address (line 1)**

**Address (line 2)**

**State**

**Zip code**

**Country**


<!-- page: 80 -->
**Chapter1 Site Planning and Maintenance Records
Chassis and Network Information**

# Chassis and Network Information

Use the following worksheets to record chassis and network information.

**Contract Number ______________________________________________________________**

**Chassis Serial Number______________________________________________________________**

**Product Number ______________________________________________________________**

**Table1-3 Network-Related Information**

**Switch IP address**

**Switch IP netmask**

**Host name**

**Domain name**

**IP broadcast address**

**Gateway/router address**

**DNS address**

**Modem telephone number**
