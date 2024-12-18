#!/bin/bash

# Odoo 17

modules=( estate )
src_dir=.
target_dir=/opt/odoo/custom/addons/
odoo_user=odoo
odoo_service=/etc/init.d/odoo-server

for mod_name in "${modules[@]}";
do
   echo sudo $mod_name $src_dir $target_dir

   echo sudo rm -rf  ${target_dir}/${mod_name}
   sudo rm -rf  ${target_dir}/${mod_name}

   echo sudo cp -r ./${mod_name} ${target_dir}
   sudo cp -r ./${mod_name} ${target_dir}

   echo sudo chown -R ${odoo_user}:${odoo_user} ${target_dir}
   sudo chown -R ${odoo_user}:${odoo_user} ${target_dir}
done
echo sudo ${odoo_service} stop
echo sudo ${odoo_service} start