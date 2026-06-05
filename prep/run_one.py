import sys, build_md as b
fname = sys.argv[1]
b.build(fname, b.META[fname])
