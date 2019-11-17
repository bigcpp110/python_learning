from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Account(db.Model):
    __tablename__="account"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(255))
    name=db.Column(db.String(20))
    telephone=db.Column(db.String(50),unique=True)
    role=db.Column(db.Integer)
    flag_telephone=db.Column(db.Integer)
    checkcode=db.Column(db.String(20))
    source=db.Column(db.String(20))
    dtcreate=db.Column(db.DateTime,default=datetime.now)


    def __repr__(self):
        return "<Account %s"%self.name

class Terminal(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    account_id=db.Column(db.ForeignKey("account.id"))
    os=db.Column(db.String(20))
    code=db.Column(db.String(255))

    account=db.relationship("account",backref=db.backref("terminal"))


    def __repr__(self):
        return "<Terminal %d,%d,%s"%(self.account_id.self.type,self.code)


class Agespan(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Unicode(50,collation="utf8_bin"))
    fromage=db.Column(db.Integer)
    toage=db.Column(db.Integer)

    def __repr__(self):
        return "<Agespan %s"%self.name

class Area(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)

    def __repr__(self):
        return "<Area %s>"%self.name

class Feature(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)

    def __repr__(self):
        return "<Feature %s>" % self.name

class Feettype(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)

    def __repr__(self):
        return "<Feetype %s>" % self.name


class Schooltype(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)

    def __repr__(self):
        return "<Schooltype %s" % self.name

class Bullentin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    dt=db.Column(db.DateTime,default=datetime.now)
    title=db.Column(db.String(68))
    content=db.Column(db.String(3000))
    valid=db.Column(db.Integer)
    source=db.Column(db.String(68))
    author=db.Column(db.String(68))

    def __repr__(self):
        return "<Bulletin %s" % self.title

class Bulletinimage(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    bulletin_id=db.Column(db.ForeignKey("bulletin.id"))
    file=db.Column(db.String(500))
    bulletin=db.relationship("Bulletin",backref=db.backref("bulletinimages",cascade="alll,delete-orphan"))

    def __repr__(self):
        return "<Bulltinimage %d,%s"%(self.bulletin_id,self.file)


class Institution(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String9100)
    agespan_id=db.Column(db.ForeignKey("agespan.id"))
    area_id=db.Column(db.ForeignKey("area.id"))
    address=db.Column(db.String(100))
    location=db.Column(db.String(100))
    website = db.Column(db.String(100))
    telephone = db.Column(db.String(50))
    feedesc=db.Column(db.String(100))
    timeopen=db.Column(db.DateTime,default=datetime.now)
    timeclose=db.Column(db.DateTime,default=datetime.now)
    feetype_id=db.Column(db.ForeignKey("feetype.id"))
    longitude=db.Column(db.Float)
    latitude=db.Column(db.Float)
    featuredesc=db.Column(db.String(200))

    feetype=db.relationship("Feetype")
    area=db.relationship("Area")
    agespan=db.relationship("Agespan")

    def __repr__(self):
        return "<Institution %s>" % self.name

class InstitutionFeature(db.Model):
    institution_id=db.Column(db.ForeignKey("institution.id"),primary_key=True)
    feature_id=db.Column(db.ForeignKey("feature.id"),primary_key=True)
    institution=db.relationship("Institution",backref=db.backref("institutionfeatures",casade="all, delete-orphan"))
    feature=db.relationship("Feature")

class Institutionimage(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    institution_id=db.Column(db.ForeignKey("institution.id"))
    file=db.Column(db.String(500))
    institution=db.relationship("Institution",backref=db.backref("institutionimages",cascade="all, delete-orphan"))


    def __repr__(self):
        return "<Institutionimage %d,%s》" % (self.institution_id,self.file)


class School(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    area_id=db.Column(db.ForeignKey("area.id"))
    teachdesc=db.Column(db.Text)
    address=db.Column(db.String(100))
    schooltype_id=db.Column(db.ForeignKey("schooltype.id"))
    website=db.Column(db.String(100))
    distinguish=db.Column(db.Text)
    leisure=db.Column(db.String(1000))
    threashold=db.Column(db.String(1000))
    partner = db.Column(db.String(100))
    artsource=db.Column(db.String(1000))
    feedec=db.Column(db.String(1000))
    longitude=db.Column(db.Float)
    latitude=db.Column(db.Float)

    schooltype=db.relationship("schooltype")
    area=db.relationship("Area")


    def __repr__(self):
        return "<School %s>" % self.name

class SchoolFeature(db.Model):
    school_id=db.Column(db.ForeignKey("school.id"),primary_key=True)
    feature_id=db.Column(db.ForeignKey("feature.id"),primary_key=True)
    school=db.relationship("School",brackref=db.backref("schoolfeatures",cascade="all, delete-orphan"))
    feature=db.relationship("Feature")

    def __repr__(self):
        return "<SchoolFeature %d, %d" % (self.school_id,self.feature_id)


class Schoolimage(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    school_id=db.Column(db.ForeignKey("school.id"))
    file=db.Column(db.String(500))

    school=db.relationship("School",backref=db.backref("schoolimages",cascade="all, delete-orphan"))


    def __repr__(self):
        return "<Schoolimage %d,%s>" % (self.school_id,self.file)
