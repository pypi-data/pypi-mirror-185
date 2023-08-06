# Readme of `yasiu.visualisation`

High level functions, to quickly visualise data frames.

## Installation

```shell
pip install yasiu.visualisation
```

## Sequence reader Generators

- `summary_plot` - plot dataframe, possible grouping by columns

### Import:

```py
from yasiu_vis.visualisation import summary_plot
```

### Use example:

```py
summary_plot(df)
summary_plot(df, group="column-name")
summary_plot(df, group="column-name", split_widnow="column")
```

# All packages

[1. Time Package](https://pypi.org/project/yasiu-time/)

[2. Math Package](https://pypi.org/project/yasiu-math/)

[3. Image Package](https://pypi.org/project/yasiu-image/)

[4. Pyplot visualisation Package](https://pypi.org/project/yasiu-visualisation/)

