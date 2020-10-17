#!/bin/bash

echo "Setting up the system..."

echo "System Update!")
sudo apt-get update

clear 
echo -e "System Upgrade!"
sudo apt-get upgrade -y > /dev/null/ 2>&1

clear
echo -e "Downloading files"
sudo apt install python3 -y > /dev/null/ 2>&1
sudo apt install python3-pip -y > /dev/null/ 2>&1

echo -e "Files are huge...it might take few minutes. Sit back and relax!" 


wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux32.tar.gz > /dev/null/ 2>&1
tar -xf geckodriver-v0.27.0-linux32.tar.gz > /dev/null/ 2>&1
mv geckodriver /usr/bin/
rm -r geckodriver-v0.27.0-linux32.tar.gz
sudo pip3 install selenium -y

pip3 install -r requirements.txt > /dev/null/ 2>&1
clear 
echo -e "Almost Done!" 
sudo apt install firefox -y /dev/null 2>&1

touch announcement.txt
touch new-update.txt
clear 
let x=4
for i in {1..3}
do
    echo "$(( $x - $i ))"
    sleep 1 
done
echo "You're all set!"
