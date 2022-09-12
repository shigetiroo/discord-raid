# discord-raid
A simply PY-Bot to nuke or raid a Discord Server made by [NOVA]timo#4735.
A simply PY-Bot to nuke or raid a Discord Server.

## Features:  


• Mass-delete Channels  

• Mass-delete Channels  

• Mass-delete Roles  

• Ban, softban and kick every User  

•  Mass-ping @everyone, members and every taggable Role  

• Change Servername and Icon  

• Mass-delete Emojis  

• Dm every user of the Guild  

• Create an admin role for the Bot Owner


## Upcoming:  


• Assign a Role to all members  

• Nuke-Command  


## Setup:


• Install Python 3.10  

• Install pip 22.2.2  

• Clone GitHub Repo using [this link](https://github.com/shigetiroo/discord-raid.git).  

• Move into the cloned Folder  
```
pip install -r requirements.txt

python3 main.py
```
(Take into considerartion that you first have to fill in the gaps in config.json)


## Configuration  
config.json holds the basic configuration for the Bot. Change it to your needs.  


    "token" : "" # The Bot Token

    "status" : "" # The Rich Presence Status the Bot will show

    "restart_message" : "" # Message in Command Line when restarting the Bot through Discord

    "shutdown_message" : "" # Message in Command Line when shutting down the Bot through Discord

    "your_name" : "" # Name displayed when creating channels and category's

    "your_spam_message" : "" # The message which will be spammed in text channels when using the spam command

    "your_role_name" : "" # The name of the Role which will be generated using the role create command

    "servername" : "" # The name of the Server which will be set using the servername command

    "dm_message" : "" # The message which will be dm'd to every user of the guild

    "nuke_role" : "" # Will be used in an future update

    "admin_role" : "" # The role which will be given to the bot Owner

    "prefix_settings" : {
        "prefix" : "", # Bot Prefix
        "use_space" : false} # If the Prefix should have a space inbetween
