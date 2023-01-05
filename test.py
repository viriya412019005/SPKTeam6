# line_data = 0
# line_data2 = 0
# lines = []
# test=222
# test2=666

# with open(r'project_d.dzn', 'r') as fp:
#         lines = fp.readlines()
#         for line in lines:
#             if line.find("max_calories") != -1:
#                 line_data += lines.index(line)
#             if line.find("max_cost") != -1:
#                 line_data2 += lines.index(line)

# with open(r"project_d.dzn", 'w') as fp:
#     for number, line in enumerate(lines):
#         if number in [line_data]:
#             fp.write('max_calories='+str(test)+";\n")
#         if number in [line_data2]:
#             fp.write('max_cost='+str(test2)+";\n")
#         if number not in [line_data, line_data2]:
#             fp.write(line)

import minizinc

def m_project():
    array_solution = []
    final_array_solution = []
    model = minizinc.Model("project.mzn")
    model.add_file("project_d.dzn")
    gecode = minizinc.Solver.lookup("gecode")
    instance = minizinc.Instance(gecode, model)
    result = instance.solve(all_solutions=True)
    for i in range(len(result)):
        arr_result = str(result[i]).split(",")
        array_solution.append(arr_result)
    for x in array_solution:
        temp = []
        for y in x:
            temp.append(int(y))
        final_array_solution.append(temp)
    return final_array_solution

hasil = m_project()

print(hasil)