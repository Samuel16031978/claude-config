---
name: performing-memory-forensics-with-volatility3
description: Analyze memory dumps to extract processes, network connections, and malware artifacts using Volatility3.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response]
version: "1.0"
author: mahipal
license: Apache-2.0
language: es
---

# An├ílisis Forense de Memoria con Volatility3

## Descripci├│n General

Volatility3 es el framework l├¡der de c├│digo abierto para an├ílisis forense de memoria. Permite extraer procesos en ejecuci├│n, conexiones de red, m├│dulos cargados, artefactos de malware, credenciales en memoria, y evidencia de actividad maliciosa desde volcados de memoria RAM de sistemas Windows, Linux y macOS.

## Prerrequisitos

- Python 3.8+ con Volatility3 instalado (`pip install volatility3`)
- Volcado de memoria adquirido (formatos: raw, EWF, LiME, VMware .vmem)
- Tablas de s├¡mbolos apropiadas para el SO analizado
- Espacio en disco suficiente (2-3x el tama├▒o del volcado de memoria)

## Conceptos Clave

| Concepto | Descripci├│n |
|----------|-------------|
| **Plugin PsList** | Lista procesos activos con PID, PPID, tiempo de creaci├│n |
| **Plugin NetScan** | Extrae conexiones de red y puertos en escucha |
| **Plugin MalFind** | Detecta inyecci├│n de c├│digo en procesos (secciones PAGE_EXECUTE_READWRITE) |
| **Plugin DllList** | Lista DLLs cargadas por cada proceso |
| **Plugin Handles** | Muestra handles abiertos (archivos, registros, mutex) |
| **Plugin CmdLine** | Extrae l├¡neas de comando de procesos |

## Pasos

1. Identificar el perfil del SO del volcado de memoria
2. Ejecutar `vol -f memory.dmp windows.pslist` para listar procesos
3. Analizar procesos sospechosos con `windows.pstree` para ver jerarqu├¡a
4. Buscar conexiones de red con `windows.netscan`
5. Detectar inyecci├│n de c├│digo con `windows.malfind`
6. Extraer artefactos espec├¡ficos (DLLs, handles, l├¡neas de comando)
7. Correlacionar hallazgos para construir timeline del ataque

## Resultado Esperado

Reporte detallado de hallazgos forenses incluyendo procesos maliciosos identificados, conexiones C2, artefactos de malware extra├¡dos, y timeline de actividad del atacante en el sistema comprometido.
