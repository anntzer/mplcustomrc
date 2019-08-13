Use Python for your matplotlibrc
================================

Set your backend to "module://mplcustomrc.the_backend_of_your_choice"
(e.g. "module://mplcustomrc.qt5agg") and put the code of your choice in
``Path(mpl.get_configdir(), "matplotlibrc.py")``.  This file will be ``exec``'d
when setting up pyplot.

This is intended for custom logic in setting up your matplotlibrc, e.g.

.. code-block:: python

   from matplotlib import rcParams
   if some_logic:
       rcParams["some.rc.key"] = some_value
