.. _toc_cmd_dev-name:

!!!!!!!!!!!
toc_cmd_dev
!!!!!!!!!!!

.. meta::
   :keywords: toc_cmd_dev, get, page, names, children, page

.. index:: toc_cmd_dev, get, page, names, children, page

.. _toc_cmd_dev-title:

Get file and page names for children of this page
#################################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _toc_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _toc_cmd_dev@Arguments@data_in:

data_in
=======
is the data for the page before the toc commands have been processed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _toc_cmd_dev@Arguments@file_name:

file_name
=========
is the name of the file that this data comes from. This is only used
for error reporting.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _toc_cmd_dev@Arguments@page_name:

page_name
=========
is the name of the page that this data is in. This is only used
for error reporting.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _toc_cmd_dev@Arguments@group_name:

group_name
==========
We are only including information for pages in this group.

.. meta::
   :keywords: returns

.. index:: returns

.. _toc_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _toc_cmd_dev@Returns@data_out:

data_out
========
is a copy of data_in with the toc commands replaced by {xrst_command}
where command is TOC_hidden, TOC_list, or TOC_table depending on
which command was in data_in.
There is a newline directly before and after the {xrst_command}.

.. meta::
   :keywords: file_list

.. index:: file_list

.. _toc_cmd_dev@Returns@file_list:

file_list
=========
is the list of files in the toc command
(and in same order as in the toc command).

.. meta::
   :keywords: child_page_list

.. index:: child_page_list

.. _toc_cmd_dev@Returns@child_page_list:

child_page_list
===============
Is the a list of page names corresponding to the children of the
this page that are in the files specified by file_list.
If a file in file_list has a begin_parent command, there is only
one page in child_page_list for that file. Otherwise all of the
pages in the file are in child_page_list.

.. literalinclude:: ../../xrst/toc_commands.py
   :lines: 172-176
   :language: py

.. literalinclude:: ../../xrst/toc_commands.py
   :lines: 331-339
   :language: py
