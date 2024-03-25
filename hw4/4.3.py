import codecs
import datetime
import multiprocessing as mp
import time


def A(input_queue, output_pipe):
    while True:
        input_ = input_queue.get()
        if input_ == "exit":
            output_pipe.send(input_)
            break
        output_pipe.send(input_)
        time.sleep(5)


def B(input_pipe, output_queue):
    while True:
        input_ = input_pipe.recv()
        if input_ == "exit":
            output_queue.put(input_)
            break
        input_ = codecs.encode(input_, 'rot_13')
        output_queue.put(input_)


if __name__ == "__main__":
    queue_a = mp.Queue()
    parent_conn, child_conn = mp.Pipe()
    queue_b = mp.Queue()

    process_a = mp.Process(target=A, args=(queue_a, child_conn))
    process_b = mp.Process(target=B, args=(parent_conn, queue_b))

    process_a.start()
    process_b.start()

    try:
        while True:
            print(datetime.datetime.now())
            msg = input()
            queue_a.put(msg)
            if msg == "exit":
                break
            processed_msg = queue_b.get()
            print(datetime.datetime.now())
            print(processed_msg)
    finally:
        process_a.join()
        process_b.join()
