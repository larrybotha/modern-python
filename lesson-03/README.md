# Improving reliability with mypy and type hinting

## Takeaways

- a tuple with homogenous items can be expressed in type annotations using an
  ellipsis:
  ```python
  my_tuple: Tuple[str, ...] = ("a", "b", "c")
  ```
- `pyflakes` is useful for code analysis
- floating point arithmetic can be problematic in Python:
  ```python
  1.1 + 2.2
  # 3.3000000000000003
  ```
  `math.fsum` doesn't solve all floating point issues, such as the one above,
  but it does fix many other cases of problematic floating point arithmetic
- `defaultdict` is a regular dictionary that will run a factory function when a
  lookup is made for a key that doesn't exist
- `defaultdict` is particularly useful for grouping values
- the idiomatic approach for grouping in Python is as follows:

  ```python
  xs = ...
  group_dict = defaultdict(list) # or whatever factory makes sense

  for x in xs:
    feature = x[0] # or some other feature, such as len(x), etc.
    group_dict[feature].append(x)
  ```

- a key function is a function that takes one argument, and transforms it into a
  key. This is common in SQL:
  ```sql
  -- get names ordered by the length of the name - len is a key function
  SELECT name FROM names ORDER BY len(name);
  ```
- `zip` is useful for transposing sequences. `itertools.zip_longest` allows for
  zipping sequences without dropping
- as in Javascript, one can spread lists, which can be useful for dealing with
  multi-dimensional lists:
  ```python
  xs = [
    [1,2,3],
    [4,5,6],
  ]
  transposed_xs = [list(row) for row in zip(*xs)]
  ```
- nested sequences can be flattened using the following strategy:
  ```python
  xxs = [ ys, zs, ... ]
  xs = [ x for ROW in xxs for x in ROW ]
  ```

### Additional

- `collections.deque` is a _double-ended queue_ - useful for creating queues and
  stacks
- `pprint.pprint` accepts a number of arguments which allow for updating how the
  interrogated value is rendered, with `width` being particularly useful for
  preventing output from being too long
- _feature_ is a word used commonly in machine learning to describe the aspect
  of the items we are working with that we are interested in
