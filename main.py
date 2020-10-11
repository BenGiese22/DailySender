from weather import Weather

def main():
    
    # Broomfield Colorado Info
    latitude = '39.9205'
    longitude = '-105.0867'
    exclude = 'minutely,hourly,alerts'
    units = 'imperial'


    weather = Weather(latitude, longitude, exclude, units)

if __name__ == "__main__":
    main()