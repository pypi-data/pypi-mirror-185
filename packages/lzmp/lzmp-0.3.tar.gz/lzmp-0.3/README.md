lzmp
----

``lzmp`` is a simple wrapper around the multiprocessing module,
allowing the lazy programmer to run batches of processes.

lzmp contains the class ``Pool`` which lets the user specify one or more
callable objects (such as functions) along with lists or argument to
process. ``lzmp`` collects the return value of each call and return
the whole lot as a list, keeping the original submission order. For
a single type of callable, the standalone function ``run`` wraps the
wrapper and allows one-line parallelization. Optionally, a function
may be called on the list of compiled results.

The documentation can be found at: <https://lzmp.readthedocs.io/en/latest/>
