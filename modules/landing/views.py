from flask import Blueprint, flash, render_template

landing_bp = Blueprint('landing', __name__)

@landing_bp.route('/')
def landing():
    return render_template('landing/index.html')