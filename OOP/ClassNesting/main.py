from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math
geolocator = Nominatim(user_agent="myGeocoder")

class Point:
    def __init__(self, latitude = 0, longitude = 0):
        self.latitude = latitude
        self.longitude = longitude

    def SetCity(self, name):
        location = geolocator.geocode(name)
        if location != None:
            self.latitude = location.latitude
            self.longitude = location.longitude
            return True
        else:
            return None

    def GetName(self):
        return geolocator.reverse(self.GetCoordinates()).raw["address"]["city"]

    def setLatitude(self, latitude):
        self.latitude = latitude

    def setLongitude(self, longitude):
        self.longitude = longitude

    def GetLatitude(self):
        return self.latitude
    
    def GetLongitude(self):
        return self.longitude
    
    def GetCoordinates(self):
        return (self.latitude, self.longitude)




class Route:
    def __init__(self, start = ""):
        self.paths = []

        if self.AddPoint(start) == None:
            print("Start point is invalid")
            return exit()

    def AddPoint(self, name):
        point = Point()
        
        if point.SetCity(name) != None:
            self.paths.append(point.GetCoordinates())
            return True
        else:
            return print("Point is invalid: ", name)
    

        
    def GetTotalDistance(self):
        distance = 0
        for i in range(len(self.paths)-1):
            distance += geodesic(self.paths[i], self.paths[i+1]).km
        return distance
        
    def GetAllPointsCordinates(self):
        return self.paths
    
    def GetAllPoints(self):
        return [geolocator.reverse(point).raw["address"]["city"] for point in self.paths]
    
    def __str__(self):
        return f"Route: \n Start: {self.GetAllPoints()[0]}\n Finish: {self.GetAllPoints()[len(self.paths)-1]} \nTotalDistance: {math.floor(self.GetTotalDistance())}km \n Points (LeftToRight): {self.GetAllPoints()}"
    
Navigate = Route("Praha") # Defaultní parametr reprezentuje začátek cesty
Navigate.AddPoint("Brnoosac") # Přidá další bod (Tento je invalidní)
Navigate.AddPoint("Brno")
Navigate.AddPoint("Ostrava")
print(Navigate)
