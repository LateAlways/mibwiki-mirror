# instructions

(p)ACC Activation Instructions:

1. Flash the "X" firmware first. Before flashing, there must be a static fault with component protection enabled.
2. After flashing the "X" firmware, go to the KS master station and and remove component protection.
3. Find the activation code for transmitting SWAP, put it with the right FEC from list below in the activation tool and generate the offline SWAP.
4. Load the SWAP file into control unit 13.
5. After the activation is successful, refresh the ACC with last firmnware index and write the correct dataset parameters.
6. Do coding...

FEC list:
10009001	MRR-Paket 1: ACClow (Basis-ACC) + FrontAssist inkl. CityANB
10009002	MRR-Paket 2: ACClow (ACC FTS) + FrontAssist inkl. CityANB 
10009003	MRR-Paket 3: ACClow (ACC S&G) + FrontAssist inkl. CityANB 
10009004	MRR-Paket 4: FrontAssist inkl. CityANB (ohne ACC) 
10009005	MRR-Paket 5: CityANB (ohne ACC) 
10009006	MRR-Paket 6: ACChigh (Basis-ACC) + FrontAssist inkl. CityANB 
10009007	MRR-Paket 7: ACChigh (ACC FTS) + FrontAssist inkl. CityANB 
10009008	MRR-Paket 8: ACChigh (ACC S&G) + FrontAssist inkl. CityANB 
10009101	ACC-Funktionserweiterungs-Paket "predictiveACC" 
10009102	ACC-Funktionserweiterungs-Paket "StauAssistent" 
10009103	ACC-Funktionserweiterungs-Paket "predictiveACC&StauAssistent" 
10009201	AWV-Auspraegung "AWV1,2 - Warnung nur visuell&auditiv" 
10009202	AWV-Auspraegung "AWV1,2" 
10009203	AWV-Auspraegung "AWV1,2,3" 
10009204	AWV-Auspraegung "AWV1,2,3, vFGS 
10009205	AWV-Auspraegung „AWV1,2,3, vFGS, vRFS"
10009301	AWV-Funktionserweiterungs-Paket "Elektronische Parkbremse"
10009301	AWV-Funktionserweiterungs-Paket "EmergencyAssist" 
10009302	AWV-Funktionserweiterungs-Paket "Abbiegeassistent" 
10009303	AWV-Funktionserweiterungs-Paket "AWV-Gegenverkehr" 
10009304	AWV-Funktionserweiterungs-Paket "Abbiegeassistent&AWV-Gegenverkehr" 
10009305	AWV-Funktionserweiterungs-Paket "EmergencyAssist&AWV-Gegenverkehr" 
10009306	AWV-Funktionserweiterungs-Paket "EmergencyAssist&Abbiegeassistent" 
10009307	AWV-Funktionserweiterungs-Paket "EmergencyAssist&Abbiegeassistent&AWV-Gegenverkehr" 
10009500	Verkehrszeichenerkennung (VZE)
10009600	Vorrausschauender Fussgaengerschutz (VFS) - FCWP