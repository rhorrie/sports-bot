from bs4 import BeautifulSoup
import requests

def run(data, bot_info, send):
	message = data['text']

	if message == '.test':
		send("yes master", bot_info[0])
		return True
	
	#NCAA Players
	if '@sports-bot ncaa career' in message:
		text_split = message.split(' ')
		
		url = 'https://www.sports-reference.com/cbb/players/' +text_split[3] + '-' +text_split[4] +'-1.html'
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
		
		schools = []
		for i in range(0, games):
			if game_stats[i][0] == 'Career':
				if game_stats[i][1] == 'Overall':
					for f in range(i+1, games):
						schools.append(game_stats[f][1])
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], schools, game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
				if game_stats[i][1] != 'Overall':
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
		return True
	
	
	#NBA Players
	if '@sports-bot nba career' in message:
		text_split = message.split(' ')
		
		count = len(text_split[4])
		
		if count <= 5:
			url = 'https://www.basketball-reference.com/players/'+text_split[4][0] + '/' + text_split[4] + text_split[3][0] + text_split[3][1] + '01.html'
		if count > 5:
			url = 'https://www.basketball-reference.com/players/'+text_split[4][0] + '/' + text_split[4][0] + text_split[4][1] + text_split[4][2] + text_split[4][3] + text_split[4][4] + text_split[3][0] + text_split[3][1] + '01.html'
		
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['season', 'team_id', 'g', 'mp_per_g', 'fg_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'pts_per_g']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)

		game_stats = [text_stats[x:x+11] for x in range (0, len(text_stats), 11)]

		games = len(stats) / 11
		games = int(games)
		
		schools = []
		for i in range(0, games):
			if game_stats[i][0] == 'Career':
				if game_stats[i][1] == '':
					for f in range(i+1, games):
						schools.append(game_stats[f][1])
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], schools, game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
				if game_stats[i][1] != '':
					career_stats = '{0} Stats\nSchool(s) {1}\nGames {2}\n{3} MPG\n{10} PPG\n{4} FG%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG'.format(game_stats[i][0], game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10])
					send(career_stats, bot_info[0])
		return True
	
	
	#MLB Hitters
	if '@sports-bot mlb career' in message:
		
		text_split = message.split(' ')
		count = len(text_split[4])

		if count <= 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[4][0] + '/' + text_split[4] + text_split[3][0] + text_split[3][1] + '01.shtml'
		if count > 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[4][0] + '/' + text_split[4][0] + text_split[4][1] + text_split[4][2] + text_split[4][3] + text_split[4][4] + text_split[3][0] + text_split[3][1] + '01.shtml'

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'batting_avg', 'onbase_perc', 'slugging_perc']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)


		game_stats = [text_stats[x:x+13] for x in range (0, len(text_stats), 13)]

		games = len(stats) / 13
		games = int(games)

		career_stats = ('{0} Games\n{1} At Bats\n{2} Runs\n{3} Hits\n{4} Doubles\n{5} Triples\n{6} Home Runs\n{7} RBIs\n{8} Steals\n{9} Walks\n{10} AVG\n{11} OBP\n{12} SLUG'.format(game_stats[games-2][0], game_stats[games-2][1], game_stats[games-2][2], game_stats[games-2][3], game_stats[games-2][4], game_stats[games-2][5], game_stats[games-2][6], game_stats[games-2][7], game_stats[games-2][8], game_stats[games-2][9], game_stats[games-2][10], game_stats[games-2][11], game_stats[games-2][12]))
		send(career_stats, bot_info[0])
		
		return True
	
	return True
