import multiprocessing as mp

def job(v, n):
    v.value += 1
    n += 1

if __name__ == '__main__':
    array = mp.Array('i', [1, 2, 3])
    value = mp.Value('d', 1)
    num = 10
    print(array[:])

    print('before p, value=', value.value, ', num=', num)

    p1 = mp.Process(target=job, args=(value, num))
    p1.start()
    p1.join()
    print('after p1, value=', value.value, ', num=', num)

    p2 = mp.Process(target=job, args=(value, num))
    p2.start()
    p2.join()
    print('after p2, value=', value.value, ', num=', num)