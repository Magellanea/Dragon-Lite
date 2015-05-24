# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import login_required
from dragon_lite.user_group.forms import UserGroupForm
from dragon_lite.user_group.models import UserGroup
from dragon_lite.utils import flash_label_errors


blueprint = Blueprint("user_group", __name__, url_prefix='/user_group',
                        static_folder="../static")


@blueprint.route("/", methods=['GET', 'POST'])
@login_required
def new():
    form = UserGroupForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            UserGroup.create(name=form.name.data)
            flash("User Group Created", 'success')
            return redirect(url_for('public.home'))
        else:
            flash_label_errors(form)
            return render_template("user_groups/new.html", form=form)
    else:
        return render_template("user_groups/new.html", form=form)
