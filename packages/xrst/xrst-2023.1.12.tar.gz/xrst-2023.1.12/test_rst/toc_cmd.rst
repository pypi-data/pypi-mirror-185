.. _toc_cmd-name:

!!!!!!!
toc_cmd
!!!!!!!

.. meta::
   :keywords: toc_cmd, table, children, commands

.. index:: toc_cmd, table, children, commands

.. _toc_cmd-title:

Table of Children Commands
##########################

.. contents::
   :local:

.. _toc_cmd@Syntax:

Syntax
******

.. meta::
   :keywords: toc_hidden

.. index:: toc_hidden

.. _toc_cmd@Syntax@toc_hidden:

toc_hidden
==========
| ``{xrst_toc_hidden``
|   *file_1*
|   ...
|   *file_n*
| ``}``

.. meta::
   :keywords: toc_list

.. index:: toc_list

.. _toc_cmd@Syntax@toc_list:

toc_list
========
| ``{xrst_toc_list``
|   *file_1*
|   ...
|   *file_n*
| ``}``

.. meta::
   :keywords: toc_table

.. index:: toc_table

.. _toc_cmd@Syntax@toc_table:

toc_table
=========
| ``{xrst_toc_table``
|   *file_1*
|   ...
|   *file_n*
| ``}``

.. meta::
   :keywords: table, contents

.. index:: table, contents

.. _toc_cmd@Table of Contents:

Table of Contents
*****************
These commands specify the pages that are children
of the current page; i.e., pages that are at the
next level in the table of contents.

.. meta::
   :keywords: names

.. index:: names

.. _toc_cmd@File Names:

File Names
**********
A new line character must precede and follow each
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the
:ref:`config_file@directory@project_directory` .
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

.. meta::
   :keywords: children

.. index:: children

.. _toc_cmd@Children:

Children
********
Each of the files may contain multiple :ref:`pages<begin_cmd@Page>`.
The first of these pages may use a
:ref:`parent begin<begin_cmd@Parent Page>` command.

#. The first page in a file is always a child of the
   page where the toc command appears..

#. If the first page in a file is a begin parent page,
   the other pages in the file are children of the frist page.
   Hence the other pages are grand children of the page
   where the begin toc command appears.

#. If there is no begin parent command in a file,
   all the pages in the file are children of the
   page where the toc command appears.

#. If the first page in a file is a begin parent page,
   and there is also a toc command in this page,
   links to the toc command children come first and then links to
   the children that are other pages in the same file.

.. meta::
   :keywords: child, links

.. index:: child, links

.. _toc_cmd@Child Links:

Child Links
***********
#. The toc_list syntax generates links to the children that
   display the title for each page.
   The toc_table syntax generates links to the children that
   display both the page name and page tile.

#. If a page has a toc_list or toc_table command,
   links to all the children of the page are placed where the
   toc command is located.
   You can place a heading directly before these commands
   to make the links easier to find.

#. If a page uses the hidden syntax,
   no automatic links to the children of the current page are generated.

#. If a page does not have a toc command,
   and it has a begin parent command,
   links to the children of the page are placed at the end of the page.

.. meta::
   :keywords: toctree

.. index:: toctree

.. _toc_cmd@toctree:

toctree
*******
These commands replaces the sphinx ``toctree`` directive.
A ``toctree`` directive is automatically generated and includes each
page that is a child of the current page.

.. _toc_cmd@Example:

Example
*******
:ref:`toc_list_example-name`
