from discord.ext import commands

class AutoSnippet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        """Automatically send a .response snippet when a thread is opened."""
        snippet_name = "response"  # 👈 change this to your snippet name

        snippets_cog = self.bot.get_cog("Snippets")
        if not snippets_cog:
            print("[AutoSnippet] Snippets cog not found.")
            return

        last_msg = thread.channel.last_message
        if not last_msg:
            messages = [m async for m in thread.channel.history(limit=1)]
            if not messages:
                print("[AutoSnippet] No messages found in the thread.")
                return
            last_msg = messages[0]

        ctx = await self.bot.get_context(last_msg)
        await snippets_cog.send_snippet(ctx, snippet_name)
        print(f"[AutoSnippet] Sent snippet '{snippet_name}' in {thread.channel.name}")

async def setup(bot):
    await bot.add_cog(AutoSnippet(bot))
