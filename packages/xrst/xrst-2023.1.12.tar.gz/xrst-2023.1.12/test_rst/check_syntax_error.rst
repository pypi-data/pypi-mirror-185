.. _check_syntax_error-name:

!!!!!!!!!!!!!!!!!!
check_syntax_error
!!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: check_syntax_error, check, xrst, removed

.. index:: check_syntax_error, check, xrst, removed

.. _check_syntax_error-title:

Check that an xrst command has been removed
###########################################

.. contents::
   :local:

.. meta::
   :keywords: command_name

.. index:: command_name

.. _check_syntax_error@command_name:

command_name
************
is the name of the xrst command; i.e., the following pattern
constitute a match for this command

- ``[^\\]{xrst_`` *command_name* ``[^z-a]``

.. meta::
   :keywords: data

.. index:: data

.. _check_syntax_error@data:

data
****
is the data for this page.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _check_syntax_error@file_name:

file_name
*********
is the input that this page appears in (used for error reporting).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _check_syntax_error@page_name:

page_name
*********
is ``None`` or the name of this page (used for error reporting).

.. literalinclude:: ../../xrst/check_syntax_error.py
   :lines: 34-38
   :language: py
