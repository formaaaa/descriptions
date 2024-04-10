"""
The goal objective is to come up with a passive investment product that we can offer to clients, by validating 3
strategies of hedging clients' exposure using options
Our KR is to achieve back-tested historical return on those options trading strategies of minimum 10% yearly

PREPARATIONS
At the beginning we plan to formulate hypothesis, define success conditions, like ROI, hit ratio, maximal DD, maximum
stagnation period, Sharpe ratio, and find the options data provider, when we successfully connect him, then
download and filter the necessary data, and start testing

Hypothesis 1:
Is that when the total aggregated PnL of either long and short side becomes positive, we buy options in the same direction.
The logic behind this is that when clients' become profitable on one leg, we want to hedge it, so
the potential profits they might gain will be offset by our profit on options. While at the same time, we allow losing
side to be unhedged.

Hypothesis 2:
Is a modified version of Hypothesis 1, but we exclude clients that are internally hedged. So if a client is hedged, we
exclude his PnL from calculations on both sides, so we leave only unhedged PnL. The rest of the logic is same as in
Hypothesis 1.

Hypothesis 3:
Is when the client's net positioning becomes overly extended to one side, we open a contrarian position.
The thresholds are measured by 1.5 standard deviation from one-month moving average (red and yellow lines),
and by 85th percentile of the rolling 3 months exposure (orange and green lines).
So, for long positions they need to be above 1.5 st. dev. from the average, and in the top 15% extreme long values from
the last 3 months, and for short below 1.5 st.dev. and in the 15% of the lowest values from last 3 months.
If the clients' net positioning exceeds both of those values to the long or short side, that tells us that they became
overly bullish or bearish, and we buy options in the opposite direction.
The logic behind this is that majority of clients lose, they are overly optimistic and overly leveraged at some points,
and the markets adjust that positioning by moving in the opposite direction, liquidating positions or forcing clients
to close.

PROPOSAL
When we successfully validate those hypothesis, or some of them, we will propose a trading strategy based on clients'
positioning data, formulate the conditions for a passive investment product, like min investment, success fee,
management fee, and lockup period. And start working on preparing brokers setups for a live test.

RISKS
-first one is that even most detailed backtest doesn't guarantee the future results
-historical data accuracy, but we will mitigate it by checking several data providers
"""