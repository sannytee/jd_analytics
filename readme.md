# Justdice Analytics
This project is an analytics project to help the team at JustDice to understand the overall financial situation of the 
company as well as any relevant findings that can be driven fom the data. The project is built using Python and Mode Analytics.

### Financial KPI Dashboard

The KPI Dashboard is a web application that allows users to view and interact with data from the Justdice project. 
The dashboard is built using Mode and is available at [https://app.mode.com/taiwo_justdice/reports/d39f999ed2bd](https://app.mode.com/taiwo_justdice/reports/d39f999ed2bd).

**NB**: An account on mode is required to view the dashboard.


### Assumptions
1. The data provided is an export of production data. Hence, the python functions are written to load the data to a postgres database (Data warehouse). This will be the ideal case in a production setting. The transformations are done using sql queries and can be view on Mode Analytics.
2. From the [Monthly Ad Spend Over Time](https://app.mode.com/taiwo_justdice/reports/d39f999ed2bd/viz/0f8972e3f382), we can see that network id 26 and 1111 had zero cost in total ad spending all through the year. This is probably due to missing data. So I assumed that the cost for these networks is zero.



### Conclusion
The company's success depend largely on the efficiency of the user acquisition strategy, the retention rate of the users and the quality of the users acquired. 
As mentioned in the case study, higher fees do not necessarily translate to higher profits.

To optimize revenue generation, the following should be considered:
1. review of network performance and fees adjustment to ensure the company is acquiring high quality users at a reasonable cost.
2. If possible, analyse the performance of partner apps to ensure they are providing a positive user experience and are not driving users away.
3. Product analytics: Continuous analysis of products and optimize to keep users engaged and attract new users.

