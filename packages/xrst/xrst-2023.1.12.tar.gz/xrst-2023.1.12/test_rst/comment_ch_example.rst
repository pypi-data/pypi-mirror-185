.. _comment_ch_example-name:

!!!!!!!!!!!!!!!!!!
comment_ch_example
!!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: comment_ch_example, comment, character

.. index:: comment_ch_example, comment, character

.. _comment_ch_example-title:

Comment Character Command Example
#################################

.. contents::
   :local:

.. meta::
   :keywords: discussion

.. index:: discussion

.. _comment_ch_example@Discussion:

Discussion
**********
The ``%`` at the beginning of a line,
and space directly after it (if it exists), are removed before
processing xrst commands.

.. meta::
   :keywords: xrst_code

.. index:: xrst_code

.. _comment_ch_example@xrst_code:

xrst_code
*********
The xrst_code command reports the original source code, before removing
the comment character or the indentation.

.. literalinclude:: ../../example/comment_ch.m
   :lines: 26-33
   :language: matlab

.. meta::
   :keywords: indent

.. index:: indent

.. _comment_ch_example@Indent:

Indent
******
Note that the special character ``%`` has the same indentation as
the source code in this page.

.. meta::
   :keywords: xrst_comment_ch

.. index:: xrst_comment_ch

.. _comment_ch_example@xrst_comment_ch:

xrst_comment_ch
***************
The file below demonstrates the use of ``xrst_comment_ch`` .

.. _comment_ch_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/comment_ch.m
   :language: matlab
