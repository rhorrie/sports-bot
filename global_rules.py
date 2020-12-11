from bs4 import BeautifulSoup
import requests

def run(data, bot_info, send):

    message = data['text']

    if message == '.test':
        send("Yea im working idiot.", bot_info[0])
        return True
    

    if message == 'matt haarms':
    	url = 'https://www.sports-reference.com/cbb/players/matt-haarms-1/gamelog/2021/'
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['opp_name', 'game_result', 'mp', 'trb', 'ast', 'stl', 'blk', 'pf', 'pts']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)

		game_stats = [text_stats[x:x+9] for x in range (0, len(text_stats), 9)]

		games = len(stats) / 9
		games = int(games)

		recent_game_stats = 'Opponent: {0}\nGame Result: {1}\n{2} Minutes\n{8} Points\n{3} Rebounds\n{4} Assists\n{5} Steals\n{6} Blocks\n{7} Fouls\n'.format(game_stats[int(games - 2)][0], game_stats[int(games - 2)][1], game_stats[int(games - 2)][2], game_stats[int(games - 2)][3], game_stats[int(games - 2)][4], game_stats[int(games - 2)][5], game_stats[int(games-2)][6], game_stats[int(games-2)][7], game_stats[int(games-2)][8])
		
    	send(recent_game_stats, bot_info[0])
    	return True



    return True
