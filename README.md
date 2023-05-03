# Code repository for AK-201-426 (Data Science)

This is a collection of all jupyter notebook including the scratch library,
based on (Gruz, 2019).

Some modification to the scratch library:
- Modularizing all the Python files in scratch library into classes
- Remove nested functions
- Use `numpy.randomn.default_rng()` for pseudo-random number generator
- Consistency in matplotlib command to plot a figure. Instead using
  sequence of `plt.`, we prefer to use a pair of `fig`, `ax` and
  update `ax` instance with plot of the data

Some issues and to do lists:
- In NLP chapter and section of "Word Vector", we didn't achieve a closed
  result to the result in the textbook. Maybe we need to test 
  the `TextEmbedding` layer (or `Embedding` layer) 

- Several section in some chapters are skipped due to the limited time
  delivering the material to the students. 

## References
- (Gruz, 2019) - Data science from scratch, 2nd. Ed.