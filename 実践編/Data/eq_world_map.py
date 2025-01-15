import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# データの構造を調査する
filename = 'Data\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'Data\data\\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'] ['mag']
    lon = eq_dict['geometry'] ['coordinates'][0]
    lat = eq_dict['geometry'] ['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='世界の地震')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')