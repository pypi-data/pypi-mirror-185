# Remembering

<!--
Remembering (working name) - This idea came from Marieke (mbed) originally and is an application prototype which gives
the user reminders in the forms of texts (maybe a quote, or something encouraging someone has said to us), images
(maybe a photo of your best friend), and custom external commands (maybe playing an audio file)
-->

Project status: Runnable prototype

*Remembering* is a reminder application for things we'd like to stay aware of during the day when
using the
computer

The application runs in the background "in the system tray" and notifications are shown in the
systray menu. Clicking a
menu item will launch the associated action

These actions are supported at the moment:

* Showing a text
* Displaying an image
* Launching a website
* Custom command (for example launching an application)

The time of the reminders can be set to a certain frequency or to specific times of day (or both)

Examples of how this application can be used:

* Showing a reminder of a loved one by adding images
* Quotes and wisdom that we want to remember can be shown
* Reminding us of an intention that we set at the start of the day
* Launching a website which has content that is updated daily
* A kind and encouraging word from a friend
* Someone expressing gratitude for something you have contributed

If you are looking for a more typical reminder application this may be interesting for you:

* [remind](https://www.roaringpenguin.com/products/remind)

## Running from Source

On Ubuntu:

1. `sudo apt-get install python3`
1. `sudo apt-get install python3-pip`
1. `sudo -H pip3 install --upgrade pip`
1. Download the latest code by
   clicking [here](https://gitlab.com/SunyataZero/remembering/-/archive/master/remembering-master.tar.gz)
1. Go to the directory where you downloaded the files
1. `tar xvf remembering-master.tar.gz`
1. `cd remembering-master`
1. `sudo -H pip3 install -r requirements.txt`
1. `python3 remembering.py`


