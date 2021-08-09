#Author: Julio Aviña 27/09/2020
import sys 
import os  
import re  
import time 
from socket import *

ports_lower_limit = 1
ports_upper_limit = 49151

#Función para validar IP
def validateIP(ip_address):
   regex = '^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
   if re.search(regex, ip_address):
      return True
   else:
      return False

#Función para definir y validar los limites inferior y superior de los puertos permitidos a escanear
def validatePorts(lower_limit, upper_limit):
       
   check_lower = int(lower_limit) in range(ports_lower_limit, ports_upper_limit)
   check_upper = int(upper_limit) in range(ports_lower_limit, ports_upper_limit)
   if check_lower == True and check_upper == True:
      return True
   else:
      return False

#Función para el escaneo de puertos
def scan_ports(ip_address, lower_limit, upper_limit):

   print('\n')
   #recorremos el rango de puestos ingresados por el usuario y validamos el estatus 
   for port in range(int(lower_limit), int(upper_limit) + 1):
      socket_instance = socket(AF_INET, SOCK_STREAM)
      scanner_response = socket_instance.connect_ex((ip_address, port))
      if scanner_response == 0:
         print('El puerto ' + str(port) + ' está abierto')
      else:
         print('El puerto ' + str(port) + ' está cerrado')
      socket_instance.close()

#Función para comenzar el proceso si estamos en windows
def win_platform():
   os.system('cls')    
   os.system('color B')
   response_validate_ip = False
   print('\n** ESCANER DE PUERTOS WIN [jenlogic] **\n')
   #validar si la dirección ip ingresada es correcta
   while response_validate_ip != True:
      ip_address = input('Ingrese una dirección IP valida para realizar un escaneo de puertos: ').lower()
      if ip_address == 'localhost':
         ip_address = gethostbyname(ip_address)
         response_validate_ip = True
      else:
         response_validate_ip = validateIP(ip_address)
         if response_validate_ip == False:
            print('\nLa dirección IP ingresada es inválida')
                
   #Terminó la validacion y continua el proceso
   response_validate_ports = False
   while response_validate_ports != True:
      os.system('cls')
      print('\nSe va a realizar el escaneo de puertos de la dirección IP: ' + ip_address)
      print('\nIngrese el limite inferior y superior de los puertos que desea escanear [Permitidos del: ' + str(ports_lower_limit) + ' al ' + str(ports_upper_limit) + ']')
      upper_limit = 0
      lower_limit = 0
      while upper_limit <= lower_limit:
         print('\nEl límite superior debe ser mayor al inferior')
         lower_limit = input('\nIngrese el puerto (limite inferior):')
         upper_limit = input('\nIngrese el puerto (limite superior):')
       
      response_validate_ports = validatePorts(lower_limit, upper_limit)
      if response_validate_ports == True:
         scan_ports(ip_address, lower_limit, upper_limit) 
      else:
         os.system('cls')
         print('\nPor favor ingrese puertos en el rango permitidos')
         time.sleep(2)
         response_validate_ports = False  
        
   print('\n')
   os.system('pause')
   os.system('color 7')
   

def main():
   if sys.platform.startswith('win32'):
      win_platform()
   elif sys.platform.startswith('linux'):
      #PROXIMAMENTE
      print('\nPróximamente')
main()