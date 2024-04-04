"""
The goal objective is to ensure competitive trading conditions on Indices and Energies and increase the company's
profitability
Our KR1 is to increase the volume by 22.5% compared to quarterly average from last year on selected instruments
KR2 is to Increase the total PnL after IB commission by 302k

WHAT WAS ALREADY DONE
We did a competition analysis in 10 GEOs, the top GEOs India, Indonesia, Malaysia and Pakistan, and 6 new GEOs
Emirates, Nigeria, Philippines, South Africa, Brazil and Thailand.
LEVERAGE
When we look at the summary for the main Indices and Energies, we can see that the average leverage that the
competitors offer is much higher than ours. For Indices, it's around 400, compared to our 50, and for energies it's
close to 300, whereas we offer 100.
SPREADS
For spreads we can see that we are only competitive on German DAX, and close to competition on Nasdaq. For the rest of
the symbols like Crude Oil, Brent, SPX, Dow Jones and Nikkei we are very far from the main competitors.

ROADMAP
The roadmap for the goal is as follows
IN THE 2nd SPRINT
-we will make a final decision regarding which instruments will be included, and what will be the new trading conditions
for now the plan is to increase the leverage on main indices (Nasdaq, Dow Jones, SPX, DAX and Nikkei) and Brent and
Crude Oil to 200, and reduce spreads for the following symbols: NAS100 -2, SPX500 -5, US30 -10, XBRUSD -1, XTIUSD -1
-and start working on dividend adjustment for Indices with Change Team

IN THE 3rd SPRINT
we want to implement the dividend adjustment for indices, decide with Antifraud Team how to track swap abusing clients,
apply changes in leverage and spreads for regular instruments and their .Daily equivalents, for them not to lose their
competitive advantage, and send notifications to clients. We will also have a promo featuring Nasdaq, where we will
decrease spreads by -15%.

IN THE SUBSEQUENT SPRINTS
We want to come up with metrics to track the results, manually analyze them, and adjust our trading conditions as
needed, this includes adjusting trading conditions on currently selected instruments, and also possibly adding new ones,
and also keep track of swap abusers

RISKS
as for the risks, we outlined three main risks:
-Increased exposure due to higher leverages, that needs to be monitored
-Increased risk of swap abuse due to higher leverage, in here we will work with AF team to implement their workflow to
catch early potential abusers
-That for now we are lacking a dividend adjustment mechanism, which will be developed with Change Team during the goal

QUESTIONS AND CONCERNS
As for the Questions and concerns, we need to investigate whether the anticipated increased volume on indices and
energies, is taking share from our other TOP20 symbols, and what is the profitability of the new volume in contrast to
volume on TOP20, not to switch clients to less profitable instruments
"""