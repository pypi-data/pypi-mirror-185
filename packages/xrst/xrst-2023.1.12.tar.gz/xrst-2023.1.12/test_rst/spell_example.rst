.. _spell_example-name:

!!!!!!!!!!!!!
spell_example
!!!!!!!!!!!!!

.. meta::
   :keywords: spell_example, spell

.. index:: spell_example, spell

.. _spell_example-title:

Spell Command Example
#####################

.. contents::
   :local:

.. meta::
   :keywords: text

.. index:: text

.. _spell_example@Text:

Text
****
The word ``iterable`` is not in the dictionary,
so we have included it in the special words for this page.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _spell_example@Spelling File:

Spelling File
*************
The word ``xrst`` is included by the spelling file used to build this
documentation and hence need not be in the special words for this page.

.. meta::
   :keywords: math

.. index:: math

.. _spell_example@Math:

Math
****
Words that are preceded by a backslash; e.g., latex commands,
are automatically included as correct spelling.

.. math::

   z = \cos( \theta ) + {\rm i} \sin( \theta )

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_example@Double Words:

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this page.

.. meta::
   :keywords: off, on

.. index:: off, on

.. _spell_example@Off and On:

Off and On
**********
In some cases it is better to turn spell checking.
For example when displaying the git hash code:
7c35a3ce607a14953f070f0f83b5d74c2296ef93

.. meta::
   :keywords: xrst_spell

.. index:: xrst_spell

.. _spell_example@xrst_spell:

xrst_spell
**********
The file below demonstrates the use of ``xrst_spell``

.. _spell_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/spell.xrst
   :language: rst
