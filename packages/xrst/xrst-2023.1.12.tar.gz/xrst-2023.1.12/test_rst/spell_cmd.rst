.. _spell_cmd-name:

!!!!!!!!!
spell_cmd
!!!!!!!!!

.. meta::
   :keywords: spell_cmd, spell

.. index:: spell_cmd, spell

.. _spell_cmd-title:

Spell Command
#############

.. contents::
   :local:

.. _spell_cmd@Syntax:

Syntax
******
- ``{xrst_spell`` *word_1* ...  *word_n* ``}``
- ``{xrst_spell_off}``
- ``{xrst_spell_on}``

The lines containing the ``{`` ( ``}`` ) character
must have nothing but white space before ( after )  it.

.. meta::
   :keywords: spell_off

.. index:: spell_off

.. _spell_cmd@spell_off:

spell_off
*********
By default xrst does spell checking.
You can turn spell checking off using this command.

.. meta::
   :keywords: spell_on

.. index:: spell_on

.. _spell_cmd@spell_on:

spell_on
********
If spell checking has been turned off,
you can turn it back on using this command.

.. meta::
   :keywords: spell

.. index:: spell

.. _spell_cmd@spell:

spell
*****
You can specify special words to include as correct spelling for
this page using this command.

.. meta::
   :keywords: words

.. index:: words

.. _spell_cmd@Words:

Words
*****
Each word, that is checked for spelling, is a sequence of letters.
Upper case letters start a new word (even when preceded by a letter).

.. meta::
   :keywords: special, words

.. index:: special, words

.. _spell_cmd@Special Words:

Special Words
*************
In the syntax above, the special word list is

| *word_1* ... *word_n*

These words are considered correct spelling even though
they are not in the dictionary.
In the syntax above the special words are all in one line.
They could be on different lines which helps when displaying
the difference between  versions of the corresponding file.
Latex commands should not be in the special word list because
words that have a backslash directly before them
are not include in spell checking.

.. meta::
   :keywords: project_dictionary

.. index:: project_dictionary

.. _spell_cmd@project_dictionary:

project_dictionary
******************
The list of words in the
:ref:`config_file@project_dictionary`
are considered correct spellings for all pages.

.. meta::
   :keywords: capital, letters

.. index:: capital, letters

.. _spell_cmd@Capital Letters:

Capital Letters
***************
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.
Each capital letter starts a new word; e.g., `CamelCase` is considered to
be the two words 'camel' and 'case'.
Single letter words are always correct and not included in the
special word list; e.g., the word list entry ``CppAD`` is the same as ``Cpp``.

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_cmd@Double Words:

Double Words
************
It is considered an error to have only white space between two occurrences
of the same word. You can make an exception for this by entering
the same word twice (next to each other) in the special word list.

Double words errors occur in the output the user sees.
for example, the input:
::

   `python package index <https://pypi.org/>`_ index.

results in the double word 'index index' in the output the user sees; i.e.,
the following output:
`python package index <https://pypi.org/>`_ index.

.. _spell_cmd@Example:

Example
*******
:ref:`spell_example-name`
