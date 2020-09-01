# Nota: Todas las Clases de "SkLearn" deben tener los métodos "transform" y "fit"
# Las Clases "BaseEstimator" y "TransformerMixin" pertenecientes a "sklearn.base" nos permitirán que
# la Clase "DataSetBalancer" herede métodos pertenecientes a "SkLearn"
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import resample
import pandas as pd



# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')



class DataSetBalancer( BaseEstimator , TransformerMixin ):
    
    def __init__( self , X , y ):
        self.X = pd.concat( [ X , y ] , axis = 1 )
    
    def fit( self , X , y = None ):
        return self
    
    def transform( self , X ):
        
        # Determinamos la clase con mayor cantidad de registros
        minimum = min( len( self.X['PROFILE'][ self.X['PROFILE'] == 'advanced_data_science' ] ) , len( self.X['PROFILE'][ self.X['PROFILE'] == 'beginner_front_end' ] ) , len( self.X['PROFILE'][ self.X['PROFILE'] == 'beginner_data_science' ] ) , len( self.X['PROFILE'][ self.X['PROFILE'] == 'advanced_backend' ] ) , len( self.X['PROFILE'][ self.X['PROFILE'] == 'advanced_front_end' ] ) , len( self.X['PROFILE'][ self.X['PROFILE'] == 'beginner_backend' ] ) )
 
        # Igualamos la cardinalidad del conjunto muestra de cada registro
        aux_df = pd.concat( [ resample( self.X[ self.X['PROFILE'] == 'advanced_data_science' ] , replace = True , n_samples = minimum , random_state = 100 ) , resample( self.X[ self.X['PROFILE'] == 'beginner_front_end' ] , replace = True , n_samples = minimum , random_state = 100 ) , resample( self.X[ self.X['PROFILE'] == 'beginner_data_science' ] , replace = True , n_samples = minimum , random_state = 100 ) , resample( self.X[ self.X['PROFILE'] == 'advanced_backend' ] , replace = True , n_samples = minimum , random_state = 100 ) , resample( self.X[ self.X['PROFILE'] == 'advanced_front_end' ] , replace = True , n_samples = minimum , random_state = 100 ) , resample( self.X[ self.X['PROFILE'] == 'beginner_backend' ] , replace = True , n_samples = minimum , random_state = 100 ) ] )
        
        # Retomo de columnas que seran features
        features = ["Unnamed: 0", "NAME", "USER_ID", "HOURS_DATASCIENCE", "HOURS_BACKEND", "HOURS_FRONTEND","NUM_COURSES_BEGINNER_DATASCIENCE", "NUM_COURSES_BEGINNER_BACKEND", "NUM_COURSES_BEGINNER_FRONTEND","NUM_COURSES_ADVANCED_DATASCIENCE", "NUM_COURSES_ADVANCED_BACKEND", "NUM_COURSES_ADVANCED_FRONTEND","AVG_SCORE_DATASCIENCE", "AVG_SCORE_BACKEND", "AVG_SCORE_FRONTEND"]

        # Retomo de variable objetico
        target = ["PROFILE"]

        # Devolvemos un nuevo dataframe equilibrado
        return aux_df[features] , aux_df[target]