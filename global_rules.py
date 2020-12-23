from bs4 import BeautifulSoup
import requests

def get_url(user_message_array, count):
	if 'nba' in user_message_array[1]:
		if len(user_message_array[4]) <= 5:
			url = 'https://www.basketball-reference.com/players/'+user_message_array[4][0] + '/' + user_message_array[4] + user_message_array[3][0] + user_message_array[3][1] + '0' + str(count) + '.html'
		if len(user_message_array[4]) > 5:
			url = 'https://www.basketball-reference.com/players/'+user_message_array[4][0] + '/' + user_message_array[4][0] + user_message_array[4][1] + user_message_array[4][2] + user_message_array[4][3] + user_message_array[4][4] + user_message_array[3][0] + user_message_array[3][1] + '0' + str(count) + '.html'
		return url

	if 'mlb' in user_message_array[1]:	
		if len(user_message_array[4]) <= 5:
			url = 'https://www.baseball-reference.com/players/'+user_message_array[4][0] + '/' + user_message_array[4] + user_message_array[3][0] + user_message_array[3][1] + '0' + str(count) + '.shtml'
		if len(user_message_array[4]) > 5:
			url = 'https://www.baseball-reference.com/players/'+user_message_array[4][0] + '/' + user_message_array[4][0] + user_message_array[4][1] + user_message_array[4][2] + user_message_array[4][3] + user_message_array[4][4] + user_message_array[3][0] + user_message_array[3][1] + '0' + str(count) + '.shtml'
		return url

	if 'ncaa' in user_message_array[1]:
		url = 'https://www.sports-reference.com/cbb/players/' + user_message_array[3] + '-' +user_message_array[4] +'-' + str(count) + '.html'
		return url
	if 'nfl' in user_message_array[1]:
		first_name_capital = user_message_array[3].capitalize()
		last_name_capital = user_message_array[4].capitalize()
		if len(user_message_array[4]) <= 4:
			url = 'https://www.pro-football-reference.com/players/'+ last_name_capital[0] + '/' + last_name_capital + first_name_capital[0] + first_name_capital[1] + '0' + str(count) + '.htm'
		if len(user_message_array[4]) > 4:
			url = 'https://www.pro-football-reference.com/players/'+ last_name_capital[0] + '/' + last_name_capital[0] + last_name_capital[1] + last_name_capital[2] + last_name_capital[3] + first_name_capital[0] + first_name_capital[1] + '0' + str(count) + '.htm'
		return url

def get_stats(url, sport):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	stats = []
	seasons = ''
	if sport == 'ncaa':
		stats = soup.findAll(attrs={'data-stat': ['season', 'g', 'mp_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g']})		#13
		teams = soup.findAll(attrs={'data-stat': 'school_name'})
		teams = get_teams(teams)
	if sport == 'nba':
		stats = soup.findAll(attrs={'data-stat': ['season', 'g', 'mp_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g']})			#13
		teams = soup.findAll(attrs={'data-stat': 'team_id'})
		teams = get_teams(teams)
	if sport == 'mlb-pitching':
		stats = soup.findAll(attrs={'data-stat': ['player_stats_summary_explain', 'W', 'L', 'earned_run_avg', 'CG', 'SHO', 'IP', 'H', 'ER', 'HR', 'BB', 'SO', 'whip', 'strikeouts_per_nine']})    #13
		teams = soup.findAll(attrs={'data-stat': 'team_ID'})
		teams = get_teams(teams)
	if sport == 'mlb-batting':
		stats = soup.findAll(attrs={'data-stat': ['player_stats_summary_explain', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'batting_avg', 'onbase_perc', 'slugging_perc']})
		teams = soup.findAll(attrs={'data-stat': 'team_ID'})
		teams = get_teams(teams)
	if sport == 'nfl-skill':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'rush_yds', 'rush_td', 'rush_yds_per_att', 'rush_yds_per_g', 'rec', 'rec_yds', 'rec_td', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']})	#13
		teams = soup.findAll(attrs={'data-stat': 'team'})
		teams = get_teams(teams)
	if sport == 'nfl-passing':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'qb_rec', 'pass_cmp', 'pass_att', 'pass_cmp_perc', 'pass_yds', 'pass_td', 'pass_int', 'pass_rating', 'qbr', 'pass_sacked', 'gwd']})							#13
		teams = soup.findAll(attrs={'data-stat': 'team'})
		teams = get_teams(teams)
		
	name = soup.find('h1', {'itemprop': 'name'})
	if not name:
		return 0
	
	text_stats = []
	for thing in stats:
		stat = thing.text
		text_stats.append(stat)
	
	if 'nfl' in sport:
		return text_stats, seasons, teams
	
	season_stats = [text_stats[x:x+13] for x in range (0, len(text_stats), 13)]
	seasons = int(len(text_stats) / 13)

	return season_stats, seasons, teams

