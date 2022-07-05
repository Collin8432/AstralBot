"""
Astral cogs

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
from .giveaway import *


def setup(bot):
   """
   * `setup`
   Used by bot.load_extention to load classes
   """
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
   bot.add_cog(Giveaways(bot))