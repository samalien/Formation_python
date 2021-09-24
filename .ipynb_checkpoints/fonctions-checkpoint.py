from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import clear_output
import ipywidgets as widgets
def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Correct." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Error. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

Q1 = create_multipleChoice_widget('print((17 - 6)%(5 + 2))',['Correct','Incorrect'],'Correct')
Q2 = create_multipleChoice_widget('print(4/2 - 7*7)',['Correct','Incorrect'],'Correct')
Q3 = create_multipleChoice_widget('print((1 + 2 + 4) / 13',['Correct','Incorrect'],'Incorrect')
Q4 = create_multipleChoice_widget(' Si nous ajoutons maintenant cette nouvelle 5ème ligne de code à ce qui précède, quelle sera la sortie ? >>> print(crs_per_rab) ',['0,5','2.0','3.0','Aucune de ces réponses'],'3.0')




#--------------------------------------------------------------------------------------
data = {"del = 1":"data_1", "delware = 1":"data_2", "1 de = first":"data_3", "de = 1":"data_4"}
responses = ["delware = 1", "de = 1"]
data2 = {"Combien de personnes sont venues lors de votre voyage de pêche ?":"data_1", 
        "Longueur d'un poisson que vous avez pêché en mètres":"data_2", 
        "nombre de poissons pêché":"data_3", "Temps qu'il a fallu pour pour attraper le premier poisson, en heures":"data_4"}
responses2 = ["Longueur d'un poisson que vous avez pêché en mètres", "Temps qu'il a fallu pour pour attraper le premier poisson, en heures"]

data3 = {"Pour qu'il soit long de deux caracères comme !=":"data_1", "parce que = est utilisé pour affecter des variables":"data_2", "l'un ou l'autre fonctionne":"data_3", "parce que = est utilisé pour vérifier si deux valeurs sont approximativement égales":"data_4"}
responses3 = ["parce que = est utilisé pour affecter des variables"]
def quiz_checkBox(data, responses):
    feedback_out = widgets.Output()
    names = []
    checkbox_objects = []
    for key in data:
        checkbox_objects.append(widgets.Checkbox(value=False, description=key))
        names.append(key)

    arg_dict = {names[i]: checkbox for i, checkbox in enumerate(checkbox_objects)}

    ui = widgets.VBox(children=checkbox_objects)

    selected_data = []
    def select_data(**kwargs):
        selected_data.clear()

        for key in kwargs:
            if kwargs[key] is True:
                selected_data.append(key)

        #print(selected_data)

    def check_selection(b):
        if responses==selected_data:
            s = '\x1b[6;30;42m' + "Correct." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Error. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return

    check = widgets.Button(description="submit")
    button_submit=widgets.VBox([check,feedback_out])
    check.on_click(check_selection)
    out = widgets.interactive_output(select_data, arg_dict)
    display(ui, out,button_submit)