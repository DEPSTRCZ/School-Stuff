
# 0. Stažení iso souboru
## 0.1 Stažení
1. Půjdeme na stránku https://archlinux.org/download/
2. Vybereme nejbližší mirror
3. Stáhneme [archlinux-2023.03.01-x86_64.iso](https://mirror.dkm.cz/archlinux/iso/2023.03.01/archlinux-2023.03.01-x86_64.iso)
![[0.gif]]


# 1. Tvorba VMware virtálního prostředí!
## 1.1 Stáhnutí programu WMware Workstation Player
1. Půjdeme na stránku [WMware.com](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1701&productId=1377&rPId=100675)
2. Stáhneme edici programu pro náš systém
![[1,1.gif]]

## 1.2 Instalace Programu WMware Workstation Player
1. Otevřeme stažený soubor
2. Na další straně si přečteme podmínky
3. Potvrdíme že jsme si přečtli licenční podmínky
4. Projedeme instalací.. Není potřeba nic měnit všude pouze "`Next`"
5. A dokončíme instalaci programu
![[1,2.gif]]

## 1.3 Tvorba Virtálního počítače
1. Zapneme program
2. Klikneme na "`Create a New Virtual Mechine`"
3. Vybereme "`Installer disc image file (iso)`"
5. Najdeme a vybereme `archlinux-2023.03.01-x86_64.iso`
7. Na další stránce vybereme "`Linux`""
8. Ve "Version" vybereme "`Other Linux 5.x kernel 64-bit`"
10. Na další stránce pojmenujeme náš virtuální počítač
12. Vybereme kam jej chceme uložit
14. Na další stránce zadáme maximální veliksot disku (Nejméně 50GB)
15. Vybereme "`Store virtual disk as single file`" pro lepší přenášení
16. Na další stránce změníme Hardware
**Doporučuji:**
- Ram: Více jak 2Gb
- Processors: 2. Minimálně pro lepší zážitek více pokud je to možné
- Virtualization engine: Pokud je možné zapněte
- Network Adapter: Nejlépe NAT, záleží na vás
17. Klikneme "`Finish`"
