#!/usr/bin/env python3

import subprocess
import argparse
import os

def listar_interfaces():
    try:
        resultado = subprocess.run(["ifconfig"], capture_output=True, text=True)
        ifconfig_output = resultado.stdout
    except subprocess.CalledProcessError:
        ifconfig_output = ""

    interfaces = []
    for line in ifconfig_output.splitlines():
        if "flags=" in line:
            interface_name = line.split(":")[0]
            if interface_name not in interfaces:
                interfaces.append(interface_name)

    excluded_words = ["flags=", "inet", "netmask", "broadcast", "up", "mtu", "ether"]
    interfaces = [iface for iface in interfaces if all(word not in iface for word in excluded_words)]

    print("Interfaces disponibles:")
    options = {}
    counter = 1

    for iface in interfaces:
        print(f"{counter}) {iface}")
        options[counter] = iface
        counter += 1

    try:
        choice = int(input(f"Seleccione una interfaz (1-{counter-1}): "))
    except ValueError:
        print("Opción inválida.")
        return

    if 1 <= choice < counter:
        selected_iface = options[choice]
        print(f"Ha seleccionado: {selected_iface}")
        return selected_iface
    else:
        print("Opción inválida.")
        return

def manejar_arg_iniciar(interfaz):
    ruta_archivo = os.path.expanduser("~/default_interface.txt")
    try:
        with open(ruta_archivo, "r") as archivo:
            interfaz = archivo.read().strip()
            
        # Ejecutar comandos bash
        print("Matando procesos que pueden interferir con el modo monitor...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"])

        subprocess.run(["sudo", "ip", "link", "set", interfaz, "down"])

        print(f"Activando modo monitor en la interfaz {interfaz}...")
        subprocess.run(["sudo", "iw", "dev", interfaz, "set", "type", "monitor"])

        print(f"Ejecutando airodump-ng en la interfaz {interfaz}...")
        subprocess.run(["sudo", "airodump-ng", interfaz])

        print("Proceso completado.")
        
    except Exception as e:
        print(f"Error: {e}")

def manejar_arg_apagar(interfaz):
    ruta_archivo = os.path.expanduser("~/default_interface.txt")
    try:
        with open(ruta_archivo, "r") as archivo:
            interfaz = archivo.read().strip()

        subprocess.run(["sudo", "airmon-ng", "check", "kill"])
            
        # Detener el modo monitor en la interfaz identificada
        print(f"Desactivando modo monitor en la interfaz {interfaz}...")
        subprocess.run(["sudo", "airmon-ng", "stop", interfaz]) #Detiene la interfaz que esté en modo monitor (promiscuo)
        
        print(f"Bajando la interfaz {interfaz}...")
        subprocess.run(["sudo", "ip", "link", "set", interfaz, "down"])

        print(f"Estableciendo el modo manage en la interfaz {interfaz}...")
        subprocess.run(["sudo", "iw", "dev", interfaz, "set", "type", "managed"])

        print(f"Reiniciando interfaces...")
        subprocess.run(["sudo", "service", "NetworkManager", "restart"])
        print("Proceso completado.")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Gestión de interfaces de red")
    parser.add_argument("-inter", type=str, help="Especificar la interfaz a utilizar")
    parser.add_argument("-iniciar", action="store_true", help="Iniciar la interfaz especificada en default_interface.txt")
    parser.add_argument("-apagar", action="store_true", help="Apagar la interfaz especificada en default_interface.txt")

    args = parser.parse_args()

    if args.inter:
        ruta_archivo = os.path.expanduser("~/default_interface.txt")
        try:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(args.inter)
            print(f"Se ha establecido la interfaz {args.inter} como predeterminada.")
        except Exception as e:
            print(f"Error al escribir en el archivo {ruta_archivo}: {e}")
        
    elif args.iniciar:
        interfaz = ""
        ruta_archivo = os.path.expanduser("~/default_interface.txt")
        try:
            with open(ruta_archivo, "r") as archivo:
                interfaz = archivo.read().strip()
                
            if interfaz:
                manejar_arg_iniciar(interfaz)
            else:
                print("No se ha seleccionado una interfaz.")
                
        except Exception as e:
            print(f"Error al leer el archivo {ruta_archivo}: {e}")
            
    elif args.apagar:
        interfaz = ""
        ruta_archivo = os.path.expanduser("~/default_interface.txt")
        try:
            with open(ruta_archivo, "r") as archivo:
                interfaz = archivo.read().strip()
                
            if interfaz:
                manejar_arg_apagar(interfaz)
            else:
                print("No se ha seleccionado una interfaz.")
                
        except Exception as e:
            print(f"Error al leer el archivo {ruta_archivo}: {e}")
    
    if not args.inter and not args.iniciar and not args.apagar:
        interfaz_elegida = listar_interfaces()
        if interfaz_elegida:
            with open(os.path.expanduser("~/default_interface.txt"), "w") as archivo:
                archivo.write(interfaz_elegida)

if __name__ == "__main__":
    main()
