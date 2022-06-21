"""
Astral cogs
"""



# Imports
from .fun import *
from .general import *
from .listeners import *
from .moderation import *
from .nsfw import *
from .setup import *
from .tasks import *
from .verification import *
from .astral import *
from .info import *


def setup(bot):
   bot.add_cog(Astral(bot))
   bot.add_cog(Fun(bot))
   bot.add_cog(General(bot))
   bot.add_cog(Events(bot))
   bot.add_cog(Moderation(bot))
   bot.add_cog(nsfw(bot))
   bot.add_cog(setupcmds(bot))
   bot.add_cog(Tasks(bot))
   bot.add_cog(Verification(bot))
   bot.add_cog(Info(bot))
