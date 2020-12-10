def run(data, bot_info, send):

    message = data['text']

    if message == '.test':
        send("Hi there! Your bot is working, you should start customizing it now.", bot_info[0])
        return True
    
    return True
