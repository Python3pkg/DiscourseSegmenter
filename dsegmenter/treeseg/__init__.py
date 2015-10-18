#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

##################################################################
# Documentation
"""
Package for constructing segmentation trees from parse trees.

Modules:
constants - defines constants specific to that package
discourse_segment - defines class for handling discourse segments
treesegmenter - defines auxiliary class for converting syntax trees
                   to dicsourse segments

"""

##################################################################
# Imports
from .constants import DEFAULT_SEGMENT, ENCODING, GREEDY, GENEROUS, \
    DEPENDENCY, CONSTITUENCY
from .discourse_segment import DiscourseSegment
from .treesegmenter import TreeSegmenter

##################################################################
# Intialization
__name__ = "treeseg"
__all__ = ["DEFAULT_SEGMENT", "ENCODING", "GREEDY", "GENEROUS", "DEPENDENCY", \
           "CONSTITUENCY", "DiscourseSegment", "TreeSegmenter"]
__author__ = "Uladzimir Sidarenka"
__email__ = "sidarenk at uni dash potsdam dot de"
__version__ = "0.0.1"
