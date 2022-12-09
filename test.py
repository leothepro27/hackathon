
    gaming_laptops = []
    touchscreen_laptops = []
    #os:
    os = request.form.get("question1")

    #budget:
    min_range_budget = request.args.get("")
    max_range_budget = request.args.get("")

    #brand:
    brand = request.args.get("")

    #screen_size:
    min_range_screen = request.args.get("")
    max_range_screen = request.args.get("")

    #weight:
    min_range_weight = request.args.get("")
    max_range_weight = request.args.get("")

    #gaming:
    if request.args.get("") == "Gaming":
        gaming_laptops = db.execute("SELECT * FROM laptop WHERE Category = 'Gaming'")
    else:
        gaming_laptops = db.execute("SELECT * FROM laptop")

    #touchscreen:
    if request.args.get("") == "Touchscreen":
        touchscreen_laptops: db.execute("SELECT * FROM laptop WHERE Screen LIKE '%Touchscreen%'")
    else:
        touchscreen_laptops = db.execute("SELECT * FROM laptop")

    results = db.execute("SELECT * FROM laptop WHERE Operatingsystem = ? AND Price BETWEEN ? AND ? AND Manufacturer = ? AND Screensize BETWEEN ? AND ? AND Weight BETWEEN ? AND ?", operating_system, min_range_budget, max_range_budget, brand, min_range_screen, max_range_screen, min_range_weight, max_range_weight)

    final_results = []
    for i in range(len(results)):
        for j in range(len(gaming_laptops)):
            for k in range(len(touchscreen_laptops)):
                if results[i] == gaming_laptops[j] == touchscreen_laptops[k]:
                    final_results.append(results[i])

    return jsonify(final_results)


let form1 = document.getElementById("question1");
let options = Array.from(document.querySelectorAll(".Manufacturer_options"))
let answer = []

form1.addEventListener("click", function() {
    for (option of options) {
        if (option.checked) {
            answer.push(option.value)
        }
    }

    myFunction(answer)
})


//
let form2 = document.getElementById("question2");
let options2 = Array.from(document.querySelectorAll(".budget_options"))
let answer2

form2.addEventListener("click", function() {
    for (option of options) {
        if (option.checked) {
            answer2 = option.value
        }
    }

    myFunction(answer2)
})

