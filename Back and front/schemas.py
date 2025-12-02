from marshmallow import fields
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from models import Location, Plant, Image,PreviousResearch,Use,Toponimo,InterviewCustomer, InterviewVendor,Review, db


#Setting the schemas for serialization of all tables (Begin)
class ImageSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Image
        sqla_session = db.session
        load_instance = True

    id_image_pk = fields.Int(dump_only=True)
    id_plant_pk = fields.Int(required=True)
    id_location_pk = fields.Int(required=True)
    link = fields.String(required=True)
    date = fields.Date(required=True)
    place = fields.String(required=True)


class PlantSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Plant
        sqla_session = db.session
        load_instance = True

    id_plant_pk = fields.Int(dump_only=True)
    current_name = fields.String(required=True)
    scientific_name = fields.String(required=True)

    #ninclude if we want to retrieve the images in plants
    #images = fields.Nested('ImageSchema', many=True)


class LocationSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Location
        sqla_session = db.session
        load_instance = True

    id_location_pk = fields.Int(dump_only=True)
    city_name = fields.String(required=True)
    province_name = fields.String(required=True)

    #plants = fields.Nested('PlantSchema', many=True)

class PreviousResearchSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = PreviousResearch
        sqla_session = db.session
        load_instance = True

    id_research_pk = fields.Int(dump_only=True)
    id_plant_pk = fields.Int(required=True)
    id_location_pk = fields.Int(required=True)
    title = fields.String(required=True)
    link = fields.String()

class UseSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Use
        sqla_session = db.session
        load_instance = True

    id_use_pk = fields.Int(dump_only=True)
    id_plant_pk = fields.Int(required=True)
    id_location_pk = fields.Int(required=True)
    description = fields.String(required=True)
    type_use = fields.String(required=True)

class ToponimoSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Toponimo
        sqla_session = db.session
        load_instance = True

    id_toponimo_pk = fields.Int(dump_only=True)
    id_plant_pk = fields.Int(required=True)
    id_location_pk = fields.Int(required=True)
    origin = fields.String(required=True)
    commercial_distribution = fields.String(required=True)
    distribution = fields.String(required=True)


class InterviewCustomerSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = InterviewCustomer
        sqla_session = db.session
        load_instance = True

    id_interviews_customer_pk = fields.Int(dump_only=True)
    id_location_pk = fields.Int(required=True)
    link = fields.String(required=True)

    q1 = fields.String(required=True)
    q2 = fields.String(required=True)
    q3 = fields.String(required=True)
    q4 = fields.String(required=True)
    q5 = fields.String(required=True)
    q6 = fields.String(required=True)
    q7 = fields.String(required=True)
    q8 = fields.String(required=True)
    q9 = fields.String(required=True)
    q10 = fields.String(required=True)
    q11 = fields.String(required=True)
    q12 = fields.String(required=True)
    q13 = fields.String(required=True)
    q14 = fields.String(required=True)
    q15 = fields.String(required=True)
    q16 = fields.String(required=True)
    q17 = fields.String(required=True)
    q18 = fields.String(required=True)
    q19 = fields.String(required=True)
    q20 = fields.String(required=True)
    q21 = fields.String(required=True)
    q22 = fields.String(required=True)
    q23 = fields.String(required=True)
    q24 = fields.String(required=True)


class InterviewVendorSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = InterviewVendor
        sqla_session = db.session
        load_instance = True

    id_interviews_vendor_pk = fields.Int(dump_only=True)
    id_location_pk = fields.Int(required=True)
    link = fields.String(required=True)

    q1 = fields.String(required=True)
    q2 = fields.String(required=True)
    q3 = fields.String(required=True)
    q4 = fields.String(required=True)
    q5 = fields.String(required=True)
    q6 = fields.String(required=True)
    q7 = fields.String(required=True)
    q8 = fields.String(required=True)
    q9 = fields.String(required=True)
    q10 = fields.String(required=True)
    q11 = fields.String(required=True)
    q12 = fields.String(required=True)
    q13 = fields.String(required=True)
    q14 = fields.String(required=True)
    q15 = fields.String(required=True)
    q16 = fields.String(required=True)
    q17 = fields.String(required=True)
    q18 = fields.String(required=True)
    q19 = fields.String(required=True)
    q20 = fields.String(required=True)
    q21 = fields.String(required=True)
    q22 = fields.String(required=True)
    q23 = fields.String(required=True)
#Setting the schemas for serialization of all tables (end)

#Setting the schemas for review table
class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Review
        sqla_session = db.session
        load_instance = True

    id_review_pk = fields.Int(dump_only=True)
    id_plant_pk = fields.Int(required=True)
    author = fields.String(required=True)
    content = fields.String(required=True)
    rating = fields.Int(required=True)
    date = fields.Date()
