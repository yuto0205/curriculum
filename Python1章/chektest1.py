# 問1-1
# int型のリストdataを作成し、値を1,3,5,7で初期化
data = [1,3,5,7]


for i in data:
    print(i ** 2)

# 問1-2
for j in list(range(1,8,2)):
    print(j **2)


#問2-1
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in "横浜":
        print(place + "のチケットが当選しました！")
    elif place in "札幌" or place in "大阪":
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

#問2-2
wait_place.extend(get_place)
print(wait_place)
s = "{}と{}と{}のチケットが当選しました！"
print(s.format(wait_place[2],wait_place[0],wait_place[1]))
