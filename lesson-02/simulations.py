from collections import Counter
from math import factorial as fact
from random import choice, choices, sample, shuffle
from statistics import mean, median, stdev
from textwrap import dedent


def six_roulette_wheel_naive():
    population = ["red"] * 18 + ["black"] * 18 + ["green"] * 2
    spins = [choice(population) for _ in range(6)]
    counter = Counter(spins)

    print(f"spins, naive:\n{counter}")
    print()


def six_roulette_wheel_less_naive():
    population = ["red"] * 18 + ["black"] * 18 + ["green"] * 2
    spins = choices(population, k=6)
    counter = Counter(spins)

    print(f"spins, better:\n{counter}")
    print()


def six_roulette_wheel():
    spins = choices(["red", "black", "green"], [18, 18, 2], k=6)
    counter = Counter(spins)

    print(f"spins:\n{counter}")
    print()


def dealing_cards():
    # create a deck of cards
    deck = Counter({"tens": 16, "lows": 36})
    # create a list of tuples
    deck = list(deck.elements())
    # shuffle the deck
    deal = sample(deck, 52)
    # evaluate the remainder of the deck after 20 cards are removed
    remainder = deal[20:]

    print(f"remaining cards:\n{Counter(remainder)}")
    print()


def biased_coin_empirical():
    # create a trial that returns a result for 7 throws of a biased coin
    trial = (
        lambda: choices(
            # given a population of 2 sides of a coin
            ["heads", "tails"],
            # where heads should appear approximately 60% of the time
            cum_weights=[0.6, 1.00],
            # spin the coin 7 times
            k=7,
        ).count("heads")
        >= 5
    )

    n = 100_000
    # what ratio of 7 spins results in 5 or more heads
    result = sum(trial() for _ in range(n)) / n

    print(f"empirical result: {result}")
    print()


def biased_coin_analytical():
    """
    This is the equivalent analytical implementation of biased_coin above

    Despite being more accurate, it's far more verbose, and requires a lot more
    cognitive overhead to interpret
    """

    def combination(n, r):
        return fact(n) // fact(r) // fact(n - r)

    def apply_binomial_theorem(probability, n, population_size):
        return (
            probability**n
            * (1 - probability) ** (population_size - n)
            * combination(population_size, n)
        )

    probability_of_heads = 0.6
    total_spins = 7
    probabilities = [
        apply_binomial_theorem(probability_of_heads, n, total_spins)
        # for spins where there are 5, 6, or 7 heads
        for n in range(5, total_spins + 1)
    ]
    result = sum(probabilities)

    print(f"analytical result: {result}")
    print()


def probability_median_middle_quartile():
    n = 100_000
    trial = lambda: n // 4 < median(sample(range(n), 5)) <= 3 * n / 4
    result = sum(trial() for _ in range(n)) / n

    print(
        f"approximately {result * 100}% of the sample means fall in the middle quartile"
    )
    print()


def bootstrapping_for_confidence_interval():
    """
    Determine a confidence interval for where 90% of observations should fall
    """

    def bootstrap(data):
        return choices(data, k=len(data))

    # timings in minutes from a large query
    network_event_timings = [
        7.18,
        8.59,
        12.24,
        7.39,
        8.16,
        8.68,
        6.98,
        8.31,
        9.06,
        7.06,
        7.67,
        10.02,
        6.87,
        9.07,
    ]

    print(f"mean of timings: {mean(network_event_timings)}")
    print(f"stdev of timings: {stdev(network_event_timings)}\n")

    bootstrapped_data = bootstrap(network_event_timings)

    print(f"{'network_event_timings data:':<30} {network_event_timings}")
    print(f"{'bootstrapped data:':<30} {bootstrapped_data}\n")

    n = 10_000
    means = sorted(mean(bootstrap(network_event_timings)) for _ in range(n))
    confidence = 0.9
    index = round(n * (1 - 0.9) / 2)
    (lower_bound, upper_bound) = (means[index], means[-index])

    print(
        dedent(
            f"""
                The observed mean of {mean(network_event_timings)} falls within
                the {confidence * 100 :.0f}% confidence interval of
                {lower_bound :.1f} and {upper_bound :.1f}
            """
        ).strip()
    )
    print()


def statistical_significance_birth_weights():
    def trial_factory(obs_diff, num_drug_users, observations):
        def run_trial():
            # we are permuting / relabeling the observations here
            shuffle(observations)
            drug_users = observations[:num_drug_users]
            placebo_users = observations[num_drug_users:]
            shuffled_diff = mean(drug_users) - mean(placebo_users)

            # is the difference in means of the relabeled datasets more
            # extreme than the original?
            # The more values that are true, the less significant the observed
            # difference is, and the higher the likelihood that the study could
            # have used any participant in either group without affecting the
            # outcome
            # i.e. is the observed difference unusual, or is it expected?
            return shuffled_diff >= obs_diff

        return run_trial

    drug_birth_weights = [
        7.1,
        8.5,
        6.4,
        7.7,
        8.2,
        7.6,
        8.4,
        5.1,
        8.1,
        7.4,
        6.9,
        8.4,
    ]
    placebo_birth_weights = [
        8.2,
        6.1,
        7.1,
        7.1,
        4.9,
        7.4,
        8.1,
        7.1,
        6.2,
        7.0,
        6.6,
        6.3,
    ]
    obs_diff_means = mean(drug_birth_weights) - mean(placebo_birth_weights)
    num_trials = 10_000
    trial = trial_factory(
        obs_diff_means,
        len(drug_birth_weights),
        [*drug_birth_weights, *placebo_birth_weights],
    )
    p_value = sum(trial() for _ in range(num_trials)) / num_trials

    print(f"p-value for the drug trial with relabeled datasets is {p_value}")
    print()


if __name__ == "__main__":
    six_roulette_wheel_naive()
    six_roulette_wheel_less_naive()
    six_roulette_wheel()

    dealing_cards()

    biased_coin_empirical()
    biased_coin_analytical()

    probability_median_middle_quartile()

    bootstrapping_for_confidence_interval()

    statistical_significance_birth_weights()
