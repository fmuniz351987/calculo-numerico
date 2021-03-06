import unittest

import numpy as np

from numerico import eqroot


class EqRootTest(unittest.TestCase):
    def test_limits(self):
        coef = [24,-14,-13,2,1]
        l = eqroot.Limits(coef)
        min_pos, max_pos = l.pos
        min_neg, max_neg = l.neg
        self.assertEqual(min_pos, 0.631578947368421)
        self.assertEqual(max_pos, 4.741657386773941)
        self.assertEqual(min_neg, -14.0)
        self.assertEqual(max_neg, -0.5760434788494824)

    def test_briot_ruffini(self):
        p = np.poly1d([1,-5,6])
        q, r = eqroot.briot_ruffini(p, 2)
        self.assertTrue((q == np.poly1d([1,-3])).all())
        self.assertEqual(r, 0)

    def test_bissection(self):
        poly = np.poly1d([1,0,-1])
        x, err = eqroot.bissection(poly, 0, 3)
        self.assertEqual(round(x), 1)

    def test_secant(self):
        poly = np.poly1d([1,0,-1])
        x, err = eqroot.secant(poly, 0, 3)
        self.assertEqual(round(x), 1)

    def test_regula_falsi(self):
        poly = np.poly1d([1,0,-1])
        x, err = eqroot.regula_falsi(poly, 0, 3)
        self.assertEqual(round(x), 1)

    def test_pegasus(self):
        poly = np.poly1d([1,0,-1])
        x, err = eqroot.pegasus(poly, 0, 3)
        self.assertEqual(round(x), 1)

    def test_muller(self):
        func = lambda x: 0.05 * x**3 - 0.4 * x ** 2 + 3 * np.sin(x) * x
        x, err = eqroot.muller(func, 10, 12, toler=1e-10)
        self.assertEqual(x, 11.743931234468302)

    def test_wdb(self):
        func = lambda x: 0.05 * x**3 - 0.4 * x ** 2 + 3 * np.sin(x) * x
        x, err = eqroot.wijngaarden_dekker_brent(func, 10, 12, toler=1e-10)
        self.assertEqual(x, 11.743931232127181)

    def test_newton(self):
        func = np.poly1d([1,2,-13,-14,24])
        x, err = eqroot.newton(func, func.deriv(), 4, toler=1e-5)
        self.assertEqual(round(x, 5), 3)

    def test_schroder(self):
        func = np.poly1d([1,2,-12,14,-5])
        x, err = eqroot.schroder(func, func.deriv(), x0=2, m=3, toler=1e-5)
        self.assertEqual(round(x, 5), 1)
