import sys
import heapq

def ints_from_stdin():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            break
        sign = 1
        if data[i] == 45: 
            sign = -1
            i += 1
        x = 0
        while i < n and 48 <= data[i] <= 57:
            x = x * 10 + (data[i] - 48)
            i += 1
        yield sign * x

def main():
    it = ints_from_stdin()
    try:
        n = next(it)
    except StopIteration:
        return

    threshold = next(it)
    drain = next(it)

    times = [0] * n
    sizes = [0] * n
    for i in range(n):
        times[i] = next(it)
        sizes[i] = next(it)

    idx = 0
    t = 0
    water = 0
    max_water = 0

    heap = []
    sum_base = 0 
    count = 0   

    if n > 0 and times[0] > 0:
        t = times[0]

    while True:
        while idx < n and times[idx] == t:
            base = sizes[idx] - times[idx]
            heapq.heappush(heap, -base)
            sum_base += base
            count += 1
            idx += 1

        if heap:
            base = -heapq.heappop(heap)
            sum_base -= base
            count -= 1

        total_unfixed_size = sum_base + count * t
        water = water + total_unfixed_size - drain
        if water < 0:
            water = 0

        if water > max_water:
            max_water = water

        if water >= threshold:
            sys.stdout.write("FLOOD\n")
            sys.stdout.write(str(t) + "\n")
            sys.stdout.write(str(water) + "\n")
            return

        if idx >= n and count == 0:
            sys.stdout.write("SAFE\n")
            sys.stdout.write(str(max_water) + "\n")
            return

        t += 1

        if count == 0 and idx < n and t < times[idx]:
            water = 0
            t = times[idx]

if __name__ == "__main__":
    main()
