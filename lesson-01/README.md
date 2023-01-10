# Lesson 1 - Foundational Python skills for data analytics

## Takeaways

### Formatting

[./formatting.py](./formatting.py)

- `f"{x!r}"` indicates that we want the **representation** of `x`
- `type(x).__name__` gets the name of a type

### `Counter`

[./counter.py](./counter.py)

- `collections.Counter` is useful for counting things, and behaves similarly to
  `Dict`:

  ```python
  from collections import Counter

  counter = Counter()
  num_dragons = counter['dragons'] # => 0
  num_dragons += 1
  ```

- one can also initialise a counter with a list:

  ```python
  from collections import Counter

  x = "red blue green red blue red"
  counter = Counter(x.split(" "))
  counter['red'] # => 3
  ```

- we can get the most common values out of a `Counter` instance:

  ```python
  counter = Counter([1,2,3,1])
  num_tuples = 1
  counter.most_common(num_tuples) # => (1, 2)
  ```

- `Counter.elements` retrieves an iterator of the values of each key. Since
  `Counter` is a dict, we have all the same methods available, too:
  - `counter.items()`
  - `counter.values()`
  - `counter.keys()` etc.

### `statistics`

[./stats.py](./stats.py)

- accuracy was emphasised when creating this module. Despite being able to
  implement many of the functions yourself, this module will likely give more
  accurate results
- `statistics.median` will _average_ the two middle values of a list if the
  number of elements is even
- standard deviation measures the typical distance between data points in a set:
  - if you know the population size, use `statistics.pstdev`. The denominator
    inside the square root uses `N`
    - if the population size is 1, the result is 0 (i.e. no deviation between
      values)
  - if you're working with a sample of the population, use `statistics.stdev`.
    The denominator inside the square root uses `n - 1`
    - if the sample size is 1, we get infinity

### List concatenation

[./list_concatenation.py](./list_concatenation.py)

- one can concatenate using slices:

  ```python
  xs = [1,2,3]
  ys = [4,5,6]
  zs = xs[:2] + ys[:2]
  ```

- one can get the number of instances of a particular value in a list using
  `xs.index(x)`
- `sorted` will coerce a value into a list:

  ```python
  sorted('cat')
  # => ['a', 'c', 't']
  ```

### lambdas

[./lambda.py](./lambda.py)

- lambdas can be defined with an arbitrary number of positional arguments:

  ```python
  fn = lambda x,y,z: x + y + z
  ```

### Chained comparisons

[./lambda.py](./lambda.py)

- chained comparisons prevent unnecessarily adding the same value to the stack
  multiple times, e.g.

  ```python
  x = 5

  # optimised
  if 6 > x > 4:
    # ...

  # vs unoptimised
  if x < 6 and x > 4:
    # ...
  ```

### `random` continuous distribution

[./rand_continuous.py](./rand_continuous.py)

- `random.seed` allows for seeding a random number
- a seed is useful in research to provide insight into conclusions, so as to
  provide confidence to others that you're not cherry picking data to
  support your hypotheses, while providing a reproducible dataset
- one can select numbers at random using different distributions:
  - `random.uniform(min, max)` will select numbers in a range as if they were
    normally distributed
  - `random.triangle(min, max)` selects numbers closer to the midpoint much more
    than those at the edges
  - `random.gauss(mu, sigma)` produces a gaussian distribution - similar to what
    we would expect for something like IQs. We provide the desired mean, and the
    desired standard deviation. The larger the dataset, the closer to the mean
    and standard deviation we should see
  - `random.expovariate(lambd)` produces values in a distribution given a
    desired mean, but as `1 / lambd` - i.e. the reciprocal of the value we
    provide. This is useful to simulate arrival times in a queuing system, such
    as network requests

### `random` discrete distribtions

[./rand_discrete.py](./rand_discrete.py)

- `random.choice` picks a single value out of a list
- `random.choices` picks a list of values out of a list, allowing for the number
  of selections to provided
- `random.sample` samples unique values from a list, while allowing for defining
  the number of occurrences of different items in the list in the function call
- `random.shuffle` will mutate a given list of values
- `random.choices` allows for weights to be passed through. If no weights are
  provided, the items in the choices will be yielded with an even distribution
- the first item `sample` out of sample is equivalent to using `choice`:

  ```python
  xs = [1,2,3]

  # y and z are equivalent
  y: int = sample(xs, k=1)[0]
  z: int = choice(xs)
  ```

- `shuffle` is also a specialised case of `sample`:

  ```python
  xs = [1,2,3]
  sample_shuffle = sample(xs, k=len(xs)) # => similar outcome to shuffle
  ```

## Links and resources

- [Population and sample standard deviation](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review)
