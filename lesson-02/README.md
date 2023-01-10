# Lesson 2 - Analysing data using simulations and resampling

## Takeaways

- bootstrapping is useful when getting another dataset is expensive or difficult;
  we shuffle the original dataset n times, comparing the original dataset to
  the shuffled datasets
- _permuting_ or _relabeling_ is useful when making comparisons between
  datasets; if we shuffle the observations, randomly assigning them to new
  datasets of the original size, does the original observed difference appear
  unique, or is it similar to the results of the randomised datasets?

### Roulette

- roulette wheel traditionally has:
  - 18 red
  - 18 black
  - 2 green
- some naive ways to make a choice a list of entries:
  - `choice(['red', 'red', 'red', ..., 'black', 'black', ...])
  - `choices(['red'] _ 18 + ['black'] _ 18 + ['green'] \* 2)
- `choices` allows us to specify weightings, though, so we can specify a number
  of spins with a single line:
  ```python
  spins = choices(['red', 'black', 'green'], [18, 18, 2], k=6)
  ```

### Dealing cards

- Task: deal 20 playing cards without replacement (16 tens, 36 low)
- for someone playing blackjack, it's important to know what to play based on
  the remaining cards in the deck. We need to:
  - create a deck of cards, separating highs and lows, using `Counter`
  - create a list of cards as tuples, where each tuple is either a `ten` or a `low`
  - shuffle the cards
  - extract the first 20 cards, as if they were dealt
  - evaluate the remaining cards, using `Counter` to aggregate the list of
    tuples

### Biased coin

- what are the odds of 5 or more heads from 7 spins of a biased coin?
- we could use `weights` in the call to `choices` to specify a heavy side of the
  coin, but `choices` has an additional option where we can specify a
  cumulative weight:
  ```python
  # 3 spins, where heads should show up 40% of the time
  choices(['heads', 'tails'], cum_weights=[.4, 1.00], k=3)
  ```
- because `choices` returns a list, we can count the number of items in the
  list:
  ```python
  num_heads = choices(['heads', 'tails'], cum_weights=[.4, 1.00], k=3).count('heads')
  ```
- the equivalent analytical approach (see [./examples.py](./examples.py))
  requires significantly more effort to implement
- the empirical approach also has the benefit that the simulation scales up much
  more easily than the analytical approach

### Quick sort with pivot from 5 values

- for quick sort, is the mean of a sample of 5 values from a population sufficient
  to extract a pivot point that would sit within the middle quartile of the
  population?
- we can generate a mean of sample of 5 values from a population:
  ```python
  n = 10000
  xs = sample(range(n), 5)
  avg = median(xs)
  ```
- given a median from a sample, does it fall in the 2nd and 3rd quartiles of the
  population's distribution:
  ```python
  trial = lambda: n // 4 <= median(sample(range(n))) <= n // 4 * 3
  ```
- what percentage of these medians can we expect to fall in the middle quartile:
  ```python
  result = sum(trial() for _ in range(n)) / n
  ```

### Bootstrapping

- bootstrapping in statistics is when a sample is resampled to create new
  sample
- bootstrapping is used when getting a new sample is expensive or difficult
- to bootstrap a dataset, one ideally wants duplicated values. This improves the
  odds that the bootstrapped dataset will be missing some values from the original
  dataset:

  ```python
  def bootstrap(data: List):
    return choices(data, k=len(data))

  xs = [1,2,3,1]
  ys = bootstrap(xs) # => potentially yields [1,2,2,1]
  ```

- given a dataset, does the observed mean of that dataset fall into a 90%
  confidence interval after resampling the dataset?
  - get the dataset's mean
  - resample the dataset many times using bootstrapping
  - get the means of all the bootstrapped datasets
  - get the upper and lower bounds of the bootstrapped means
  - 90% of the time we can expect the observed mean to fall within these bounds
  - 10% of the time we can expect we likely had a sampling error

### Statistical significance analysis

- p-values means: "What is the probability that what we observed was due
  to chance, rather than a real effect?"
- given two datasets, is the difference between them significant, or must we
  perceive it as down to randomness and chance?
  - start with the null hypothesis - there is no statistically significant
    difference between the datasets
  - get the means of the two sets
  - get the difference of the means of the two sets
  - combine the two sets, and then repeat the following:
    - shuffle the set
    - split the set into two datasets
    - get the difference of the means of those datasets
  - compare the observed mean to the shuffled means:
    - if the shuffled means are consistently less extreme (i.e. the difference
      in the means are lower than the observed mean) there may be a statistically
      significant difference between the two sets, and we reject the null
      hypothesis
    - otherwise, we accept the null hypothesis
- shuffling the combined observations is known as _permuting_ or _relabeling_
- a p-value of 5% is often used as a basis for determining whether there is a
  statistically significant result. If the value is only just over 5%, it
  usually indicates that a larger sample is required to improve feedback

### Single server queue simulation

[./queue.py](./queue.py)

## Additional

- multiplying a list `xs` by an integer `n` will create a new list with repeated
  values and a length of `len(xs) * n`:
  ```python
  xs = [1,2]
  ys = xs * 2 # => [1,2,1,2]
  ```
- flipping a weighted coin generally yields a 50% chance of landing on either
  side, whereas _spinning_ a weighted coin has a higher probability of landing
  on the weighted side
- `/` is true division, whereas `//` is floor division:
  ```python
  true_div = 100 / 2 # 50.0
  floored_div = 100 // 2 # 50
  ```
- given a list, get the:
  - first 5 values: `xs[5:]`
  - last 5 values: `xs[-5:]`
- `random.expovariate` produces values in an exponential distribution, using the
  reciprocal of the value provided
- `xs.append(item)` is significantly faster than `[*xs, item]` and `xs + [item]`!
- `random.gauss` produces values in a normal distribution, given a mean and
  standard deviation

## Links and resources

- [Jake Vanderplas - Statistics for Hackers](https://www.youtube.com/watch?v=Iq9DzN6mvYA)
- [Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
- [Statistical Thinking for Data Science](https://www.youtube.com/watch?v=TGGGDpb04Yc)
- [Statistics is easy!](https://www.goodreads.com/book/show/6001341-statistics-is-easy)
- [Resampling: The New Statistics](https://www.goodreads.com/book/show/2953659-resampling)
