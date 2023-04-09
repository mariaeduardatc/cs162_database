import calendar
from datetime import datetime, timedelta

from queries import avg_days_market, avg_selling_price, commission_calc, top5_agents, top5_offices

# creating months
beg_month = datetime(datetime.year, datetime.month, 1)
last_day = beg_month.replace(
    day=calendar.monthrange(
        beg_month.year, beg_month.month
    )[1]
)
end_month = (
    last_day + timedelta(days=1) - timedelta(seconds=1)
)

# calling quey functions
top5_offices(beg_month, end_month)
top5_agents(beg_month, end_month)
avg_selling_price(beg_month, end_month)
avg_days_market(beg_month, end_month)
commission_calc(beg_month, end_month)