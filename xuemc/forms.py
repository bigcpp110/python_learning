from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,HiddenField,SelectField,TextAreaField
from wtforms.validators import Length,Email,DataRequired,EqualTo

class SchoolForm(FlaskForm):
    id=HiddenField("id")
    name=StringField("学校名称",validators=[Length(min=1,max=50)])
    area_id=SelectField("所在区县",coerce=int)
    teachdesc=TextAreaField("校长及教师情况")
    address=StringField("地址")
    schooltype_id=SelectField("学校类型",coerce=int)
    website=SelectField("网址")
    distinguish=TextAreaField("教学特色")
    leisure=TextAreaField("招生条件及招生条件")
    threashold=TextAreaField("")