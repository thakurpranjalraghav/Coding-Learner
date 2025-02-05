def find_cheaper_taxi():
    # Read input
    D = int(input().strip())  # Distance to office
    
    # Read online taxi costs
    Oc, Oy, Oa = map(int, input().strip().split())
    
    # Read classic taxi costs
    C, Ch, Cm, Ca = map(int, input().strip().split())
    
    # Calculate Online Taxi Cost
    if D <= Oy:
        online_cost = Oc
    else:
        online_cost = Oc + (D - Oy) * Oa
    
    # Calculate Classic Taxi Cost
    classic_cost = Ch + (D / C) * Cm + (D * Ca)
    
    # Determine cheaper option
    if online_cost <= classic_cost:
        print("Online Taxi")
    else:
        print("Classic Taxi")

# Run the function
find_cheaper_taxi()
