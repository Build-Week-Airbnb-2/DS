import logging
import random
import os

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from keras.models import load_model
import tensorflow as tf
import numpy as np
from joblib import load
import joblib
import category_encoders

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """The base data model to parse the request body JSON."""

    host_about_len: str = Field(
        ..., example='My wife and I own this house and rent out the guest rooms on weekends')
    description_len: str = Field(..., example='A quiet house in north seattle')
    property_type: str = Field(..., example='House')
    neighbourhood: str = Field(..., example='Silver Lake')
    city: str = Field(..., example='Everett')
    state: str = Field(..., example='WA')
    zipcode: str = Field(..., example='98208')
    bathrooms: float = Field(..., example=1.75)
    bedrooms: int = Field(..., example=3)
    beds: int = Field(..., example=6)
    accommodates: float = Field(..., example=6.0)
    guests_included: float = Field(..., example=2.0)
    square_feet: int = Field(..., example='1200')
    cancellation_policy: str = Field(..., example='moderate')
    instant_bookable: bool = Field(..., example='t')
    is_business_travel_ready: bool = Field(..., example='f')
    review_scores_rating: float = Field(..., example=90.0)
    number_of_reviews: int = Field(..., example=4)
    transit_len: str = Field(...,
                             example='There is a bus stop at the end of the street')
#    amenities: str = Field(..., example='Internet, Wifi, Kitchen, Laundry')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row.
        Also alters the Item to shape the DF correctly for modeling."""
        self.description_len = len(self.description_len)
        self.host_about_len = len(self.host_about_len)
        self.transit_len = len(self.transit_len)
        return pd.DataFrame([dict(self)])

    @validator('bathrooms')
    def bath_must_be_positive(cls, value):
        """Validate that bathrooms is a positive number."""
        assert value > 0, f'bathrooms == {value}, must be > 0'
        return value

    @validator('bedrooms')
    def bed_must_be_positive(cls, value):
        """Validate that bedrooms is a positive number."""
        assert value > 0, f'bedrooms == {value}, must be > 0'
        return value

    @validator('beds')
    def beds_must_be_positive(cls, value):
        """Validate that beds must be a positive number."""
        assert value > 0, f'beds == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """Predict optimal pricing for Airbnb."""
    model2 = load_model('app/api/model1.h5')
    preprocessor = joblib.load('app/api/preprocessor1.pkl')
    X_new = item.to_df()    
    X_test = preprocessor.fit_transform(X_new)
    log.info(X_new)
    y_pred = model2.predict(X_test)
    y_pred = round(float(y_pred[0][0]), 2)
    return {
        'predicted_price': y_pred   
    }
