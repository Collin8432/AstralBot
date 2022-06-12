# Imports
import disnake



from helpers.color import color



# Embeds 
helpemb = disnake.Embed(
    title="General ⚙️",
    description="**/help** - Displays Help Command\n **/Shutdown** - Shuts Bot Down(Permissions Required)\n**/randomchoice (choice) (choice)** - Picks A Random Choice - Simlar To Heads/Tails\n**/ticket** - Creates A Support Ticket\n**/ping** - Shows Bot Latency\n**/astral invite** - Gets Bot Invite Link\n**/astral support** - Gets Bot Server Link\n**/astral credits** - Shows Bot Credits\n**/astral uptime** - Shows Bot Uptime",
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
    description="**/ban** - Bans A User\n**/kick** - Kicks A User\n**/purge** - Purges All The Messages In A Channel\n**/moderatorapplication** - Apply For Mod\n**/rules** - Only Can Be Used By Administrators - Displays Simple Rules\n**/Testhooksend** - Sends A Test Message To The Webhook On Your Database\n**/Mute (member)** - Mutes A Selected Member\n**/UnMute (Member)** - Unmutes A Selected Member",
    color=color,
    timestamp=disnake.utils.utcnow(),
)
setupemb = disnake.Embed(
    title="Setup ⚙️",
    description="**/setup** - Only Can Be Used By Administrators - Sets Up The Bot",
    color=color,
    timestamp=disnake.utils.utcnow(),
)