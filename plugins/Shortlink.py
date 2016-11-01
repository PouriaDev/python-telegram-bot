@bot.message_handler(commands=['short'])
def short(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
        text = m.text.replace("/short ","")
        res = urllib.urlopen("http://yeo.ir/api.php?url={}".format(text)).read()
        bot.send_message(m.chat.id, "*Your Short Link :* {}".format(res), parse_mode="Markdown", disable_web_page_preview=True)
    if str(banlist) == 'True':
            bot.send_message(m.chat.id, "*You Are Banned!*", parse_mode="Markdown")
