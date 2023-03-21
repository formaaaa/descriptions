"""
After dividing the phases of the market into 4 regimes: High Volatility + No Trend, High Volatility + Trend,
Low Volatility + No Trend and Low Volatility + Trend. And checking the company's PnL data from 2020, we can see that
by far the best phase is High Volatility + Trend which has the biggest PnL per lot metric for all top4 symbols.  In
terms of PnL per lot good phases are also High Volatility + No Trend and Low Volatility + Trend. with exception to Gold
which has expected PnL per lot for Low Volatility + Trend very close to zero. The worst phase is Low Volatility + No
Trend, which has the expected PnL per lot positive for Gold and EURUSD, and slightly negative for GBPUSD and USDJPY, but
in absolute terms positive.

Taking into consideration the percentage of occurrences and the volume generated in these phases we cen see that we make
basically all our profit in Volatile phases.

We also investigated the PnL per lot and execution spreads dynamics, and The most interesting takeaways are:
- execution spreads increased on margin in 2023 for all of our crosses, while the PnL per lot picture was more mixed
- for GOLD execution spread decreased, and the PnL per lot is rising for all regimes from the client's
perspective.

The fact that the clients are doing better in terms of PnL per lot for Gold, can be the possibly explained by the
more experienced profile on average, as the cohort that trades with us for 12-24 months is the most active one at the
moment. As we cannot control this, we can control the spreads.

In this table we can see how much the expected result differed from the actual in 2023, and how much can be attributed
to execution spreads difference from the average:
- as for crosses the result was better by -2.7M, while the spreads increase impact accounted for -3.6M, so all the
difference can be explained by spreads
- as for Gold our result was worse by 22.8M than expected, and the negative impact of lower execution spreads was -3.8M

So the main ideas based on this data is that:
1. we should increase our spreads for Gold, to account for the difference from the expected execution spread that we are
losing, especially in the trending phases
2. and also to increase the spreads in the Low Volatility + No Trend phase, as it is the most favourable one for the
clients, and the % impact of 1$ increase of execution spread in this phase has a pretty sunstantial impact on PnL.

To do this we are working on the trend indicator, that will help us determine in real time in which market phase
are we, and also do this research on the hourly basis.

"""