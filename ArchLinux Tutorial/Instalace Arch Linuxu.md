
# 0. Stažení iso souboru
>Tento soubor se používá k vytvoření bootovatelného média, které umožňuje instalaci operačního systému na nový počítač nebo jeho obnovu.
## 0.1 Stažení
1. Půjdeme na stránku https://archlinux.org/download/
2. Vybereme nejbližší mirror
3. Stáhneme [archlinux-2023.03.01-x86_64.iso](https://mirror.dkm.cz/archlinux/iso/2023.03.01/archlinux-2023.03.01-x86_64.iso)
![[0.gif]]


# 1. Tvorba VMware virtálního prostředí!
>Tvorba virtuálního prostřední / virtálního počítače ve kterém bude Arch Linux běžet
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
14. Na další stránce zadáme maximální veliksot disku (Nejméně 30GB)
15. Vybereme "`Store virtual disk as single file`" pro lepší přenášení
16. Na další stránce změníme Hardware:
**Doporučuji:**
- Ram: Více jak 2Gb
- Processors: 2. Minimálně pro lepší zážitek více pokud je to možné
- Virtualization engine: Pokud je možné zapněte
- Network Adapter: Nejlépe NAT, záleží na vás

17. Klikneme "`Finish`"
![[1,3.gif]]


# 2 Instalace Operačního Systému Arch Linux
>Celý instalační proces systému Arch Linux
## 2.1 Tvorba "prvního/celkového oddílu"
1. Zapneme Virtuální počítač "`Play virtual mechine`"
2. Počkáme než se zapne a načte systém do operačního řádku
3. Zjistíme si jméno disku na kterém budeme dělat partice = `fdisk -l` = Můj disk = `/dev/sda`
4. Začneme proces dělaná particí = `fdisk /dev/sda` ve většině případů /dev/sda může se ovšem lišit.. 
5. Napíšeme `o` pro vytvoření nového partition table
6. Napíšeme `n` pro zvolení typu oddílu/partition
7. Vybereme `p` pro primární typ oddílu
8. Vybereme `1` u čísla oddílu (Zakl)
9. Potvrdíme první sektor (Zakl)
![[2,1.gif]]

# 2,2 Změnení typu celkového oddílu na LVM
*Pořád jsme v fdsiku*
1. Napíšeme `t` pro výběr
2. Napíšeme alias pro lvm = `8e`
![[2,2.gif]]

## 2,3 Nastavení oddílu jako bootable a uložení všech provedených změn
1. Napíšeme `a` pro nastavení bootable možnost
2. Napíšeme `w` pro "uložení" všech změn
![[2,3.gif]]
*Můžeme podívat na změny které jsme udělal příkazem `fdisk -l`
*Náš svazek se jmenuje `/dev/sda1`*

## 2,4 Nastavení LVM
### 2,4,1 Tvorba fyzického svazku
1. Napíšeme `pvcreate --dataalignment 1m /dev/sda1` = vytvoří fyzický svazek a srovná na dnešní standard 1m na oddílu `/dev/sda1`
## 2,4,2 Tvorba logické skupiny
1. Napíšeme  `vgcreate volumegroup0 /dev/sda1` = `volumegroup0` jako jmeno a `/dev/sda1` jak jméno svazku
## 2,4,3 Tvorba logických LVM skupin
1. Napíšeme `lvcreate -L 10GB volumegroup0 /dev/sda1 -n lvroot` = 