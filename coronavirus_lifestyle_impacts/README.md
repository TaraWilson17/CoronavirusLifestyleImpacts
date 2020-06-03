## How to run

At current package root, run the following executable:
```
./coronavirus_lifestyle_impacts.py [-h] [-s STATE] [-k KEYWORDS]
```

### Usage
```
$ ./coronavirus_lifestyle_impacts.py --help
usage: coronavirus_lifestyle_impacts.py [-h] [-s STATE] [-k KEYWORDS]
Coronavirus Lifestyle Impacts CLI
optional arguments:
  -h, --help            show this help message and exit
  -s STATE, --state STATE
                        the US state to pull the data from. Can take either
                        full name and abbreviation. Default: "Washington"
  -k KEYWORDS, --keywords KEYWORDS
                        the comma delimited search keyword string. Default:
                        "Bars near me, Home workouts"
```

### Loading into PowerBI

1. Download powerBIdesktop from here. https://powerbi.microsoft.com/en-us/desktop/
2. Import the data from the Coronavirus Lifesytle Impacts into PowerBI. 
3. Publish the dashboard on to a workspace.
