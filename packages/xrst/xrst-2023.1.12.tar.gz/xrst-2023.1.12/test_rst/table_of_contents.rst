.. _table_of_contents-name:

!!!!!!!!!!!!!!!!!
table_of_contents
!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: table_of_contents, create, table, contents, modify, titles

.. index:: table_of_contents, create, table, contents, modify, titles

.. _table_of_contents-title:

Create the table of contents and Modify Titles
##############################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _table_of_contents@Arguments:

Arguments
*********

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _table_of_contents@Arguments@tmp_dir:

tmp_dir
=======
is the temporary directory where the temporary rst files are written.

.. meta::
   :keywords: target

.. index:: target

.. _table_of_contents@Arguments@target:

target
======
is either 'html' or 'tex'.

.. meta::
   :keywords: tex

.. index:: tex

.. _table_of_contents@Arguments@target@tex:

tex
---
If target is 'tex',  for each temporary file
tmp_dir/page_name.rst the text \\n{xrst_before_title}
is removed and  the page number followed by the page name is added
at the front of the title for the page.
The page number includes the counter for each level.

.. meta::
   :keywords: html

.. index:: html

.. _table_of_contents@Arguments@target@html:

html
----
If target is 'html',
\\n{xrst_before_title} is removed without other changes.

.. meta::
   :keywords: all_page_info

.. index:: all_page_info

.. _table_of_contents@Arguments@all_page_info:

all_page_info
=============
is a list with length equal to the number of pages.
The value all_page_info[page_index] is a dictionary for this page
with the following key, value pairs (all the keys are strings):

..  csv-table::
    :header: key, value, type

    page_name, contains the name of this page, str
    page_title,  contains the title for this page, str
    parent_page, index in all_page_info for the parent of this page, int
    in_parent_file, is this page in same input file as its parent, bool

.. meta::
   :keywords: root_page_list

.. index:: root_page_list

.. _table_of_contents@Arguments@root_page_list:

root_page_list
==============
is a list of strings containing the root page name for each group.
The order of the root page names determine the order of the groups
int the table of contents.

.. meta::
   :keywords: returns

.. index:: returns

.. _table_of_contents@Returns:

Returns
*******

.. meta::
   :keywords: content

.. index:: content

.. _table_of_contents@Returns@content:

content
=======
The return content is the table of contents entries for all the pages.
The title Table of Contents and the label xrst_table_of_contents
are placed at the beginning of the of content.

.. literalinclude:: ../../xrst/table_of_contents.py
   :lines: 207-216
   :language: py

.. literalinclude:: ../../xrst/table_of_contents.py
   :lines: 247-248
   :language: py
