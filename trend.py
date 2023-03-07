"""
In addition to above two standard deviation daily moves analysis, that we presented last week we researched the price
trends of our TOP4 major instruments, in an attempt figure out how the clients are doing when the markets are trending,
and how do they do when the markets are ranging, without clear trend in place.

The investigated period was from 4.2015 to 2.2023 on daily candles, for EURUSD,
GBPUSD, XAUUSD and USDJPY, that were responsible for 70% of the realized profit dating back to 2019

We wanted to focus on periods when markets are in a clear short term trends, highlighted here in green, when high risk
strategies like Martingale and Grid have a hard time working

Periods when instruments were trending were identified using the Choppiness Index, which is a volatility indicator
designed to determine if the market is trading sideways or trading within a trend in either direction.

Then we investigated each symbol for the percent of time that it was trending, and the realized PnL for the company, and
it's percent share depending on the phase. We also calculated the number of trending periods and their average length.
Then we checked for the seasonality, using both number of trending days in each month, and the realized PnL.

The Top4 instruments were trending on average 33% of the time, and that is consistent over a different time periods.
In periods when instruments were trending client's realized approx 68% of our profit dating back to 2019.
The average duration of the trending phase was 22 days.

As for the seasonality, we can see that these trending periods are spread pretty evenly through the 1-3Q, with fewer
trending days in 4Q. Based on our realized PnL and excluding the day the war started we can see that the best months
for us are from February to April, July, September, and November, while the worst are October, and December.

When we check last 3 months, we see that EURUSD, GBPUSD, and USDJPY had 0 trending periods according to the methodology
we used, and only XAUUSD had 29 out of 60 days when it was trending, and GOLD was responsible for 74% of the profit for
this time, while on average it is 42%. The total realized PnL for Top4 instruments in this time period was 31M, while the average for 3 month window
based on historical data is 60M. Also, our realized PnL in last 3 months in the trending phase was just 16M compared to
the average of 40M.

The reason behind this might be the price action of the US dollar, which is either quote or base currency for all Top4
symbols. For the last 3 months the price is virtually unchanged with rather small range and no major short term moves
in any direction.

So, to sum up, this combined with twice fewer number of above 2 standard deviation moves tells us that these last 3
months differed from what we could've expected based on historical data. But judging from seasonality, and the reversion
to the mean for number of volatile days we can expect the period from March to September to be much better in terms
of our profitability.


"""