def format_stats(season_stats, num_of_seasons, teams, sport):
	career_stats = ''
	
	if sport == 'ncaa' or sport == 'nba':
		for i in range(0, num_of_seasons):
			if season_stats[i][0] == 'Career':
				career_stats = '{0} Stats\nTeams:{13}\nGames {1}\n{2} MPG\n{12} PPG\n{3} FG%\n{4} 3PT%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG\n{10} TO\n{11} PF'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], teams)
				
	
	if 'mlb' in sport:
		for i in range(0, num_of_seasons):
			if 'Yrs' in season_stats[i][0]:
				if sport == 'mlb-batting':
					career_stats = 'Career Stats\nTeams:{13}\n{0} Games\n{1} At Bats\n{2} Runs\n{3} Hits\n{4} Doubles\n{5} Triples\n{6} Home Runs\n{7} RBIs\n{8} Steals\n{9} Walks\n{10} AVG\n{11} OBP\n{12} SLUG'.format(season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], season_stats[i+1][0], teams)
					
				if sport == 'mlb-pitching':
					career_stats = 'Career Stats\nTeams:{13}\n{0} Wins\n{1} Losses\n{2} ERA\n{3} CG\n{4} Shut Outs\n{5} IP\n{6} Hits\n{7} Earned Runs\n{8} Home Runs\n{9} Walks\n{10} Strike Outs\n{11} WHIP\n{12} K/9'.format(season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], season_stats[i+1][0], teams)
					

	if 'nfl' in sport:
		for i in range(0, len(season_stats)):
			if 'Career' in season_stats[i]:
				if sport == 'nfl-passing':
					career_stats = 'Career Stats\nTeams:{12}\n{0} Games\n{1} Record as Starter\n{2} Completions\n{3} Attempts\n{4} CMP%\n{5} Pass Yards\n{6} TDs\n{7} INTs\n{8} Passer Rating\n{9} QBR\n{10} Sacks\n{11} Game Winning Drives'.format(season_stats[i+1], season_stats[i+2], season_stats[i+3], season_stats[i+4], season_stats[i+5], season_stats[i+6], season_stats[i+7], season_stats[i+8], season_stats[i+9], season_stats[i+10], season_stats[i+11], season_stats[i+12], teams)
					
				if sport == 'nfl-skill':
					if season_stats[0] == 'Yds' or season_stats[2] == 'Yds':
						career_stats = 'Career Stats\nTeams:{11}\n{0} Games\n{1} Rushing Yards\n{2} Rushing TDs\n{3} YPA\n{4} YPG\n{5} Receptions\n{6} Receiving Yards\n{7} Receiving TDs\n{8} Scrammage Yards\n{9} Total TDs\n{10} Fumbles'.format(season_stats[i+1], season_stats[i+2], season_stats[i+3], season_stats[i+4], season_stats[i+5], season_stats[i+6], season_stats[i+7], season_stats[i+8], season_stats[i+9], season_stats[i+10], season_stats[i+11], teams)
						
					if season_stats[0] == 'Rec' or season_stats[2] == 'Rec':
						career_stats = 'Career Stats\nTeams:{11}\n{0} Games\n{1} Receptions\n{2} Receiving Yards\n{3} Receiving TDs\n{4} Rushing Yards\n{5} Rush TDs\n{6} Rush YPA\n{7} Rush YPG\n{8} Scrimmage Yards\n{9} Total TDs\n{10} Fumbles'.format(season_stats[i+1], season_stats[i+2], season_stats[i+3], season_stats[i+4], season_stats[i+5], season_stats[i+6], season_stats[i+7], season_stats[i+8], season_stats[i+9], season_stats[i+10], season_stats[i+11], teams)
						

	return career_stats

def get_teams(teams):
	total_teams = ''
	for team in teams:
		add = team.text
		if add not in total_teams:
			total_teams += add + ' '
	total_teams = total_teams.replace('Tm', '')
	total_teams = total_teams.replace('School', '')
	total_teams = total_teams.replace('-min', '')
	return total_teams

def run(data, bot_info, send):
	message = data['text']

	if message == '.test':
		send("yes master", bot_info[0])
		return True
	
	if '@sports-bot' in message:
		count = 0
		user_message = message
		user_message_array = user_message.split(' ')
		if 'nba' in user_message_array[1] or 'mlb' in user_message_array[1] or 'ncaa' in user_message_array[1]:
			count = 1
		while True:
			url = get_url(user_message_array, count)
			season_info = get_stats(url, user_message_array[1])
			if season_info == 0:
				break
			career_stats = format_stats(season_info[0], season_info[1], season_info[2], user_message_array[1])
			send(career_stats, bot_info[0])
			count += 1
	
	return True
