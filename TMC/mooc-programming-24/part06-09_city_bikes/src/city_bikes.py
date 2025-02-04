# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str) -> dict:
    daftar = {}
    with open("src/"+filename) as file_name:
        for alamat in file_name:
            addy = alamat.strip().split(";")
            if addy[0] == "Longitude":
                continue
            long = float(addy[0])
            lat = float(addy[1])
            daftar[addy[3]] = (long, lat)
    return daftar

def distance(stations: dict, station1: str, station2: str) -> float:
    if station1 in stations and station2 in stations:
        long1 = stations[station1][0]
        lat1 = stations[station1][1]
        long2 = stations[station2][0]
        lat2 = stations[station2][1]
        x_km = (long1 - long2) * 55.26
        y_km = (lat1 - lat2) * 111.2
        jarak_km = math.sqrt(x_km**2 + y_km**2)
        return jarak_km
    else:
        raise ValueError("One or both stations not found in the provided dictionary.")

def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    station_pair = ("", "")
    
    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                current_distance = distance(stations, station1, station2)
                if current_distance > max_distance:
                    max_distance = current_distance
                    station_pair = (station1, station2)
    
    return (station_pair[0], station_pair[1], max_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)