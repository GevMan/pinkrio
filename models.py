from app import db,app
from datetime import datetime
import re
from flask_login import UserMixin
from sqlalchemy import Column, types,FLOAT
from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(), validators.Email()])
    message = TextAreaField("Message",  [validators.Required()])
    submit = SubmitField("Send Message")


class articles(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    text=db.Column(db.String(1000))
    desc=db.Column(db.String(1000))
    alias=db.Column(db.String(200),unique=True)
    img=db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))
    keywords = db.Column(db.String(200))
    meta_desc = db.Column(db.String(200))
    article_id = db.relationship('comments', backref='articles_id')
    author = db.Column(db.String(200))
    


    def __init__(self,*args,**kwargs):
        super(articles,self).__init__(*args,**kwargs)

    def __repr__(self):
        return self.title

class categories(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    parent_id= db.Column(db.Integer)
    alias=db.Column(db.String(200),unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    article_catgeories=db.relationship('articles',backref='category')

    def __init1__(self,*args,**kwargs):
        super(categories,self).__init1__(*args,**kwargs)

    def __repr__(self):
        return self.title

class comments(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(2000))
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    site=db.Column(db.String(100))
    parent_id= db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    article_id=db.Column(db.Integer,db.ForeignKey('articles.id'))
   

    def __init2__(self,*args,**kwargs):
        super(comments,self).__init2__(*args,**kwargs)

    def __repr__(self):
        return self.text

class filters(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    alias=db.Column(db.String(200),unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    #filter_alias=db.relationship('portfolios',backref='aliass')

    def __init3__(self,*args,**kwargs):
        super(filters,self).__init3__(*args,**kwargs)

    def __repr__(self):
        return self.title

class menus(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    path=db.Column(db.String(200))
    parent= db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init4__(self,*args,**kwargs):
        super(menus,self).__init4__(*args,**kwargs)

    def __repr__(self):
        return self.title

class users(db.Model,UserMixin):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    name=db.Column(db.String(100))
    login=db.Column(db.String(100))
    password=db.Column(db.String(100))
    remember_token = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    role_user=db.relationship('role_user',backref='user')
    comments_user=db.relationship('comments',backref='users_id')
    article_user=db.relationship('articles',backref='article_user_id')
    #user_email=db.relationship('password_resets',backref='email_user')
    #remeber=db.relationship('password_resets',backref='token')
    def __init5__(self,*args,**kwargs):
        super(users,self).__init5__(*args,**kwargs)

    def __repr__(self):
        return self.name
"""
class migrations(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    migration=db.Column(db.String(100))
    batch=db.Column(db.Integer)

    def __init6__(self,*args,**kwargs):
        super(migrations,self).__init6__(*args,**kwargs)

    def __repr__(self):
        return self.migration
"""

class permissions(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    permission_id=db.relationship('permission_role',backref='permission')

    def __init7__(self,*args,**kwargs):
        super(permissions,self).__init7__(*args,**kwargs)

    def __repr__(self):
        return self.name

class roles(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    role_id=db.relationship('permission_role',backref='perm_role',lazy='dynamic')
    role_user=db.relationship('role_user',backref='role')

    def __init8__(self,*args,**kwargs):
        super(roles,self).__init8__(*args,**kwargs)

    def __repr__(self):
        return self.name


class permission_role(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    permission_id=db.Column(db.Integer,db.ForeignKey('permissions.id'))

    def __init9__(self,*args,**kwargs):
        super(permission_role,self).__init9__(*args,**kwargs)

    def __repr__(self):
        return str(self.id)

class portfolios(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    text=db.Column(db.String(500))
    customer=db.Column(db.String(200))
    alias=db.Column(db.String(200),unique=True)
    img=db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    #filter_alias=db.Column(db.String(200),db.ForeignKey('filters.id'))
    keywords=db.Column(db.String(200))
    meta_desc=db.Column(db.String(200))
    skills=db.Column(db.String(200))
    year=db.Column(db.String(200))
    
    
    def __init10__(self,*args,**kwargs):
        super(portfolios,self).__init10__(*args,**kwargs)

    def __repr__(self):
        return self.title

class role_user(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __init11__(self,*args,**kwargs):
        super(role_user,self).__init11__(*args,**kwargs)

    def __repr__(self):
        return str(self.id)

class sliders(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.String(200))
    desc=db.Column(db.String(1000))
    title=db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init12__(self,*args,**kwargs):
        super(sliders,self).__init12__(*args,**kwargs)

    def __repr__(self):
        return str(self.id)
"""
class password_resets(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(200),db.ForeignKey('users.id'))
    token=db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init13__(self,*args,**kwargs):
        super(password_resets,self).__init12__(*args,**kwargs)

    def __repr__(self):
        return str(self.id)
"""