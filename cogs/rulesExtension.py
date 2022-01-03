import discord
from discord import permissions
from discord.commands.permissions import permission
from discord.ext.commands import view
from discord.ext.commands.core import command
from discord.ui import Button, View
from discord.ext import commands

# change the server ids
server_list = [875236232303636491]  # alskiir's server id


class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label='Join the fun!',
        style=discord.ButtonStyle.primary,
        custom_id='persistent_view:rules'
    )
    async def green(self, button: discord.ui.Button, interaction: discord.Integration):
        # gets the user who clicked the button
        user = interaction.user
        # role id
        print(f'user roles {user.roles}')
        role = interaction.guild.get_role(
            875242889943347211)  # lettuce role id

        if role not in user.roles:
            await user.add_roles(role)
            await interaction.response.send_message(f'Welcome in!', ephemeral=True)


class Alskiir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(PersistentView())

    @commands.command(name='getrules')
    @permissions.has_role(875240659311800340)
    async def alskiir(self, ctx):
        # role = ctx.guild.get_role(875240659311800340)
        # if role not in ctx.author.roles:
        #     return
        title = 'Welcome!'
        desc = '-----------------------'
        embed = discord.Embed(title=title, description=desc)
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/484432102402555935/926974132539781140/no-background-shadow-cropped.png')
        embed.add_field(name='Get Your Role!',
                        value='Select the button below to get your role and see the rest of the server!')
        embed.add_field(name='For Twitch Subscribers!',
                        value='Link your Twitch account to your Discord account for emotes and roles!')
        embed.color = discord.Color.from_rgb(31, 175, 197)
        await ctx.send(embed=embed, view=PersistentView())


def setup(bot):
    bot.add_cog(Alskiir(bot))
    print('loading Alskiir')
