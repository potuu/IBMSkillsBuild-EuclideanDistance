import math

# Öklid mesafesi hesaplamak için fonk
def euclideanDistance(point1, point2):
    # verilen (x2 - x1)² + (y2 - y1)² formulünü uygulama
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeleri Hesapla ve 'distances' Listesinde Sakla
distances = []

# Noktalar arası mesafeleri hesaplamak için çiftler oluşturma
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı iki kez kontrol etmemek için j = i+1
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafe
min_distance = min(distances)

# Sonuçlar
print(f"Mesafeler: {distances}")
print(f"Minimum Mesafe: {min_distance}")
