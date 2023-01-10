from random import expovariate, gauss
from statistics import mean, median, stdev

AVG_ARRIVAL_INTERVAL = 5.6
AVG_SERVICE_TIME = 5.0
STDEV_SERVICE_TIME = 0.5

if __name__ == "__main__":
    num_waiting = 0
    arrivals = []
    starts = []
    arrival = service_end = 0.0

    for _ in range(100_000):
        # if the arrival time is before the service_end, add an arrival time
        # to our list of arrival times
        if arrival <= service_end:
            num_waiting += 1
            # Get a random arrival time along an exponential distribution
            # Use the interval as a denominator, as expovariate returns the
            # reciprocal of the random value
            arrival = expovariate(1.0 / AVG_ARRIVAL_INTERVAL)

            # arrivals = [*arrivals, arrival]
            # arrivals = arrivals + [arrival]
            arrivals.append(arrival)

        # if arrival time is after service_end, the item can be processed
        # immediately, and we can append our start times with a new start
        # time
        else:
            num_waiting -= 1
            # set the service start for this iteration to the most recent
            # service end time if there are items in the queue, otherwise use
            # the arrival time
            service_start = service_end if num_waiting else arrival
            # get the length of the service time, given the median service time,
            # and the standard deviation of the service time
            service_time = gauss(AVG_SERVICE_TIME, STDEV_SERVICE_TIME)
            # set the end time of this iteration
            service_end = service_start + service_time

            # starts = [*starts, service_start]
            starts.append(service_start)

    # for each arrival and start time, generate the difference between
    # the two
    waits = [start - arrival for arrival, start in zip(arrivals, starts)]

    print(f"Mean wait: {mean(waits):.1f}.    Stdev wait: {stdev(waits):.1f}")
    print(f"Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}")
