# Imports
import disnake



# Embeds 
helpemb = disnake.Embed(
    title="General ⚙️",
    description="**/help**, Displays Help Command\n**/Uptime**, Displays Bot Uptime\n **/Shutdown**, Shuts Bot Down(Permissions Required)\n**/randomchoice (choice) (choice)**, Picks A Random Choice, Simlar To Heads/Tails\n**/ticket**, Creates A Support Ticket\n**/ping**, Shows Bot Latency\n**/invite bot**, Gets Bot Invite Link\n**/invite link**, Gets Bot Server Link", 
    color=0xDC143C,
    timestamp=disnake.utils.utcnow(),
)
funemb = disnake.Embed(
    title="Fun ⚙️",
    description="**/nerd**, NerdButton\n**/balls**, BallsButton",
    color=0xDC143C,
    timestamp=disnake.utils.utcnow(),
)
modemb = disnake.Embed(
    title="Moderation ⚙️",
    description="**/ban**, Bans A User\n**/kick**, Kicks A User\n**/purge**, Purges All The Messages In A Channel\n**/moderatorapplication**, Apply For Mod\n**/rules**, Only Can Be Used By Administrators, Displays Simple Rules\n**/setup**, Only Can Be Used By Administrators, Sets Up The Bot\n**Testhooksend**, Sends A Test Message To The Webhook On Your Database\n**/Mute (member)**, Mutes A Selected Member\n**/UnMute (Member), Unmutes A Selected Member",
    color=0xDC143C,
    timestamp=disnake.utils.utcnow(),
)