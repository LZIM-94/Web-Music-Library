from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
	ForeignKey,
    )
	
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
    )

from pyramid.security import (
    Allow,
    Everyone,
    )


from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(Text, primary_key=True)
    info = Column(Text)
    year_of_found = Column(Integer)
    parent_id = Column(Integer, ForeignKey(id))
    parent_genre = relationship("Genre", remote_side="Genre.id")


    def __repr__(self):
        return self.name or ''

	
class Music(Base):
	__tablename__ = 'music'
	author = Column(Text, primary_key=True)
	title = Column(Text, primary_key=True)
	year = Column(Integer)
        source_static = Column(Text)
        itunes_ref = Column(Text) 	
	genre_id = Column(Integer,ForeignKey('genre.id'))
	genre = relationship("Genre", backref='music')
        def __repr__(self):
            return self.author + ' - ' + self.title or ''




class RootFactory(object):
    __acl__ = [ (Allow, 'group:editors', ('pyramid_sacrud_home', 'pyramid_sacrud_create', 'pyramid_sacrud_update', 'pyramid_sacrud_delete', 'pyramid_sacrud_list')),]
    def __init__(self, request):
        pass
	
