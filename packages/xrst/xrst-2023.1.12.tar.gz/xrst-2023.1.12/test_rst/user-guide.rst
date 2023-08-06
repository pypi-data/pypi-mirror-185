.. _user-guide-name:

!!!!!!!!!!
user-guide
!!!!!!!!!!

.. meta::
   :keywords: user-guide, extract, sphinx, rst, files

.. index:: user-guide, extract, sphinx, rst, files

.. _user-guide-title:

Extract Sphinx RST Files
########################
This is a sphinx wrapper that extracts RST file from source code
and then runs sphinx to obtain html, tex, or pdf output files.
It includes automatic processing and commands that make sphinx easier to use.

.. contents::
   :local:

.. meta::
   :keywords: git, repository

.. index:: git, repository

.. _user-guide@Git Repository:

Git Repository
**************
`<https://github.com/bradbell/xrst>`_

.. meta::
   :keywords: version, documentation

.. index:: version, documentation

.. _user-guide@Version of this Documentation:

Version of this Documentation
*****************************
xrst-2023.1.12

.. meta::
   :keywords: install, stable, version

.. index:: install, stable, version

.. _user-guide@Install Stable Version:

Install Stable Version
**********************
The current stable version freezes features at the beginning of 2023
and only includes bug fixed after that.
::

   pip install xrst

.. meta::
   :keywords: install, testing, version

.. index:: install, testing, version

.. _user-guide@Install Testing Version:

Install Testing Version
***********************
Search for ``xrst`` on `test.pypi <https://test.pypi.org>`_
to determine the date corresponding to this version.
::

   pip install --index-url https://test.pypi.org/simple/ xrst

.. meta::
   :keywords: install, from, source

.. index:: install, from, source

.. _user-guide@Install From Source:

Install From Source
*******************
The following commands will download, test, build, and install
the current version from the master branch.
::

   git clone https://github.com/bradbell/xrst.git xrst.git
   cd xrst.git
   pytest -s pytest
   python3 -m build --sdist
   pip install dist/*

You can determine the date corresponding to a version of the source code
using the following command:
::

   grep '^version *=' pyproject.toml

.. meta::
   :keywords: run, program

.. index:: run, program

.. _user-guide@Run Program:

Run Program
***********
:ref:`run_xrst-title`

.. meta::
   :keywords: contents

.. index:: contents

.. _user-guide@Contents:

Contents
********

-  :ref:`config_file-title`
-  :ref:`run_xrst-title`
-  :ref:`commands-title`
-  :ref:`automatic-title`
-  :ref:`wish_list-title`
-  :ref:`release_notes-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   config_file
   run_xrst
   commands
   automatic
   wish_list
   release_notes
