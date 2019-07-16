from mapsparser.googlemapsparser import GoogleMapsParser

if __name__ == '__main__':
    parser = GoogleMapsParser()
    parser.find_travel_time("ауэзова 8 минск", "нестерова 49 минск")

    # parser.quit()
