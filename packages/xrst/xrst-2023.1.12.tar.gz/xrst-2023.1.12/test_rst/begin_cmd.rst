.. _begin_cmd-name:

!!!!!!!!!
begin_cmd
!!!!!!!!!

.. meta::
   :keywords: begin_cmd, begin, end, commands

.. index:: begin_cmd, begin, end, commands

.. _begin_cmd-title:

Begin and End Commands
######################

.. contents::
   :local:

.. _begin_cmd@Syntax:

Syntax
******
- ``{xrst_begin_parent`` *page_name* *group_name* ``}``
- ``{xrst_begin``        *page_name* *group_name* ``}``
- ``{xrst_end``          *page_name* ``}``

.. meta::
   :keywords: page

.. index:: page

.. _begin_cmd@Page:

Page
****
The start (end) of a page of the input file is indicated by a
begin (end) command.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _begin_cmd@page_name:

page_name
*********
A *page_name* must satisfy the following conditions:

#. It must be a non-empty sequence of the following characters:
   dash ``-``, period ``.``, underbar ``_``, the letters A-Z, letters a-z,
   and decimal digits 0-9.
#. The page name can not be ``index`` or ``genindex`` ,
   and it can not begin with the characters ``xrst_``.
#. The lower case version of two page names cannot be equal.

A link is included in the index under the page name to the page.
The page name is also added to the html keyword meta data.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _begin_cmd@group_name:

group_name
**********
The *group_name* can be empty or a sequence of the letters a-z.
This is the group that this page belongs to; see
:ref:`run_xrst@group_list`.

.. meta::
   :keywords: default, group

.. index:: default, group

.. _begin_cmd@group_name@Default Group:

Default Group
=============
The default value for *group_name* is ``default``; i.e.,
if *group_name* is the empty string, this page is part of the default group.

.. meta::
   :keywords: output

.. index:: output

.. _begin_cmd@Output File:

Output File
***********
The output file corresponding to *page_name* is

   *rst_directory*\ /\ *page_name*\ /``.rst``

see :ref:`config_file@directory@rst_directory` .

.. meta::
   :keywords: parent, page

.. index:: parent, page

.. _begin_cmd@Parent Page:

Parent Page
***********
The following conditions hold for each *group_name*:

#. There can be at most one begin parent command in an input file.
#. If there is a begin parent command, it must be the first begin command
   in the file and there must be other pages in the file.
#. The other pages are children of the parent page.
#. The parent page is a child
   of the page that included this file using a
   :ref:`toc command<toc_cmd-name>`.
#. If there is no begin parent command in an input file,
   all the pages in the file are children
   of the page that included this file using a
   :ref:`toc command<toc_cmd-name>`.

Note that there can be more than one begin parent command in a file if
they have different group names. Also note that pages are only children
of pages that have the same group name.
