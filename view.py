import os
import os.path as op
from app import app,db,mail
from flask import Flask, render_template,redirect,url_for,request,request,flash,session,jsonify,json,session
from flask_admin import Admin,AdminIndexView,form
from flask_admin.contrib.sqla import ModelView
from models import *
from flask_login import current_user,login_manager,LoginManager,login_user,logout_user
from flask_admin.menu import MenuLink
from sqlalchemy import desc,exc,desc,select
from flask_paginate import Pagination, get_page_parameter,get_page_args,CURRENT_PAGES
import calendar
import datetime
from validate_email import validate_email
from flask_mail import Mail,Message
from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

#app = Flask(__name__)
class MyModelView(ModelView):
    def is_accessible(self):       
        return  current_user.is_authenticated
        #return False  
    
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
            return  current_user.is_authenticated
            #return False

#def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
       # return redirect(url_for('login', next=request.url))

admin=Admin(app,index_view=MyAdminIndexView(),template_mode='bootstrap3')
admin.add_view(ModelView(articles, db.session))
admin.add_view(ModelView(users, db.session))
admin.add_view(ModelView(categories, db.session))
admin.add_view(ModelView(comments, db.session))
admin.add_view(ModelView(filters, db.session))
admin.add_view(ModelView(menus, db.session))
admin.add_view(ModelView(permissions, db.session,category="permissions"))
admin.add_view(ModelView(permission_role, db.session,category="permissions"))
admin.add_view(ModelView(portfolios, db.session))
admin.add_view(ModelView(roles, db.session,category="roles"))
admin.add_view(ModelView(role_user, db.session,category="roles"))
admin.add_view(ModelView(sliders, db.session))
admin.add_sub_category(name="Links", parent_name="menu")
admin.add_link(MenuLink(name='Home Page', url='/index', category='Links'))

class LogoutMenuLink(MenuLink):
   

    def is_accessible(self):
        return current_user.is_authenticated 
     


admin.add_link(LogoutMenuLink(name='Logout', category='', url="/logout"))



login_manager = LoginManager(app)
#login_manager.init_app(app)
#login_manager.login_view = ''
 
app.secret_key='zzz'

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(user_id)
@app.route('/login')
def login():
    user=users.query.get(1)
    login_user(user)
    return(redirect(url_for("admin.index")))

@app.route('/logout')
def logout():
    logout_user()
    return(redirect(url_for("login_admin")))

@app.route("/")
def index():
    project=portfolios.query.order_by(portfolios.id.desc()).all()
    article=articles.query.order_by(articles.id.desc()).all()
    return(render_template('index.html',projects=project,articles=article))




@app.route('/test/')
def test():
    msg = Message('Hello',sender = 'admin@gmail.com', recipients=['gevman97@gmail.com'])
    msg.body = '<b>hi, this is the mail sent by using the flask web application</b>'
    mail.send(msg)
    return "sent"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
 
    return render_template('contact.html', form=form)

@app.route("/sendMessage",methods=['POST'])
def sendMsg():
    print("-*/*-/-*/-*/*-")
    print(request.form['message'])
    msg = Message(request.form['name'], 
                    recipients=['gevman97@gmail.com'],
                    html="Email: " +request.form['email'] +'<br>'+ "  Message: " + request.form['message']+" ")
    mail.send(msg)
    return(redirect(url_for('contact')))
@app.route("/project/<id>")
def project(id):
    projects=portfolios.query.get_or_404(id)
    projectById=portfolios.query.all()
    return(render_template('project.html',projects=projects,projectById=projectById))

@app.route("/portfolio/<int:page_num>")
def portfolio(page_num):    
    projects_paginate=portfolios.query.order_by(portfolios.id.desc()).paginate(per_page=2,page=page_num,error_out=True)
    projects=portfolios.query.all()
    return(render_template('portfolio.html',projects_paginate=projects_paginate,projects=projects))

