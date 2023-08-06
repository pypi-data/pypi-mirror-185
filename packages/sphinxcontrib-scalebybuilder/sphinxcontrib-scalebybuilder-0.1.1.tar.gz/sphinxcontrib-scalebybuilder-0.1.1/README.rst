***************************************
Sphinx Scale Image By Builder Extension
***************************************

This extension allows setting the scaling factor of images and figures
depending on the builder.


Installation
============

Just install via ``pip``:

.. code-block:: console

   $ pip install sphinxcontrib-scalebybuilder

Then add the module ``sphinxcontrib.scalebybuilder`` to the
``extensions`` list in your ``conf.py``.


Usage
=====

Scale images or figures differently depending on the builder by suffixing the
``scale`` option with ``-<builder>``:

.. code-block:: rst

   .. image:: img.png
      :scale-html: 75%
      :scale-latex: 50%

   .. figure:: fig.png
      :scale-html: 150%
      :scale-latex: 25%

      A figure scaled to 150 % in HTML and 25 % in LaTeX.
