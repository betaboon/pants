# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.python.tasks.checkstyle.plugin_subsystem_base import PluginSubsystemBase


class ImportOrderSubsystem(PluginSubsystemBase):
  options_scope = 'pycheck-import-order'

  def get_plugin_type(self):
    from pants.backend.python.tasks.checkstyle.import_order import ImportOrder
    return ImportOrder
