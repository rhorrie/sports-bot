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
	if 'ncaa-basketball' in user_message_array[1]:
		url = 'https://www.sports-reference.com/cbb/players/' + user_message_array[3] + '-' + user_message_array[4] + '-' + str(count) + '.html'
		return url
	if 'ncaaf' in user_message_array[1]:
		url = 'https://www.sports-reference.com/cfb/players/' + user_message_array[3] + '-' + user_message_array[4] + '-' + str(count) + '.html'
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

	num_of_stats = 13

	seasons = ''
	if sport == 'ncaa-basketball':
		stats = soup.findAll(attrs={'data-stat': ['season', 'g', 'mp_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g']})		#13
		teams = soup.findAll(attrs={'data-stat': 'school_name'})
	if sport == 'nba':
		stats = soup.findAll(attrs={'data-stat': ['season', 'g', 'mp_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g']})			#13
		teams = soup.findAll(attrs={'data-stat': 'team_id'})
	if sport == 'mlb-pitching':
		stats = soup.findAll(attrs={'data-stat': ['year_ID', 'player_stats_summary_explain', 'W', 'L', 'earned_run_avg', 'CG', 'SHO', 'IP', 'H', 'ER', 'HR', 'BB', 'SO', 'strikeouts_per_nine']})    #13
		teams = soup.findAll(attrs={'data-stat': 'team_ID'})
	if sport == 'mlb-batting':
		stats = soup.findAll(attrs={'data-stat': ['year_ID', 'player_stats_summary_explain', 'G', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'BB', 'batting_avg', 'onbase_perc', 'slugging_perc']})
		teams = soup.findAll(attrs={'data-stat': 'team_ID'})
	if sport == 'nfl-skill':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'rush_yds', 'rush_td', 'rush_yds_per_att', 'rush_yds_per_g', 'rec', 'rec_yds', 'rec_td', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']})	#13
		teams = soup.findAll(attrs={'data-stat': 'team'})
		num_of_stats = 12
	if sport == 'nfl-passing':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'qb_rec', 'pass_cmp', 'pass_att', 'pass_cmp_perc', 'pass_yds', 'pass_td', 'pass_int', 'pass_rating', 'qbr', 'pass_sacked', 'gwd']})							#13
		teams = soup.findAll(attrs={'data-stat': 'team'})
	if sport == 'ncaaf-passing':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'pass_cmp', 'pass_att', 'pass_cmp_pct', 'pass_yds', 'pass_td', 'pass_int', 'pass_rating']})
		teams = soup.findAll(attrs={'data-stat': 'school_name'})
		num_of_stats = 9
	if sport == 'ncaaf-skill':
		stats = soup.findAll(attrs={'data-stat': ['year_id', 'g', 'rush_yds', 'rush_td', 'rec', 'rec_yds', 'rec_td', 'scrim_yds', 'scrim_td']})
		teams = soup.findAll(attrs={'data-stat': 'school_name'})
		num_of_stats = 9

	name = soup.find("h1", {'itemprop': 'name'})
	if not name:
		return 0

	seasons = len(stats) / num_of_stats


	text_stats = get_text_stats(stats, num_of_stats, sport)
	
	return text_stats, seasons, teams

