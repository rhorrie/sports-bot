# GroupMe Bot Driver
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/paulpfeister/GroupMe-BotDriver/issues) ![GitHub last commit](https://img.shields.io/github/last-commit/paulpfeister/groupme-botdriver.svg)

This driver is written entirely in Python, and with easy configuration in mind.

Using this driver, you'll be able to monitor multiple group chats with ease and set custom rules for each one (or the same for all, if that's what you want). For easy maintenance, each group's rules will be kept in their own files. I have also taken care to make debugging simple and logs easy to read, but more on that later.

## Deploying the bot

This driver has been built to run on Heroku. If you don't have an account, register at [signup.heroku.com](https://signup.heroku.com/).
You can likely run this bot elsewhere, but as of yet only Heroku has been verified as working.

The steps here might look daunting if you are unfamiliar, but I tried making them as easily understood and step-by-step as possible. If there are any issues, feel free to [open a ticket](https://github.com/paulpfeister/GroupMe-BotDriver/issues).

Steps for using *GitHub Desktop* on Windows will be added shortly, along with steps for using HerokuGit instead of GitHub.

#### Linux command line
1. Create a new repository on github. [See this page for help](https://help.github.com/en/articles/create-a-repo).
   - Ensure the repo is private. More on this later.
2. Open the terminal, and enter these commands where \*USERNAME\* is your github username and \*REPO\* is your new repository name.
```
$ git clone --mirror https://github.com/paulpfeister/groupme-botdriver.git
$ cd groupme-botdriver.git
$ git remote set-url --push origin https://github.com/*USERNAME*/*REPO*.git
$ git push --mirror
```
3. Create a new app on your [Heroku dashboard](https://dashboard.heroku.com/apps)
   1. Click **Create new app** in the dropdown menu labled **New** (top right corner).
   2. Create a name for your app. This won't be seen by your users.
   3. Under **Deployment Method**, click **GitHub**.
   4. Link your account and select your respository.
      - Enabling automatic deploys is recommended. Doing so will simplify the process. Otherwise, you will have to manually deploy each time you update the bot or change rules. If you enable automatic deploys, check that *Wait for CI to pass...* is **disabled**.
   6. Finally, click **Open app** on the top right. Take note of this url.
   7. Leave Heroku open for now.
4. Register your bot at [dev.groupme.com/bots/new](https://dev.groupme.com/bots/new)
   - The name you pick here will be visible to your users. This only applies to the group selected here.
   - The link you saved before goes in **Callback URL** (https://*my-app-name*.herokuapp.com/)
   - You can ignore Avatar URL for now, unless you have a picture in mind.
   - Take note of your Bot ID and Group ID. Keep this information to yourself.
5. Return to Heroku and configure your bot.
   1. Under the **Settings** tab (when within your app's dashboard), click **Reveal Config Vars**.
   2. Define key `BOT_INFO` for your group.
      - Value should equal `GROUP_ID, BOT_ID, BOT_NAME` so if your group id is 123, your bot id is 98765, and name is John the resulting value would be `123, 98765, John`
   - If you have multiple groups, want to toggle debugging, or want to toggle concurrency, see the Advanced section.

**Cheers!** Your bot should now be functioning. See the customization section to make it do stuff.

If you keep the files locally, you can update your bot with two simple commands. Otherwise, you can just run step 2 again.
```
$ git fetch -p origin
$ git push --mirror
```

## Advanced setup
#### Handling multiple groups simultaneously
See the original `BOT_INFO` format. To handle multiple groups, simply append the same format again after a semicolon.    

For instance, if I want to handle three different groups, I will update `BOT_INFO` to the form `GID_1, BID_1, N_1; GID_2, BID_2, N_2; GID_3, BID_3, N_3`
#### Changing amount of concurrency
Web concurrency means the number of processes running your bot side by side. For larger apps, higher concurrency is a good thing. It is unlikely you will need concurrency with your bot, and disabling it will possibly give you a cleaner log. To change the number of concurrent processes, add a new Config Var `WEB_CONCURRENCY` and set the value equal to the number of desired processes. Setting it equal to `1` disables concurrency.
#### Toggle debugging in logs
The bot will automatically log some items *all the time* and others only when debugging. I tend to leave this on for more in depth logs, but if you like simpler readouts you can easily disable it. Create a new Config Var `BOT_DEBUG` and set the value equal to `True` or `False` for enabled and disabled. Defaults to True if no variable is found.
#### Monitoring logs
You can use many different outside tools to monitor the logs, and they may even give you greater personalization. To use the standard Heroku logs, called *logplex*, you will need to install their command line interface, called Heroku CLI.
- Linux via snap `sudo snap install --classic heroku`
- Windows x64 [download installer](https://cli-assets.heroku.com/heroku-x64.exe)
- Otherwise, see the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) page for help.

Once HerokuCLI is installed, you can run Heroku commands straight from your normal command line. Read about monitoring logs on [Heroku's help page](https://devcenter.heroku.com/articles/logging#log-retrieval). Typically, a simple `heroku logs -a APP_NAME --tail --source app` is your best bet. (Replace APP_NAME with your app name.)
#### Customizing log formatting
Changing the format of log entries couldn't be easier. Editing your *groupme-bot.py* will present you with a class called *errcol* under the customization section. Here, you can read each tag's description and change how it is presented in the log.

## Customization

The bot is easily customizable. You are given the option to set either global rules, group rules, or both. When managing multiple groups, global rules will apply to *all* and group rules will only apply to their group. Group rules can also override global rules - your choice.

- Global rules are defined in a file called `global_rules.py`
- Group rules are defined in a file called `group_GROUP_ID.py` (for instance, `group_253468.py`)

None of these files are *required*, but each file you add can add functionality. In either file, you should create a function called *run* that takes parameters for the data packet, bot info, and the send function, as shown below.
```
1  |  # rules example
2  |
3  |  def run(data, bot_info, send_message):
4  |    if data['text'] == 'hi':
5  |      send_message('Hi there!', bot_info[0])
6  |      return True
```
In line 3, we see the method declaration. This can be anything that follows the format `def run(DATA_PARAM, BOT_PARAM, MSG_PARAM):`

The first argument, what we called `data` above, is the message data sent by GroupMe. This data contains information such as the username, text, attachments, and more. You can read about each data point on [GroupMe's tutorial](https://dev.groupme.com/tutorials/bots), but they all follow the same pattern (`data['text']` will return the message text).

The second argument, what we called `bot_info` above, is exactly what you think - the bot's info. This will be an array, where `bot_info[0]` returns the Bot ID and `bot_info[1]` returns its name.

The third and final argument, what we called `send_message`, does exactly that. In order to send messages as the bot, you have to use `send_message(MESSAGE, BOT_ID)` such as on line 5.

You can use control statements, such as the `if` statement on line 4 to control how the bot interacts with users. For instance, in this example the bot will say *Hi there!* any time a user says *hi*.

In line 6, we returned `True`. This means no other code following that line will run, and the bot will move on to the next task. *Note: When writing group rules, return True to skip global rules, and return False to run global rules anyways.*
### Pushing your rules to the repository
Now that you created custom rules, you need to deploy them to your bot. Assuming you kept the files from earlier, add your rules (with the proper names) to the same directory. After opening the terminal, you will need to run these commands (or use the web interface):
```
Ensure you are in the correct directory
$ git commit -am "Created custom rules"
$ git push
```
