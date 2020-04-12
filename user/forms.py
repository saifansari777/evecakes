from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class Newloginform(LoginForm):

    def __init__(self, *args, **kwargs):
        super(Newloginform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'

        self.helper.add_input(Submit('submit', 'Submit'))

    