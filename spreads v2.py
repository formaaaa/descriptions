"""
(pivots2020-2023)
After analyzing the market phases and our company's PnL data from 2020, we have identified four market regimes:
High Volatility + Trend, High Volatility + No Trend, Low Volatility + Trend, and Low Volatility + No Trend.
Our findings show that the most profitable phase is High Volatility + Trend, which consistently generates the highest
PnL per lot metric for all top four symbols. It also has the biggest absolute PnL value. High Volatility + No Trend
and Low Volatility + Trend also produce strong results, except Gold, whose PnL per lot for Low Volatility + Trend is
only slightly below zero. The least profitable phase is Low Volatility + No Trend, which yields mixed results,
but overall has a positive PnL per lot.

Then we checked how big of an impact increasing our execution spread by 1$ would have on the total PnL over the course
of 3 years. As we can see the biggest impact of spread's increase in percent terms would be in the Low Volatility +
No Trend, ranging from 8% to 46%, and allowing us to increase our profit by 11.4M. In absolute terms the biggest gain
for us would come from increasing our spreads in High Volatility + No Trend phase.

(PnL_lot dynamics)
Having that in mind we also investigated the PnL per lot and execution spread dynamics.

1. For currency crosses the execution spreads have increased on margin in 2023 for all, while the PnL per lot picture
is more varied.
For example for EURUSD in the High Volatility non trending phase, it decreased from an average of 6-8$ to -32$, whilst
for GBPUSD it flipped from negative to positive for clients

2. For Gold, execution spreads have decreased, and PnL per lot is rising for all regimes from the client's perspective.

The improved PnL per lot for Gold could be attributed to our clients' more experienced profile, as the most
active cohort at the moment has been trading with us for 13-24 months. Although we cannot control this aspect, we can
adjust the spreads.

(2023 vs expectations)
In here is our analysis of the expected and actual results in 2023.

- As we mentioned before, for currency crosses, the actual execution spread increased, and the overall result was better
by -$2.7 million tha expected, while the impact of increased spreads accounted for -$3.6 million, indicating that the
difference can be explained by spreads.
- For Gold, our actual execution spreads were lower than in past years, and overall result was worse by $22.8 million
than expected, with the negative impact of lower execution spreads amounting to -$3.8 million.

Based on these findings, we propose the following strategies:

1. Increase our spreads for Gold to account for the difference between actual and the expected execution spread that we
are losing, particularly during trending phases.
(pivots2020-2023)
2. Increase spreads during the Low Volatility + No Trend phase, as it is the most favorable for clients, and the impact
of a $1 increase in execution spread in this phase has a substantial effect on total PnL.

To implement these changes, we are working on expanding our trend indicator to help us determine in real-time the
current market phase, and based on that, having the expected returns for each, use it to adjust our spreads accordingly.
We will also conduct the same research, after the trend indicator is finished, but on an hourly basis to investigate
whether some changes to spreads could be automated.

In the future, we can also consider potentially reducing our spreads during periods that are most favorable for us,
after conducting further research to determine whether there is a positive correlation between decreased spreads and
increased trading volume during these phases.

"""