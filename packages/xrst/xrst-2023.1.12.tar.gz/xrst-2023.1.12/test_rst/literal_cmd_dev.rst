.. _literal_cmd_dev-name:

!!!!!!!!!!!!!!!
literal_cmd_dev
!!!!!!!!!!!!!!!

.. meta::
   :keywords: literal_cmd_dev, process, literal, commands, in, page

.. index:: literal_cmd_dev, process, literal, commands, in, page

.. _literal_cmd_dev-title:

Process the literal commands in a page
######################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _literal_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _literal_cmd_dev@Arguments@data_in:

data_in
=======
is the data for a page before the
:ref:`literal commands <literal_cmd-name>` have been removed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _literal_cmd_dev@Arguments@file_name:

file_name
=========
is the name of the file that this data comes from. This is used
for error reporting and for the display file (when the display file
is not included in the command).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _literal_cmd_dev@Arguments@page_name:

page_name
=========
is the name of the page that this data is in. This is only used
for error reporting.

.. meta::
   :keywords: rst2project_dir

.. index:: rst2project_dir

.. _literal_cmd_dev@Arguments@rst2project_dir:

rst2project_dir
===============
is a relative path from the :ref:`config_file@directory@rst_directory`
to the :ref:`config_file@directory@project_directory` .

.. meta::
   :keywords: returns

.. index:: returns

.. _literal_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _literal_cmd_dev@Returns@data_out:

data_out
========
Each xrst literal command is converted to its corresponding sphinx commands.

.. literalinclude:: ../../xrst/literal_command.py
   :lines: 183-187
   :language: py

.. literalinclude:: ../../xrst/literal_command.py
   :lines: 335-337
   :language: py
