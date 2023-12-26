from flask import Flask, render_template, request
from view.models import BattleSimulator

app = Flask(__name__, template_folder='./view/templates')
app.config['SECRET_KEY'] = "mysupersecretkey"

@app.route('/', methods=['GET', 'POST'])
def home():
    battleForm = BattleSimulator()
    if request.method == "POST":
        if battleForm.validate():
            # We would actually go off and run the battle here
            for entry in battleForm.attacker_army.entries:
                print(entry.data)
            return render_template('results.html', attacker=battleForm.attacker.data, defender=battleForm.defender.data)
        else:
            print("Form did not validate on submit")
    return render_template('index.html', form=battleForm)

if __name__ == '__main__':
    app.run()
