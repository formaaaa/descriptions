"""
OK, so we have just a few unfinished ones

1. Is that the issue with Other accounts in Elastic persists, I asked Zhenya about it yesterday, he will try to fix it
tomorrow or the next week

2. Is the problem we experienced with Singaporean and Swedish Stocks, that the profit and margin rates were calculated
as 0 in MT5, so basically clients could open any size they wanted as the required margin was 0. Fortunately, the PnL
was also 0 for each trade, so it could have been used only for generating volume, but none of these clients was under
IB. Yesterday we added Forex Exotic symbols to all clients groups, so the conversion could be made.

3. So because of these issue we have some proposals on how to detect such cases in the future
-1st is already done, Igor added a new table to Stocks dashboard in Elastic, that will be sorted by volume, so even if
there is no PnL but large volume we will spot it
-2nd is to create a query, that will be run weekly or daily that will give us the list of orders where any of the
profit or margin conversion rate was 0
-3rd is a report in Amplitude

4. And the last one is the pending report for the Platinum client, we are waiting for the clarification for which
account the client wants the report, and the translation team is ready to start on 29th AUG
"""