@app.route("/blog/<int:page_num>")
def blog(page_num):
    months=[]
    for month_val in range(1, 13):
        month=calendar.month_abbr[month_val]
        months.append(month)
    articles_paginate=articles.query.order_by(articles.id.desc()).paginate(per_page=2,page=page_num,error_out=True)
    
    category_id=categories.query.filter(categories.id==articles.category_id).all()
    comment=comments.query.order_by(comments.id.desc()).all()
    article=articles.query.order_by(articles.id.desc()).all()
    count=[]
    #commentById=comments.query.filter(comments.article_id==articles.id).all()
    k= db.session.query(articles,comments).join(comments,comments.article_id ==  articles.id).filter( articles.id==2).all()
    print(k)
    comm=0 
    for com in k:
       
        comm+=1
    count.append(comm)
    print(comm)
    
    print("-*/*-/*-/*-*/")


    return(render_template('blog.html',articles_paginate=articles_paginate,month=months,category=category_id,comments=comment,articles=article,comm=count))





@app.route("/blog/computers")
def computers():
    months=[]
    for month_val in range(1, 13):
        month=calendar.month_abbr[month_val]
        months.append(month)
    computers=articles.query.filter(articles.category_id==2).all()
    comment=comments.query.order_by(comments.id.desc()).all()
    article=articles.query.order_by(articles.id.desc()).all()
    return(render_template('blog-computers.html',computer=computers,month=months,comments=comment,articles=article))


@app.route("/blog/interesting")
def interesting():
    months=[]
    for month_val in range(1, 13):
        month=calendar.month_abbr[month_val]
        months.append(month)
    interesting=articles.query.filter(articles.category_id==3).all()
    comment=comments.query.order_by(comments.id.desc()).all()
    article=articles.query.order_by(articles.id.desc()).all()
    return(render_template('blog-interesting.html',interesting=interesting,month=months,comments=comment,articles=article))

@app.route("/blog/advices")
def advices():
    months=[]
    for month_val in range(1, 13):
        month=calendar.month_abbr[month_val]
        months.append(month)
    advices=articles.query.filter(articles.category_id==4).all()
    comment=comments.query.order_by(comments.id.desc()).all()
    article=articles.query.order_by(articles.id.desc()).all()
    
    return(render_template('blog-advices.html',advices=advices,month=months,comments=comment,articles=article))

@app.route("/article/<id>")
def article(id):
    category=categories.query.all()
    comment=comments.query.order_by(comments.id.desc()).all()
    months=[]
    for month_val in range(1, 13):
        month=calendar.month_abbr[month_val]
        months.append(month)
    articleById=articles.query.get_or_404(id)
    blog_articles=articles.query.all()
    commentById=comments.query.filter(comments.article_id==articles.id).all()
    commentQty=0
    for com in commentById:
        if com.article_id==articleById.id:
            commentQty+=1
    messages = None
    if request.args.get('messages') is not None:
        messages =json.loads(request.args.get('messages'))
    return(render_template('article.html',articleById=articleById,blog_articles=blog_articles,month=months,comments=commentById,commentQty=commentQty,errors=messages,categories=category,commentById=comment))

@app.route("/addComment",methods=['POST'])
def addComment():
    messages=dict()
    newComment=comments(text=request.form['comment'],name=request.form['author'],email=request.form['email'],site=request.form['url'],article_id=request.form['article_id'])
    if len(request.form['author'])<1:
        messages['author'] = 'Please input Your name!'

    if not validate_email(request.form['email']):
        messages['email'] = 'Email is not valid'
        return (redirect(url_for('article',id=request.form['article_id'],messages=json.dumps(messages))))
    db.session.add(newComment)
    db.session.commit()
    return redirect(url_for('article',id=request.form['article_id']))




@app.route("/login_admin")
def login_admin():
    return(render_template('admin_login.html'))

@app.route("/admin_login",methods=['POST'])
def admin_login():
    user=users.query.filter(db.and_(users.login==request.form['username'],users.password==request.form['pass'])).first()
    print("-*/-*/-*/*-")
    print(user)
    if user == None:
        flash("65656")
        return render_template('admin_login.html')
    if user!=None:
        if user.id == 1:
            login_user(user)
            user=users.query.get(user.id)
            return redirect(url_for("admin.index"))
        else:
            #flash("65656")
            return("65656")
            return render_template('admin_login.html')
    return render_template('admin_login.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html'),404