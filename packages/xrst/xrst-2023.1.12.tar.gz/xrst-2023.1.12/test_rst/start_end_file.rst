.. _start_end_file-name:

!!!!!!!!!!!!!!
start_end_file
!!!!!!!!!!!!!!

.. meta::
   :keywords: start_end_file, convert, literal, start,, end, from, text, line, numbers

.. index:: start_end_file, convert, literal, start,, end, from, text, line, numbers

.. _start_end_file-title:

Convert literal command start, end from text to line numbers
############################################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _start_end_file@Arguments:

Arguments
*********

.. meta::
   :keywords: file_cmd

.. index:: file_cmd

.. _start_end_file@Arguments@file_cmd:

file_cmd
========
is the name of the file where the xrst_literal command appears.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _start_end_file@Arguments@page_name:

page_name
=========
is the name of the page where the xrst_literal command appears.

.. meta::
   :keywords: display_file

.. index:: display_file

.. _start_end_file@Arguments@display_file:

display_file
============
is the name of the file that we are displaying. If it is not the same as
file_cmd, then it must have appeared in the xrst_literal command.

.. meta::
   :keywords: cmd_line

.. index:: cmd_line

.. _start_end_file@Arguments@cmd_line:

cmd_line
========
If file_cmd is equal to display_file, the lines of the file
between line numbers cmd_line[0] and cmd_line[1] inclusive
are in the xrst_literal command and are excluded from the search.

.. meta::
   :keywords: start_after

.. index:: start_after

.. _start_end_file@Arguments@start_after:

start_after
===========
is the starting text. There must be one and only one copy of this text in the
file (not counting the excluded text). This text has no newlines and cannot
be empty.  If not, an the error is reported and the program stops.

.. meta::
   :keywords: end_before

.. index:: end_before

.. _start_end_file@Arguments@end_before:

end_before
==========
is the stopping text. There must be one and only one copy of this text in the
file (not counting the excluded text). This text has no newlines and cannot
be empty.  Furthermore, the stopping text must come after the end of the
starting text. If not, an the error is reported and the program stops.

.. meta::
   :keywords: returns

.. index:: returns

.. _start_end_file@Returns:

Returns
*******

.. meta::
   :keywords: start_line

.. index:: start_line

.. _start_end_file@Returns@start_line:

start_line
==========
is the line number where start_after appears.

.. meta::
   :keywords: end_line

.. index:: end_line

.. _start_end_file@Returns@end_line:

end_line
========
is the line number where end_before appears.

.. literalinclude:: ../../xrst/start_end_file.py
   :lines: 62-77
   :language: py

.. literalinclude:: ../../xrst/start_end_file.py
   :lines: 159-162
   :language: py
