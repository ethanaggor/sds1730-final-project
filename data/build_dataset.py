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

SUFFIXES = ['STHPI', 'UR', 'PCPI', 'POP']
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd=2000-01-01&coed=2012-12-31"


def download():
    raw_dir = os.path.join(os.path.dirname(__file__), 'raw')
    os.makedirs(raw_dir, exist_ok=True)

    for st in STATES:
        for suffix in SUFFIXES:
            series = f"{st}{suffix}"
            out_path = os.path.join(raw_dir, f"{series}.csv")
            if os.path.exists(out_path):
                continue
            try:
                urllib.request.urlretrieve(FRED_URL.format(series=series), out_path)
                print(f"Downloaded {series}")
            except Exception as e:
                print(f"FAILED {series}: {e}")
            time.sleep(0.2)

    print(f"\nDone. {len(STATES) * len(SUFFIXES)} series in {raw_dir}/")


if __name__ == '__main__':
    download()
