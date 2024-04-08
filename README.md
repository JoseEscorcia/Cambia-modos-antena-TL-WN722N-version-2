# 🔁 Cambia modos antena TL-WN722N version 2
Con la ejecución de este archivo de codigo python podrás alternar entre el modo manage y monitor (promiscuo) de la antena [TL-WN722N](https://www.tp-link.com/co/home-networking/adapter/tl-wn722n/) versión 2 de una manera muy fácil y rapida.

Nota: este archivo fue pensado para usarlo en Kali Linux.

<div align="center">
    <img src="https://static.tp-link.com/TL-WN722N_EU_3.0_05_normal_1506586575378d.jpg" width="200px"/>
</div>

## Resumen de comandos
| Comando | Función | Ejemplo |
| -- | -- | -- |
| sin argumentos | **Listar y seleccionar** la interfaz de red | *python3 antena.py* | 
| -h, -help | **Información** de todas las opciones | *python3 antena.py -h* |
| -inter | **Especificar** la interfaz de red | *python3 antena.py -inter holaMundo* |
| -iniciar | **Inicia** el modo monitor (promiscuo) para la interface especificada en default_interface.txt | *python3 antena.py -iniciar* |
| -apagar | **Regresa** al modo manage y reestablece las interfaces | *python3 antena.py -apagar*|


## Listar y seleccionar interfaz
Con este comando podrás listar las interfaces de red disponibles y seleccionar aquella donde se encuentra la antena. La opción que selecciones quedará almacenada en un archivo de texto llamado "default_interface.txt" (este se guardará de forma automatica en la ruta /home/kali), de manera que ya la proxima vez que vayas a usar la antena no tendrás que especificar la antena y puedes proceder a activar/desactivar el modo monitor de una vez.

```
python3 antena.py -inter El_Valecita
```
<img src="inter.jpg">



## Opción de ayuda
Al ejecutar este comando se dará la lista completa de todos los comandos que proporciona "antena.py".

```
python3 antena.py -h
```
<img src="help.jpg">


## Especificar manualmente la interfaz
Con este comando podrás escribir el nombre de la interfaz en la cual está la antena. El nombre de la interfaz que ingreses quedará almacenada en un archivo de texto llamado "default_interface.txt" (este se guardará de forma automatica en la ruta /home/kali), de manera que ya la proxima vez que vayas a usar la antena no tendrás que especificar la antena y puedes proceder a activar/desactivar el modo monitor de una vez.

```
python3 antena.py
```
<img src="listar.jpg">

 
## 🧠 Gracias a...
Gracias a [Jupiter](https://www.instagram.com/ciber_jupiter/?hl=es) por sus aportes en el código.

## 📌 Creditos
Este es un reconocimiento para los creadores de las herramientas usadas en el proceso.

| Herramienta | Autor |
| -- | -- |
| rtl8188eus | KanuX-14 |
| Aircrack-ng | Thomas d'Otreppe |
