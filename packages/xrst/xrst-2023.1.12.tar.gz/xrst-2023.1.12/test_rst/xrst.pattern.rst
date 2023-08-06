.. _xrst.pattern-name:

!!!!!!!!!!!!
xrst.pattern
!!!!!!!!!!!!

.. meta::
   :keywords: xrst.pattern, xrst.pattern, dictionary

.. index:: xrst.pattern, xrst.pattern, dictionary

.. _xrst.pattern-title:

The xrst.pattern Dictionary
###########################

.. contents::
   :local:

.. meta::
   :keywords: pattern

.. index:: pattern

.. _xrst.pattern@pattern:

pattern
*******
This dictionary contains compiled regular expressions.
It does not change after its initial setting when this file is imported.

.. literalinclude:: ../../xrst/pattern.py
   :lines: 26-26
   :language: py

.. meta::
   :keywords: begin

.. index:: begin

.. _xrst.pattern@begin:

begin
*****
Pattern for the begin command.

0. preceding character or empty + the command.
1. preceding character or empty
2. begin or begin_parent
3. the page name (without leading or trailing spaces or tabs)
4. the group name (with leading and trailing spaces and tabs)

.. literalinclude:: ../../xrst/pattern.py
   :lines: 40-42
   :language: py

.. meta::
   :keywords: toc

.. index:: toc

.. _xrst.pattern@toc:

toc
***
Patterns for the toc_hidden, toc_list, and toc_table commands.

0. preceding character + the command.
1. command name; i.e., hidden, list, or table
2. the rest of the command that comes after the command name.
   This is a list of file names with one name per line.
   The } at the end of the command is not included.
   This pattern may be empty.

If you change this pattern, check pattern_toc in process_children.py

.. literalinclude:: ../../xrst/pattern.py
   :lines: 58-60
   :language: py

.. meta::
   :keywords: code

.. index:: code

.. _xrst.pattern@code:

code
****
Pattern for code command.

0. the entire line for the command with newline at front.
1. the indent for the command (spaces and tabs)
2. is the command with or without characters in front
3. This is the non space characters after the indent and before
   command (or None)
4. the language argument which is empty (just white space)
   for the second code command in each pair.
5. the line number for this line; see pattern['line'] above.

.. literalinclude:: ../../xrst/pattern.py
   :lines: 77-80
   :language: py

.. meta::
   :keywords: comment_ch

.. index:: comment_ch

.. _xrst.pattern@comment_ch:

comment_ch
**********
Pattern for comment_ch command

1. empty or character before command + the command
2. is the character (matched as any number of not space, tab or }

.. literalinclude:: ../../xrst/pattern.py
   :lines: 91-93
   :language: py

.. meta::
   :keywords: dir

.. index:: dir

.. _xrst.pattern@dir:

dir
***
Pattern for dir command

1. Is either empty of character before command
2. Is the file_name in the command

.. literalinclude:: ../../xrst/pattern.py
   :lines: 104-107
   :language: py

.. meta::
   :keywords: end

.. index:: end

.. _xrst.pattern@end:

end
***
Pattern for end command

0. preceding character + white space + the command.
1. the page name.

.. literalinclude:: ../../xrst/pattern.py
   :lines: 118-118
   :language: py

.. meta::
   :keywords: line

.. index:: line

.. _xrst.pattern@line:

line
****
Pattern for line numbers are added to the input by add_line_number

0. the line command.
1. the line_number.

.. literalinclude:: ../../xrst/pattern.py
   :lines: 130-130
   :language: py

.. meta::
   :keywords: arg,, lin

.. index:: arg,, lin

.. _xrst.pattern@arg, lin:

arg, lin
********

.. meta::
   :keywords: literal_0

.. index:: literal_0

.. _xrst.pattern@literal_0:

literal_0
*********
xrst_literal with no arguments

0. preceding newline + white space + the command.
1. line number where } at end of command appears

.. literalinclude:: ../../xrst/pattern.py
   :lines: 144-147
   :language: py

.. meta::
   :keywords: literal_1

.. index:: literal_1

.. _xrst.pattern@literal_1:

literal_1
*********
xrst_literal with display_file

0. preceding newline + white space + the command.
1. the line number where this command starts
2. the display file
3. line number where display file appears
4. line number where } at end of command appears

.. literalinclude:: ../../xrst/pattern.py
   :lines: 161-164
   :language: py

.. meta::
   :keywords: literal_2

.. index:: literal_2

.. _xrst.pattern@literal_2:

literal_2
*********
xrst_literal with start, stop

0. preceding newline + white space + the command.
1. the line number where this command starts
2. the start text + surrounding white space
3. line number where start text appears
4. the stop text + surrounding white space
5. the line number where stop text appears
6. line number where } at end of command appears

.. literalinclude:: ../../xrst/pattern.py
   :lines: 180-182
   :language: py

.. meta::
   :keywords: literal_3

.. index:: literal_3

.. _xrst.pattern@literal_3:

literal_3
*********
xrst_literal with start, stop, display_file

0. preceding character + the command.
1. the line number where this command starts
2. the display file
3. line number where display file appears
4. the start text + surrounding white space
5. line number where start text appears
6. the stop text + surrounding white space
7. the line number where stop text appears
8. line number where } at end of command appears

.. literalinclude:: ../../xrst/pattern.py
   :lines: 200-202
   :language: py
