.. _sphinx_label-name:

!!!!!!!!!!!!
sphinx_label
!!!!!!!!!!!!

.. meta::
   :keywords: sphinx_label, get, labels, declared, using, sphinx, commands

.. index:: sphinx_label, get, labels, declared, using, sphinx, commands

.. _sphinx_label-title:

Get Labels Declared Using Sphinx Commands
#########################################

.. contents::
   :local:

.. meta::
   :keywords: data_in

.. index:: data_in

.. _sphinx_label@data_in:

data_in
*******
is the data for one page.
Line numbers have been added to this data; see
:ref:`add_line_numbers-name` .

.. meta::
   :keywords: file_name

.. index:: file_name

.. _sphinx_label@file_name:

file_name
*********
is the name of the xrst input file corresponding to data_in
(only used for error reporting).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _sphinx_label@page_name:

page_name
*********
is the page name corresponding to data_in
(only used for error reporting).

.. meta::
   :keywords: external_line

.. index:: external_line

.. _sphinx_label@external_line:

external_line
*************
For each label declared in data_in using sphinx commands,
and that links to an external web site,
*external_line* [ *label*.lower() ] is the line number in
*file_name* where the label was defined.

.. meta::
   :keywords: internal_line

.. index:: internal_line

.. _sphinx_label@internal_line:

internal_line
*************
For each label declared in data_in using sphinx commands,
and that links to a page in this web site,
*internal* [ *label* ] is the line number in
*file_name* where the label was defined.

.. meta::
   :keywords: errors

.. index:: errors

.. _sphinx_label@Errors:

Errors
******
If two or external labels have the same lower case value,
an error is reported using :ref:`system_exit-name` .

.. literalinclude:: ../../xrst/sphinx_label.py
   :lines: 60-64
   :language: py

.. literalinclude:: ../../xrst/sphinx_label.py
   :lines: 151-156
   :language: py
