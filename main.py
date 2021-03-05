import pandas as pd
import urllib3 as urllib
import urllib.request as urllib2
import json
import glob
import IPython.display
import re
from altair_saver import save
import altair as alt
import newLambda
from newLambda import chartname
import chart2s3
from chart2s3 import keyandval



chart = "chart.png"
bucket = "chickinlickin"
chartname(chart)

keyandval(chart, bucket)
url = "https://%s.s3.amazonaws.com/%s" % (bucket, chart)
print(url)
