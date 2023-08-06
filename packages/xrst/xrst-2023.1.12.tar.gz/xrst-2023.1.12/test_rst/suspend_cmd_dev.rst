.. _suspend_cmd_dev-name:

!!!!!!!!!!!!!!!
suspend_cmd_dev
!!!!!!!!!!!!!!!

.. meta::
   :keywords: suspend_cmd_dev, remove, text, specified, suspend, /, resume, pairs

.. index:: suspend_cmd_dev, remove, text, specified, suspend, /, resume, pairs

.. _suspend_cmd_dev-title:

Remove text specified by suspend / resume pairs
###############################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _suspend_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _suspend_cmd_dev@Arguments@data_in:

data_in
=======
is the data for this page.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _suspend_cmd_dev@Arguments@file_name:

file_name
=========
is the input file corresponding to this page.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _suspend_cmd_dev@Arguments@page_name:

page_name
=========
is the name of this page.

.. meta::
   :keywords: returns

.. index:: returns

.. _suspend_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _suspend_cmd_dev@Returns@data_out:

data_out
========
The return data_out is a copy of data_in except that the text between
and including each suspend / resume pair has been removed.

.. literalinclude:: ../../xrst/suspend_command.py
   :lines: 71-74
   :language: py

.. literalinclude:: ../../xrst/suspend_command.py
   :lines: 138-139
   :language: py
