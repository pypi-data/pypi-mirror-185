.. _remove_indent-name:

!!!!!!!!!!!!!
remove_indent
!!!!!!!!!!!!!

.. meta::
   :keywords: remove_indent, remove, indentation, page

.. index:: remove_indent, remove, indentation, page

.. _remove_indent-title:

Remove indentation for a page
#############################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _remove_indent@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _remove_indent@Arguments@data_in:

data_in
=======
is the data for this page.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _remove_indent@Arguments@file_name:

file_name
=========
is the input that this page appears in (used for error reporting).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _remove_indent@Arguments@page_name:

page_name
=========
is the name of this page (used for error reporting).

.. meta::
   :keywords: returns

.. index:: returns

.. _remove_indent@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _remove_indent@Returns@data_out:

data_out
========
is a copy of data_in with the indentation for this section removed.

.. meta::
   :keywords: indent

.. index:: indent

.. _remove_indent@Returns@indent:

indent
======
is the white space that was removed from each line (except for empty lines)

.. literalinclude:: ../../xrst/remove_indent.py
   :lines: 60-63
   :language: py

.. literalinclude:: ../../xrst/remove_indent.py
   :lines: 121-124
   :language: py
