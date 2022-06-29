"""
Contains embeds for the help pages

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake


from utils.color import color


helpemb = disnake.Embed(
    title="General ⚙️",
    description="**/help** - Displays Help Command\n **/Shutdown** - Shuts Bot Down(Permissions Required)\n**/randomchoice (choice) (choice)** - Picks A Random Choice - Simlar To Heads/Tails\n**/ticket** - Creates A Support Ticket\n**/ping** - Shows Bot Latency\n**/astral invite** - Gets Bot Invite Link\n**/astral support** - Gets Bot Server Link\n**/astral credits** - Shows Bot Credits\n**/astral uptime** - Shows Bot Uptime\n**/appinfo** - Shows Info About Astral's Application\n**/userinfo** - Gets Information On A User\n**/firstmessage** - Gets The Link To The First Message In A Channel\n**/todo** - Fetches The Todo.txt List For The Bot\n**/serverinfo** - Gets The Information On A Server\n**/getauditlogs** - Gets The Most Recent Audit Logs",
    color=color,
    timestamp=disnake.utils.utcnow(),
)


funemb = disnake.Embed(
    title="Fun ⚙️",
    description="**/nerd** - NerdButton\n**/balls** - BallsButton\n**/9-11** - 9/11 In Discord\n**/emojify (text)** - Translates Text To Emojis\n**/slots** - Slots In Discord",
    color=color,
    timestamp=disnake.utils.utcnow(),
)


modemb = disnake.Embed(
    title="Moderation ⚙️",
    description="**/ban** - Bans A User\n**/kick** - Kicks A User\n**/purge** - Purges All The Messages In A Channel\n**/moderatorapplication** - Apply For Mod\n**/rules** - Only Can Be Used By Administrators - Displays Simple Rules\n**/Testhooksend** - Sends A Test Message To The Webhook On Your Database\n**/Mute (member)** - Mutes A Selected Member\n**/UnMute (Member)** - Unmutes A Selected Member\n**/editguild (args)** - Edits A Guild\n**/fetchdatabase** - Fecthes All Of The Information From Your Server's Database",
    color=color,
    timestamp=disnake.utils.utcnow(),
)


setupemb = disnake.Embed(
    title="Setup ⚙️",
    description="**/setup** - Only Can Be Used By Administrators - Sets Up The Bot",
    color=color,
    timestamp=disnake.utils.utcnow(),
)


nsfwemb = disnake.Embed(
    title = "NSFW 🔞",
    description = "**/nsfw** (ass, tits, thighs, or hentai)",
    color=color,
    timestamp=disnake.utils.utcnow(),
)
