# PYSCORD 🐘
A simple bot for Discord :) 

### Tecnologies

- [Python 3.9.7](https://www.python.org/) 
- [Discordpy](https://discordpy.readthedocs.io/en/stable/) 
- [python-dotenv](https://pypi.org/project/python-dotenv/) 

### Getting started

Clone the repository
```bash
$ git clone https://github.com/wribeiiro/pyscord
```
Switch to the repo folder
```bash
$ cd pyscord
```

Install all the dependencies using pip or install only discord lib and dotenv
```bash
$ pip install -r /path/to/requirements.txt
$ #or only discord lib and dot env
$ py -3 -m pip install -U discord.py
$ pip install python-dotenv
```
Create a new App in Discord Developers [discord-developers](https://discord.com/developers/applications)

1. Click in Create Application [example1](./assets/step0.png)
1. Set the App Name
1. Click in Create
2. Next, click in the left tab called Bot, and click Add Bot (Yes, do it) [example2](./assets/step1.png)
3. With created bot, next, where there Token, click in Copy (this key, will be used for DISCORD_KEY) [example3](./assets/step3.png)
4. Check PUBLIC BOT, and scroll down and check SERVER MEMBERS INTENT [example4](./assets/step4.png)

Create and set Permissions for Bot [discord-permissions](https://discordapi.com/permissions.html
) 

1. In General Permissions, check the Administrator
2. Scroll down and see the input CLIENT ID [permission1](./assets/permission.png)
3. For get to the Client ID, back to Discord developers, click in General Information Tab
4. Where there APPLICATION ID click in Copy
5. Now, back to permissions and paste the Client ID.
6. Next, below a link was generated
7. Next, click the link, and select the desired server and Continue [permission2](./assets/permission2.png)
8. Next, Autorize.
9. Finally enter the discord server, and see if the bot is there [bot-off](./assets/bot-off.png)
10. When your bot is started, must be avaliable [bot-avaliable](./assets/bot-avaliable.png)

Set param DISCORD_KEY, in .env
You can get your key in 

```bash
$ DISCORD_KEY=MYKEY
```
Start the bot
```bash
$ python mybot.py
```

Available Commands in the discord
| Command                     |function|
|:----------------------------|:--:| 
| `?regras`                   |Returns the server rules|
| `?level`                    |Returns the level of user in private|
