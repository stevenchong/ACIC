from netCDF4 import Dataset #access netcdf data
import plotly.plotly as py
import plotly.graph_objs as go #use plotly

#Collect user input for plotly API
username = raw_input("Enter your plotly user name: ")
API = raw_input("Enter your plotly API key: ")

py.sign_in(username, API) 

with Dataset("/data/tmin.nc", "r") as tmin:
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
py.image.save_as(data1,"data1.png")

data2 = [go.Heatmap(
    z = tempMinA,
    zmin=-7,
    zmax=27,
    )]
py.image.save_as(data2,"data2.png")

data3 = [go.Heatmap(
    z = tempMinY,
    zmin=-7,
    zmax=27,
    )]
py.image.save_as(data3,"data3.png")

data4 = [go.Heatmap(
    z = tempMinO,
    zmin=-7,
    zmax=27,
    )]
py.image.save_as(data4,"data4.png")
