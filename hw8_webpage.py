from netCDF4 import Dataset #access netcdf data
#import plotly.plotly as py
import plotly.offline as py
import plotly.graph_objs as go #use plotly

#Collect user input for plotly API
#username = raw_input("Enter your plotly user name: ")
#API = raw_input("Enter your plotly API key: ")

#py.sign_in(username, API) 

with Dataset("tmin.nc", "r") as tmin:
    tempMinJ = tmin.variables["tmin"][0]
    tempMinA = tmin.variables["tmin"][91]
    tempMinY = tmin.variables["tmin"][182]
    tempMinO = tmin.variables["tmin"][274] 
    
#min temps at certain days of year
#of course I would loop this through every day of the year if I wasn't just doing four for now...
#plot the heatmaps for tmin with the same zmin and zmax values
data1 = [go.Heatmap(
    z = tempMinJ,
    zmin = -7,
    zmax = 27,
    )]

data2 = [go.Heatmap(
    z = tempMinA,
    zmin=-7,
    zmax=27,
    )]

data3 = [go.Heatmap(
    z = tempMinY,
    zmin=-7,
    zmax=27,
    )]

data4 = [go.Heatmap(
    z = tempMinO,
    zmin=-7,
    zmax=27,
    )]

#Creates divs from plots
plot1 = py.plot(data1, include_plotlyjs=False, output_type='div')
plot2 = py.plot(data2, include_plotlyjs=False, output_type='div')
plot3 = py.plot(data3, include_plotlyjs=False, output_type='div')
plot4 = py.plot(data4, include_plotlyjs=False, output_type='div')

#Beginning of webpage 
html_str1 = """
<html>
<head><b>Daymet 2000 Minimum Temperature Heat Maps of Tucson, AZ<b/></head>
<p>
<p>
<body>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
"""

#End of webpage
html_str2 = """
</body>
</html>
"""

#Writes html file output
html_file = open('webpage.html', 'w')
html_file.write(html_str1)
html_file.write(plot1)
html_file.write(plot2)
html_file.write(plot3)
html_file.write(plot4)
html_file.write(html_str2)
html_file.close()