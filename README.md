<img align="left" width="88" height="88" src="https://cdn.discordapp.com/attachments/772832118161932308/1232030038841622579/Square44x44Logo.scale-200.png?ex=66391c63&is=6626a763&hm=43f3e0d0c2ef2103199be31f8e64eb2b13e990d6bf9bc4753a48e47bac604aa2&">

# MuseSDKIntoVRChat

This project is based off BrainFlowsIntoVRChat, using some of the same math from it, with my own code alongside it. THANK YOU SO MUCH TO CHARLES (Creator of BrainFlowsIntoVRChat) for help with the math!

Some quick disclaimers before we get started:
I am not associated with Interaxon or the Muse corporation (whatever they go by these days).
Most of the software used alongside this project is abandonware, and it isn't guarenteed to work.

# What you'll need:

ANY MUSE BEFORE 2018

MuseIO 3.4.1 (can be found at https://github.com/DrBrainlove/muse_tools)

OR

Muse Direct 2018

Bluetooth Adapter

# METHOD 1 (MUSE 2014 MU-01 ONLY)
1. Install the Windows Muse SDK
2. Open CMD and navigate to C:/Program Files (x86)/Muse/
4. Put your muse in Pairing Mode (flashing light, hold down for 5 secs)
5. Connect it using bluetooth. (It will disconnect, just keep it paired)
6. Run this command:
   ```muse-io --device-name <DEVICE NAME> --osc osc.udp://localhost:1647```

And it should re-connect.

6. Download the zip of this repo and navigate into its folder on CMD
7. ```pip install -r requirements.txt```
8. Open main.py
9. Set VRChat avatar params properly (or use TouchOSC to map them)

# METHOD 2 (ANY MUSE BEFORE 2018)
We will need to get the unlisted Muse Direct SDK from the Microsoft Store.

1. Download and install Alt App Installer (https://github.com/mjishnu/alt-app-installer/releases/latest)
2. Paste this link in to install Muse Direct (https://apps.microsoft.com/detail/9p0mbp6nv07x)
3. Open Muse Direct
4. Connect your Muse through Windows bluetooth
5. Add a new OSC output
<img  width="500" height="329" src="https://cdn.discordapp.com/attachments/772832118161932308/1237184511964479648/Screenshot_2024-05-06_192859.png?ex=663ab95d&is=663967dd&hm=b2dd1a9d0ab36356cae0935fe63dd575c5f3a11225cb05cd3439ba6b7f3c8670&">
6. Copy these settings (scroll down and check EVERYTHING)
<img  width="500" height="351" src="https://cdn.discordapp.com/attachments/1208173006011105310/1237186679400562688/Screenshot_2024-05-06_193754.png?ex=663abb62&is=663969e2&hm=46ada8c8ec9cfb47ec1c893a9d465b5703ea55d520bf5e3be349af0adfe69ff6&">

7. Turn on the OSC output
   
8. Verify your headband is connected with the "Info" tab
    
10. Download the zip of this repo and navigate into its folder on CMD
    
11. ```pip install -r requirements.txt```
   
12. Open main.py
    
13. Set VRChat avatar params properly (or use TouchOSC to map them)

 #   Params are:
   
       /Focus (0-1) (Float)
   
       /FocusLeft (0-1) (Float
   
       /FocusRight (0-1) (Float)
   
       /Blink (0,1) (Int)

Will write better docs when I get a minute. Thanks!


