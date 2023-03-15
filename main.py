# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    heap = [(0, i) for i in range(n)]
    output = []
    for i in range(m):
        time, thread = heapq.heappop(heap)
        output.append((thread, time))
        heapq.heappush(heap, (time + data[i], thread))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    output = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(output[i][0], output[i][1])


if __name__ == "__main__":
    main()
