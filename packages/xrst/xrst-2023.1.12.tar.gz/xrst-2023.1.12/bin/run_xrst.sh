#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/run_xrst.sh' ]
then
   echo 'must execut bin/run_xrst.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'html' ] && [ "$1" != 'tex' ]
then
   echo 'usage: bin/run_xrst.sh (html|tex) [--rst_line_numbers]'
   exit 1
fi
if [ "$2" != '' ] && [ "$2" != '--rst_line_numbers' ]
then
   echo 'usage: bin/run_xrst.sh (html|tex) [--rst_line_numbers]'
   exit 1
fi
target="$1"
rst_line_numbers="$2"
# -----------------------------------------------------------------------------
# index_page_name
index_page_name=$(\
   sed -n -e '/^ *--index_page_name*/p' .readthedocs.yaml | \
   sed -e 's|^ *--index_page_name *||' \
)
# -----------------------------------------------------------------------------
echo_eval python -m xrst  \
   --page_source \
   --group_list      default user dev \
   --html_theme      sphinx_book_theme \
   --target          $target \
   --index_page_name $index_page_name
   $rst_line_numbers
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
