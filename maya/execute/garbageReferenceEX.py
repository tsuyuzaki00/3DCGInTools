# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ..library import cleanLB as cLB
cit.reloads([cLB])

def main():
    cLB.delGarbageReference_edit_func()