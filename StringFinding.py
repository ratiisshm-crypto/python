tour_locations = ["New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:


            matches.append(idx)


    if not matches:
        raise ValueError("{} is not in the list".format(target_value))
    else:
        return matches        
    
tour_stops = linear_search(tour_locations, target_city)
print("{} is present in following locations in the list: {}".format(target_city, tour_stops))