from discord.ext import commands

class AutoSnippet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("[AutoSnippet] Loaded.")

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        """Automatically send the `.response` snippet when a new thread opens."""
        snippet_name = "response"  # Name of your snippet

        snippets_cog = self.bot.get_cog("Snippets")
        if not snippets_cog:
            print("[AutoSnippet] Snippets cog not found.")
            return

        # Get the last message in the thread, or send a placeholder if empty
        last_msg = thread.channel.last_message
        if not last_msg:
            # Send a temporary blank message to get a context
            last_msg = await thread.channel.send(".")

        ctx = await self.bot.get_context(last_msg)

        try:
            await snippets_cog.send_snippet(ctx, snippet_name)
            print(f"[AutoSnippet] Sent snippet '{snippet_name}' in {thread.channel.name}")
        except Exception as e:
            print(f"[AutoSnippet] Failed to send snippet: {e}")

async def setup(bot):
    await bot.add_cog(AutoSnippet(bot))

