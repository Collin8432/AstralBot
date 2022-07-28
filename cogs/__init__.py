"""
Astral cogs
~~~~~~~~~~~

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



# Imports
from .balls import *
from .listeners import *
from .kick import *
from .nsfw import *
from .setup import *
from .tasks import *
from .verification import *
from .astral import *
from .info import *
from .giveaway import *
from .poll import *
from .allcommands import *
from .astralsub import *
from .ticket import *
from .shutdown import *
from .help import *
from .appinfo import *
from .userinfo import *
from .nerd import *
from .slots import *
from .emojify import *
from .modapp import *
from .mute import * 
from .timeout import *
from .editguild import *
from .purge import *
from .ban import *
from .donate import *


def setup(bot):
   """
   * `setup`
   Used by bot.load_extention to load classes
   """
   bot.add_cog(Astral(bot))
   bot.add_cog(Balls(bot))
   bot.add_cog(Kick(bot))
   bot.add_cog(Ban(bot))
   bot.add_cog(Nsfw(bot))
   bot.add_cog(Setup(bot))
   bot.add_cog(Tasks(bot))
   bot.add_cog(Verification(bot))
   bot.add_cog(Info(bot))
   bot.add_cog(Giveaways(bot))
   bot.add_cog(Poll(bot))
   bot.add_cog(Helpall(bot))
   bot.add_cog(Astralsub(bot))
   bot.add_cog(Tickets(bot))
   bot.add_cog(Shutdown(bot))
   bot.add_cog(Help(bot))
   bot.add_cog(Appinfo(bot))
   bot.add_cog(Userinfo(bot))
   bot.add_cog(Nerd(bot))
   bot.add_cog(Slots(bot))
   bot.add_cog(Emojify(bot))
   bot.add_cog(Moderatorapp(bot))
   bot.add_cog(Muteunmute(bot))
   bot.add_cog(Timeout(bot))
   bot.add_cog(Editguild(bot))
   bot.add_cog(Purge(bot))
   bot.add_cog(Donate(bot))
   