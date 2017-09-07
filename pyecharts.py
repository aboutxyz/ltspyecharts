from pyecharts import Bar

voyagename = ['CAT','NEAX','PAN NKT1','SITC NJ1','SITC NA1','SCT', 'NT1','ST2','CPS','CPF','CHS','CTI','EASNSP']

CATV = [314,67,406,338,188,86,120,101]
NEAXV = []
NKT1V = []
NJ1V = []
NA1V = []
SCTV = []
NT1V = []
ST2V = []
CPSV = []
CPFV = []
CHSV = []
CTIV = []
EASNSPV = []

attr = ["{}月".format(i) for i in range(1,13)]
bar = Bar("按月统计各航线出货量")
bar.add("CAT",attr, CATV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NEAX",attr, NEAXV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NKT1",attr, NKT1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("SCT",attr, SCTV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NA1",attr, NA1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NT1",attr, NT1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("ST2",attr, ST2V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CPS",attr, CPSV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CPF",attr, CPFV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CHS",attr, CHSV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CTI",attr, CTIV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("EASNSP",attr, EASNSPV, mark_line = ["average"], mark_point = ["max","min"])