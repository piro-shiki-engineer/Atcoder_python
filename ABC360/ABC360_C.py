import heapq


def my_answer():
    N = int(input())
    box_address_list = list(map(int, input().split()))
    weight_list = list(map(int, input().split()))

    box_each_weights = {i: [] for i in range(N)}
    count_lug_each_box = [0] * N
    total_cost = 0

    for i in range(N):
        count_lug_each_box[box_address_list[i] - 1] += 1
        heapq.heappush(box_each_weights[box_address_list[i] - 1], weight_list[i])

    max_heap = [(-count, i) for i, count in enumerate(count_lug_each_box)]
    min_heap = [(count, i) for i, count in enumerate(count_lug_each_box)]
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    while True:
        # 最大値と最小値のヒープの先頭を取得
        max_count, from_index = heapq.heappop(max_heap)
        min_count, to_index = heapq.heappop(min_heap)

        if -max_count <= 1:
            break

        if min_count >= 1:
            heapq.heappush(max_heap, (max_count, from_index))
            heapq.heappush(min_heap, (min_count, to_index))
            break

        weight = heapq.heappop(box_each_weights[from_index])
        heapq.heappush(box_each_weights[to_index], weight)

        count_lug_each_box[from_index] -= 1
        count_lug_each_box[to_index] += 1

        total_cost += weight

        heapq.heappush(max_heap, (-(count_lug_each_box[from_index]), from_index))
        heapq.heappush(min_heap, (count_lug_each_box[to_index], to_index))

    print(total_cost)


if __name__ == "__main__":
    my_answer()
