# nmk-github
Github plugin for **`nmk`** build system

<!-- NMK-BADGES-BEGIN -->
[![License: MPL](https://img.shields.io/github/license/dynod/nmk-github)](https://github.com/dynod/nmk-github/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/nmk-github/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/nmk-github/actions?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/nmk-github)](https://pypi.org/project/nmk-github/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- NMK-BADGES-END -->

This plugin adds support for Github features in an **`nmk`** project:
* [Github workflow file](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) generation
* README badges generation (link to license + build action status; only if [**`nmk-badges`**](https://github.com/dynod/nmk-badges) plugin is also used)

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```
refs:
    - pip://nmk-github!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://github.com/dynod/nmk/wiki/nmk-github-plugin)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:github** label.
