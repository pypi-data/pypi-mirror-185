# Install
`pip install dpy-check`
# Docs
PENDING...
Until then, here is some implementation code:
```py
import dpycheck as chk
from discord.ext import commands


bot = commands.Bot(...)

# if the error handler has been attached to an object,
# it can be acquired through `ErrorHandler.get(object)`
error_handler = chk.ErrorHandler(..., attach_to=bot)


@bot.command()
@chk.ctx.Check.all(
    chk.user_has_role(...),
    chk.Any(
        chk.membership("d") >= 5,
        chk.user_has_channel_perms(...)
    )
)
async def cmd(...): ...
cmd.error(error_handler.error)

bot.run(...)
```
*When using extensions, you must use `.placeholder` in combination with `resolve_placeholders` if you want to use the error handler:*
```py
import dpycheck as chk
from discord.ext import commands


class mycog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # get the attached ErrorHandler and run `resolve_placeholders`
        chk.ErrorHandler.get(bot).resolve_placeholders(self)
    
    # we use a placeholder and resolve in `__init__`
    # to attach the error handler. Make sure the
    # placeholder is at the very top (or more specifically,
    # make sure it happens *after* the command is created)
    @chk.ErrorHandler.placeholder
    @chk.ctx.Check.all(
        10 >= chk.membership("m") >= 5,
        chk.in_channel(...),
        chk.Not(chk.user_has_role(...))
    )
    @commands.command()
    async def cmd(...): ...


async def setup(...):...
```