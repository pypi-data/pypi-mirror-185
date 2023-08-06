.. _toc_list_example-name:

!!!!!!!!!!!!!!!!
toc_list_example
!!!!!!!!!!!!!!!!

.. meta::
   :keywords: toc_list_example, toc_list, parent, page

.. index:: toc_list_example, toc_list, parent, page

.. _toc_list_example-title:

toc_list Example Parent Page
############################

.. contents::
   :local:

.. meta::
   :keywords: links, child, pages

.. index:: links, child, pages

.. _toc_list_example@Links to Child Pages:

Links to Child Pages
********************

-  :ref:`child_example_one-title`
-  :ref:`child_example_two-title`

.. meta::
   :keywords: xrst_toc_list

.. index:: xrst_toc_list

.. _toc_list_example@xrst_toc_list:

xrst_toc_list
*************
The file below demonstrates the use of ``xrst_toc_list`` .

.. _toc_list_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/toc_list.xrst
   :language: rst

.. toctree::
   :maxdepth: 1
   :hidden:

   child_example_one
   child_example_two
