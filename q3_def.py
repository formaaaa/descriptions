"""
Introduction

Our current objective "Real time testing of passive investment strategies based on trading off client exposure." builds
upon our Q2 goal, where we successfully back-tested options trading strategies and aims to validate our strategies in a
live market environment.

Purpose and Importance

The primary goal of this project is to ensure that our trading strategies, which have shown promising results in
backtesting, perform equally well in real-time conditions. The outcomes of this testing will provide insights
into the strategies' reliability, and potential profitability, allowing us to prepare to launch passive investment
product for our offshore clients.

Project Overview

Let me walk you through our roadmap and the key activities we have planned over the next few months:

Sprint 13 (01.07 - 12.07): Planning

We begin with comprehensive planning, where we formulate hypotheses and define success conditions, such as
1. the anticipated compounded annual growth rate -> based on quarterly performance, which is set to 10% as our original
goal from the last quarter
2. maximal draw down not more than 35%, based on back tested 2Y returns
3. maximal count of consecutive losses max 8, also based on back tested results
The reasoning behind the draw down, and consecutive losses numbers is that these are the maximum numbers we got from the
backtest. And in order to correctly measure the risk we are willing to take on each trade attempt, we need to make sure
these numbers are not dramatically exceeded.
We will also conduct research on the regulatory-compliant money flow structure from offshore clients to the SAXO
account, ensuring we meet all legal and compliance requirements.
And set up and deposit Saxo account.


Sprint 14 (15.07 - 26.07): Set Up

During this sprint, we will work closely with CySEC dealers and the holding team to work on the money flow structure.
And start executing trades based on system signals on Saxo account.
As for risks and its mitigation:
To mitigate relatively short period for testing strategies, we will increase the number of symbols to 4:
EURUSD, GBPUSD and NAS100 in addition to Gold. In the previous quarter we have backtested Gold on data from exchange,
and in addition we also back tested those symbols, using approximation of option premium prices based on real time
market data, and historical prices. And the back tests for all those symbols also look very favourable, using exactly
the same input settings as for Gold.

Sprint 15 - 17 (29.07 - 06.09): Live Tests

Over the subsequent sprints, we will continuously test both strategies and start analyzing the results against our
predefined success metrics.
Parallel we will work on finalizing the money flow structure, that we anticipate to have ready in 16th Sprint.

Sprint 18 (09.09 - 20.09): Final Analysis

In the final phase, we will conduct final results analysis, compare the real time results to back tested results, and
look for any indications that the real environment performance differs in any way from the expected performance.
Additionally, we will start to work on anticipated client base, and the amount of deposits, and also on the amount of
projected fees from the product. We will also make a proposal of product conditions, like: minimal investment amount,
management fee, success fee and lock - up period.

Conclusion

To sum up, we think that the successful implementation of this product will diversify our trading offerings,
provide us with some passive income from management fees, and potentially from success fees. While also keeping our
risks to the minimum, as all the market risk from using those strategies will be on clients, since we will use their
money to trade.
"""