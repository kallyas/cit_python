"""
get and plot covid data for us states
"""

import requests
import matplotlib.pyplot as plt
from datetime import datetime
import sys

us_states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def get_data(state):
    """
    get data for a given state
    """
    url = "https://covidtracking.com/api/v1/states/{}/daily.json".format(state)
    r = requests.get(url)
    data = r.json()
    if not data:
        print("no data for {}".format(us_states[state.upper()]))
        sys.exit(1)
    state_name = data[0]['state']
    return data, state_name


def plot_data(data, state_name=None):
    """
    plot data for a given state
    """
    dates, cases, deaths = [], [], []
    recovered, negative = [], []

    for d in data:
        dates.append(datetime.strptime(str(d['date']), "%Y%m%d"))
        # check if data is null and replace with 0
        cases.append(d['positive'] if d['positive'] else 0)
        deaths.append(d['death'] if d['death'] else 0)
        recovered.append(d['recovered'] if d['recovered'] else 0)
        negative.append(d['negative'] if d['negative'] else 0)

    plt.subplot(2, 1, 1)
    # pie chart
    labels = ["cases", "deaths", "recovered", "negative"]
    sizes = [sum(cases), sum(deaths), sum(recovered), sum(negative)]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0.1, 0.1, 0.1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title("{} covid data".format(state_name))
    plt.legend()


    plt.subplot(2, 1, 2)
    # line chart for all data(cases, deaths, recovered, negative)
    plt.plot(dates, cases, label="cases")
    plt.plot(dates, deaths, label="deaths")
    plt.plot(dates, recovered, label="recovered")
    plt.plot(dates, negative, label="negative")
    plt.legend()
    plt.title("{} covid data".format(state_name))

    plt.show()


def main():
    """
    main function
    """
    if len(sys.argv) != 2:
        print("usage: covid.py <state>")
        sys.exit(1)
    state = sys.argv[1]
    data, state_name = get_data(state)
    plot_data(data, us_states[state_name])


if __name__ == "__main__":
    main()