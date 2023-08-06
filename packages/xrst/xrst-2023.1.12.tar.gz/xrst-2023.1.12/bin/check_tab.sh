#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-22 Bradley M. Bell
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_tab.sh" ]
then
   echo "bin/check_tab.sh: must be executed from its parent directory"
   exit 1
fi
ok='yes'
for file in $(git ls-files)
do
   if grep -P '\t' $file > /dev/null
   then
      echo "$file has a tab"
      ok='no'
   fi
done
if [ "$ok" != 'yes' ]
then
   echo 'check_tab: Error'
   exit 1
fi
echo 'check_tab.sh: OK'
exit 0
