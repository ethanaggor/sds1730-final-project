"""
Downloads raw state-level time series from FRED into data/raw/.

FRED series per state ({ST} = two-letter abbreviation):
  {ST}STHPI   FHFA All-Transactions House Price Index (quarterly)
  {ST}UR      Unemployment Rate, seasonally adjusted (monthly)
  {ST}PCPI    Per Capita Personal Income (annual)
  {ST}POP     Resident Population, thousands (annual)

Downloads via FRED's public CSV endpoint (no API key required):
  https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES&cosd=START&coed=END

Run: python data/build_dataset.py
"""

import os
import time
import urllib.request

STATES = [
    'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA',
    'HI','ID','IL','IN','IA','KS','KY','LA','ME','MD',
    'MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
    'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC',
    'SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'
]

SERIES_SUFFIXES = ['STHPI', 'UR', 'PCPI', 'POP']
START = '2000-01-01'
END = '2012-12-31'


def download():
    raw_dir = os.path.join(os.path.dirname(__file__), 'raw')
    os.makedirs(raw_dir, exist_ok=True)

    for st in STATES:
        for suffix in SERIES_SUFFIXES:
            series_id = f"{st}{suffix}"
            out_path = os.path.join(raw_dir, f"{series_id}.csv")

            if os.path.exists(out_path):
                continue

            url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={START}&coed={END}"
            try:
                urllib.request.urlretrieve(url, out_path)
                print(f"Downloaded {series_id}")
            except Exception as e:
                print(f"FAILED {series_id}: {e}")

            time.sleep(0.2)

    print(f"\nDone. Raw files in {raw_dir}/")


if __name__ == '__main__':
    download()
