#Hero Honda showroom at Jamal.

Jamal_showroom = ['Honda', 'Suzuki', 'Hero-Honda', 'pulsar', 'Duke', 'Yamaha', 'VR', 'Enfield']
price_in_dollor = [3000, 4000, 3450, 4200, 5001, 6500, 7500, 9105]
Bike_sold_last_week = [5, 3, 2, 7, 8, 10, 50, 70]

total_price = 0

for price in price_in_dollor:
  total_price += price
  average_price = total_price/len(price_in_dollor)
print('Average Price: {0}'. format(average_price))

new_prices = [price -250.89 for price in price_in_dollor]
print(new_prices)

total_revenue = 0
for i in range (len(Jamal_showroom)):
  total_revenue += price_in_dollor[i] * Bike_sold_last_week[i]
print('Total Revenue: ${0}'.format(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: ${0}".format(average_price))
      
Bike_under_4000 = [Jamal_showroom[i] for i in range (len(Jamal_showroom)) if new_prices[i] < 4000]
print(Bike_under_4000)  