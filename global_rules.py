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
	if '@sports-bot mlb hitting career' in message:
		
		text_split = message.split(' ')
		count = len(text_split[5])

		if count <= 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[5][0] + '/' + text_split[5] + text_split[4][0] + text_split[4][1] + '01.shtml'
		if count > 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[5][0] + '/' + text_split[5][0] + text_split[5][1] + text_split[5][2] + text_split[5][3] + text_split[5][4] + text_split[4][0] + text_split[4][1] + '01.shtml'

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['player_stats_summary_explain', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'batting_avg', 'onbase_perc', 'slugging_perc']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)


		game_stats = [text_stats[x:x+13] for x in range (0, len(text_stats), 13)]

		games = len(stats) / 13
		games = int(games)
		
		for i in range(0, games):
			if 'Yrs' in game_stats[i][0]:
				career_stats = ('Career Stats\n{0} Games\n{1} At Bats\n{2} Runs\n{3} Hits\n{4} Doubles\n{5} Triples\n{6} Home Runs\n{7} RBIs\n{8} Steals\n{9} Walks\n{10} AVG\n{11} OBP\n{12} SLUG'.format(game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10], game_stats[i][11], game_stats[i][12], game_stats[i+1][0]))
				send(career_stats, bot_info[0])
		
		return True
	
	#MLB Pitchers
	if '@sports-bot mlb pitching career' in message:
		
		text_split = message.split(' ')
		count = len(text_split[5])

		if count <= 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[5][0] + '/' + text_split[5] + text_split[4][0] + text_split[4][1] + '01.shtml'
		if count > 5:
			url = 'https://www.baseball-reference.com/players/'+text_split[5][0] + '/' + text_split[5][0] + text_split[5][1] + text_split[5][2] + text_split[5][3] + text_split[5][4] + text_split[4][0] + text_split[4][1] + '01.shtml'

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['player_stats_summary_explain', 'W', 'L', 'earned_run_avg', 'CG', 'SHO', 'IP', 'H', 'ER', 'HR', 'BB', 'SO', 'whip', 'strikeouts_per_nine']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)


		game_stats = [text_stats[x:x+13] for x in range (0, len(text_stats), 13)]

		games = len(stats) / 13
		games = int(games)
		
		for i in range(0, games):
			if 'Yrs' in game_stats[i][0]:
				career_stats = ('Career Stats:\n{0} Wins\n{1} Losses\n{2} ERA\n{3} CG\n{4} Shut Outs\n{5} IP\n{6} Hits\n{7} Earned Runs\n{8} Home Runs\n{9} Walks\n{10} Strike Outs\n{11} WHIP\n{12} K/9'.format(game_stats[i][1], game_stats[i][2], game_stats[i][3], game_stats[i][4], game_stats[i][5], game_stats[i][6], game_stats[i][7], game_stats[i][8], game_stats[i][9], game_stats[i][10], game_stats[i][11], game_stats[i][12], game_stats[i+1][0]))
				send(career_stats, bot_info[0])
		
		return True
	
	
	if '@sports-bot nfl career' in message:
		
		text_split = message.split(' ')

		count = len(text_split[4])

		first_name_capital = text_split[3].capitalize()
		last_name_capital = text_split[4].capitalize()

		if count <= 4:
			url = 'https://www.pro-football-reference.com/players/'+ last_name_capital[0] + '/' + last_name_capital + first_name_capital[0] + first_name_capital[1] + '00.htm'
		if count > 4:
			url = 'https://www.pro-football-reference.com/players/'+ last_name_capital[0] + '/' + last_name_capital[0] + last_name_capital[1] + last_name_capital[2] + last_name_capital[3] + first_name_capital[0] + first_name_capital[1] + '00.htm'

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'rush_yds', 'rush_td', 'rush_yds_per_att', 'rush_yds_per_g', 'rec', 'rec_yds', 'rec_td', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']})

		text_stats = []

		for thing in stats:
			stat = thing.text
			text_stats.append(stat)

		print(text_stats)


		for i in range(0, int(len(stats))):
			if 'Career' in text_stats[i]:
				if text_stats[0] == 'Yds':
					career_stats = 'Career:\n{0} Games\n{1} Rushing Yards\n{2} Rushing TDs\n{3} YPA\n{4} YPG\n{5} Receptions\n{6} Receiving Yards\n{7} Receiving TDs\n{8} Scrammage Yards\n{9} Total TDs\n{10} Fumbles'.format(text_stats[i+1], text_stats[i+2], text_stats[i+3], text_stats[i+4], text_stats[i+5], text_stats[i+6], text_stats[i+7], text_stats[i+8], text_stats[i+9], text_stats[i+10], text_stats[i+11])
					send(career_stats, bot_info[0])
				if text_stats[0] == 'Rec':
					career_stats = 'Career:\n{0} Games\n{1} Receptions\n{2} Receiving Yards\n{3} Receiving TDs\n{4} Rushing Yards\n{5} Rush TDs\n{6} Rush YPA\n{7} Rush YPG\n{8} Scrimmage Yards\n{9} Total TDs\n{10} Fumbles'.format(text_stats[i+1], text_stats[i+2], text_stats[i+3], text_stats[i+4], text_stats[i+5], text_stats[i+6], text_stats[i+7], text_stats[i+8], text_stats[i+9], text_stats[i+10], text_stats[i+11])
					send(career_stats, bot_info[0])
		return True

	
	return True
