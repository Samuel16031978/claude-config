---
name: detecting-credential-dumping-techniques
description: Detect LSASS credential dumping, SAM database extraction, and NTDS.dit theft using Sysmon Event ID 10, Windows Security logs, and SIEM correlation rules
domain: cybersecurity
subdomain: threat-detection
tags:
  - credential-dumping
  - lsass
  - mimikatz
  - sysmon
  - active-directory
  - windows-security
  - defense-evasion
version: "1.0"
author: mahipal
license: Apache-2.0
language: es
---

# Detecci├│n de T├®cnicas de Volcado de Credenciales

## Descripci├│n General

El volcado de credenciales (MITRE ATT&CK T1003) es una t├®cnica de post-explotaci├│n donde los adversarios extraen credenciales de autenticaci├│n de la memoria del sistema operativo, hives del registro o bases de datos del controlador de dominio. Esta habilidad cubre la detecci├│n de acceso a la memoria de LSASS mediante Sysmon Event ID 10 (ProcessAccess), la exportaci├│n del hive del registro SAM mediante reg.exe, la extracci├│n de NTDS.dit mediante ntdsutil/vssadmin, y el abuso de MiniDump con comsvcs.dll. Las reglas de detecci├│n analizan bitmasks de GrantedAccess, procesos invocantes sospechosos y firmas de herramientas conocidas.

## Requisitos Previos

- Sysmon v14+ desplegado con registro de ProcessAccess (Event ID 10) para lsass.exe
- Pol├¡tica de auditor├¡a de seguridad de Windows habilitando la creaci├│n de procesos (Event ID 4688) con registro de l├¡nea de comandos
- SIEM Splunk o Elastic ingiriendo registros de Sysmon y de seguridad de Windows
- Python 3.8+ para an├ílisis de registros

## Pasos

1. Configurar Sysmon para registrar eventos ProcessAccess dirigidos a lsass.exe
2. Reenviar Sysmon Event ID 10 y Windows Event ID 4688 al SIEM
3. Crear reglas de detecci├│n para patrones de GrantedAccess conocidos (0x1010, 0x1FFFFF)
4. Detectar MiniDump con comsvcs.dll y procdump.exe apuntando al PID de LSASS
5. Alertar sobre comandos de exportaci├│n de hives SAM/SECURITY/SYSTEM mediante reg.exe
6. Detectar creaci├│n de shadow copy con ntdsutil/vssadmin para robo de NTDS.dit
7. Correlacionar detecciones con contexto de usuario/host para puntuaci├│n de riesgo

## Salida Esperada

Informe JSON que contiene indicadores detectados de volcado de credenciales con clasificaci├│n de t├®cnica, calificaciones de severidad, detalles del proceso, mapeo a MITRE ATT&CK, y consultas de detecci├│n para Splunk/Elastic.
