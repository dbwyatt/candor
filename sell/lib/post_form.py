__author__ = 'Daniel'

import django.forms
from django.http import HttpRequest


class Form(django.forms.Form):

    submit_buttons = "<input type='submit' value='Submit' class='btn btn-warning' />"

    def __init__(self, request, *args, **kwargs):
        assert isinstance(request, HttpRequest), 'Invalid request object'
        self.request = request
        self.form_id = next(request.generator)
        super().__init__(*args, **kwargs)
        self.init()

    def __str__(self):
        return self.as_full()

    def as_full(self):
        html = []

        # if the form is multipart
        if self.is_multipart():
            html.append("<form method='POST' enctype='multipart/form-data' id={}>".format(self.form_id))
        else:
            html.append("<form method='POST' id={}>".format(self.form_id))

        # put in non field errors
        error = self.non_field_errors()
        print(error)
        if error:
            html.append("<div class='alert alert-danger' roles='alert'>{}</div>".format(error))

        # begin table
        html.append("   <table class='form-table'>")
        # html.append("{% CSRF %}")
        # hidden fields
        for field in self.hidden_fields():
            html.append("<tr>")
            html.append("   <td><label for={}>{}</label></td>".format(field.name, field.name))
            html.append("   <td><input type='hidden' name={} id={} /></td>".format(field.name, field.name))
            html.append("</tr>")

        # visible fields
        for field in self.visible_fields():
            html.append("<tr>")
            if field.label:
                html.append("   <td data-name='{}'><label for={}>{}</label></td>".format(field.name, field.name, field.label))
            html.append("<td>")
            html.append(field.as_widget(attrs={'class': 'form-control'}))
            html.append("</td>")
            # else:
            #     html.append("   <td><input name={} id={} class='form-control' /><span>{}</span>".format(field.name, field.name, field.help_text))

            if field.errors:
                html.append("<div class='alert alert-danger' roles='alert'>{}</div>".format(field.errors))
            html.append("</td></tr>")

#$('td[name=startdate]')

        # submit button
        html.append("   <tr>")
        html.append("       <td>{}</td>".format(self.submit_buttons))
        html.append("   </tr>")
        # close table and form
        html.append("   </table>")
        html.append("</form>")

        # join string together
        return "\n".join(html)

    # def add_fields_as_table(self, html):
    #     html = []
    #     # hidden fields
    #     for field in self.hidden_fields():
    #         html.append("<input type='hidden' name={} />".format(field.name))
    #
    #     # visible fields
    #     for field in self.visible_fields():
    #         html.append("<input name={} />".format(field.name))
    #

    def init(self):
        pass

    def commit(self):
        pass