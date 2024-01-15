"""
(pivots2020-2023)
We divided market regimes into four based on The Choppiness Index and the historical volatility median on a daily basis:
High Volatility + Trend, High Volatility + No Trend, Low Volatility + Trend, and Low Volatility + No Trend.

After analyzing this phases and our company's PnL data from 2020 to February 2023, our findings show that the most
profitable phase is High Volatility + Trend, which consistently generates the highest PnL per lot metric for all top
four symbols. It also has the biggest absolute PnL value. High Volatility + No Trend and Low Volatility + Trend also
produce strong results in PnL per lot terms, except Gold, whose PnL per lot for Low Volatility + Trend is only slightly
below zero. The worst phase is Low Volatility + No Trend, which yields mixed results, but overall has a positive PnL
and PnL per lot for clients.

Then we checked how big of an impact increasing our execution spread by 1$ would have on the total PnL over the course
of 3 years. As we can see the biggest impact of spread's increase on total PnL in percent terms would be in the Low
Volatility + No Trend, ranging from 8% to 46% with the average of 33%, and allowing us to increase our profit by 11.4M.
In absolute terms the biggest gain for us would come from increasing our spreads in High Volatility + No Trend phase.

(PnL_lot dynamics)
Having that in mind we also investigated the PnL per lot and execution spread dynamics.

1. For currency crosses the execution spreads have increased on margin in 2023 for all, while the PnL per lot picture
is more varied.
2. For Gold, execution spreads have increased for no trending phases, but decreased for trending phases,
and PnL per lot is rising for all regimes from the client's perspective.

The improved PnL per lot for Gold could potentially be attributed to our clients' more experienced profile, as the most
active cohort at the moment has been trading with us for 13-24 months and the second most active from 25-36 months.

(2023 vs expectations)
In here is our analysis of the expected and actual results in 2023.

- As we mentioned before, for currency crosses, the actual execution spread increased, and the overall result was better
by -$2.7 million tha expected, while the impact of increased spreads accounted for -$3.6 million, indicating that the
difference can be explained by spreads.
- For Gold, our actual execution spreads were lower than in past years for trending phases, and higher for non trending,
and overall result was worse by $22.8 million than expected, with the negative impact of lower execution spreads
amounting to -$3.8 million.

Based on these findings, we can see that the increased spreads on crosses are working fine we see no volume decrease,
so we should continue to watch it, and perhaps do some marketing surveys what the client's think about our current spreads.
We plan to keep our execution spreads for Gold in the 29-30 range, to account for the PnL that we were losing on lower
spreads in the past

As for tasks in the pipeline, we are working on expanding our trend indicator and the model for volatility to help us
determine in real-time the current market phase, and based on that, having the expected returns for each phase,
use it to adjust our spreads accordingly. We will also do similar research, but on an hourly basis to investigate
whether some changes to spreads could be automated. Moreover, we are in process of developing a model to predict the
client's expected behavior and PnL, based on the client's risk profile

In the future, we can also consider potentially reducing our spreads during periods that are most favorable for us,
after conducting further research to determine whether there is a positive correlation between decreased spreads and
increased trading volume during these phases.

"""