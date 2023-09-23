from app.short import URLShortner

short = URLShortner
url = "https://www.databricks.com/resources/demos/tutorials/lakehouse-platform/full-delta-live-table-pipeline?itm_data=demo_center"
short_url = short.swap_letters(url)
print('This is the url: ', short_url)

short.swap_letters('CENTURION', 2)