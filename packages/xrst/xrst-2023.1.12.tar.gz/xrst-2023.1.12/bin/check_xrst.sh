#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
function echo_eval {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
# bash funciton that prompts [yes/no] and returns (exits 1) on yes (no)
function continue_yes_no {
   read -p '[yes/no] ? ' response
   while [ "$response" != 'yes' ] && [ "$response" != 'no' ]
   do
      echo "response = '$response' is not yes or no"
      read -p '[yes/no] ? ' response
   done
   if [ "$response" == 'no' ]
      then exit 1
   fi
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_xrst.sh" ]
then
   echo "bin/check_xrst.sh: must be executed from its parent directory"
   exit 1
fi
PYTHONPATH="$PYTHONPATH:$(pwd)"
# -----------------------------------------------------------------------------
# index_page_name
index_page_name=$(\
   sed -n -e '/^ *--index_page_name*/p' .readthedocs.yaml | \
   sed -e 's|^ *--index_page_name *||' \
)
# -----------------------------------------------------------------------------
# html
# run from html directory so that project_directory is not working directory
if [ ! -e build ]
then
   mkdir build
fi
cd    build
#
# ./xrst.toml
sed -e "s|^project_directory *=.*|project_directory = '..'|"  \
   ../xrst.toml > xrst.toml
#
for group_list in 'default' 'default user dev'
do
   if [ -e rst ]
   then
      echo_eval rm -r rst
   fi
   args='--local_toc'
   if [ "$group_list" == 'default' ]
   then
      args="$args --config_file ../xrst.toml"
   else
      args="$args --index_page_name $index_page_name"
      args="$args --config_file xrst.toml"
   fi
   args="$args --group_list $group_list"
   args="$args --html_theme sphinx_rtd_theme"
   echo "python -m xrst $args"
   if ! python -m xrst $args 2> check_xrst.$$
   then
      type_error='error'
   else
      type_error='warning'
   fi
   if [ -s check_xrst.$$ ]
   then
      cat check_xrst.$$
      rm check_xrst.$$
      echo "$0: exiting due to $type_error above"
      exit 1
   fi
done
rm check_xrst.$$
cd ..
# -----------------------------------------------------------------------------
rst_dir='build/rst'
file_list=$(ls -a $rst_dir | sed -n -e "s|^$rst_dir/||" -e '/[.]rst$/p' )
for file in $file_list
do
   if [ ! -e test_rst/$file ]
   then
      echo "The output file test_rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    cp $rst_dir/$file test_rst/$file"
      continue_yes_no
      cp $rst_dir/$file test_rst/$file
   elif ! diff $rst_dir/$file test_rst/$file
   then
      echo "$rst_dir/$file changed; above is output of"
      echo "    diff $rst_dir/$file test_rst/$file"
      echo 'Should we use the following command to fix this'
      echo "    cp $rst_dir/$file test_rst/$file"
      continue_yes_no
      cp $rst_dir/$file test_rst/$file
   else
      echo "$file: OK"
   fi
done
# -----------------------------------------------------------------------------
file_list=$(ls test_rst/*.rst | sed -e 's|^test_rst/||' )
file_list=$(ls -a test_rst | sed -n -e "s|^test_rst/||" )
for file in $file_list
do
   if [ ! -e build/rst/$file ]
   then
      echo "The output file build/rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    git rm -f test_rst/$file"
      continue_yes_no
      git rm -f test_rst/$file
   fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
