import folium
import pandas

data = pandas.read_csv ("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
loc = list(data["LOCATION"])
elev= list(data["ELEV"])

def color_detector(elevation):
	if elevation < 1000:
		return "green"
	elif 1000 >= elevation <= 3000:
		return "orange"
	else:
		return "red"


map = folium.Map(location = [38.58, -99.09], zoom_start =6, tiles = "OpenStreetMap")
#the location above is the location that opens on the map


fgv = folium.FeatureGroup(name = "Volcanoes")

for lt,ln,lc, el in zip(lat,lon,loc, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 8,
    popup = "This Volcano is located at "+ lc +" and is " + str(el) 
    + " metres high." ,fill_color = color_detector(el), fill = True, 
    color = "grey", fill_opacity = 0.7))
#the location above is the location marked with circles across the map


fgp = folium.FeatureGroup (name = "Population")
   
fgp.add_child (folium.GeoJson(data = open ("world.json" , "r" , encoding = "utf-8-sig").read(),
style_function = lambda x:{"fillColor" : "green" if x ['properties']['POP2005'] < 10000000 else
"orange" if 10000000 <= x ['properties']['POP2005'] < 20000000 else "red" } ))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("index.html")
