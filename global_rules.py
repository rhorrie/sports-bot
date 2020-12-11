from bs4 import BeautifulSoup
import requests

def run(data, bot_info, send):
	message = data['text']

	if message == '.test':
		send("yes master", bot_info[0])
		return True
	
	if '@sports-bot' in message and 'career' in message:
		text_split = message.split(' ')
		
		url = 'https://www.sports-reference.com/cbb/players/' +text_split[2] + '-' +text_split[3] +'-1.html'
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['season', 'g', 'mp_per_g', 'fg_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)

		game_stats = [text_stats[x:x+10] for x in range (0, len(text_stats), 10)]

		games = len(stats) / 10
		games = int(games)
		
		for i in range(0, games):
			if game_stats[i][0] == 'Career':
				career_stats = '{0} Stats\nGames {1}\n{2} MPG\n{9} PPG\n{3} FG%\n{4} FT%\n{5} RPG\n{6} APG\n{7} SPG\n{8} BPG'.format(game_stats[i][0], game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9])
				send(career_stats, bot_info[0])
		return True

	return True
