## The problem of choosing transportation

## CONTEXT
# user
user_departure_name      = "Chisinau"
user_departure_km        = 0
user_destination_name    = "Balti"
user_destination_km      = 120
user_road_max_duration_h = 6

# transportation options
# - walking
transport_walk_speed_km_h = 10

# - bike
transport_bike_speed_km_h = 40

# - car
transport_car_speed_km_h  = 120

# - bus
transport_bus_speed_km_h  = 60


##### HELPER FUNCTIONS ###########
def calcDistance(u_dep, u_des):
    distance_km = abs(u_des - u_dep)
    return distance_km


def calcDuration(dist, t_speed):
    duration_h = dist / t_speed
    return duration_h



def evaluateTransport(u_dep, u_des, u_max_dur, t_speed,):
    distance_km = calcDistance(u_dep, u_des)
    duration_h  = calcDuration(distance_km, t_speed)
    answer      = duration_h <= u_max_dur
    return answer


def printResult(distance_km, duration_h, transp_type):
    print(
    "\nThe distance between", 
    user_departure_name,
    "and",
    user_destination_name,
    "is",
    distance_km,
    "km"
    )

    print(
    "The estimated duration with", transp_type,
    duration_h,
    "h",
    )



##### DECISION MAKING ############

############# <BUS> ##############
answer_b = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_bus_speed_km_h
    )

distance_km = calcDistance(
    user_departure_km,
    user_destination_km
    )

duration_h = calcDuration(
    distance_km,
    transport_bus_speed_km_h
)

printResult(distance_km, duration_h, "BUS")


############# <BUS> ##############

############# <WALK> ##############

answer_w = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_walk_speed_km_h
    )

distance_km = calcDistance(
    user_departure_km,
    user_destination_km
    )

duration_h = calcDuration(
    distance_km,
    transport_walk_speed_km_h
)
    
printResult(distance_km, duration_h, "WALKING")

############# <WALK> ##############

############# <BIKE> ##############

answer_bK = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_bike_speed_km_h
    )

distance_km = calcDistance(
    user_departure_km,
    user_destination_km
    )

duration_h = calcDuration(
    distance_km,
    transport_bike_speed_km_h
)

printResult(distance_km, duration_h, "BIKE")

############# <BIKE> ##############

############# <CAR> ##############

answer_c = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_car_speed_km_h
    )

distance_km = calcDistance(
    user_departure_km,
    user_destination_km
    )

duration_h = calcDuration(
    distance_km,
    transport_car_speed_km_h
)

printResult(distance_km, duration_h, "CAR")

############# <CAR> ##############
if answer_b == True:
    print("Bus is ok",)
elif answer_w == True:
    print("Walk is ok",)
elif answer_bk == True:
    print("Bike is ok",)
elif answer_w == True:
    print("Car is ok",)
else:
    print("No solution!")

