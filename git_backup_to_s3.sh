#!/bin/bash

# Ref: https://gist.github.com/philippb/1988919
# Script to backup git repo to S3
# s3cmd - needs to be configured...
bucket='<bucket_full_path>'
dir='/tmp/test_backup'
#(for cloning it asks for the password, to automate its hard-code here...)
#Keeping Password is not safe
#If special characters are there in password, escape
#E,g., Special character for @ is %40
account='<account username>:<password>@bitbucket.org/<proj>'

# Setup repository to $1
repository=$1  #repository

date=`date '+%Y%m%d%H%M%S'`
s3_date=`date '+%Y%m%d'`

# Create the backup directory
mkdir -p $dir

echo "Backing up $repository"

git clone https://$account/$repository $dir/$repository.$date
if [ $? -ne 0 ]; then
  echo "Error cloning $repository"
  exit 1
fi

tar cpzf $dir/$repository.$date.tgz $dir/$repository.$date
if [ $? -ne 0 ]; then
  echo "Error compressing $repository"
  exit 1
fi

if [ -f $dir/$repository.$date.tgz ]; then
  s3cmd put $dir/$repository.$date.tgz s3://$bucket/$s3_date/$repository/$repository.$date.tgz
fi

if [ $? -ne 0 ]; then
  echo "Error uploading $repository to S3"
  exit 1
fi

#delete tar file and checked out folder
/bin/rm $dir/$repository.$date.tgz
/bin/rm -rf $dir/$repository.$date
if [ $? -ne 0 ]; then
  echo "Error removing $repository"
  exit 1
fi

echo "Successfully backed up $repository"
