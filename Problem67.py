


def main():
    triangle = []
    #problem67.txt isimli dosyadaki her satırı bir liste olucak şekilde triangle listesine ekliyorum
    with open("Problem67.txt", "r", encoding="utf-8") as f:
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
    main()