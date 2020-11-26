#!/usr/bin/env python3
import json
import folium
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def home():
    """
        Rendering the home page
    """
    m = Map() # Create map html
    return render_template('index.html') # pulls map html using jinja2

class Map(object):
    """ 
        Class to create map html 
    """
    def __init__(self):
        # Initialize
        self.makeMap()
    
    def makeMap(self):
        # Create base map
        self.map1 = folium.Map(location = [20, 7], tiles='CartoDB dark_matter', zoom_control=False, zoom_start = 3)
        self.importPoints()
    
    def importPoints(self):
        # Import data to put on base map from json
        with open('./static/points.json') as f:
            self.data = json.load(f)

        for point in self.data.keys():
            # For each data point
            p = self.data[point]
            # Extract info into html
            popup_text = f"<h4 style=\"color:#f71e5b;\">{p['pop_up_title']}</h4><h5 style=\"color:#f71e5b;\">{p['pop_up_subtitle']}</h5><h6>{p['pop_up_text']}</h6>"
            pup = folium.Popup(html=popup_text, max_width=250)
            # Create marker
            folium.Marker([p['lat'], p['lon']], popup=pup, tooltip=p['tooltip'], icon=folium.Icon(color='lightblue', icon=p['icon'], prefix='fa', icon_color='#f71e5b')).add_to(self.map1)

        self.saveMap()
        
    def saveMap(self):
        # Output map with data as html file
        self.map1.save('./templates/map.html')
        return self

@app.route('/map-portfolio')

def map_page():
    """
        Rendering the home page
    """
    m = Map() # Create map html
    return render_template('index.html') # pulls map html using jinja2


if __name__ == '__main__':
   app.run()
