import discord
from discord.ext.commands import view
from discord.ui import Button, View
from discord.ext import commands

#change the server ids
server_list =[875236232303636491] # alskiir's server id

class myButtons(Button):
    def __init__(self, style, label):
        super().__init__(style=style, label=label)
    
    async def callback(self, interaction):
        #gets the user who clicked the button
        user = interaction.user
        #role id
        print(f'user roles {user.roles}')
        role = interaction.guild.get_role(875242889943347211) #lettuce role id

        if role not in user.roles:
            await user.add_roles(role)
            await interaction.response.send_message(f'given role {role.mention}', ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f'taken role {role.mention}',ephemeral=True)
        
class Alskiir(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # @commands.user_command(name='alskiir',guild_ids=server_list)
    @commands.command(name='alskiir')
    async def alskiir(self, ctx):
        title = 'Welcome!'
        desc=u'''
        **Get Your Role!**

        the button below to get your role and see the rest of the server!
    
        **For Twitch Subscribers!**
        
        Link your Twitch account to your Discord account for emotes and roles!
        '''
        embed = discord.Embed(title=title,description=desc)
        embed.set_image(url='https://cdn.discordapp.com/attachments/484432102402555935/926974132539781140/no-background-shadow-cropped.png')
        alskiir_button = myButtons(style=discord.ButtonStyle.primary,label='Join the Fun!')
        view = View()
        view.add_item(alskiir_button)
        await ctx.send(embed=embed,view=view)

def setup(bot):
    bot.add_cog(Alskiir(bot) )
    print('loading Alskiir')