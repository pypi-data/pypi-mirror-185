.. _comment_cmd_dev-name:

!!!!!!!!!!!!!!!
comment_cmd_dev
!!!!!!!!!!!!!!!

.. meta::
   :keywords: comment_cmd_dev, remove, all, comment, commands

.. index:: comment_cmd_dev, remove, all, comment, commands

.. _comment_cmd_dev-title:

Remove all comment commands
###########################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _comment_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _comment_cmd_dev@Arguments@data_in:

data_in
=======
is the data for this page.

.. meta::
   :keywords: returns

.. index:: returns

.. _comment_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _comment_cmd_dev@Returns@data_out:

data_out
========
The return data_out is a copy of data_in except that the comment
commands have been removed.

.. literalinclude:: ../../xrst/comment_command.py
   :lines: 56-57
   :language: py

.. literalinclude:: ../../xrst/comment_command.py
   :lines: 103-104
   :language: py
