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

## Customization

*Will be updated soon*
