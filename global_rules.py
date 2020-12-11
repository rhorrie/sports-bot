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

		stats = soup.findAll(attrs={'data-stat': ['season', 'school_name', 'g', 'mp_per_g', 'fg_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)

		game_stats = [text_stats[x:x+11] for x in range (0, len(text_stats), 11)]

		games = len(stats) / 11
		games = int(games)
		
		schools = ''
		for i in range(0, games):
			if game_stats[i][0] == 'Career':
				if game_stats[i][1] == 'Overall':
					for f in range(i+1, games):
						schools = schools + (game_stats[f][1]) + ', '
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], schools, game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
				if game_stats[i][1] != 'Overall':
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
		return True

	return True
