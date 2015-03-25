Python @lazyprop decorator
-------------------------
Implementation of http://en.wikipedia.org/wiki/Lazy_initialization
Based on http://stackoverflow.com/a/3013910 - extended to support invalidation / setting, fully unit tested


Basic usage - very_expensive_calculation() is only called the first time, the result is cached and returned for subsequent calls


    class YourClass(object):
        @lazyprop
        def lazy(self):
            return very_expensive_calculation()

        def print_result(self):
            print "You can safely use lazy twice without any performance penalty: %s %s" % (self.lazy, self.lazy)


You can also invalidate the cache if needed


    class YourClass(object):
        @lazyprop
        def lazy(self):
            return very_expensive_calculation()

        def change_params_for_expensive_calculation():
            ...
            # This will invalidate the lazy cache and force recalculation next time self.lazy is accessed
            del self.lazy 


Or even set it:


    class YourClass(object):
        @lazyprop
        def lazy(self):
            return very_expensive_calculation()

        def do_something_else():
            ...
            # This will change the stored lazy cache value
            self.lazy = new_value()


See the unit tests for more examples
