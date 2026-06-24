# Workflows ÔÇö Wireless Penetration Testing

## Attack Flow
```
Monitor Mode Activation
    Ôöé
    Ôö£ÔöÇÔöÇ Passive Reconnaissance
    Ôöé   Ôö£ÔöÇÔöÇ SSID/BSSID discovery
    Ôöé   Ôö£ÔöÇÔöÇ Client enumeration
    Ôöé   ÔööÔöÇÔöÇ Channel mapping
    Ôöé
    Ôö£ÔöÇÔöÇ WPA2-PSK Attacks
    Ôöé   Ôö£ÔöÇÔöÇ Handshake capture (deauth + capture)
    Ôöé   Ôö£ÔöÇÔöÇ PMKID attack (clientless)
    Ôöé   ÔööÔöÇÔöÇ Offline cracking (Hashcat/Aircrack)
    Ôöé
    Ôö£ÔöÇÔöÇ WPA2-Enterprise Attacks
    Ôöé   Ôö£ÔöÇÔöÇ Rogue AP (hostapd-mana)
    Ôöé   Ôö£ÔöÇÔöÇ EAP credential capture
    Ôöé   ÔööÔöÇÔöÇ MSCHAP hash cracking
    Ôöé
    Ôö£ÔöÇÔöÇ Evil Twin / Captive Portal
    Ôöé   Ôö£ÔöÇÔöÇ Clone SSID
    Ôöé   Ôö£ÔöÇÔöÇ Deauth real AP
    Ôöé   ÔööÔöÇÔöÇ Credential harvest
    Ôöé
    ÔööÔöÇÔöÇ Segmentation Testing
        Ôö£ÔöÇÔöÇ Client isolation
        Ôö£ÔöÇÔöÇ VLAN traversal
        ÔööÔöÇÔöÇ Corporate network reach
```
