# sextant

A tool to compose and manage helm charts from the wikimedia library of template modules.

It offers multiple functions:
* `sextant [OPTIONS] vendor [-f] CHART_DIR` allows you to generate the vendored modules bundle for your chart, provided you have a package.json in `CHART_DIR`
* `sextant [OPTIONS] search CHARTS_DIR NAMESPACE.MODULE:VERSION` finds, within a charts collection, all the ones that depend on a specific module
* `sextant [OPTIONS] update CHARTS_DIR NAMESPACE.MODULE:VERSION...` allows to update the module dependencies for a chart or multiple ones

The available global options are:
* `--debug` to print out debug information; useful when reporting bugs (there are many)
* `--modulepath` to indicate where your modules are located; defaults to `./modules` which is ok if you're running from the root of the deployment-charts repository.

## Installation

Get the latest released version from pip:

    $ pip install sextant

If you want the latest improvements, clone this repository and run

    $ python3 setup.py install

## Create a new release

Create a version tag and push it to gitlab. Then clean previous build artifacts, rebuild the wheels for the package, and upload them using twine:

    $ rm -rf dist/ build/ *.egg-info/
    $ python setup.py sdist bdist_wheel
    $ python -m twine upload dist/*

Several folks on the wikimedia SRE team have the right to perform the upload

## Examples

### Vendor a new dependency
Say you added a dependency on a new module; just edit `package.json`, then run:

    $ sextant vendor charts/mychart

This should add the desired module, at the latest patch release of the requested version.

### Update all dependencies to the latest patch version
Force re-vendoring; you can either remove the package.lock file or use `-f`

    $ sextant vendor -f charts/mychart

All modules should be upgraded to the latest patch version.

### Update to a new minor/major version
You can do this either on a single chart:

    $ sextant update charts/mychart foo.bar:2.1 foo.baz:2.0

or on a whole collections of charts

    $ sextant update charts foo.bar:2.1 foo.baz:2.0

It must be noted that if one of the charts has failed dependencies, the process will stop there.



## License
See the LICENSE file.