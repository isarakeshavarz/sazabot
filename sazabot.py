import telepot
import time
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot('604621575:AAFD8fOkB1L2ChT9lAM9cRVXwqWPEh6YLHE')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
            if msg['text'] == '/start':
                bot.sendMessage(chat_id,'Hi.Wellcome')
                bot.sendMessage(chat_id,'1.square area')
                bot.sendMessage(chat_id,'2.triangle area')
                bot.sendMessage(chat_id,'3.rectangle area')
                bot.sendMessage(chat_id,'4.circle area')
                bot.sendMessage(chat_id,'5.diamond area')
                bot.sendMessage(chat_id,'enter the number that you want:')
            elif msg['text'] == '1':
                bot.sendMessage(chat_id,'side*4')
            elif msg['text'] == '2':
                bot.sendMessage(chat_id,'(base+height)*1/2')
            elif msg['text'] == '3':
                bot.sendMessage(chat_id,'width*height')
            elif msg['text'] == '4':
                bot.sendMessage(chat_id,'radius*radius*PI')
            elif msg['text'] == '5':
                bot.sendMessage(chat_id,'(large diameter*small diameter)*1/2')
            else :
                bot.sendMessage(chat_id,'enter a number among 1 and 5:')

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
