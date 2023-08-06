:Name: czmlpy
:Authors: Juan Luis Cano Rodríguez, Eleftheria Chatziargyriou

czmlpy is a Python library to write CZML.

What is CZML?
=============

From the official
`CZML Guide <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CZML-Guide>`_:

  CZML is a JSON format for describing a time-dynamic graphical scene,
  primarily for display in a web browser running Cesium.
  It describes lines, points, billboards, models, and other graphical primitives,
  and specifies how they change with time.
  While Cesium has a rich client-side API,
  CZML allows it to be data-driven
  so that a generic Cesium viewer can display a rich scene
  without the need for any custom code.

Installation
============

You can install czmlpy using pip::

  $ pip install czmlpy

or conda::

  $ conda install czmlpy --channel conda-forge

czmlpy requires Python >= 3.7.

Examples
========

A CZML document is a list of *packets*, which have several properties.
When using czmlpy in an interactive interpreter,
all objects show as nice CZML (JSON)::

  >>> from czmlpy import Packet
  >>> print(Packet())
  {
      "id": "adae4d3a-7087-4fda-a70b-d18a262a890e"
  }
  >>> packet0 = Packet(id="Facility/AGI", name="AGI")
  >>> print(packet0)
  {
      "id": "Facility/AGI",
      "name": "AGI"
  }
  >>> packet0.dumps()
  '{"id": "Facility/AGI", "name": "AGI"}'

And there are more complex examples available::

  >>> from czmlpy.examples import simple
  >>> print(simple)
  [
      {
          "id": "document",
          "version": "1.0",
          "name": "simple",
          "clock": {
              "interval": "2012-03-15T10:00:00Z/2012-03-16T10:00:00Z",
              "currentTime": "2012-03-15T10:00:00Z",
              "multiplier": 60,
              "range": "LOOP_STOP",
              "step": "SYSTEM_CLOCK_MULTIPLIER"
          }
      },
  ...

Jupyter widget
--------------

You can easily display your CZML document using our interactive widget::

  In [1]: from czmlpy.examples import simple

  In [2]: from czmlpy.widget import CZMLWidget

  In [3]: CZMLWidget(simple)

And this would be the result:

.. image:: https://raw.githubusercontent.com/mixxen/czmlpy/master/widget-screenshot.png

Support
=======

If you find any issue on czmlpy or have questions,
please `open an issue on our repository <https://github.com/mixxen/czmlpy/issues/new>`_

Contributing
============

You want to contribute? Awesome! There are lots of
`CZML properties <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Packet>`_
that we still did not implement. Also, it would be great to have
better validation, a Cesium widget in Jupyter notebook and JupyterLab...
Ideas welcome!

We recommend `this GitHub workflow <https://www.asmeurer.com/git-workflow/>`_
to fork the repository. To run the tests,
use `tox <https://tox.readthedocs.io/>`_::

  $ tox

Before you send us a pull request, remember to reformat all the code::

  $ tox -e reformat

This will apply black, isort, and lots of love ❤️

To build a wheel file, update version in setup.py and __init__.py, then::

  $ python setup.py sdist bdist_wheel
  $ twine upload --repository testpypi dist/*

License
=======

czmlpy is released under the MIT license, hence allowing commercial
use of the library. Please refer to the :code:`LICENSE` file.