def format_stats(season_stats, num_of_seasons, teams, sport, season_or_career):
	career_stats = ''
	season_or_career = season_or_career.upper()

	print(season_stats)

	for i in range(0, int(num_of_seasons)):
		if season_or_career == 'CAREER':
			if 'mlb' in sport:	
				season_or_career = 'YRS'
		player_teams = get_teams(teams, season_or_career, season_stats, num_of_seasons)
		if season_or_career in season_stats[i][0].upper():
			if sport == 'mlb-pitching':
				career_stats = '{0} Stats\nTeams:{13}\n{1} Wins\n{2} Losses\n{3} ERA\n{4} CG\n{5} Shut Outs\n{6} IP\n{7} Hits\n{8} Earned Runs\n{9} Home Runs\n{10} Walks\n{11} Strike Outs\n{12} K/9'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], player_teams)
			if sport == 'mlb-batting':
				career_stats = '{0} Stats\nTeams:{13}\n{1} Games\n{2} Runs\n{3} Hits\n{4} Doubles\n{5} Triples\n{6} Home Runs\n{7} RBIs\n{8} Steals\n{9} Walks\n{10} AVG\n{11} OBP\n{12} SLUG'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], player_teams)
			if sport == 'ncaa-basketball':
				career_stats = '{0} Stats\nTeams:{13}\nGames {1}\n{2} MPG\n{12} PPG\n{3} FG%\n{4} 3PT%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG\n{10} TO\n{11} PF'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], player_teams)
			if sport == 'nba':
				career_stats = '{0} Stats\nTeams:{13}\nGames {1}\n{2} MPG\n{12} PPG\n{3} FG%\n{4} 3PT%\n{5} FT%\n{6} RPG\n{7} APG\n{8} SPG\n{9} BPG\n{10} TO\n{11} PF'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], player_teams)
			if sport == 'nfl-passing':
				career_stats = '{0} Stats\nTeams: {13}\n{1} Games\n{2} Record as Starter\n{1} Completions\n{4} Attempts\n{5} CMP%\n{6} Pass Yards\n{7} TDs\n{8} INTs\n{9} Passer Rating\n{10} QBR\n{11} Sacks\n{12} Game Winning Drives'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], season_stats[i][12], player_teams)
			if sport == 'nfl-skill':
				if season_stats[0][2] == 'Yds':
					career_stats = '{0} Stats\nTeams: {12}\n{1} Games\n{2} Rushing Yards\n{3} Rushing TDs\n{4} YPA\n{5} YPG\n{6} Receptions\n{7} Receiving Yards\n{8} Receiving TDs\n{9} Scrammage Yards\n{10} Total TDs\n{11} Fumbles'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], player_teams)
				if season_stats[0][2] == 'Rec':
					career_stats = '{0} Stats\nTeams: {12}\n{1} Games\n{2} Receptions\n{3} Receiving Yards\n{4} Receiving TDs\n{5} Rushing Yards\n{6} Rush TDs\n{7} Rush YPA\n{8} Rush YPG\n{9} Scrimmage Yards\n{10} Total TDs\n{11} Fumbles'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], season_stats[i][9], season_stats[i][10], season_stats[i][11], player_teams)
			if sport == 'ncaaf-passing':
				career_stats = '{0} Stats\n Teams: {9}\n{1} Games\n{2} Completions\n{3} Attempts\n{4} CMP%\n{5} Pass Yards\n{6} TDs\n{7} INTs\n{8} Rating'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], player_teams)
			if sport == 'ncaaf-skill':
				if season_stats[0][2] == 'Yds':
					career_stats = '{0} Stats\nTeams: {9}\n{1} Games\n{2} Rush Yards\n{3} Rush TDs\n{4} Receptions\n{5} Receving Yards\n{6} Receiving TDs\n{7} Scrimmage Yards\n{8} Total TDs'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], player_teams)
				if season_stats[0][2] == 'Rec':
					career_stats = '{0} Stats\nTeams: {9}\n{1} Games\n{2} Receptions\n{3} Receiving Yards\n{4} Receiving TDs\n{5} Rushing Yards\n{6} Rush TDs\n{7} Scrimmage Yards\n{8} Total TDs'.format(season_stats[i][0], season_stats[i][1], season_stats[i][2], season_stats[i][3], season_stats[i][4], season_stats[i][5], season_stats[i][6], season_stats[i][7], season_stats[i][8], player_teams)

			return career_stats


def get_teams(teams, season_or_career, season_stats, num_of_seasons):
	total_teams = []
	for team in teams:
		add = team.text
		total_teams.append(add)
	
	career_teams = ''
	if 'CAREER' in season_or_career or 'Yrs' in season_or_career:
		for i in range(0, len(total_teams)):
			add = str(total_teams[i])
			if add not in career_teams:
				career_teams +=  add + ' '
		career_teams = career_teams.replace('Tm', '').replace('School', '').replace('-min', '').replace('Overall', '')
		return career_teams

	for i in range(0, int(num_of_seasons)):
		if season_or_career in season_stats[i][0]:
			career_teams = total_teams[i]
			return career_teams


def get_text_stats(stats, num_of_stats, sport):
	text_stats = []
	for thing in stats:
		stat = thing.text
		text_stats.append(stat)

	if sport == 'nba' and text_stats[1] != 'G':
		count = 0
		season_count = 0
		for i in range(0, len(text_stats)):
			if text_stats[i] == 'Season':
				season_count += 1
			if season_count == 2:
				break
			if season_count < 2:
				count += 1
		text_stats = text_stats[count:]

	if 'nfl' in sport:
		count = 0
		for i in range(0, len(text_stats)):
			if text_stats[i] != 'Year':
				count += 1
			if text_stats[i] == 'Year':
				break
		text_stats = text_stats[count:]


	game_stats = [text_stats[x:x+num_of_stats] for x in range (0, len(text_stats), num_of_stats)]
	return game_stats


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
			career_stats = format_stats(season_info[0], season_info[1], season_info[2], user_message_array[1], user_message_array[2])
			send(career_stats, bot_info[0])
			count += 1
	
	return True
