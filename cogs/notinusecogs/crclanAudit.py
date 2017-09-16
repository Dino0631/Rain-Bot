
    @crclan.command(name="roster", pass_context=True, no_pm=True)
    async def crclan_roster(self, ctx, key, *args):
        """Clan roster by key.
        To associate a key with a clan tag:
        [p]bsclan addkey
        
        Optional arguments:
        --sort {name,trophies,level,donations,crowns}
        
        Example: Display clan roster associated with key “alpha”, sorted by donations
        [p]bsclan roster alpha --sort donations
        """
        # Process arguments
        parser = argparse.ArgumentParser(prog='[p]crclan roster')
        # parser.add_argument('key')
        parser.add_argument(
            '--sort',
            choices=['name', 'trophies', 'level', 'donations', 'crowns'],
            default="trophies",
            help='Sort roster')

        try:
            p_args = parser.parse_args(args)
        except SystemExit:
            # await self.bot.send_message(ctx.message.channel, box(parser.format_help()))
            await send_cmd_help(ctx)
            return

        # key = p_args.key

        # Load data
        server = ctx.message.server
        await self.bot.send_typing(ctx.message.channel)
        clan_data = await self.model.get_clan_data(server, key=key)
        data_is_cached = False
        if not clan_data:
            data_is_cached = True
            clan_data = self.model.cached_clan_data(self.model.key2tag(server, key))
            if clan_data is None:
                await self.bot.say("Cannot find key {} in settings.".format(key))
                return

        # Sort data
        if p_args.sort == 'trophies':
            clan_data.members = sorted(clan_data.members, key=lambda member: -member['score'])
        elif p_args.sort == 'name':
            clan_data.members = sorted(clan_data.members, key=lambda member: member['name'].lower())
        elif p_args.sort == 'level':
            clan_data.members = sorted(clan_data.members, key=lambda member: -member['expLevel'])
        elif p_args.sort == 'donations':
            clan_data.members = sorted(clan_data.members, key=lambda member: -member['donations'])
        elif p_args.sort == 'crowns':
            clan_data.members = sorted(clan_data.members, key=lambda member: -member['clanChestCrowns'])


        await self.roster_view.send(
            ctx, server, clan_data, cache_warning=data_is_cached, color=random_discord_color())