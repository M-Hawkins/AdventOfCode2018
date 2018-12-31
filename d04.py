# Advent of Code 2018 Day 4
# Matthew Hawkins

from collections import defaultdict
from datetime import datetime, timedelta


class Guard:

    def __init__(self, id_num):
        self.id_num = int(id_num)
        self.naps = []

    def total_nap_time(self):
        return sum([n.duration() for n in self.naps])

    def __str__(self):
        s = str(self.id_num) + " : ["
        s += ", ".join([n.__str__() for n in self.naps])
        return s + "]"


class Nap:

    def __init__(self, start_time, end_time):
        self.format = "%Y-%m-%dT%H:%M"
        start_iso_ts = start_time.replace(" ", "T")
        end_iso_ts = end_time.replace(" ", "T")
        self.start_time = datetime.strptime(start_iso_ts, self.format)
        self.end_time = datetime.strptime(end_iso_ts, self.format)

    def duration(self):
        return (self.end_time - self.start_time).total_seconds()

    def __str__(self):
        return str(self.start_time) + " : " + str(self.end_time)


def datetime_range(nap):
    delta = timedelta(minutes=1)
    curr = nap.start_time
    while curr < nap.end_time:
        yield curr
        curr += delta


def main():
    with open("input04.txt") as file:
        guard_events = file.readlines()
        guard_events.sort()

    guards = dict()
    current_guard = None
    start_time = None
    for event in guard_events:
        timestamp, event_type = event[1:].split("]")
        if event_type.strip()[0] == "G":
            id_num = int(event_type.split("#")[1].split()[0])
            if id_num in guards:
                current_guard = guards[id_num]
            else:
                current_guard = Guard(id_num)
                start_time = None
                guards[id_num] = current_guard
        elif event_type.strip()[0] == "f":
            start_time = timestamp
        else:
            nap = Nap(start_time, timestamp)
            current_guard.naps.append(nap)

    # Part 1
    target_guard = None
    total_nap_time = -1
    for guard in guards.values():
        nap_time = guard.total_nap_time()
        if nap_time > total_nap_time:
            target_guard = guard
            total_nap_time = nap_time

    nap_minute_counts = defaultdict(int)
    for nap in target_guard.naps:
        for t in datetime_range(nap):
            nap_minute_counts[t.time()] += 1

    print(target_guard.id_num * max(nap_minute_counts, key=nap_minute_counts.get).minute)

    # Part 2
    target_guard = None
    target_time = None
    best_minute_count = -1
    for guard in guards.values():
        nap_minute_counts = defaultdict(int)
        for nap in guard.naps:
            for t in datetime_range(nap):
                nap_minute_counts[t.time()] += 1
        if nap_minute_counts:
            guard_best_time = max(nap_minute_counts, key=nap_minute_counts.get)
            guard_best_count = nap_minute_counts[guard_best_time]
            if guard_best_count > best_minute_count:
                target_guard, target_time, best_minute_count = guard, guard_best_time, guard_best_count

    print(target_guard.id_num * target_time.minute)


if __name__ == "__main__":
    main()
