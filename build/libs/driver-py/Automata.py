import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import MiscTypes
import Int
import EVMConstants
import EVMOpcodes
import OpcodeDecoder
import Hex
import StackElement
import WeakPre
import State
import EVMToolTips
import Instructions
import BinaryDecoder
import LinSegments
import Splitter
import SegBuilder
import CFGState
import ProofObject
import PrettyIns
import PrettyPrinters

# Module: Automata


class ValidAuto:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Auto_Auto(_dafny.Map({}), _dafny.Map({}), _dafny.SeqWithoutIsStrInference([]), _dafny.Map({}))

class Auto:
    @classmethod
    def default(cls, ):
        return lambda: Auto_Auto(_dafny.Map({}), _dafny.Map({}), _dafny.Seq({}), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Auto(self) -> bool:
        return isinstance(self, Auto_Auto)
    def Equals(self, b):
        return (((self).transitionsNat) == ((b).transitionsNat)) and (((self).states) == ((b).states))

    def AddState(self, i):
        if (i) in ((self).states):
            return self
        elif True:
            d_829_dt__update__tmp_h0_ = self
            d_830_dt__update_hrevTransitionsNat_h0_ = ((self).revTransitionsNat).set(len((self).states), _dafny.SeqWithoutIsStrInference([]))
            d_831_dt__update_htransitionsNat_h0_ = ((self).transitionsNat).set(len((self).states), _dafny.SeqWithoutIsStrInference([]))
            d_832_dt__update_hindexOf_h0_ = ((self).indexOf).set(i, len((self).states))
            d_833_dt__update_hstates_h0_ = ((self).states) + (_dafny.SeqWithoutIsStrInference([i]))
            return Auto_Auto(d_831_dt__update_htransitionsNat_h0_, d_830_dt__update_hrevTransitionsNat_h0_, d_833_dt__update_hstates_h0_, d_832_dt__update_hindexOf_h0_)

    def AddStates(self, xs):
        _this = self
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return _this
                elif True:
                    in102_ = (_this).AddState((xs)[0])
                    in103_ = _dafny.SeqWithoutIsStrInference((xs)[1::])
                    _this = in102_
                    
                    xs = in103_
                    raise _dafny.TailCall()
                break

    def AddEdge(self, i, j):
        pat_let_tv0_ = j
        pat_let_tv1_ = i
        pat_let_tv2_ = i
        pat_let_tv3_ = j
        d_834_a1_ = ((self).AddState(i)).AddState(j)
        if (((d_834_a1_).indexOf)[j]) in (((d_834_a1_).transitionsNat)[((d_834_a1_).indexOf)[i]]):
            return d_834_a1_
        elif True:
            def iife0_(_pat_let0_0):
                def iife1_(d_836_dt__update__tmp_h0_):
                    def iife2_(_pat_let1_0):
                        def iife3_(d_837_dt__update_hrevTransitionsNat_h0_):
                            def iife4_(_pat_let2_0):
                                def iife5_(d_838_dt__update_htransitionsNat_h0_):
                                    return Auto_Auto(d_838_dt__update_htransitionsNat_h0_, d_837_dt__update_hrevTransitionsNat_h0_, (d_836_dt__update__tmp_h0_).states, (d_836_dt__update__tmp_h0_).indexOf)
                                return iife5_(_pat_let2_0)
                            return iife4_(MiscTypes.default__.AddKeyVal((d_834_a1_).transitionsNat, ((d_834_a1_).indexOf)[pat_let_tv2_], ((d_834_a1_).indexOf)[pat_let_tv3_]))
                        return iife3_(_pat_let1_0)
                    return iife2_(MiscTypes.default__.AddKeyVal((d_834_a1_).revTransitionsNat, ((d_834_a1_).indexOf)[pat_let_tv0_], ((d_834_a1_).indexOf)[pat_let_tv1_]))
                return iife1_(_pat_let0_0)
            d_835_w_ = iife0_(d_834_a1_)
            return d_835_w_

    def AddEdges(self, i, js, index):
        if (len(js)) == (index):
            return (self).AddState(i)
        elif True:
            d_839_a1_ = (self).AddEdge(i, (js)[index])
            d_840_a2_ = (d_839_a1_).AddEdges(i, js, (index) + (1))
            return d_840_a2_

    def SSize(self):
        return len((self).states)

    def TSize(self, index):
        d_841___accumulator_ = 0
        _this = self
        while True:
            with _dafny.label():
                if (index) == (len((_this).states)):
                    return (0) + (d_841___accumulator_)
                elif True:
                    d_841___accumulator_ = (d_841___accumulator_) + (len(((_this).transitionsNat)[index]))
                    in104_ = _this
                    in105_ = (index) + (1)
                    _this = in104_
                    
                    index = in105_
                    raise _dafny.TailCall()
                break

    def Succ(self, s):
        return _dafny.SeqWithoutIsStrInference([((self).states)[(((self).transitionsNat)[((self).indexOf)[s]])[d_842_i_]] for d_842_i_ in range(len(((self).transitionsNat)[((self).indexOf)[s]]))])

    def SuccNat(self, i):
        return ((self).transitionsNat)[i]

    def PredNat(self, i):
        return ((self).revTransitionsNat)[i]

    def ToDot(self, nodeToString, labelToString, prefix, name):
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "// Number of states: "))).VerbatimString(False))
        _dafny.print(_dafny.string_of((self).SSize()))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\n"))).VerbatimString(False))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "// Number of transitions : "))).VerbatimString(False))
        _dafny.print(_dafny.string_of((self).TSize(0)))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\n"))).VerbatimString(False))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "digraph G {\n"))).VerbatimString(False))
        _dafny.print((prefix).VerbatimString(False))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\n"))).VerbatimString(False))
        hi0_ = len((self).states)
        for d_843_i_ in range(0, hi0_):
            _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s_"))).VerbatimString(False))
            _dafny.print(_dafny.string_of(d_843_i_))
            _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [label="))).VerbatimString(False))
            _dafny.print(((nodeToString(((self).states)[d_843_i_])) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "]\n")))).VerbatimString(False))
        hi1_ = len((self).states)
        for d_844_i_ in range(0, hi1_):
            hi2_ = len(((self).transitionsNat)[d_844_i_])
            for d_845_j_ in range(0, hi2_):
                _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s_"))).VerbatimString(False))
                _dafny.print(_dafny.string_of(d_844_i_))
                _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " -> "))).VerbatimString(False))
                _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s_"))).VerbatimString(False))
                _dafny.print(_dafny.string_of((((self).transitionsNat)[d_844_i_])[d_845_j_]))
                _dafny.print((labelToString(((self).states)[d_844_i_], d_845_j_, ((self).states)[(((self).transitionsNat)[d_844_i_])[d_845_j_]])).VerbatimString(False))
                _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ";\n"))).VerbatimString(False))
        _dafny.print((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "}\n"))).VerbatimString(False))


class Auto_Auto(Auto, NamedTuple('Auto', [('transitionsNat', Any), ('revTransitionsNat', Any), ('states', Any), ('indexOf', Any)])):
    def __dafnystr__(self) -> str:
        return f'Automata.Auto.Auto({_dafny.string_of(self.transitionsNat)}, {_dafny.string_of(self.revTransitionsNat)}, {_dafny.string_of(self.states)}, {_dafny.string_of(self.indexOf)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Auto_Auto) and self.transitionsNat == __o.transitionsNat and self.revTransitionsNat == __o.revTransitionsNat and self.states == __o.states and self.indexOf == __o.indexOf
    def __hash__(self) -> int:
        return super().__hash__()

