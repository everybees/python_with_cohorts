product1_name, product1_price = 'Stationeries', 85.59
product2_name, product2_price = 'Cutleries\t ', 95.99
product3_name, product3_price = 'Laundry Soap', 100.00
product4_name, product4_price = 'Provisions\t', 205.29

company_name = 'Semicolon Ventures'
company_address = '312, Herbert Macaulay,'
company_city = 'Yaba, Lagos, Nigeria'

message = 'Thanks for shopping with us today!'

print('*' * 50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

print('=' * 50)

print('\tProduct Name\t\tProduct Price')

print('\t{}\t\t ₦{}'.format(product1_name.title(), product1_price))
print('\t{}\t\t ₦{}'.format(product2_name.title(), product2_price))
print('\t{}\t\t ₦{}'.format(product3_name.title(), product3_price))
print('\t{}\t\t ₦{}'.format(product4_name.title(), product4_price))

print('=' * 50)

# print('\t\t\tTotal')

total = product1_price + product2_price + product3_price + product4_price
print('\t\tTotal \t\t\t₦{}'.format(total))

print('=' * 50)

print('\n\t{}\n'.format(message))

print('*' * 50)
