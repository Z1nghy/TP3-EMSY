__author__ = "DSY - ARD"
__version__ = "1.0"
__maintainer__ = "DSY - ARD"
__email__ = ""
__status__ = "Prototype"
__date__ = "March 2025"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Library for date and time related stuff
import math                                                                 # Library for math stuff
import csv                                                                  # Library for csv handling stuffimport datetime                                                             # Library for date and time related stuff
import smtplib                                                              # Library for email related stuff
import numpy as np

from sensirion_i2c_driver import I2cConnection                              # Sensor driver
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice                          # Sensor driver
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver  # Sensor driver

#-----------------------------------------------------
# Declaring the sensor object
#-----------------------------------------------------
sht40 = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

#-----------------------------------------------------
# Declaring functions
#-----------------------------------------------------
def read_sensor(t , rh):
    try:
        t, rh = sht40.single_shot_measurement()
        # Watch out! t and rh are variable that contain not only the values but also the units.
        # You can print the values with the units (print(t)) or you can also recover only the value
        # by specifying which one: t.degrees_celsius or rh.percent_rh
    except Exception as ex:
        print("Error while recovering sensor values:", ex)
    else:
        return t, rh

    return 0 # In case something went wrong

def save_to_csv (filename, date, time, temp, humidity,dp) :
    with open (filename, "a", newline='') as file :
        writer = csv.writer(file)
        writer.writerow([filename, date, time, temp, humidity,dp])

def send_email(receiver, subject, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls() 
    server.login("jetaimediego456@gmail.com","qtye vaht paef vjkt")
    sender = "jetaimediego456@gmail.com"

    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': sender,
        'To':receiver,
        'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
        'X-Mailer': 'python',
        'Subject': subject
    }
    # create the message
    msg = ''
    for key, value in headers.items():
        msg += "%s: %s\n" % (key, value)

    # add contents
    msg += "\n%s\n" % (message)

    try:
        server.sendmail(headers['From'], headers['To'], msg.encode("utf8"))
        server.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong.", ex)





#-----------------------------------------------------
# Main script
#-----------------------------------------------------
if __name__ == "__main__":  # Runs only if called as a script but not if imported
    print("Hello and welcome to EMSY")
    #- Partie Dew Point
    temperature = float (0.00)
    humidity = 0.00
    dp = 0.00
    dp_haut = float (0.00)
    dp_bas = float (0.00)
    L = 243.12
    Beta = 17.62
    t = 0.00
    h = 0.00 
 
    t, h = read_sensor(t , h)
    temperature = str(t)
    temperature = temperature.split()
    temperature = float(temperature[0])

    humidity = str(h)
    humidity = humidity.split()
    humidity = float(humidity[0])

    dp_haut = L * (np.log(humidity / 100) + (Beta * temperature) / (L + temperature))
    dp_bas = Beta - ((np.log(humidity / 100)) + (Beta * temperature / (L + temperature)))
    dp = dp_haut / dp_bas
    print("Voici le resultat du calcul du point de rossee :",dp)

    # CSV
    system_datetime = datetime.datetime.now()            #permet de recuperer l'heure et la date actuelle 
    current_date = system_datetime.strftime("%d.%m.%Y") #permet de mettre en format jour/mois/annee
    current_time = system_datetime.strftime("%H:%M")    #permet de mettre en format heure/minute
    print ("Heure :", current_time)                      #permet d'afficher l'heure actuelle
    print ("Date :", current_date)                       #permet d'afficher la date actuelle
    #Enregister les donnees dans un fichier csv dans /home/debian/Tempelog.csv
    save_to_csv('/home/debian/TempLog.csv', current_date, current_time, temperature, humidity, dp)

    
    # SEND EMAIL
    # Sending an email to test the function

    temp_limite = 28.0
    if temperature > temp_limite:   
        
        print("Temperature limite depasse! ENVOI D'ALARME")
        subject = "Alarme de temperature"
        message = f"La temperature a depasse sa limite de {temp_limite} °C. La tmperature actuelle est de {temperature}°C"
        send_email(["jetaimediego456@gmail.com"], subject, message)
    
        




