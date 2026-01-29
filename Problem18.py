import time


def main_brute_force():
    triangle = []
    # standart dosya okumamızı yapıyoruz
    with open("Problem18.txt", "r", encoding="utf-8") as f:
        for line in f:
            triangle.append([int(num) for num in line.strip().split(" ")])

    path = 0 #bu değişken izleyeceğimiz yolu gösteren bir değişken olucak
    max_result = 0 #asıl sonucumuzu tutacağımız değişken

    while path < 16384: #16384 olasılık olduğu için eğer bu olasılıkların hepsinin üstüne çıkarsak döngü biticek
        result = triangle[0][0] #sonuca en tepedeki eleman her zaman dahil edileceği için onu en başta ekliyoruz
        index = 0 #listenin hangi sırasındaki elemanın alınacağını gösterecek olan değişken 
        for i, row in enumerate(triangle[1:]): # üçgenin her satırını kendi sıra numarası ile alıyoruz
            if path & (1 << i): # yol göstergemizin dönmemizi söyleyip söylemediğini kontrol ediyoruz (bit seviyesinde işlem)
                index += 1 # eğer dönmemiz gerkeiyorsa index + 1 
            result += row[index] #satır içerisinde index sıra numarasındaki elemanı sonuca ekliyoruz
        
        if result > max_result: #eğer bulduğumuz sonuç bir öncekilerden daha büyükse
            max_result = result #sayıyı güncelliyoruz

        path += 1 #bir sonraki yol göstergesine geçiş yapıyoruz
    print(max_result) #sonucu yazdırıyoruz


def main_solution():
    triangle = []
    with open("Problem18.txt", "r", encoding="utf-8") as f:
        for line in f:
            triangle.append([int(num) for num in line.strip().split(" ")])

    #hesaplama kısmı
    while len(triangle) != 1: # sadece tak satır yani en tepedkei satır kalana kadar devam edeceğiz
        down_row = triangle.pop() #en alttaki satırı çıkarıyoruz ve down_row olarak alıyoruz
        up_row = triangle.pop() #bir üstteki satırı da çıkarıp up_row olarak alıyoruz

        result = [] #hesaplamanın sonucunda oluşacak listeyi burada tutacağız
        for index, value in enumerate(up_row): #üstteki satırın her bir elemanını ve elemanın sıra numarasını alıyoruz
            result.append( #listeye yeni bir eleman ekleyeceğiz (ne ekleneceği aşşağıda hesaplanıyor)
                max( #listeye aşşağıdaki hesapladığımız iki elemandan en büyük olanı ekleyeceğiz
                    value + down_row[index],    #üstteki listenin elemanını alttaki listenin aynı sıradaki elemanı ile topluyoruz
                    value + down_row[index + 1],#üstteki listenin elemanını alttaki listenin bir sonraki sıradaki elemanı ile topluyoruz
                    )
                )
            # işlemi her bir üst liste elemanı için yapıyoruz
        triangle.append(result) #sonuçta oluşan listeyi üçgenin en altına ekleyip sadece tek satır kalana kadar aynı işlemi tekrarlıyoruz

    print(triangle[0][0]) #üçgenin en tepesindeki tek elemanı ekrana yazdırıyoruz (sonucumuz)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    main_brute_force()
    end = time.perf_counter_ns()
    print(f"brute force {end - start} nano saniye surdu")

    start = time.perf_counter_ns()
    main_solution()
    end = time.perf_counter_ns()
    print(f"solution {end - start} nano saniye surdu")

