.. _next_heading-name:

!!!!!!!!!!!!
next_heading
!!!!!!!!!!!!

.. meta::
   :keywords: next_heading, return, location, next, heading, in, page

.. index:: next_heading, return, location, next, heading, in, page

.. _next_heading-title:

Return location of the next heading in a page
#############################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _next_heading@Arguments:

Arguments
*********

.. meta::
   :keywords: data

.. index:: data

.. _next_heading@Arguments@data:

data
====
is the data that we are searching for a heading in. The heading text must
have at least one character and be followed by an underline of at least the
same length. The heading text may be proceeded by an overline.

.. meta::
   :keywords: data_index

.. index:: data_index

.. _next_heading@Arguments@data_index:

data_index
==========
is the index in the data where the search starts. This must be zero
or directly after a newline.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _next_heading@Arguments@file_name:

file_name
=========
name of the file that contains the input data for this page.
This is only used for error reporting.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _next_heading@Arguments@page_name:

page_name
=========
is the name of this page.
This is only used for error reporting.

.. meta::
   :keywords: results

.. index:: results

.. _next_heading@Results:

Results
*******

.. meta::
   :keywords: heading_index

.. index:: heading_index

.. _next_heading@Results@heading_index:

heading_index
=============
If there is an overline, this is the index in data of the beginning of the
overline. Otherwise, it is the index of the beginning of the heading text.
If 0 < heading_index, there is a newline just before heading_index; i.e.,
data[heading_index]=='\n'.  If heading_index is -1, there is no heading
in data that begins at or after data_index.

.. meta::
   :keywords: heading_text

.. index:: heading_text

.. _next_heading@Results@heading_text:

heading_text
============
if 0 <= heading_index, this is the heading text.

.. meta::
   :keywords: underline_text

.. index:: underline_text

.. _next_heading@Results@underline_text:

underline_text
==============
if 0 <= heading_index, this is the underline text.
If there is an overline present, it is the same as the underline text.

.. literalinclude:: ../../xrst/next_heading.py
   :lines: 60-66
   :language: py

.. literalinclude:: ../../xrst/next_heading.py
   :lines: 159-163
   :language: py
