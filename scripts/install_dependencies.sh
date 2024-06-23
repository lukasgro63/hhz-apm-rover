#!/bin/bash

# Update und Upgrade
sudo apt-get update
sudo apt-get upgrade -y

# Installiere Python und Pip
sudo apt-get install python3 python3-pip -y

# Installiere Kamera-Treiber und Bibliotheken
sudo apt-get install python3-picamera -y

# Installiere benötigte Python-Pakete
pip3 install -r requirements.txt
