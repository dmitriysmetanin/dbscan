import matplotlib.pyplot as plt
from general_functions import calculate_distance, get_random_color
from generating_points import get_points_by_mouse

# ----- Настройки ----- #
EPSILA = 0.2
M = 4

def clusterize(POINTS):
    global EPSILA, M
    NOISE = []
    current_cluster_number = 0

    visited_points = set()
    clustered_points = set()
    clusters = {}

    def get_point_neighbours(p):
        return [q for q in POINTS if calculate_distance(p, q) < EPSILA]

    def expand_cluster(p, neighbours):
        if current_cluster_number not in clusters:
            clusters[current_cluster_number] = []
        clusters[current_cluster_number].append(p)
        clustered_points.add(p)
        while neighbours:
            q = neighbours.pop()
            # если точку-соседа раньше не проверяли
            if q not in visited_points:
                visited_points.add(q)
                neighbourz = get_point_neighbours(q)
                if len(neighbourz) > M:
                    # в множество соседей точки центроида добавить соседей точки-соседа
                    neighbours.extend(neighbourz)
            # если точка-сосед еще не принадлежит какому-либо кластеру
            if q not in clustered_points:
                clustered_points.add(q)
                clusters[current_cluster_number].append(q)
                if q in NOISE:
                    NOISE.remove(q)

    for p in POINTS:
        if p in visited_points:
            continue

        visited_points.add(p)
        neighbours = get_point_neighbours(p)

        # Если кол-во соседей < m - это шумовая точка
        if len(neighbours) < M:
            NOISE.append(p)
        # Иначе если кол-во соседей >= m - это корневая или граничная точка,
        # => рекурсивно вызываем проверку этих точек
        else:
            current_cluster_number += 1
            expand_cluster(p, neighbours)

    return clusters


# Создание точек с помощью мыши
print("Рисуйте точки, для завершения нажмите Enter")
POINTS = get_points_by_mouse(1, 1)

# Определение кластеров
clusters = clusterize(POINTS)

# Формирование точечной диаграммы
for points_values in clusters.values():
    X = [p[0] for p in points_values]
    Y = [p[1] for p in points_values]
    plt.scatter(X, Y, c=get_random_color())

# Вывод точечной диаграммы
plt.axis("square")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()