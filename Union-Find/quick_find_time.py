import timeit
from quick_find import QuickFind

# test execution time for union on list of length 10
qf10_union_time = min(timeit.repeat('qf_10.union(0, 8)',
                                    setup='from __main__ import QuickFind ; qf_10 = QuickFind(10)',
                                    number=10000))
print('union on list of size 10 took {}ms'.format(qf10_union_time))

# test execution time for connected query on list of length 10
qf10_connected_time = min(timeit.repeat('qf_10.connected(0, 8)',
                                        setup='from __main__ import QuickFind ; qf_10 = QuickFind(10) ; ' +
                                                'qf_10.union(0, 8)',
                                        number=10000))
print('connected query on list of size 10 took {}ms'.format(qf10_connected_time))

# test time for union on list of length 100
qf100_union_time = min(timeit.repeat('qf_100.union(0, 96)',
                                    setup='from __main__ import QuickFind ; qf_100 = QuickFind(100)',
                                    number=10000))
print('union on list of size 100 took {}ms'.format(qf100_union_time))

# test time for connected query on list of length 100
qf100_connected_time = min(timeit.repeat('qf_100.connected(0, 96)',
                                        setup='from __main__ import QuickFind ; qf_100 = QuickFind(100) ; ' +
                                                'qf_100.union(0, 96)',
                                        number=10000))
print('connected query on list of size 100 took {}ms'.format(qf100_connected_time))

# union on a list of 1,000. Originally tried 1,000,000, but execution stalled. Quadratic time, indeed!
qf1k_union_time = min(timeit.repeat('qf_1k.union(0, 997)',
                                    setup='from __main__ import QuickFind ; qf_1k = QuickFind(1000)',
                                    number=10000))
print('union on list of size 1,000 took {}ms'.format(qf1k_union_time))

# connected query on list of 1,000
qf1k_connected_time = min(timeit.repeat('qf_1k.connected(0, 997)',
                                            setup='from __main__ import QuickFind ; qf_1k = QuickFind(1000) ; ' +
                                                'qf_1k.union(0, 997)',
                                            number=10000))
print('connected query on list of size 1,000 took {}ms'.format(qf1k_connected_time))