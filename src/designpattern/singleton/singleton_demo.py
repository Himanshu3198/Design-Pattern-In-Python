from src.designpattern.singleton.singleton_design import Singleton

s1 = Singleton().get_instance()
s2 = Singleton().get_instance()

s1.hello()
s2.hello()