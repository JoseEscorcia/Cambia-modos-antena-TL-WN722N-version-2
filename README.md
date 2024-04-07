# 🔁 Cambia modos antena TL-WN722N version 2
Con la ejecución de este archivo de codigo python podrás alternar entre el modo manage y monitor (promiscuo) de la antena [TL-WN722N](https://www.tp-link.com/co/home-networking/adapter/tl-wn722n/) versión 2 de una manera muy fácil y rapida.

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
 
## 🧠 Gracias a...
Gracias a [Jupiter](https://www.instagram.com/ciber_jupiter/?hl=es) por sus aportes en el código.

## 📌 Creditos
Este es un reconocimiento para los creadores de las herramientas usadas en el proceso.

| Herramienta | Autor |
|-----------:|-----------|
| rtl8188eus | KanuX-14 |
| Aircrack-ng | Thomas d'Otreppe |
