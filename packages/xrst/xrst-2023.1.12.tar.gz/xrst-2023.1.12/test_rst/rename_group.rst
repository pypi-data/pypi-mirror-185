.. _rename_group-name:

!!!!!!!!!!!!
rename_group
!!!!!!!!!!!!

.. meta::
   :keywords: rename_group, rename, subset, group

.. index:: rename_group, rename, subset, group

.. _rename_group-title:

Rename a Subset of a Group
##########################

.. contents::
   :local:

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _rename_group@tmp_dir:

tmp_dir
*******
is the directory where spell.toml is located

.. meta::
   :keywords: old_group_name

.. index:: old_group_name

.. _rename_group@old_group_name:

old_group_name
**************
is the old name that we are replacing in the xrst begin commands.

.. meta::
   :keywords: new_group_name

.. index:: new_group_name

.. _rename_group@new_group_name:

new_group_name
**************
is the new name that we are using in the xrst begin commands.

.. meta::
   :keywords: spell.toml

.. index:: spell.toml

.. _rename_group@spell.toml:

spell.toml
**********
see :ref:`replace_spell@spell.toml` .

.. literalinclude:: ../../xrst/rename_group.py
   :lines: 37-40
   :language: py
