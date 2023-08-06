# snek5000-phill

The [Nek5000 phill example] adapted for a workflow using [Snek5000].

## Install

```sh
pip install snek5000-phill
```

For more details, see https://snek5000.readthedocs.io/en/latest/install.html.

## Tests

```sh
pip install '.[tests]'
# Run simple tests: including compilation
pytest
# Run slow tests: launches simulation
pytest --runslow
```

[nek5000 phill example]: https://github.com/KTH-Nek5000/KTH_Examples/tree/master/phill_STAT
[snek5000]: https://github.com/exabl/snek5000
