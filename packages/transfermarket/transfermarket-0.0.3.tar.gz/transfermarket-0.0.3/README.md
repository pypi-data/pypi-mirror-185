# transfermarkt rev: v0.0.3
A python module for retrieving information from https://www.transfermarkt.com.

![Test](https://github.com/ocrosby/transfermarkt/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ocrosby/transfermarkt/badge.svg?branch=main)](https://coveralls.io/github/ocrosby/transfermarkt?branch=main)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Installation
```bash
pip install -e .
```

## Usage

```python
from transfermarket.market import Market
```

### Get a list of all clubs

```python
from transfermarket.market import Market

clubs = Market.get_clubs()
```

## Parsing of commit logs
The semver level that should be bumped on a release is determined by the commit messages since the last release. In 
order to be able to decide the correct version and generate the changelog, the content of those commit messages must 
be parsed. By default, this package uses a parser for the Angular commit message style:

```text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

## Using the command line interface

The transfermarkt appears to be a higharchy of data started with what they refer to as a competition.
Each competition can be thought of as a league or set of clubs.

List all the competitions from the transfermarkt.

```bash
$ market competition list
```

Output: 

```text
Competition(id='GB1', name='Premier League', country='England', total_clubs=20, total_players=512, avg_age=27.0, foreigners_percent=66.6, total_value='€9.74bn', tier='First Tier')
Competition(id='ES1', name='LaLiga', country='Spain', total_clubs=20, total_players=501, avg_age=27.6, foreigners_percent=41.9, total_value='€4.86bn', tier='First Tier')
Competition(id='IT1', name='Serie A', country='Italy', total_clubs=20, total_players=582, avg_age=26.2, foreigners_percent=62.2, total_value='€4.59bn', tier='First Tier')
Competition(id='L1', name='Bundesliga', country='Germany', total_clubs=18, total_players=511, avg_age=25.8, foreigners_percent=52.3, total_value='€4.17bn', tier='First Tier')
...
```

Each competition is comprised of a set of teams.  Each team has an identifier so for example the Premier League
has the identifier GB1.  You can get a list of all the teams in the Premier League by using the following command.

```bash
$ market team list GB1
```

Output:

```text
<Team(id='11', title='Arsenal FC')>
<Team(id='405', title='Aston Villa')>
<Team(id='989', title='AFC Bournemouth')>
<Team(id='1148', title='Brentford FC')>
<Team(id='1237', title='Brighton & Hove Albion')>
<Team(id='631', title='Chelsea FC')>
<Team(id='873', title='Crystal Palace')>
<Team(id='29', title='Everton FC')>
<Team(id='931', title='Fulham FC')>
<Team(id='399', title='Leeds United')>
<Team(id='1003', title='Leicester City')>
<Team(id='31', title='Liverpool FC')>
<Team(id='281', title='Manchester City')>
<Team(id='985', title='Manchester United')>
<Team(id='762', title='Newcastle United')>
<Team(id='703', title='Nottingham Forest')>
<Team(id='180', title='Southampton FC')>
<Team(id='148', title='Tottenham Hotspur')>
<Team(id='379', title='West Ham United')>
<Team(id='543', title='Wolverhampton Wanderers')>
```

Now note that each team also has an identifier.  You can get a list of all the players on a team 
(for example Arsenal - with identifier 11) by using the following command.

```bash
$ market player list 11
```

Output:

```text
<Player(id='433177', name='Bukayo Saka', gender='Male', position='Midfielder')>
<Player(id='363205', name='Gabriel Jesus', gender='Male', position='Forward')>
<Player(id='316264', name='Martin Ødegaard', gender='Male', position='Midfielder')>
<Player(id='655488', name='Gabriel Martinelli', gender='Male', position='Forward')>
<Player(id='495666', name='William Saliba', gender='Male', position='Defender')>
<Player(id='335721', name='Ben White', gender='Male', position='Defender')>
<Player(id='435338', name='Gabriel Magalhães', gender='Male', position='Defender')>
<Player(id='230784', name='Thomas Partey', gender='Male', position='Midfielder')>
<Player(id='392765', name='Emile Rowe', gender='Male', position='Midfielder')>
<Player(id='203853', name='Oleksandr Zinchenko', gender='Male', position='Defender')>
<Player(id='300716', name='Kieran Tierney', gender='Male', position='Defender')>
<Player(id='427568', name='Aaron Ramsdale', gender='Male', position='Goalkeeper')>
<Player(id='537598', name='Fábio Vieira', gender='Male', position='Midfielder')>
<Player(id='111455', name='Granit Xhaka', gender='Male', position='Midfielder')>
<Player(id='331560', name='Takehiro Tomiyasu', gender='Male', position='Defender')>
<Player(id='340324', name='Eddie Nketiah', gender='Male', position='Forward')>
<Player(id='381967', name='Albert Lokonga', gender='Male', position='Midfielder')>
<Player(id='253341', name='Rob Holding', gender='Male', position='Defender')>
<Player(id='668268', name='Marquinhos None', gender='Male', position='Forward')>
<Player(id='160438', name='Mohamed Elneny', gender='Male', position='Midfielder')>
<Player(id='340325', name='Reiss Nelson', gender='Male', position='Forward')>
<Player(id='425306', name='Matt Turner', gender='Male', position='Goalkeeper')>
<Player(id='112988', name='Cédric Soares', gender='Male', position='Defender')>
```

## References
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Transfermarkt](https://www.transfermarkt.com)
- [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
- [Packaging Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)
- [GitHub bot to enforce semantic PRs](https://github.com/apps/semantic-pull-requests)