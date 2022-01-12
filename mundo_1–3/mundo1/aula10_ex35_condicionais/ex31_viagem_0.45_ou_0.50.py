dis = float(input("How far is the trip (Km)? "))
if dis <= 200:
    dis = dis * 0.50
else:
    dis = dis * 0.45
print('You must pay R$ {:.2f}'.format(dis))
