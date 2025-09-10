diskpart
list disk
select disk X            (X = número de tu HDD externo, ej: Disco 1)
clean
convert gpt              (Convierte a GPT para soportar 2TB)
create partition primary size=32000  (Crea partición de 32GB en FAT32)
format fs=fat32 quick label="BOOT"
assign letter=B
create partition primary (Usa el resto del espacio para datos)
format fs=ntfs quick label="DATA"
assign letter=D 
exit



para crear una partición unica y completa en gpt=
diskpart
list disk
select disk X              (X = número de tu HDD, ej: Disco 1)
clean                      (Borra todo)
convert gpt                (Convierte a GPT)
create partition primary   (Crea la partición)
format fs=ntfs quick label="BLACK_ARCH_HDD"
assign letter=E            (O solo assign para letra automática)
exit




blackarch-install

avaliable installation mode:
2.intall from blackarch full-iso (offline)  //como quieres instalar black arch
	2

avaliables output modes:
2.verbose (output of system comands: mkfs, pacman, etc) //quieres que se muesten todo lo que hace la terminal?
	2

avaliable locale options:
1.set a locale:   // mostrar que region horaria y lenguaje sera blackarch
	1

set locate (en_us)  // en estados unidos
	enter

avaliable keymap options:   // en que distribución de teclado quieres que sea
1.set a keymap
	1

set keymap (us)   // estadounidense
	enter

set you hostname  // nombre de la computadora
	blackwtd

available hard drives for installation  // en donde quieres que se instale blackarch
>sda (memoria usb)
>sdb (HDD externo) // HDD
>nvme0n1 (SSD interno con windows)
	sdb

install blackarch Linux with windows/other OS y/n  // instalar Linux junto a windows como doble boot
	y

create partitions with cfdisk(root andboot, optional swap)y/n   //aquí hacemos particiones pero como ya las creamos pues le ponemos que no
	n

full encrypted root y/n  //encriptar todo root, mas seguridad
	y

created partitions
/dev/sdb1 500m efi system
/dev/sdb2 1.8t Linux filesystem  // nos muestra como esta nuestra partición
efi system partition (/dev/sdbX)
	/dev/sdb1
root partition (/dev/sdbX)
	/dev/sdb2
choose a filesystem to use in your root partition (ext2, ext3, ext4)(default: ext4)
	ext4
swap partition (/dev/sdbX - empty for none)
	start

current partition table
/boot : /dev/sdb1 (Fat32)
/ : dev/sdb2 (ext4)
swap : none (swap)
partition table correct y/n
	y

hard drive setup > partition formatting
formatting partitions. are you sure? no crying afterwards y/n?:
	y

creating luks partition
enter passphrase for /dev/sdb2:



//activar las interfaces del internet para ethernet y wifi
sudo ip link set enp3s0 up //ethernet

sudo ip link set wlan0 up //wifi

sudo dhcpcd enp3s0 //asignarle una difeccion ip automática al ethernet

// pasos para activar y usar iwd (wifi)
sudo systemctl start iwd
sudo systemctl enable iwd
sudo systemctl status iwd
sudo iwctl

//Iniciar NetworkManager manualmente
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
sudo systemctl status NetworkManager
	Active: active (running)
sudo pacman -S networkmanager

//para seleccionar una red wifi
sudo nmtui