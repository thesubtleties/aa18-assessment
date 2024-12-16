from flask import Blueprint, render_template, redirect
from ..forms import NewInstrument
from ..models import db, Instrument

simple_bp = Blueprint("simple", __name__)

@simple_bp.route("/")
def index():
    return render_template("main_page.html")

@simple_bp.route("/new_instrument", methods=["GET"])
def simple_form():
    form = NewInstrument()
    return render_template("simple_form.html", form=form)

@simple_bp.route("/new_instrument", methods=["POST"])
def simple_form_submit():
    form = NewInstrument()
    if form.validate_on_submit():
        instrument = Instrument(
            date_bought = form.date_bought.data,
            nickname = form.nickname.data,
            year = form.year.data,
            maker = form.maker.data,
            type = form.type.data,
            used = form.used.data
        )

        db.session.add(instrument)
        db.session.commit()

        return redirect("/instrument_data")
    return "Bad Data", 400

@simple_bp.route("/instrument_data")
def instrument_data():
    instruments = Instrument.query.filter(Instrument.nickname.like("M%")).all()
    return render_template("simple_form_data.html", instruments=instruments)

