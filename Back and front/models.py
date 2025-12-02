from flask_sqlalchemy import SQLAlchemy
from datetime import date as dt_date

db = SQLAlchemy()

# class Image(db.Model):
# #   Foreign Keys in Image table
#     __tablename__ = 'images'
#     id_image_pk = db.Column(db.Integer, primary_key=True)
#     id_plant_pk = db.Column(db.Integer, primary_key=True)
#     id_location_pk = db.Column(db.Integer, primary_key=True)
    
#     link = db.Column(db.Text, nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     place = db.Column(db.String(100), nullable=False)

# #   Foreign Keys contraints for id_plant_pk, id_location_pk
#     __table_args__ = (
#         db.ForeignKeyConstraint(
#             ['id_plant_pk', 'id_location_pk'],
#             ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
#         ),
#     )

# #   Required data for instance the Image table record
#     def __init__(self, id_image_pk, id_plant_pk, id_location_pk, link, date, place):
#         self.id_image_pk = id_image_pk
#         self.id_plant_pk = id_plant_pk
#         self.id_location_pk = id_location_pk
#         self.link = link
#         self.date = date
#         self.place = place

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def __repr__(self):
#         return f'<Image {self.id_image_pk}, Plant {self.id_plant_pk}, Location {self.id_location_pk}: {self.link}>'
    
class Plant(db.Model):
    __tablename__ = 'plants'
    id_plant_pk = db.Column(db.Integer, primary_key=True)
    current_name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100), nullable=False)
#   Many2many relation between plants and PlantsLocations
    locations = db.relationship('PlantsLocations', back_populates='plant')
    
    __table_args__ = (
        db.UniqueConstraint('current_name', name='PK_current_name'),
    )
    

class Location(db.Model):
    __tablename__ = 'locations'
    id_location_pk = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    province_name = db.Column(db.String(100), nullable=False)
#   Many2many relation between locations and PlantsLocations
    plants = db.relationship('PlantsLocations', back_populates='location')

class PlantsLocations(db.Model):
    __tablename__ = 'plants_locations'
    id_plant_pk = db.Column(db.Integer, db.ForeignKey('plants.id_plant_pk'), primary_key=True)
    id_location_pk = db.Column(db.Integer, db.ForeignKey('locations.id_location_pk'), primary_key=True)
#   Bidirectional conexion with Plant and Location models
    plant = db.relationship('Plant', back_populates='locations')
    location = db.relationship('Location', back_populates='plants')


# Previous Research Model
# class PreviousResearch(db.Model):
#     __tablename__ = 'previous_researchs'
#     id_research_pk = db.Column(db.Integer, primary_key=True)
#     id_plant_pk = db.Column(db.Integer, primary_key=True)
#     id_location_pk = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     link = db.Column(db.Text)

#     __table_args__ = (
#         db.ForeignKeyConstraint(
#             ['id_plant_pk', 'id_location_pk'],
#             ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
#         ),
#     )

#     def __init__(self, id_research_pk, id_plant_pk, id_location_pk, title, link):
#         self.id_research_pk = id_research_pk
#         self.id_plant_pk = id_plant_pk
#         self.id_location_pk = id_location_pk
#         self.title = title
#         self.link = link

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def __repr__(self):
#         return f'<PreviousResearch {self.id_research_pk}, Plant {self.id_plant_pk}, Location {self.id_location_pk}: {self.title}>'

# Use Model
class Use(db.Model):
    __tablename__ = 'uses'
    id_use_pk = db.Column(db.Integer, primary_key=True)
    id_plant_pk = db.Column(db.Integer, primary_key=True)
    id_location_pk = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    type_use = db.Column(db.String(200), nullable=False)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['id_plant_pk', 'id_location_pk'],
            ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
        ),
    )

    def __init__(self, id_use_pk, id_plant_pk, id_location_pk, description, type_use):
        self.id_use_pk = id_use_pk
        self.id_plant_pk = id_plant_pk
        self.id_location_pk = id_location_pk
        self.description = description
        self.type_use = type_use

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Use {self.id_use_pk}, Plant {self.id_plant_pk}, Location {self.id_location_pk}: {self.description}>'

# # Toponime Model
# class Toponimo(db.Model):
#     __tablename__ = 'toponimos'
    
#     id_toponimo_pk = db.Column(db.Integer, primary_key=True)
#     id_plant_pk = db.Column(db.Integer, primary_key=True)
#     id_location_pk = db.Column(db.Integer, primary_key=True)
#     origin = db.Column(db.Text)
#     commercial_distribution = db.Column(db.String(400))
#     distribution = db.Column(db.String(400))

#     __table_args__ = (
#         db.ForeignKeyConstraint(
#             ['id_plant_pk', 'id_location_pk'],
#             ['plants_locations.id_plant_pk', 'plants_locations.id_location_pk']
#         ),
#     )

