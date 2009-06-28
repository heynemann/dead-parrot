# -*- coding: utf-8; -*-
#
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
import re
from deadparrot import models
from utils import assert_raises

def test_model_file_manager_class_exists():
    msg1 = 'deadparrot.models should have the class FileSystemManager'
    assert hasattr(models, 'FileSystemModelManager'), msg1
    msg2 = 'deadparrot.models.FileSystemManager should have the class FileSystemManager'
    assert issubclass(models.FileSystemModelManager, models.ModelManager), msg2

def test_model_file_manager_construction_without_basepath_raises():
    def make_class():
        class Parrot(models.Model):
            objects = models.FileSystemModelManager()

    assert_raises(TypeError, make_class, exc_pattern='__setup__.. takes exactly 2 arguments .1 given.')

def test_model_file_manager_construction_with_basepath_nonstring_raises():
    def make_class_number():
        class Parrot(models.Model):
            objects = models.FileSystemModelManager(base_path=10)

    def make_class_list():
        class Parrot(models.Model):
            objects = models.FileSystemModelManager(base_path=[])

    assert_raises(TypeError, make_class_number, exc_pattern='FileSystemModelManager "base_path" parameter should be string, got %r' % 10)
    assert_raises(TypeError, make_class_list, exc_pattern='FileSystemModelManager "base_path" parameter should be string, got %s' % re.escape(repr([])))

def test_model_file_manager_has_method_create():
    class Parrot(models.Model):
        objects = models.FileSystemModelManager(base_path='/home/wee')

    classname = Parrot.objects.__class__.__name__
    assert hasattr(Parrot.objects, 'create'), '%s should have the method "create"' % classname
    assert callable(Parrot.objects.create), '%s.create should be callable' % classname