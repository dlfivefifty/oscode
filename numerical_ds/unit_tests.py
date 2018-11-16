#!/usr/bin/env python
import test
import nose
import numpy
import random

def test_dws():
    
    n = 80
    t = random.random()*100
    H = random.random()*10
    d1wa = numpy.sqrt(n**2-1) * -2 * t / (1 + t**2)**2
    d2wa = numpy.sqrt(n**2-1) * (6 * t**2 - 2 ) / (1 + t**2)**3
    d3wa = numpy.sqrt(n**2-1) * 24 * t * (1 - t**2) / (1 + t**2)**4

    print(n, t, test.dw(t,H), d1wa)
    print(n, t, test.ddw(t,H), d2wa) 
    print(n, t, test.dddw(t,H), d3wa)
    print(n, t, test.dwb(t,H), d1wa)
    print(n, t, test.ddwb(t,H), d2wa) 
    print(n, t, test.dddwb(t,H), d3wa)

    assert abs((test.dw(t,H) - d1wa)/d1wa) < 1e-6
    assert abs((test.ddw(t,H) - d2wa)/d2wa) < 1e-6 
    assert abs((test.dddw(t,H) - d3wa)/d3wa) < 1e-6
    assert abs((test.dwb(t,H) - d1wa)/d1wa) < 1e-6 
    assert abs((test.ddwb(t,H) - d2wa)/d2wa) < 1e-6 
    assert abs((test.dddwb(t,H) - d3wa)/d3wa) < 1e-6 

