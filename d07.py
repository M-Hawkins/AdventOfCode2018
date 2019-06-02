# Advent of Code 2018 Day 7
# Matthew Hawkins


from collections import defaultdict
import heapq


class Worker:

    def __init__(self):
        self.step = None
        self.remaining_time = 0

    def set_step(self, step):
        self.step = step
        self.remaining_time = ord(step) - 4

    def do_work(self):
        self.remaining_time -= 1
        return self.remaining_time

    def finish_work(self):
        step = self.step
        self.step = None
        return step

    def is_working(self):
        return self.remaining_time > 0

    def __str__(self):
        return str(self.step) + " : " + str(self.remaining_time)


def main():
    with open("puzzleInputs/07.txt") as file:
        instructions = file.readlines()
    connections = [(line[5], line[36]) for line in instructions]

    downstream = defaultdict(list)
    upstream = defaultdict(list)
    for (start, end) in connections:
        downstream[start].append(end)
        upstream[end].append(start)

    initial_steps = []
    for initial_step in downstream.keys() - upstream.keys():
        heapq.heappush(initial_steps, initial_step)

    # Part 1
    ordered_steps = []
    available_steps = initial_steps.copy()
    while available_steps:
        current_step = heapq.heappop(available_steps)
        ordered_steps.append(current_step)
        for dep in downstream[current_step]:
            if dep not in ordered_steps and all(up in ordered_steps for up in upstream[dep]):
                heapq.heappush(available_steps, dep)
    print("".join(ordered_steps))

    # Part 2
    number_of_workers = 5
    workers = [Worker() for n in range(number_of_workers)]
    ordered_steps = []
    available_steps = initial_steps.copy()
    stopwatch = 0
    while available_steps or any(worker.is_working() for worker in workers):
        freed_steps = []
        for worker in workers:
            if not worker.is_working() and available_steps:
                worker.set_step(heapq.heappop(available_steps))
            if worker.is_working() and worker.do_work() < 1:
                finished_step = worker.finish_work()
                ordered_steps.append(finished_step)
                for dep in downstream[finished_step]:
                    if dep not in ordered_steps and all(up in ordered_steps for up in upstream[dep]):
                        heapq.heappush(freed_steps, dep)
        for step in freed_steps:
            heapq.heappush(available_steps, step)
        stopwatch += 1
    print("".join(ordered_steps))
    print(stopwatch)


if __name__ == "__main__":
    main()
