rent = 715
electric = 150 
wifi = 75
pet_fee = 200
pet_rent = 15
admin_Fee = 150
people = [["Tanner", rent/2, wifi/2, electric/2, pet_fee/2, 0, admin_Fee/2], ["Hailey", rent/2, wifi/2, electric/2, pet_fee/2, pet_rent/1, admin_Fee/2]]
#Lawrence Total
foo = 0
while foo < 2:
    print(people[foo][0])
    print("rent = ", people[foo][1])
    print("electric = ", people[foo][2])
    print("Wifi = ", people[foo][3])
    print("pet_fee = ", people[foo][4])
    print("pet_rent = ", people[foo][5])
    print("admin fee = ", people[foo][6])
    foo=foo+1
tota_l = rent + electric + wifi + pet_fee + pet_rent + admin_Fee
per = (rent + electric + wifi + pet_fee + pet_rent + admin_Fee)/2
print("total = %d" % tota_l)
print ("total/person = %d" % per) 