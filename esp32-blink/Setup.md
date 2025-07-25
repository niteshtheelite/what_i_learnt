# ESP32 MicroPython Setup - Command Summary

```bash
# 1 Install pipx, which is designed to install Python CLI tools in isolated environments:
sudo apt install pipx
pipx ensurepath  # Make sure ~/.local/bin is in your PATH

# 2 Then install esptool and mpremote:
pipx install esptool
pipx install mpremote

# 3 Run this command to fix it automatically set the path:
pipx ensurepath

# 4 then restart the terminal 
source ~/.bashrc


# 5. Identify your ESP32 serial port
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null

# 6. Erase existing flash on ESP32
esptool --chip esp32 --port /dev/ttyUSB0 erase-flash

# 7. Download latest MicroPython firmware for ESP32
wget https://micropython.org/resources/firmware/esp32-20230618-v1.20.0.bin

# 8. Flash MicroPython firmware to ESP32
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20230618-v1.20.0.bin

# 9. Add your user to dialout group to access serial port without sudo
sudo usermod -a -G dialout $USER

# (Log out and log back in here)

# 10. Connect to ESP32 REPL with mpremote
mpremote connect /dev/ttyUSB0

# 11. Upload your Python script to ESP32 filesystem
mpremote connect /dev/ttyUSB0 fs cp main.py :

# 12. Reset ESP32 to run your script automatically
mpremote connect /dev/ttyUSB0 reset

# 13. If mpremote command is not found, fix PATH:
pipx ensurepath
