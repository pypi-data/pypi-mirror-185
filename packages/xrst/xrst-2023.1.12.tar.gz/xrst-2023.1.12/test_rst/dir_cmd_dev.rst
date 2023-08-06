.. _dir_cmd_dev-name:

!!!!!!!!!!!
dir_cmd_dev
!!!!!!!!!!!

.. meta::
   :keywords: dir_cmd_dev, convert, names, be, relative, rst, directory

.. index:: dir_cmd_dev, convert, names, be, relative, rst, directory

.. _dir_cmd_dev-title:

Convert File Names to be Relative to the RST Directory
######################################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _dir_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _dir_cmd_dev@Arguments@data_in:

data_in
=======
is the data for this page.

.. meta::
   :keywords: rst2project_dir

.. index:: rst2project_dir

.. _dir_cmd_dev@Arguments@rst2project_dir:

rst2project_dir
===============
is a relative path from the :ref:`config_file@directory@rst_directory`
to the :ref:`config_file@directory@project_directory` .

.. meta::
   :keywords: returns

.. index:: returns

.. _dir_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _dir_cmd_dev@Returns@data_out:

data_out
========
The return data_out is a copy of data_in except that all the occurrences of
../../file_name have been converted to the file name
relative to the rst directory.

.. literalinclude:: ../../xrst/dir_command.py
   :lines: 75-77
   :language: py

.. literalinclude:: ../../xrst/dir_command.py
   :lines: 106-107
   :language: py
