.. _get_spell_checker-name:

!!!!!!!!!!!!!!!!!
get_spell_checker
!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: get_spell_checker, get, spell, checker, object

.. index:: get_spell_checker, get, spell, checker, object

.. _get_spell_checker-title:

Get A Spell Checker Object
##########################

.. contents::
   :local:

.. _get_spell_checker@Syntax:

Syntax
******

| *spell_checker* = xrst.get_spell_checker(*local_words*, *package*)
| *known*   = *spell_checker*.known ( *word* )
| *suggest* = *spell_checker*.suggest ( *word* )

.. meta::
   :keywords: local_words

.. index:: local_words

.. _get_spell_checker@local_words:

local_words
***********
is a list of words
(each word is a non-empty str)
that get added to the dictionary for this spell checker.
No need to add single letter words because they are considered correct
by spell_command routine.
}

.. meta::
   :keywords: package

.. index:: package

.. _get_spell_checker@package:

package
*******
is an str equal to 'pyspellchecker' or 'enchant' .

.. meta::
   :keywords: word

.. index:: word

.. _get_spell_checker@word:

word
****
is a word the we are either checking to see if it is correct,
or looking for a suggested spelling for.

.. meta::
   :keywords: spell_checker

.. index:: spell_checker

.. _get_spell_checker@spell_checker:

spell_checker
*************
is the spell checking object.

.. meta::
   :keywords: known

.. index:: known

.. _get_spell_checker@known:

known
*****
is True (False) if *word* is (is not) a correctly spelled word.

.. meta::
   :keywords: suggest

.. index:: suggest

.. _get_spell_checker@suggest:

suggest
*******
if *word* is correctly spelled, *suggest* is equal to *word* .
Otherwise if *suggest* is not None, it is a suggestion
for correcting the spelling.
If *suggest* is None, the spell checker does not have a suggestion
for correcting the spelling of *word*. .
