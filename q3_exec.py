"""
The primary objective of our project is to conduct a discovery on our main competitors deal execution standards.
We are focusing on three main areas: slippage, execution delay, and spread extension on news events. We have defined
three key results to measure our progress:

Key Result 1: Slippage on news data collected from at least 3 top competitors on at least 3 main symbols.
Key Result 2: Execution delay on news collected from at least 3 top competitors on at least 3 main symbols.
Key Result 3: Extension of spreads on news collected from at least 3 top competitors on at least 3 main symbols.

We will be measuring our progress by the cumulative % of data already obtained. Which should grow from the sprint 15
onwards, in 25% increments.

To achieve these results, we have planned the following steps
===============================================================================================
Sprint 13 (01.07 - 12.07)

During the planning phase, we focus on three main activities:
- Selecting the most volatile news releases based on their price impact to ensure our data collection would be meaningful.
- Calculating the budget and approximate costs for the project. Which at the moment we approximate to be - budget 12k,
and maximal spread costs should not exceed 6k.
- Selecting our top3 competitors. At the moment we think Exness, XM and AvaTrade (ICMarkets).
================================================================================================
Sprint 14 (15.07 - 26.07)

IN the next sprint we will be
- Developing a trading bot to automate the collection of information.
- Depositing accounts, and testing the trading bot to ensure it functions correctly.
====================================================================================================
Sprint 15 (29.07 - 09.08)

In sprint 15 we will launch the bot and begin to collect the data for trades of 1 lot size to start building our
dataset. Then continue with trades for 0.1 lot and 0.01 lot to see whether there are any differences how competitors
execute different trade sizes.
====================================================================================================
Sprint 16 and 17 (12.08 - 23.08)

- We will start working on automating the data collection process, directly integrating it into BigQuery. And continue
the work in Sprint 17.
====================================================================================================
Sprint 18 (09.09 - 20.09)

In the final sprint, we will:
- Analyze the collected data to propose slippage and spread extension charges based on our findings and anticipated
increases in profitability.
- Begin building a competitors scoring system based on overall trading conditions, on top of already collected
 typical spreads.
=======================================================================================================
RISKS

As for anticipated risks:
1. The trading bot might initially fail to collect data as we want it to, which could require troubleshooting and
adjustments. That's why we selected multiple news releases available during this period of time to test again.
2. We could face some technical issues with adding data to BigQuery. In this case we might need additional consultancy
with trading area developers.
3. That regular collection of this data can be costly due to spread costs we incur while testing execution on
competitors side. To mitigate this, we can focus on news releases with the highest impact, and only test each
competitor once per quarter to optimize costs.

Conclusion and Q&A

In conclusion, our goal is to amend our execution standards and our spread extensions on news, to generate additional
PnL in the most volatile times on the market. And to be ready to implement a competitors scoring system, based not only
on average spreads, but also add execution standards, and possibly swaps.
"""