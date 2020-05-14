# Rolling\_Discord-A_Discord\_Dice\_Bot
A Bot for Discord I wrote so that you can play that sweet sweet P&P with your friends.

## THIS IS THE DEVELOPMENT BRANCH, ONLY CLONE WHEN YOU ARE READY TO TAKE THE RISK!

### Setup Windows
MusicBot can be installed on Windows 7, 8, and 10 too, though it requires installing some programs on your computer first.

1. Install [Python 3.7.](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe)
2. During the setup, tick Install launcher for all users (recommended) and Add Python 3.7 to PATH when prompted.
3. Install [Git for Windows](http://gitforwindows.org/).
4. During the setup, tick Git from the command line and also 3rd-party software, Checkout Windows-style, commit Unix-style endings, and Use MinTTY (the default terminal MSYS2).
5. Open Git Bash by right-clicking an empty space inside of a folder (e.g My Documents) and clicking Git Bash here.
6. Run ```git clone https://github.com/Sntx626/Rolling_Discord-A_Discord_Dice_Bot.git Rolling_Discord-A_Discord_Dice_Bot -b master``` in the command window that opens.

After doing that, a folder called Rolling_Discord-A_Discord_Dice_Bot will appear in the folder you opened Git Bash in. Configure your bot, then run ```python bot.py``` from the command line to start the MusicBot.

### Setup Linux/MacOS

#### Install build tools
```bash
sudo apt-get install build-essential unzip -y
sudo apt-get install software-properties-common -y
```

#### Install system dependencies
```bash
sudo apt-get update -y
sudo apt-get install git python3-pip
sudo apt-get upgrade -y
```

#### Clone the MusicBot to your home directory
```bash
git clone https://github.com/Sntx626/Rolling_Discord-A_Discord_Dice_Bot.git ~/Rolling_Discord-A_Discord_Dice_Bot -b master
cd ~/Rolling_Discord-A_Discord_Dice_Bot
```

#### Install Python dependencies
```bash
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U -r requirements.txt
```

### Additional Information
I do not own the image "dd-dice-512.png" in the folder additional stuff.
The Install Guide pretty much is a copy of the install Guide from [This nice music bot](https://just-some-bots.github.io/MusicBot/).
