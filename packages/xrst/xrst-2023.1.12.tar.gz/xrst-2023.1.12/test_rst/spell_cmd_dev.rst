.. _spell_cmd_dev-name:

!!!!!!!!!!!!!
spell_cmd_dev
!!!!!!!!!!!!!

.. meta::
   :keywords: spell_cmd_dev, process, spell, page

.. index:: spell_cmd_dev, process, spell, page

.. _spell_cmd_dev-title:

Process the spell command for a page
####################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _spell_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _spell_cmd_dev@Arguments@tmp_dir:

tmp_dir
=======
The file :ref:`replace_spell@spell.toml`
is written in the *tmp_dir* directory by the one page at a time
by this function call.

.. meta::
   :keywords: data_in

.. index:: data_in

.. _spell_cmd_dev@Arguments@data_in:

data_in
=======
is the data for this page before the spell commands are removed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _spell_cmd_dev@Arguments@file_name:

file_name
=========
is the name of the file that the data came from. This is used
for error reporting and spell.toml.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _spell_cmd_dev@Arguments@page_name:

page_name
=========
is the name of the page that this data is in. This is only used
for error reporting and spell.toml.

.. meta::
   :keywords: begin_line

.. index:: begin_line

.. _spell_cmd_dev@Arguments@begin_line:

begin_line
==========
is the line number in *file_name* where the begin command for this page
appears. This is only used for spell.toml.

.. meta::
   :keywords: spell_checker

.. index:: spell_checker

.. _spell_cmd_dev@Arguments@spell_checker:

spell_checker
=============
Is a spell checking object used for error checking; see
:ref:`get_spell_checker-name`.

.. meta::
   :keywords: returns

.. index:: returns

.. _spell_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _spell_cmd_dev@Returns@data_out:

data_out
========
is the data for this page after the spell command (if it exists)
is removed.

spell_warning
is true (false) if a spelling warning occurred (did not occur).

.. meta::
   :keywords: spelling, warnings

.. index:: spelling, warnings

.. _spell_cmd_dev@Spelling Warnings:

Spelling Warnings
*****************
A spelling warning is reported for each word (and double word) that is not
in the spell_checker dictionary or the special word list. A word is two or
more letter characters. If a word is directly preceded by a backslash,
it is ignored (so that latex commands do not generate warnings).

.. literalinclude:: ../../xrst/spell_command.py
   :lines: 206-213
   :language: py

.. literalinclude:: ../../xrst/spell_command.py
   :lines: 517-520
   :language: py
