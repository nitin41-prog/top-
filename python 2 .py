# Part 1a: Input basic pay, DA%, and HRA%
basic_pay = float(input("100 "))
da_percentage = float(input("40%: "))
hra_percentage = float(input("10%: "))

da = basic_pay * (da_percentage / 100)
hra = basic_pay * (hra_percentage / 100)
gross_pay = basic_pay + da + hra

print(f"Basic Pay: Rs.1100 {basic_pay:.2f}")
print(f"DA ({da_percentage}40%): Rs. {da:.2f}")
print(f"HRA ({hra_percentage}10%): Rs. {hra:.2f}")
print(f"Gross Pay: Rs. {gross_pay:.2f}")

# Part 1b: Using function
print("\nUsing function:")
gross = calculate_gross_pay(basic_pay, da_percentage, hra_percentage)
print(f"Gross Pay (calculated by function): Rs. {gross:.2f}")
# Part 2a: Input income and expenses
income = float(input("\nEnter monthly income: "))
rent = float(input("Enter rent expense: "))
food = float(input("Enter food expense: "))
electricity = float(input("Enter electricity expense: "))
phone = float(input("Enter phone expense: "))
cable_tv = float(input("Enter cable TV expense: "))

total_expenses = rent + food + electricity + phone + cable_tv
remainder = income - total_expenses

print(f"\nMonthly Income: Rs. {income:.2f}")
print(f"Monthly Expenses: Rs. {total_expenses:.2f}")
print(f"Remainder: Rs. {remainder:.2f}")


# Problem 3: Vehicle on-road price calculation
def calculate_on_road_price(vehicle_type, basic_price, weight):
    """Calculate on-road price for a vehicle"""
    if vehicle_type.upper() == 'P':
        vehicle_tax = basic_price * 0.05
        weight_tax = weight * 0.01
        insurance = basic_price * 0.01
    elif vehicle_type.upper() == 'B':
        vehicle_tax = basic_price * 0.10
        weight_tax = weight * 0.03
        insurance = basic_price * 0.02
    else:
        print("Invalid vehicle type")
        return None

    on_road_price = basic_price + vehicle_tax + weight_tax + insurance
    return vehicle_tax, weight_tax, insurance, on_road_price


# Part 3a: Create vehicle dictionary
def create_vehicle_dict(vehicle_type, weight, basic_price):
    """Create a dictionary with all vehicle details"""
    vehicle_tax, weight_tax, insurance, on_road_price = calculate_on_road_price(
        vehicle_type, basic_price, weight)

    vehicle_dict = {
        'type': vehicle_type.upper(),
        'weight': weight,
        'basic_price': basic_price,
        'vehicle_tax': vehicle_tax,
        'weight_tax': weight_tax,
        'insurance': insurance,
        'on_road_price': on_road_price
    }
    return vehicle_dict

# Part 3b: Get details of N vehicles
vehicles = []
n = int(input("\nEnter number of vehicles: "))

for i in range(n):
    print(f"\nEnter details for vehicle {i + 1}:")
    vehicle_type = input("Enter vehicle type (P/B): ")
    weight = float(input("Enter vehicle weight: "))
    basic_price = float(input("Enter basic price: "))

    vehicle_dict = create_vehicle_dict(vehicle_type, weight, basic_price)
    vehicles.append(vehicle_dict)

    print(f"On-road price for vehicle {i + 1}: Rs. {vehicle_dict['on_road_price']:.2f}")
# Part 3c: Analysis
if vehicles:
    # i. Vehicle with highest on-road price
    highest_price_vehicle = max(vehicles, key=lambda x: x['on_road_price'])
    print(f"\nVehicle with highest on-road price:")
    print(f"Type: {highest_price_vehicle['type']}, On-road price: Rs. {highest_price_vehicle['on_road_price']:.2f}")

    # ii. Vehicle with least weight
    least_weight_vehicle = min(vehicles, key=lambda x: x['weight'])
    print(f"\nVehicle with least weight:")
    print(f"Type: {least_weight_vehicle['type']}, Weight: {least_weight_vehicle['weight']}")
# Part 3d: Statistical analysis
if vehicles:
    # i. Average on-road price
    avg_on_road_price = sum(v['on_road_price'] for v in vehicles) / len(vehicles)
    print(f"\nAverage on-road price: Rs. {avg_on_road_price:.2f}")

    # ii. Count of vehicles with on-road price higher than average
    count_above_avg = sum(1 for v in vehicles if v['on_road_price'] > avg_on_road_price)
    print(f"Number of vehicles with on-road price above average: {count_above_avg}")

    # iii. Count of vehicles with weight above given value
    weight_threshold = float(input("\nEnter weight threshold: "))
    count_above_weight = sum(1 for v in vehicles if v['weight'] > weight_threshold)
    print(f"Number of vehicles with weight above {weight_threshold}: {count_above_weight}")
# iv. Count of vehicles with on-road price <= given budget
    budget = float(input("Enter your budget: "))
    count_within_budget = sum(1 for v in vehicles if v['on_road_price'] <= budget)
    print(f"Number of vehicles within budget Rs. {budget:.2f}: {count_within_budget}")
