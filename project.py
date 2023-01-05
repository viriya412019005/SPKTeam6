import minizinc
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

dataset_html = [
    ["Nasi uduk"            , 476,      5000],
    ["Nasi kuning"          , 150,      5000],
    ["Nasi putih"           , 130,      4000],

    ["Ayam goreng"          , 386,      10000],
    ["Ayam panggang"        , 246,      10000],
    ["Ayam goreng kecap"    , 359,      10000],
    ["Udang goreng"         , 244,      5000],
    ["Mie goreng"           , 321,      12000],
    ["Telur dadar"          , 188,      12000],
    ["Telur ceplok"         , 92,       15000],
    ["Tempe bacem"          , 157,      5000],
    ["Tempe goreng"         , 118,      5000],
    ["Tempe orek"           , 192,      1000],
    ["Tahu bacem"           , 147,      3000],
    ["Telur asin"           , 138,      3000],
    ["Ati ayam goreng"      , 98,       6000],
    ["Ikan lele goreng"     , 57,       10000],
    ["Ikan teri"            , 213,      4000],
    ["Ikan bandeng goreng"  , 181,      7000],

    ["Tumis buncis"         , 52,       4000],
    ["Sop bayam"            , 78,       4000],
    ["Kangkung"             , 106,      4000],
    ["Bayam bening"         , 15,       4000],
    ["Tumis kacang panjang" , 118,      4000],
    ["Cah toge"             , 38,       4000],
    ["Sayur lodeh"          , 59,       4000],
    ["Cah labu siam"        , 42,       5000],
    ["Sayur asam"           , 88,       5000],
    ["Acar"                 , 53,       4000],
    
    ["Semangka"             , 31,       1000],                           
    ["Nanas"                , 50,       1000],
    ["Mangga"               , 60,       3000],
    ["Anggur"               , 67,       3000],
    ["Pisang"               , 89,       2000],
    ["Jeruk"                , 47,       2500],
    ["Apel"                 , 52,       3500],
    ["Strawberry"           , 32,       5000],
    ["Alpukat"              , 160,      3500],
    ["Buah Naga"            , 50,       3000],
    ["Salak"                , 77,       1500],
    ["Manggis"              , 73,       2850],
    ["Rambutan"             , 70,       1500],
]

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post_index():    
    line_data = 0
    line_data2 = 0
    lines = []

    max_calories = request.form.get("max_calories")
    max_cost = request.form.get("max_cost")
    
    with open(r'project_d.dzn', 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find("max_calories") != -1:
                line_data += lines.index(line)
            if line.find("max_cost") != -1:
                line_data2 += lines.index(line)

    with open(r"project_d.dzn", 'w') as fp:
        for number, line in enumerate(lines):
            if number in [line_data]:
                fp.write('max_calories='+str(max_calories)+";\n")
            if number in [line_data2]:
                fp.write('max_cost='+str(max_cost)+";\n")
            if number not in [line_data, line_data2]:
                fp.write(line)
                
    return redirect("/result")

@app.route("/result")
def f_result():
    result = m_project()
    return render_template("result.html", dataset_html=dataset_html, result=result)

if __name__ == "__main__":
    app.run()

