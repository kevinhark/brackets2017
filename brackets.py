import numpy as np
import datetime
from teams import seeds
import r64, r32, s16 #, e8, f4, champ

def score(rounds,file):
    scores = np.zeros((len(rounds),len(rounds[0].picks.keys())));
    file.write('<h1>Scores</h1>\n')
    file.write('<table id="t01">\n')
    file.write('<tr>\n')
    file.write('<th>\n')
    file.write('Round')
    file.write('</th>\n')
    
    for user in rounds[0].picks.keys():
        file.write('<th>\n')
        file.write('%s' % user)
        file.write('</th>\n')
    file.write('</tr>\n')

    for m in range(len(rounds)):
        file.write('<tr>\n')
        file.write('<th>\n')
        file.write('%s' % rounds[m].name)
        file.write('</th>\n')
        for p,user in enumerate(rounds[m].picks.keys()):
            for n in range(len(rounds[m].winners)):
                if rounds[m].winners[n] == rounds[m].picks[user][n]:
                    scores[m,p] = scores[m,p] + seeds[rounds[m].winners[n]] + rounds[m].weight

            file.write('<td>\n')
            file.write('%i' % scores[m,p])
            file.write('</td>\n')
    file.write('<tr>\n')
    file.write('<th>\n')
    file.write('Total')
    file.write('</th>\n')
    for p,user in enumerate(rounds[m].picks.keys()):
        file.write('<td>\n')
        file.write('<b>%i</b>' % np.sum(scores[:,p]))
        file.write('</td>\n')

    file.write('</table>\n')


def print_round(round,file):
    file.write('<h1>%s</h1>\n' % round.name)
    file.write('<table id="t01">\n')
    
    file.write('<tr>\n')
    file.write('<th>Game winner</th>\n')
    for user in round.picks.keys():
        file.write('<th>%s</th>\n' % user)
    file.write('</tr>\n')

    for n in range(len(round.winners)):
        file.write('<tr>\n')
        file.write('<th>%s</th>\n' % round.winners[n])
        for user in round.picks.keys():
            file.write('<td>\n')
            if round.winners[n] == None:
                file.write('<font color="black">')
            elif round.winners[n] == round.picks[user][n]:
                file.write('<font color="green">')
            else:
                file.write('<font color="red">')
            file.write('%i %s' % (seeds[round.picks[user][n]],round.picks[user][n]))
            file.write('</font></td>\n')
        file.write('</tr>\n')
    file.write('</table>\n')

def print_html_begin(file):
    file.write('<html><head><title>2017 NCAA Tourney Brackets</title></head><body>\n')
    file.write('''
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        padding: 5px;
        text-align: left;
        }
        table#t01 tr:nth-child(even) {
        background-color: #eee;
        }
        table#t01 tr:nth-child(odd) {
        background-color:#fff;
        }
        table#t01 th	{
        background-color: #fff;
        color: black;
        }
        </style>
        ''')

def print_html_end(file):
    file.write('<p>Updated: ' + str(datetime.datetime.now()) + ' Central DST</p>\n')
    file.write('</div></html></body>\n')

rounds = (s16, r32, r64,) #(champ, f4, e8, s16, r32, r64,)

if __name__ == '__main__':
    file = open('index.html','w')
    print_html_begin(file)
    score(rounds,file)
    
    for round in rounds:
        print_round(round,file)
    print_html_end(file)