#     def __init__(self, id_toponimo_pk, id_plant_pk, id_location_pk, origin, commercial_distribution, distribution):
#         self.id_toponimo_pk = id_toponimo_pk
#         self.id_plant_pk = id_plant_pk
#         self.id_location_pk = id_location_pk
#         self.origin = origin
#         self.commercial_distribution = commercial_distribution
#         self.distribution = distribution

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def __repr__(self):
#         return f'<Toponimo {self.id_toponimo_pk}, Plant {self.id_plant_pk}, Location {self.id_location_pk}: {self.origin}>'

# # Interview Customer Model
# class InterviewCustomer(db.Model):
#     __tablename__ = 'interview_customers'
    
#     id_interviews_customer_pk = db.Column(db.Integer, primary_key=True)
#     id_location_pk = db.Column(db.Integer, db.ForeignKey('locations.id_location_pk'), primary_key=True)
#     link = db.Column(db.String(500), nullable=False)
    
# #   Questions in the form
#     q1 = db.Column(db.String(255))
#     q2 = db.Column(db.String(255))
#     q3 = db.Column(db.String(255))
#     q4 = db.Column(db.String(255))
#     q5 = db.Column(db.String(255))
#     q6 = db.Column(db.String(255))
#     q7 = db.Column(db.String(255))
#     q8 = db.Column(db.String(255))
#     q9 = db.Column(db.String(255))
#     q10 = db.Column(db.String(255))
#     q11 = db.Column(db.String(255))
#     q12 = db.Column(db.String(255))
#     q13 = db.Column(db.String(255))
#     q14 = db.Column(db.String(255))
#     q15 = db.Column(db.String(255))
#     q16 = db.Column(db.String(255))
#     q17 = db.Column(db.String(255))
#     q18 = db.Column(db.String(255))
#     q19 = db.Column(db.String(255))
#     q20 = db.Column(db.String(255))
#     q21 = db.Column(db.String(255))
#     q22 = db.Column(db.String(255))
#     q23 = db.Column(db.String(255))
#     q24 = db.Column(db.String(255))

#     def __init__(self, id_interviews_customer_pk, id_location_pk, link, **kwargs):
#         self.id_interviews_customer_pk = id_interviews_customer_pk
#         self.id_location_pk = id_location_pk
#         self.link = link
#         for i in range(1, 25):
#             setattr(self, f'q{i}', kwargs.get(f'q{i}', None))

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def __repr__(self):
#         return f'<InterviewCustomer {self.id_interviews_customer_pk}, Location {self.id_location_pk}>'

# # Interview Vendor Model
# class InterviewVendor(db.Model):
#     __tablename__ = 'interview_vendors'
    
#     id_interviews_vendor_pk = db.Column(db.Integer, primary_key=True)
#     id_location_pk = db.Column(db.Integer, db.ForeignKey('locations.id_location_pk'), primary_key=True)
#     link = db.Column(db.String(500), nullable=False)
    
# #   Questions in the form
#     q1 = db.Column(db.String(255))
#     q2 = db.Column(db.String(255))
#     q3 = db.Column(db.String(255))
#     q4 = db.Column(db.String(255))
#     q5 = db.Column(db.String(255))
#     q6 = db.Column(db.String(255))
#     q7 = db.Column(db.String(255))
#     q8 = db.Column(db.String(255))
#     q9 = db.Column(db.String(255))
#     q10 = db.Column(db.String(255))
#     q11 = db.Column(db.String(255))
#     q12 = db.Column(db.String(255))
#     q13 = db.Column(db.String(255))
#     q14 = db.Column(db.String(255))
#     q15 = db.Column(db.String(255))
#     q16 = db.Column(db.String(255))
#     q17 = db.Column(db.String(255))
#     q18 = db.Column(db.String(255))
#     q19 = db.Column(db.String(255))
#     q20 = db.Column(db.String(255))
#     q21 = db.Column(db.String(255))
#     q22 = db.Column(db.String(255))
#     q23 = db.Column(db.String(255))

#     def __init__(self, id_interviews_vendor_pk, id_location_pk, link, **kwargs):
#         self.id_interviews_vendor_pk = id_interviews_vendor_pk
#         self.id_location_pk = id_location_pk
#         self.link = link
#         for i in range(1, 24):
#             setattr(self, f'q{i}', kwargs.get(f'q{i}', None))

#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def __repr__(self):
#         return f'<InterviewVendor {self.id_interviews_vendor_pk}, Location {self.id_location_pk}>'

# # Review Model
# class Review(db.Model):
#     __tablename__ = 'reviews'

#     id_review_pk = db.Column(db.Integer, primary_key=True)
#     id_plant_pk = db.Column(db.Integer, db.ForeignKey('plants.id_plant_pk'), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     rating = db.Column(db.Integer, nullable=False)  # 1 a 5
#     date = db.Column(db.Date, nullable=False, default=dt_date.today)

#     def __init__(self, id_plant_pk, author, content, rating, review_date=None):
#         self.id_plant_pk = id_plant_pk
#         self.author = author
#         self.content = content
#         self.rating = rating
#         self.date = review_date or dt_date.today()

#     def __repr__(self):
#         return f'<Review {self.id_review_pk}: Plant {self.id_plant_pk} - {self.author}>'
    
