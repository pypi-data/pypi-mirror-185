.. _suspend_cmd-name:

!!!!!!!!!!!
suspend_cmd
!!!!!!!!!!!

.. meta::
   :keywords: suspend_cmd, suspend, resume, commands

.. index:: suspend_cmd, suspend, resume, commands

.. _suspend_cmd-title:

Suspend and Resume Commands
###########################

.. contents::
   :local:

.. _suspend_cmd@Syntax:

Syntax
******
- ``{xrst_suspend}``
- ``{xrst_resume}``

.. _suspend_cmd@Purpose:

Purpose
*******
It is possible to suspend (resume) the xrst extraction during a page.
One begins (ends) the suspension with a line that only contains spaces,
tabs and a suspend command (resume command).
Note that this will also suspend all other xrst processing; e.g.,
spell checking.

.. _suspend_cmd@Example:

Example
*******
:ref:`suspend_example-name`
