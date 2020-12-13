from discord.ext import commands
import os
import traceback
# APIリクエストに必要なライブラリ
import requests

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    

item_id = r_post.json()['id']
print(item_id)
# 93ead2568150009de5f1

r_get = requests.get(url_items + '/' + item_id, headers=headers)

print(r_get.status_code)
# 200


# URL＋クエリパラメータ
base_url = "https://public-api.tracker.gg/v2/apex/standard/"
# APIリクエストを送信
GET https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{platformUserIdentifier}
    
tenki_data = requests.get(url).json()

#サンプル
params = {"TRN-Api-Key":"API-KEY"}
endpoint = "profile/origin/villager_0x00"
session = requests.Session()
req = session.get(base_url+endpoint,params=params)
print(req.status_code)
req.close()
res = json.loads(req.text)
pprint(res)
#


bot.run(token)
