
#
# from basic_project_library.phase_A.growing_module import fun
# print(dir())



from basic_project_library.phase_A import growing_module

growing_module.fun()

import basic_project_library.phase_B.growing_module as gm

gm.fun()
print(dir())

import phase_A.understandStructure