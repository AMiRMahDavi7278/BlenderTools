# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Copyright (C) 2013-2014: SCS Software

import bpy
from bpy.app.handlers import persistent
from io_scs_tools.internals.containers import config as _config_container
from io_scs_tools.consts import Icons as _ICONS_consts
from io_scs_tools.utils import get_scs_globals as _get_scs_globals


@persistent
def pre_save(scene):
    # remove custom icons from blender datablock
    icon_list = _ICONS_consts.Types.as_list()
    for icon in icon_list:
        if icon in bpy.data.images:
            img = bpy.data.images[icon]
            img.use_fake_user = False
            img.user_clear()

            bpy.data.images.remove(img)

    # clear all not needed inventories
    scs_globals = _get_scs_globals()
    scs_globals.scs_hookup_inventory.clear()
    scs_globals.scs_matsubs_inventory.clear()
    scs_globals.scs_sign_model_inventory.clear()
    scs_globals.scs_traffic_rules_inventory.clear()
    scs_globals.scs_tsem_profile_inventory.clear()


@persistent
def post_save(scene):
    # reaload inventories
    readonly = True
    scs_globals = _get_scs_globals()
    _config_container.update_hookup_library_rel_path(
        scs_globals.scs_hookup_inventory,
        scs_globals.hookup_library_rel_path,
        readonly
    )
    _config_container.update_matsubs_inventory(
        scs_globals.scs_matsubs_inventory,
        scs_globals.matsubs_library_rel_path,
        readonly
    )
    _config_container.update_traffic_rules_library_rel_path(
        scs_globals.scs_traffic_rules_inventory,
        scs_globals.traffic_rules_library_rel_path,
        readonly
    )
    _config_container.update_tsem_library_rel_path(
        scs_globals.scs_tsem_profile_inventory,
        scs_globals.tsem_library_rel_path,
        readonly
    )
    _config_container.update_sign_library_rel_path(
        scs_globals.scs_sign_model_inventory,
        scs_globals.sign_library_rel_path,
        readonly
    )