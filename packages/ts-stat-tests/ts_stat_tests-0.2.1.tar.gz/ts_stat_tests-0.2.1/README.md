<div align="center">

# Time Series Statistical Tests

### `ts-stat-tests`

[![PyPI version](https://img.shields.io/pypi/v/ts-stat-tests?label=version&logo=git&color=blue)](https://pypi.org/project/ts-stat-tests/)
[![Python](https://img.shields.io/pypi/pyversions/ts-stat-tests.svg?style=flat&logo=python&logoColor=FFDE50&color=blue)](https://pypi.org/project/ts-stat-tests/)
[![OS](https://img.shields.io/static/v1?label=os&message=ubuntu+|+macos+|+windows&color=blue&logo=ubuntu&logoColor=green)](https://pypi.org/project/ts-stat-tests/)<br>
[![Unit Tests](https://img.shields.io/github/actions/workflow/status/chrimaho/ts-stat-tests/ci-unit-tests.yml?logo=github&logoColor=white&label=unit+tests)](https://github.com/chrimaho/ts-stat-tests/actions/workflows/ci-unit-tests.yml)
[![Deploy Docs](https://img.shields.io/github/actions/workflow/status/chrimaho/ts-stat-tests/cd-deploy-docs.yml?logo=github&logoColor=white&label=deploy+docs)](https://github.com/chrimaho/ts-stat-tests/actions/workflows/cd-deploy-docs.yml)
[![Publish Package](https://img.shields.io/github/actions/workflow/status/chrimaho/ts-stat-tests/cd-publish-package.yml?logo=github&logoColor=white&label=publish+package)](https://github.com/chrimaho/ts-stat-tests/actions/workflows/cd-publish-package.yml)
[![codecov](https://codecov.io/gh/chrimaho/ts-stat-tests/branch/main/graph/badge.svg)](https://codecov.io/gh/chrimaho/ts-stat-tests)<br>
[![Vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/chrimaho/ts-stat-tests?color=green)](https://github.com/chrimaho/ts-stat-tests)
[![License MIT](https://img.shields.io/pypi/l/ts-stat-tests)](https://github.com/chrimaho/ts-stat-tests/blob/master/LICENSE)
[![Downloads](https://img.shields.io/pypi/dw/ts-stat-tests)](https://github.com/chrimaho/ts-stat-tests)
[![Code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)<br>
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chrimaho/ts-stat-tests/issues)

</div>


## Motivation

Time Series Analysis has been around for a long time, especially for doing Statistical Testing. Some Python packages are going a long way to make this even easier than it has ever been before. Such as [`sktime`](https://sktime.org/) and [`pycaret`](https://pycaret.org/) and [`pmdarima`](https://www.google.com/search?q=pmdarima) and [`statsmodels`](https://www.statsmodels.org/).

There are some typical Statistical Tests which are accessible in these Python ([QS](#), [Normality](#), [Stability](#), etc). However, there are still some statistical tests which are not yet ported over to Python, but which have been written in R and are quite stable.

Moreover, there is no one single library package for doing time-series statistical tests in Python.

That's exactly what this package aims to achieve.

A single package for doing all the standard time-series statistical tests.


## Tests

Full credit goes to the packages listed in this table.

type | name | source package | source language | implemented
---|---|---|---|---
correlation | acf | `statsmodels` | Python | ✅
correlation | pacf | `statsmodels` | Python | ✅
correlation | ccf | `statsmodels` | Python | ✅
stability | stability | `tsfeatures` | Python | ✅
stability | lumpiness | `tsfeatures` | Python | ✅
suitability | white-noise (ljung-box) | ` ` | Python | 🔲
stationarity | adf | ` ` | Python | 🔲
stationarity | kpss | ` ` | Python | 🔲
stationarity | ppt | ` ` | Python | 🔲
normality | shapiro | ` ` | Python | 🔲
seasonality | qs | `seastests` | R | ✅
seasonality | ocsb | `pmdarima` | Python | ✅
seasonality | ch | `pmdarima` | Python | ✅
seasonality | seasonal strength | `tsfeatures` | Python | ✅
seasonality | trend strength | `tsfeatures` | Python | ✅
seasonality | spikiness | `tsfeatures` | Python | ✅
regularity | regularity | `antropy` | python | ✅


## Known limitations

- These listed tests is not exhaustive, and there is probably some more that could be added. Therefore, we encourage you to raise issues or pull requests to add more statistical tests to this suite.
- This package does not re-invent any of these tests. It merely calls the underlying packages, and calls the functions which are already written elsewhere.
