import folium

map = folium.Map(location=[20.5937, -78.9629], zoom_start=4, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[30, -70], [27, -60]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi there", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")
