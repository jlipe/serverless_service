This is my microservice for CS 361.

This service is setup so every 15 minutes the crawl.py function is executed and saves headline results into a DyanmoDB database.

The API runs using the serverless framework and the endpoints are for displaying recent headlines, and generating a quiz that includes a random set of headlines. All the logic for handling the API requests is in handler.js. The logic for what triggers the handler.js to actually run is in the serverless.yml file. The serverless.yml file is a description of how this should be deployed into AWS and makes deploying it (and testing it offline) much easier.

The crawl.py function is working as a standalone lambda funciton hosted on AWS with the required dependencies installed there. Currently this serverless framework is not setup to handle the crawl.py function and it is only in this repo as a reference.

# Headline Service API Reference
## Base URL
`https://s9goa8paxj.execute-api.us-east-1.amazonaws.com`

### Headlines Endpoint
`GET /headlines`

#### NOTE: There must be a query string with sources in it. So `/headlines` must be followed with a `?sources=`

| Paramater | Description | Optional |
| ------ | ------ | ------ |
| Sources | Comma seperated list of sources | No
| Limit | Per source article limit | Yes (defaults to 5)

#### NOTE: The sources must be capatlized and spelled exactly as described in the possible sources below
#### The comma seperated format would look like sources=DailyFX,NY+Times,Mother+Jones
#### Spaces in the source name are replaced with a plus sign

#### Possible Sources
| Source |
| ------ |
| Fox News |
| CNN | 
| Breitbart |
| Mother Jones | 
| NY Times |
| DailyFX | 
| CNBC |
| Financial Times |
| Crypto News |
| PC Gamer |
| Kotaku |

#### Response
[
    {"headline": "Investigators Find Gaps in White House Logs of Trump’s Jan. 6 Calls",
    "source": "NY Times",
    "time", "2022-02-10T21:45:14.105727"},
    {...},
    {...}
]


#### Example Request
`GET https://s9goa8paxj.execute-api.us-east-1.amazonaws.com/headlines?sources=DailyFX&limit=3`

#### Example Response
[
    {
    headline: "Nasdaq 100 Dives as 40-Year High Inflation Boosts Case for Aggressive Rate Hikes",
    source: "DailyFX",
    time: "2022-02-10T22:00:20.320921"
    },
    {
    headline: "Gold Price Stages Five-Day Rally for First Time Since November",
    source: "DailyFX",
    time: "2022-02-10T21:30:16.976095"
    },
    {
    headline: "Australian Dollar Technical Analysis: Failure at Significant Resistance - Setups in AUD/JPY, AUD/USD",
    source: "DailyFX",
    time: "2022-02-10T20:00:16.168286"
    }
]
