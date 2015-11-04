import sqlite3

conn = sqlite3.connect('CFB.db')
c = conn.cursor()

c.execute('''CREATE TABLE team
            (team_code num primary key, name text, conf_code num);''')

c.execute('''CREATE TABLE team_game_stats ( team_code num, game_code num,
          rush_att num, rush_yard num, rush_td num, pass_att num, pass_comp num,
          pass_yard num, pass_td num, pass_int num, pass_conv num, kickoff_ret num,
          kickoff_ret_yard num, kickoff_ret_td num, punt_ret num, punt_ret_yard num,
          punt_ret_td num, fum_ret num, fum_ret_yard num, fum_ret_td num, int_ret num,
          int_ret_yard num, int_ret_td num, misc_ret num, misc_ret_yard num,
           misc_ret_td num, field_goal_att num, field_goal_made num, off_xp_kick_att num,
           off_xp_kick_made num, off_2xp_att num, off_2xp_made num, def_2xp_att num,
           def_2xp_made num, safety num, points num, punt num, punt_yard num,
           kickoff num, kickoff_yard num, kickoff_touchback num, kickoff_out_of_bounds num,
           kickoff_onside num, fumble num, fumble_lost num, tackle_solo num,
           tackle_assist num, tackle_for_loss num, tackle_for_loss_yard num,
           sack num, sack_yard num, qb_hurry num, fumble_forced num, pass_broken_up num,
           kick_punt_blocked num, first_down_rush num, first_down_pass num, first_down_penalty num,
           time_of_possession num, penalty num, penalty_yard num, third_down_att num,
           third_down_conv num, fourth_down_att num, fourth_down_conv num,
           red_zone_att num, red_zone_td num, red_zone_field_goal,
           PRIMARY KEY(team_code, game_code),
          FOREIGN KEY(team_code) REFERENCES team(team_code));''')

c.execute('''CREATE TABLE game (
          game_code num PRIMARY KEY, played date, visit_team_code num, home_team_code num,
          stadium_code num, site text,
          FOREIGN KEY(visit_team_code) REFERENCES team(team_code),
          FOREIGN KEY(home_team_code) REFERENCES team(team_code));''')


