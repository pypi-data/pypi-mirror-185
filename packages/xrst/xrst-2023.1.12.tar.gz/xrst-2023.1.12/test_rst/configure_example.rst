.. _configure_example-name:

!!!!!!!!!!!!!!!!!
configure_example
!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: configure_example, using, toml, configure

.. index:: configure_example, using, toml, configure

.. _configure_example-title:

Example Using TOML Configure File
#################################

.. contents::
   :local:

.. meta::
   :keywords: include_all

.. index:: include_all

.. _configure_example@include_all:

include_all
***********

.. meta::
   :keywords: rst_prolog

.. index:: rst_prolog

.. _configure_example@include_all@rst_prolog:

rst_prolog
==========
|tab| This line is indented using ``|tab|``
which is defined in the rst_prolog for this documentation.

.. meta::
   :keywords: latex_macro

.. index:: latex_macro

.. _configure_example@include_all@latex_macro:

latex_macro
===========
:math:`f : \B{R}^n \rightarrow \B{R}^m`
This line uses ``\B`` which is defined as a latex_macro.

.. meta::
   :keywords: toml

.. index:: toml

.. _configure_example@Example TOML File:

Example TOML File
*****************

.. literalinclude:: ../../xrst.toml
   :language: toml

.. _configure_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/configure.xrst
   :language: rst
